import fs from 'node:fs/promises';
import path from 'node:path';
import { createHash } from 'node:crypto';

export function parseMarkdown(raw, filename) {
  let text = raw.replace(/^\uFEFF/, '').replace(/\r\n?/g, '\n').trim();
  // Only strip YAML at the very beginning, never between story sections.
  if (text.startsWith('---\n')) {
    const end = text.indexOf('\n---\n', 4);
    if (end < 0) throw new Error(`${filename}: 未闭合的 YAML 头部`);
    text = text.slice(end + 5).trim();
  }
  const heading = text.match(/^#[ \t]+([^\n]+)(?:\n|$)/);
  const title = (heading?.[1] || filename.replace(/^\d+[-_]/, '').replace(/\.md$/i, '')).trim();
  if (heading) text = text.slice(heading[0].length);
  // Conservative conversion: don't delete literal underscores or entire paragraphs.
  const body = text
    .replace(/^#{1,6}[ \t]+/gm, '')
    .replace(/^[ \t]*(?:-{3,}|\*{3,}|_{3,})[ \t]*$/gm, '')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
  if (!title || !body) throw new Error(`${filename}: 标题或正文为空`);
  const hash = createHash('sha256').update(`${title}\0${body}`).digest('hex');
  return { title, body, hash, bodyChars: [...body.replace(/\s/gu, '')].length };
}

export async function listBooks(directory) {
  return (await fs.readdir(directory, { withFileTypes: true }))
    .filter((item) => item.isFile() && /\.md$/i.test(item.name) && !item.name.startsWith('.'))
    .map((item) => path.join(directory, item.name))
    .sort((a, b) => a.localeCompare(b, 'zh-CN', { numeric: true }));
}

export async function readBooks(args) {
  if (args.all && args.books.length) throw new Error('--all 与 --book 不能同时使用');
  const files = args.all ? await listBooks(args.booksDir) : args.books.map((file) =>
    path.isAbsolute(file) ? file : path.join(args.booksDir, file));
  if (!files.length) throw new Error('请选择 --book 文件名 或 --all');
  const seen = new Set();
  const books = [];
  for (const file of files) {
    const realPath = await fs.realpath(file);
    const book = { path: realPath, file: path.basename(file), ...parseMarkdown(await fs.readFile(realPath, 'utf8'), path.basename(file)) };
    if (!seen.has(book.hash)) books.push(book);
    seen.add(book.hash);
  }
  return books;
}

function validateSpec(spec, name) {
  if (typeof spec === 'string' && spec.trim()) return;
  if (spec && typeof spec.selector === 'string' && spec.selector.trim() &&
      (spec.frame === undefined || (typeof spec.frame === 'string' && spec.frame.trim()))) return;
  throw new Error(`配置 ${name} 必须是 CSS/Playwright 选择器或 {selector, frame}`);
}

export async function loadConfig(file, forRun = false) {
  if (!file) throw new Error('请用 --config 指定平台配置文件');
  const config = JSON.parse(await fs.readFile(path.resolve(file), 'utf8'));
  if (!/^[a-zA-Z0-9_-]+$/.test(config.id || '')) throw new Error('配置 id 只能包含字母、数字、下划线或连字符');
  for (const key of ['editorUrl', 'loginUrl']) {
    if (key === 'loginUrl' && !config[key]) continue;
    const url = new URL(config[key]);
    if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password) throw new Error(`配置 ${key} 地址无效`);
  }
  config.timeoutMs ??= 15000;
  if (!Number.isInteger(config.timeoutMs) || config.timeoutMs < 100 || config.timeoutMs > 120000) {
    throw new Error('timeoutMs 应为 100～120000 的整数');
  }
  if (forRun) {
    if (config.configured !== true) throw new Error('这是未校准的示例配置。请先检查真实页面并设置 configured: true');
    validateSpec(config.fields?.title, 'fields.title');
    validateSpec(config.fields?.body, 'fields.body');
    if (JSON.stringify(config.fields.title) === JSON.stringify(config.fields.body)) throw new Error('标题与正文不能使用相同选择器');
    if (config.manualNewEntry !== undefined && typeof config.manualNewEntry !== 'boolean') throw new Error('manualNewEntry 必须是布尔值');
    for (const action of ['save', 'publish']) {
      if (config.actions?.[action]) {
        validateSpec(config.actions[action].button, `actions.${action}.button`);
        const success = config.actions[action].success;
        if (success?.manual === true) {
          if (success.selector || success.frame) throw new Error(`actions.${action}.success 不能同时配置人工确认和选择器`);
        } else {
          validateSpec(success, `actions.${action}.success`);
        }
      }
    }
  }
  return config;
}

export async function appendEvent(file, event) {
  await fs.mkdir(path.dirname(file), { recursive: true, mode: 0o700 });
  const handle = await fs.open(file, 'a', 0o600);
  try {
    await handle.writeFile(`${JSON.stringify({ time: new Date().toISOString(), ...event })}\n`);
    // Persist intent before clicking: a crash must not lead to an automatic re-post.
    await handle.sync();
  } finally {
    await handle.close();
  }
}

export async function readJournal(file) {
  let text;
  try { text = await fs.readFile(file, 'utf8'); }
  catch (error) { if (error.code === 'ENOENT') return []; throw error; }
  return text.split('\n').filter((line) => line.trim()).map((line, i) => {
    try {
      const event = JSON.parse(line);
      if (!event || typeof event.hash !== 'string' || !event.hash ||
          !['filled', 'intent', 'confirmed', 'uncertain'].includes(event.status)) throw new Error('Invalid journal event');
      return event;
    }
    catch { throw new Error(`运行记录第 ${i + 1} 行损坏，请人工检查，不能安全自动重试：${file}`); }
  });
}

export function submissionState(events, hash) {
  const relevant = events.filter((event) => event.hash === hash && event.status !== 'filled');
  if (relevant.some((event) => event.status === 'confirmed')) return 'confirmed';
  if (relevant.some((event) => ['intent', 'uncertain'].includes(event.status))) return 'uncertain';
  return 'new';
}

export async function acquireLock(file) {
  await fs.mkdir(path.dirname(file), { recursive: true, mode: 0o700 });
  let handle;
  try { handle = await fs.open(file, 'wx', 0o600); }
  catch (error) {
    if (error.code === 'EEXIST') throw new Error(`已有运行锁：${file}。若上次异常退出，请确认旧进程已结束后再删除该锁。`);
    throw error;
  }
  await handle.writeFile(JSON.stringify({ pid: process.pid, time: new Date().toISOString() }));
  return async () => { await handle.close(); await fs.unlink(file); };
}
