#!/usr/bin/env node
import fs from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import { createInterface } from 'node:readline/promises';
import { fileURLToPath } from 'node:url';
import { listBooks, readBooks, loadConfig, appendEvent, readJournal, submissionState, acquireLock } from './core.mjs';
import { calibratePage } from './calibration.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const help = `
小说发布助手（平台页面需要先校准；七猫提供登录及点选校准入口）

  node publisher.mjs list
  node publisher.mjs preview --all
  node publisher.mjs login --config platform.local.json
  node publisher.mjs inspect --config platform.local.json
  node publisher.mjs setup --config platforms/qimao.json --output qimao.local.json
  node publisher.mjs run --config platform.local.json --book 09-蓝笔.md
  node publisher.mjs run --config platform.local.json --all --save-draft
  node publisher.mjs run --config platform.local.json --book 09-蓝笔.md --publish

--book <文件>        相对小说目录的文件名或绝对路径，可重复
--all                只读取目录一级 Markdown，忽略隐藏备份
--books-dir <目录>   默认 batches/20261019-xuanyi/codex-recommend
--config <JSON>      平台新建页面、精确字段选择器、操作成功信号
--output <JSON>      setup 写入校准配置，不覆盖已有文件
--browser <类型>     auto（默认）、chrome 或 chromium（Playwright 自带）
--state-dir <目录>   默认 state/novel-publisher，按平台 id 隔离
--save-draft         保存草稿并等待配置的成功信号
--publish            执行发布（默认只填稿，绝不自动点击发布）
--yes                不等待人工确认；必须已经登录并校准页面
--headless           无界面，必须配合 --yes（login/inspect 不支持）
--keep-open          结束前按回车关闭浏览器，不能配合 --yes
--help               显示帮助
`;

function parseArgs(argv) {
  const args = { command: argv[0] || 'help', books: [] };
  const values = { '--book': 'book', '--books-dir': 'booksDir', '--config': 'config', '--output': 'output', '--state-dir': 'stateDir', '--browser': 'browser' };
  const flags = { '--all': 'all', '--save-draft': 'saveDraft', '--publish': 'publish', '--keep-open': 'keepOpen', '--yes': 'yes', '--headless': 'headless' };
  for (let i = 1; i < argv.length; i++) {
    const flag = argv[i];
    if (flag === '--help' || flag === '-h') { args.command = 'help'; continue; }
    if (flags[flag]) { args[flags[flag]] = true; continue; }
    const key = values[flag];
    if (!key) throw new Error(`未知参数：${flag}`);
    const value = argv[++i];
    if (!value || value.startsWith('--')) throw new Error(`${flag} 缺少参数值`);
    if (key === 'book') args.books.push(value); else args[key] = value;
  }
  if (args.command === '--help' || args.command === '-h') args.command = 'help';
  if (!['help', 'list', 'preview', 'login', 'inspect', 'setup', 'run'].includes(args.command)) throw new Error('未知命令，使用 --help 查看帮助');
  if (args.saveDraft && args.publish) throw new Error('--save-draft 和 --publish 不能同时使用');
  if (args.headless && !args.yes) throw new Error('--headless 必须配合 --yes');
  if (args.keepOpen && args.yes) throw new Error('--keep-open 不能配合 --yes');
  if (['login', 'inspect', 'setup'].includes(args.command) && (args.yes || args.headless)) throw new Error('login/inspect/setup 需要人工交互');
  if (args.command === 'setup' && !args.output) throw new Error('setup 必须使用 --output 指定本地校准文件');
  if (args.browser && !['auto', 'chrome', 'chromium'].includes(args.browser)) throw new Error('--browser 只能是 auto、chrome 或 chromium');
  args.booksDir = path.resolve(args.booksDir || path.join(root, 'batches/20261019-xuanyi/codex-recommend'));
  args.stateDir = path.resolve(args.stateDir || path.join(root, 'state/novel-publisher'));
  return args;
}

async function prompt(message) {
  if (!process.stdin.isTTY || !process.stdout.isTTY) throw new Error('需要交互终端；已登录、校准后可用 --yes 运行');
  const rl = createInterface({ input: process.stdin, output: process.stdout });
  try { return await rl.question(message); } finally { rl.close(); }
}

function locator(page, spec) {
  if (typeof spec === 'string') return page.locator(spec);
  return (spec.frame ? page.frameLocator(spec.frame) : page).locator(spec.selector);
}

async function uniqueVisible(page, spec, name) {
  // Fail closed on ambiguity instead of selecting the first arbitrary input.
  const matches = locator(page, spec).filter({ visible: true });
  await matches.first().waitFor({ state: 'visible' });
  if (await matches.count() !== 1) throw new Error(`${name} 匹配到多个可见元素，已停止以避免误填/误点`);
  return matches;
}

async function readValue(field) {
  return field.evaluate((element) => {
    if (element instanceof HTMLInputElement) {
      if (!['text', 'search'].includes(element.type)) throw new Error('拒绝向密码、手机号等非文本字段填稿');
      return element.value;
    }
    if (element instanceof HTMLTextAreaElement) return element.value;
    if (element.isContentEditable) return element.innerText;
    throw new Error('字段不是 input、textarea 或 contenteditable');
  });
}

const normalize = (text) => text.replace(/\r\n?/g, '\n').replace(/\u00a0/g, ' ').trim();

async function fillBook(page, config, book) {
  // No fallback selectors: an auth screen must never receive a novel as a password.
  const title = await uniqueVisible(page, config.fields.title, '标题');
  const body = await uniqueVisible(page, config.fields.body, '正文');
  const titleHandle = await title.elementHandle();
  const bodyHandle = await body.elementHandle();
  try {
    const sameFrame = await titleHandle.ownerFrame() === await bodyHandle.ownerFrame();
    if (sameFrame && await title.evaluate((element, other) => element === other || element.contains(other) || other.contains(element), bodyHandle)) {
      throw new Error('标题和正文输入区域重叠，已停止');
    }
  } finally {
    await titleHandle?.dispose();
    await bodyHandle?.dispose();
  }
  if (normalize(await readValue(title)) || normalize(await readValue(body))) {
    throw new Error('编辑页面已有内容，拒绝覆盖。请配置真正的新建页面或人工清空后再运行');
  }
  if (!await title.isEditable() || !await body.isEditable()) throw new Error('标题或正文不可编辑');
  await title.fill(book.title);
  await body.fill(book.body);
  if (normalize(await readValue(title)) !== normalize(book.title) ||
      normalize(await readValue(body)) !== normalize(book.body)) {
    throw new Error('填稿后回读不一致，可能存在字数截断或编辑器兼容问题，已停止提交');
  }
}

async function inspectPage(page, output) {
  const frames = [];
  for (const frame of page.frames()) {
    const elements = await frame.locator('input, textarea, [contenteditable], button, [role="button"]').evaluateAll((nodes) =>
      nodes.filter((node) => node.getClientRects().length).map((node) => ({
        tag: node.tagName.toLowerCase(), id: node.id, name: node.getAttribute('name'),
        type: node.getAttribute('type'), placeholder: node.getAttribute('placeholder'),
        ariaLabel: node.getAttribute('aria-label'), contenteditable: node.getAttribute('contenteditable'),
        // Never export input values, cookies or localStorage.
        buttonText: node.matches('button, [role="button"]') ? node.textContent?.trim().slice(0, 80) : undefined,
      })));
    frames.push({ origin: new URL(frame.url() || 'about:blank').origin, elements });
  }
  await fs.writeFile(output, JSON.stringify(frames, null, 2), { mode: 0o600 });
  console.log(`字段清单已保存：${output}（未导出输入框内容）`);
}

async function browserSession(args, config, books) {
  const directory = path.join(args.stateDir, config.id);
  await fs.mkdir(directory, { recursive: true, mode: 0o700 });
  const release = await acquireLock(path.join(directory, 'run.lock'));
  let context;
  let page;
  const journal = path.join(directory, 'publish-log.jsonl');
  try {
    let pending = books;
    if (args.command === 'run' && (args.saveDraft || args.publish)) {
      const events = await readJournal(journal);
      pending = books.filter((book) => {
        const state = submissionState(events, book.hash);
        if (state === 'uncertain') throw new Error(`${book.file} 上次提交结果不确定，请先人工检查平台，记录：${journal}。为防止重复发布，已停止`);
        if (state === 'confirmed') console.log(`跳过已确认提交的稿件：${book.file}`);
        return state !== 'confirmed';
      });
      if (!pending.length) return;
    }
    if (args.publish && !args.yes) {
      console.log(pending.map((book) => `${book.file}（${book.bodyChars} 字）`).join('\n'));
      if (await prompt(`将公开发布 ${pending.length} 篇，输入“发布”继续：`) !== '发布') throw new Error('已取消发布');
    }
    const { chromium } = await import('playwright');
    const executablePath = process.env.NOVEL_PUBLISHER_CHROME || (args.browser === 'chromium' ? undefined :
      ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/Applications/Chromium.app/Contents/MacOS/Chromium'].find(existsSync));
    if (args.browser === 'chrome' && !executablePath) throw new Error('未找到本机 Chrome，请使用 --browser chromium 或 NOVEL_PUBLISHER_CHROME 指定路径');
    context = await chromium.launchPersistentContext(path.join(directory, 'profile'), {
      headless: Boolean(args.headless),
      ...(executablePath ? { executablePath } : {}),
      viewport: { width: 1440, height: 1000 }, locale: 'zh-CN',
    });
    context.setDefaultTimeout(config.timeoutMs);
    context.setDefaultNavigationTimeout(config.timeoutMs);
    page = context.pages()[0] || await context.newPage();
    if (args.command === 'login') {
      await page.goto(config.loginUrl || config.editorUrl, { waitUntil: 'domcontentloaded' });
      await prompt('请在浏览器人工完成登录/验证码，完成后回到终端按回车保存会话：');
      console.log(`会话已保存在 ${directory}/profile，请勿分享该目录。`);
      return;
    }
    if (args.command === 'inspect') {
      await page.goto(config.editorUrl, { waitUntil: 'domcontentloaded' });
      await prompt('请登录并进入空白的新建小说编辑页，然后按回车检查字段（不会填稿）：');
      await inspectPage(page, path.join(directory, 'fields.json'));
      return;
    }
    if (args.command === 'setup') {
      await page.goto(config.loginUrl || config.editorUrl, { waitUntil: 'domcontentloaded' });
      await prompt('请人工登录七猫，进入“短故事”的空白新建编辑页；完成分类等必填项后回到终端按回车。此步骤不填稿、不提交：');
      const calibrated = await calibratePage(page, config, { includePublish: Boolean(args.publish) });
      await fs.mkdir(path.dirname(path.resolve(args.output)), { recursive: true, mode: 0o700 });
      await fs.writeFile(path.resolve(args.output), `${JSON.stringify(calibrated, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
      console.log(`七猫实际页面字段已记录：${path.resolve(args.output)}。未保存草稿或发布；运行时仍需人工确认提交结果。`);
      return;
    }
    const action = args.publish ? 'publish' : args.saveDraft ? 'save' : null;
    for (const [index, book] of pending.entries()) {
      // Either navigate afresh, or require the user to create a new entry before filling.
      if (index === 0 || !config.manualNewEntry) await page.goto(config.editorUrl, { waitUntil: 'domcontentloaded' });
      if (!args.yes) await prompt(`第 ${index + 1}/${pending.length} 篇：${book.file}。请${config.manualNewEntry ? '手工进入一个独立短故事的空白新建页，' : ''}完成登录/分类并确认是空白新建页面，按回车填稿：`);
      if (new URL(page.url()).origin !== new URL(config.editorUrl).origin) throw new Error('当前页面不属于配置的站点，拒绝填稿');
      console.log(`填稿：${book.file}`);
      await fillBook(page, config, book);
      const event = { file: book.file, title: book.title, hash: book.hash, action };
      if (!action) {
        await appendEvent(journal, { ...event, status: 'filled' });
        console.log('已填入，未点击保存或发布。某些编辑器可能自行自动保存。');
        continue;
      }
      const settings = config.actions[action];
      const button = await uniqueVisible(page, settings.button, action);
      const manual = settings.success?.manual === true;
      const success = manual ? null : locator(page, settings.success).filter({ visible: true });
      if (success && await success.count()) throw new Error('操作成功标记在点击前已出现，不能据此确认本次提交，请调整选择器');
      await appendEvent(journal, { ...event, status: 'intent' });
      try {
        await button.click();
        if (manual) {
          const word = action === 'save' ? '已保存' : '已发布';
          const confirmation = await prompt(`已点击${action === 'save' ? '保存草稿' : '发布'}。请在七猫完成后续提示并核对稿件，确认成功后输入“${word}”（失败/不确定请直接回车）：`);
          if (confirmation !== word) throw new Error('人工未确认提交成功');
        } else {
          await success.first().waitFor({ state: 'visible' });
        }
        await appendEvent(journal, { ...event, status: 'confirmed', confirmedBy: manual ? 'human' : 'selector' });
      } catch (error) {
        await appendEvent(journal, { ...event, status: 'uncertain' });
        throw new Error(`${book.file} 未确认提交结果；不会自动重试，请人工检查。原因：${error.message}`);
      }
      console.log(`${manual ? '人工已确认' : '已观察到'}${action === 'save' ? '保存草稿' : '发布'}成功：${book.file}`);
    }
    if (!args.yes && (args.keepOpen || !action)) await prompt('请检查浏览器内容。按回车关闭浏览器并结束：');
  } catch (error) {
    if (page && !page.isClosed()) {
      const screenshot = path.join(directory, `error-${Date.now()}.png`);
      try {
        await page.screenshot({ path: screenshot, fullPage: true, timeout: 5000 });
        await fs.chmod(screenshot, 0o600);
        console.error(`异常截图（可能含账号信息，请勿分享）：${screenshot}`);
      } catch { /* A closed/crashed browser may not support screenshots. */ }
      if (!args.yes && process.stdin.isTTY) await prompt('已停止后续操作，请人工检查页面。按回车关闭浏览器：');
    }
    throw error;
  } finally {
    try { await context?.close(); } finally { await release(); }
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.command === 'help') { console.log(help); return; }
  if (args.command === 'list') {
    console.log((await listBooks(args.booksDir)).map((file) => path.basename(file)).join('\n'));
    return;
  }
  const books = ['preview', 'run'].includes(args.command) ? await readBooks(args) : [];
  if (args.command === 'preview') {
    console.log(JSON.stringify(books.map(({ body, ...metadata }) => metadata), null, 2));
    return;
  }
  const config = await loadConfig(args.config, args.command === 'run');
  if (args.command === 'setup') {
    if (!process.stdin.isTTY || !process.stdout.isTTY) throw new Error('setup 需要交互终端，请在本机终端运行');
    try { await fs.access(path.resolve(args.output)); }
    catch (error) { if (error.code !== 'ENOENT') throw error; }
    if (existsSync(path.resolve(args.output))) throw new Error(`校准文件已存在，拒绝覆盖：${args.output}。请指定新的 --output 文件名`);
  }
  if (args.command === 'run') {
    const action = args.publish ? 'publish' : args.saveDraft ? 'save' : null;
    if (!action && books.length > 1) throw new Error('批量填稿需要 --save-draft 或 --publish，避免未保存就切换页面');
    if (action && !config.actions?.[action]) throw new Error(`配置缺少 actions.${action} 的按钮及成功信号`);
    if (args.yes && (config.manualNewEntry || config.actions?.[action]?.success?.manual)) {
      throw new Error('当前校准要求人工进入新建页或核对提交结果，不能使用 --yes/--headless；请在交互终端运行');
    }
  }
  await browserSession(args, config, books);
}

main().catch((error) => {
  console.error(`失败：${error.message}`);
  process.exitCode = 1;
});
