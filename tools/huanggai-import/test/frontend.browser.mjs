import test from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const repo = fileURLToPath(new URL('../../../', import.meta.url));
const frontend = process.env.HUANGGAI_FRONTEND_DIR ?? path.resolve(repo, '../../information-github/next-huanggai');

async function listen(server) {
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  return server.address().port;
}

test('前端真实浏览器检查（临时模拟 API，不导入真实平台）', { timeout: 180000 }, async (t) => {
  const markdown = [
    '这是第一段，包含**关键线索**。', '', '## 第二节', '', '---', '',
    '这是第二段。“一句对话。”', '',
    '<script>window.__huanggai_xss = true</script>', '',
    '<img id="unsafe-image" src="x" onerror="window.__huanggai_xss = true">', '',
    '[危险链接](javascript:alert%281%29)',
  ].join('\n');
  const published = {
    id: 'published-id', title: '阅读排版样例', slug: 'browser-published', content: markdown,
    summary: '模拟作品摘要，不是真实导入。', status: 'published', work_type: 'article',
    sort_order: 9, external_url: 'https://example.com/original', cover_url: null,
    created_at: new Date().toISOString(), updated_at: new Date().toISOString(),
  };
  const draft = { ...published, id: 'draft-id', title: '待审草稿', slug: 'browser-draft', status: 'draft' };
  const works = [published, draft];
  const writes = [];
  const mock = http.createServer(async (req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Headers', 'Authorization, Content-Type');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, OPTIONS');
    if (req.method === 'OPTIONS') { res.writeHead(204); res.end(); return; }
    const json = (status, data) => {
      res.writeHead(status, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(data));
    };
    if (req.url === '/api/v1/works' && req.method === 'GET') return json(200, works.filter((work) => work.status === 'published'));
    if (req.url === '/api/v1/works/admin/all') {
      return req.headers.authorization === 'Bearer browser-test-admin'
        ? json(200, works) : json(401, { detail: 'Unauthorized' });
    }
    if (req.method === 'PUT' && req.url === '/api/v1/works/draft-id') {
      if (req.headers.authorization !== 'Bearer browser-test-admin') return json(401, { detail: 'Unauthorized' });
      let raw = '';
      for await (const chunk of req) raw += chunk;
      const body = JSON.parse(raw);
      writes.push(body);
      Object.assign(draft, body);
      return json(200, draft);
    }
    if (req.method === 'GET' && req.url?.startsWith('/api/v1/works/')) {
      const work = works.find((item) => item.slug === req.url.split('/').at(-1) && item.status === 'published');
      return work ? json(200, work) : json(404, { detail: 'Work not found' });
    }
    json(404, { detail: 'Not found' });
  });
  const apiBase = `http://127.0.0.1:${await listen(mock)}`;
  t.after(() => { mock.closeAllConnections(); return new Promise((resolve) => mock.close(resolve)); });
  const reservation = http.createServer();
  const webPort = await listen(reservation);
  await new Promise((resolve) => reservation.close(resolve));
  const base = `http://127.0.0.1:${webPort}`;
  let serverOutput = '';
  const web = spawn(process.execPath, [
    path.join(frontend, 'node_modules/next/dist/bin/next'), 'dev',
    '--hostname', '127.0.0.1', '--port', String(webPort),
  ], {
    cwd: frontend,
    env: {
      ...process.env, NEXT_PUBLIC_API_URL: apiBase, INTERNAL_API_URL: apiBase,
      NEXT_PUBLIC_INFOHUB_HOME_VISIT_URL: '', NEXT_TELEMETRY_DISABLED: '1',
      WATCHPACK_POLLING: '1000',
    },
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  web.stdout.on('data', (chunk) => { serverOutput = (serverOutput + chunk).slice(-12000); });
  web.stderr.on('data', (chunk) => { serverOutput = (serverOutput + chunk).slice(-12000); });
  t.after(async () => {
    if (web.exitCode !== null) return;
    web.kill('SIGTERM');
    await Promise.race([
      new Promise((resolve) => web.once('exit', resolve)),
      new Promise((resolve) => setTimeout(() => { if (web.exitCode === null) web.kill('SIGKILL'); resolve(); }, 5000).unref()),
    ]);
  });
  let ready = false;
  for (let i = 0; i < 120; i++) {
    if (web.exitCode !== null) throw new Error(`Next.js 启动失败：\n${serverOutput}`);
    if (serverOutput.includes('EMFILE')) throw new Error('Next.js 文件监听达到系统限制；请提高当前 shell 文件描述符上限后重试');
    try {
      if ((await fetch(`${base}/works`, { signal: AbortSignal.timeout(1500) })).ok) { ready = true; break; }
    } catch { /* Wait for compilation. */ }
    await new Promise((resolve) => setTimeout(resolve, 500));
  }
  assert.ok(ready, `Next.js 未就绪：\n${serverOutput}`);
  await t.test('HTTP/SSR：公开列表不泄漏草稿，正文输出语义化 Markdown', async () => {
    const list = await fetch(`${base}/works`);
    assert.equal(list.status, 200);
    const listHtml = await list.text();
    assert.match(listHtml, /阅读排版样例/);
    assert.doesNotMatch(listHtml, /待审草稿/);
    const detail = await fetch(`${base}/works/browser-published`);
    assert.equal(detail.status, 200);
    const html = await detail.text();
    const article = html.match(/<article\b[^>]*>([\s\S]*?)<\/article>/)?.[1];
    assert.ok(article, '服务器应输出 article 正文');
    assert.match(article, /<h2>第二节<\/h2>/);
    assert.match(article, /<strong>关键线索<\/strong>/);
    assert.match(article, /<hr\s*\/?>/);
    assert.doesNotMatch(article, /<script[\s>]|onerror=|unsafe-image|href=["']javascript:/i);
    assert.match(html, /https:\/\/example\.com\/original/);
    const stylesheets = [...html.matchAll(/<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"/g)].map((match) => match[1]);
    // Next can emit attributes in either order.
    if (!stylesheets.length) {
      for (const match of html.matchAll(/<link[^>]*href="([^"]+\.css[^"]*)"[^>]*rel="stylesheet"/g)) stylesheets.push(match[1]);
    }
    assert.ok(stylesheets.length > 0, '应加载正文排版样式');
    const css = (await Promise.all(stylesheets.map(async (url) => (await fetch(new URL(url, base))).text()))).join('\n');
    assert.match(css, /--tw-prose-body/);
  });
  await t.test('HTTP/SSR：草稿详情为 404，不输出标题和正文', async () => {
    const response = await fetch(`${base}/works/browser-draft`);
    assert.equal(response.status, 404);
    const html = await response.text();
    assert.doesNotMatch(html, /待审草稿|这是第一段/);
    assert.equal(writes.length, 0);
  });
  if (process.env.HUANGGAI_SKIP_BROWSER === '1') {
    await t.test('后台交互、手机视口及脚本执行检查', {
      skip: '显式设置 HUANGGAI_SKIP_BROWSER=1；本次仅验证 HTTP/SSR，不代表浏览器验收通过',
    }, () => {});
    return;
  }
  // Reuse the existing browser tool only for optional UI checks. The importer has no dependencies.
  const { chromium } = await import('../../novel-publisher/node_modules/playwright/index.mjs');
  const browser = await chromium.launch({
    headless: true,
    executablePath: process.env.HUANGGAI_TEST_CHROME ?? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  });
  t.after(() => browser.close());
  const context = await browser.newContext();
  const page = await context.newPage();
  const artifacts = await fs.mkdtemp(path.join(os.tmpdir(), 'huanggai-browser-'));
  t.diagnostic(`检查截图：${artifacts}`);

  await t.test('公开列表只包含已发布作品，详情安全渲染 Markdown 和排版', async () => {
    await page.goto(`${base}/works`);
    assert.ok(await page.getByRole('heading', { name: '阅读排版样例' }).isVisible());
    assert.equal(await page.getByText('待审草稿', { exact: true }).count(), 0);
    const response = await page.goto(`${base}/works/browser-published`);
    assert.equal(response.status(), 200);
    await page.locator('article h2').waitFor();
    assert.equal(await page.getByRole('heading', { name: '阅读排版样例', level: 1 }).count(), 1);
    assert.equal(await page.locator('article strong').textContent(), '关键线索');
    assert.equal(await page.locator('article hr').count(), 1);
    assert.equal(await page.locator('article script, article #unsafe-image').count(), 0);
    assert.equal(await page.evaluate(() => window.__huanggai_xss), undefined);
    assert.ok(!(await page.locator('article a').getAttribute('href') ?? '').startsWith('javascript:'));
    assert.equal(await page.getByRole('link', { name: '查看原文' }).getAttribute('href'), published.external_url);
    const metrics = await page.locator('article p').first().evaluate((el) => ({
      margin: parseFloat(getComputedStyle(el).marginTop), lineHeight: parseFloat(getComputedStyle(el).lineHeight),
    }));
    assert.ok(metrics.margin > 0 && metrics.lineHeight >= 28, JSON.stringify(metrics));
    await page.screenshot({ path: path.join(artifacts, 'public-desktop.png'), fullPage: true });
  });

  await t.test('手机正文不横向溢出；草稿详情为 404', async () => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(`${base}/works/browser-published`);
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth));
    await page.screenshot({ path: path.join(artifacts, 'public-mobile.png'), fullPage: true });
    const response = await page.goto(`${base}/works/browser-draft`);
    assert.equal(response.status(), 404);
    assert.equal(await page.getByText('待审草稿', { exact: true }).count(), 0);
  });

  await t.test('未登录访问后台跳转登录页', async () => {
    await page.goto(`${base}/admin/works`);
    await page.waitForURL('**/admin/login');
    assert.equal(writes.length, 0);
  });

  await context.close();
  const admin = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  await admin.addInitScript(() => localStorage.setItem('hg_access_token', 'browser-test-admin'));
  const adminPage = await admin.newPage();
  await t.test('管理员查看草稿只读预览，不保存、不公开', async () => {
    await adminPage.goto(`${base}/admin/works`);
    const row = adminPage.getByRole('row').filter({ hasText: '待审草稿' });
    await row.getByRole('button', { name: '预览', exact: true }).click();
    await adminPage.locator('section article').waitFor();
    assert.ok(await adminPage.getByText('仅管理员可见 · 只读预览 · 预览不会保存或发布', { exact: true }).isVisible());
    assert.equal(await adminPage.locator('section article hr').count(), 1);
    assert.equal(await adminPage.locator('section article script, #unsafe-image').count(), 0);
    assert.equal(await adminPage.evaluate(() => window.__huanggai_xss), undefined);
    assert.equal(writes.length, 0);
    assert.equal(draft.status, 'draft');
    await adminPage.screenshot({ path: path.join(artifacts, 'admin-draft-preview.png'), fullPage: true });
  });

  await t.test('后台正文为多行输入，切换预览不保存；显式保存保留数值类型和草稿状态', async () => {
    const row = adminPage.getByRole('row').filter({ hasText: '待审草稿' });
    await row.getByRole('button', { name: '编辑', exact: true }).click();
    const content = adminPage.getByLabel('正文（Markdown）');
    assert.equal(await content.evaluate((el) => el.tagName), 'TEXTAREA');
    assert.equal(await content.inputValue(), markdown);
    assert.equal(await adminPage.getByLabel('状态', { exact: true }).inputValue(), 'draft');
    assert.equal(await adminPage.getByLabel('作品类型').evaluate((el) => el.tagName), 'SELECT');
    await adminPage.getByLabel('排序', { exact: true }).fill('12');
    await content.fill(`${markdown}\n\n**本地编辑预览**`);
    await adminPage.getByRole('button', { name: '阅读预览（不保存）' }).click();
    assert.ok(await adminPage.locator('article strong').filter({ hasText: '本地编辑预览' }).isVisible());
    assert.equal(writes.length, 0);
    assert.equal(draft.content, markdown);
    await adminPage.getByRole('button', { name: '保存', exact: true }).click();
    await adminPage.locator('section').waitFor({ state: 'detached' });
    assert.equal(writes.length, 1);
    assert.equal(writes[0].sort_order, 12);
    assert.equal(writes[0].status, 'draft');
    assert.ok(writes[0].content.endsWith('**本地编辑预览**'));
    assert.equal(writes[0].id, undefined);
    assert.equal(draft.status, 'draft');
  });
  await admin.close();
});
