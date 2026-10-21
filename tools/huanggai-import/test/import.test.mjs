import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import http from 'node:http';
import { createHash, randomUUID } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { ApiError, HuanggaiApi, contentHash, executeBooks, normalizeBase, parseMarkdown, readBooks } from '../core.mjs';
import { parseArgs } from '../publisher.mjs';

const entry = fileURLToPath(new URL('../publisher.mjs', import.meta.url));
const batch = '20261019-xuanyi';
const story = '# 蓝笔\n\n第一段，**加粗**。\n\n## 第二节\n\n---\n\n“这是一句话。”\n';

async function localFiles(t, files = { '09-蓝笔.md': story }) {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), 'huanggai-test-'));
  t.after(() => fs.rm(root, { recursive: true, force: true }));
  const booksDir = path.join(root, 'books');
  await fs.mkdir(booksDir);
  for (const [name, value] of Object.entries(files)) {
    await fs.mkdir(path.dirname(path.join(booksDir, name)), { recursive: true });
    await fs.writeFile(path.join(booksDir, name), value);
  }
  const books = await readBooks({ booksDir, batch, all: true });
  return { root, booksDir, stateDir: path.join(root, 'state'), books };
}

function remoteBook(book, changes = {}) {
  return {
    id: randomUUID(), title: book.title, slug: book.slug, content: book.content,
    summary: book.summary, status: 'draft', work_type: 'article',
    sort_order: book.sort_order, cover_url: null, external_url: null, ...changes,
  };
}

async function mockApi(t, { initial = [], hook, env, timeoutMs = 500 } = {}) {
  const works = new Map(initial.map((work) => [work.slug, work]));
  const calls = [];
  const server = http.createServer(async (req, res) => {
    try {
      let raw = '';
      for await (const chunk of req) raw += chunk;
      const body = raw ? JSON.parse(raw) : undefined;
      const call = { method: req.method, route: req.url, body };
      calls.push(call);
      const json = (status, data) => {
        res.writeHead(status, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(data));
      };
      if (hook && await hook({ ...call, req, res, works, calls, json })) return;
      if (req.url === '/api/v1/auth/login') {
        if (body.account !== 'admin' || body.password !== 'test-password-private') return json(401, { detail: 'bad login' });
        return json(200, { access_token: 'test-token-private', refresh_token: 'never-save-this' });
      }
      if (req.headers.authorization !== 'Bearer test-token-private') return json(401, { detail: 'private-debug' });
      if (req.method === 'GET' && req.url === '/api/v1/works/admin/all') return json(200, [...works.values()]);
      if (req.method === 'POST' && req.url === '/api/v1/works') {
        if (works.has(body.slug)) return json(409, { detail: 'exists' });
        const work = { id: randomUUID(), ...body };
        works.set(work.slug, work);
        return json(201, work);
      }
      if (req.method === 'PUT' && req.url.startsWith('/api/v1/works/')) {
        const id = req.url.split('/').at(-1);
        const work = [...works.values()].find((item) => item.id === id);
        if (!work) return json(404, { detail: 'missing' });
        Object.assign(work, body);
        return json(200, work);
      }
      json(404, { detail: 'missing' });
    } catch {
      if (!res.headersSent) res.writeHead(500);
      res.end();
    }
  });
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  t.after(() => {
    server.closeAllConnections();
    return new Promise((resolve) => server.close(resolve));
  });
  const base = `http://127.0.0.1:${server.address().port}`;
  const api = new HuanggaiApi(base, { env: env ?? { HUANGGAI_TOKEN: 'test-token-private' }, timeoutMs });
  return { api, works, calls, base };
}

const writes = (calls) => calls.filter((call) => ['POST', 'PUT'].includes(call.method) && call.route !== '/api/v1/auth/login');

test('解析只提取首行标题，保留小标题、分隔线、强调和段落', () => {
  const book = parseMarkdown(`\uFEFF${story.replaceAll('\n', '\r\n')}`, '09-蓝笔.md', batch);
  assert.equal(book.title, '蓝笔');
  assert.equal(book.content, story.slice('# 蓝笔\n\n'.length).trimEnd());
  assert.match(book.content, /## 第二节\n\n---/);
  assert.equal(book.slug, `${batch}-09`);
  assert.equal(book.sort_order, 9);
  assert.equal(book.hash, contentHash(book.title, book.content));
  assert.ok(!book.summary.includes('**'));
});

test('没有一级标题时用文件名，保留首段缩进；摘要按 Unicode 字符截取', () => {
  const book = parseMarkdown(`    首段\n\n${'😀'.repeat(200)}`, '84-旧钢笔.md', batch);
  assert.equal(book.title, '旧钢笔');
  assert.ok(book.content.startsWith('    首段'));
  assert.equal([...book.summary].length, 160);
});

test('拒绝空正文、无编号、过长标题、非法批次和 YAML 头部', () => {
  for (const args of [
    ['# 标题\n', '09-a.md', batch], [story, 'a.md', batch],
    [`# ${'字'.repeat(256)}\n\n正文`, '09-a.md', batch],
    [story, '09-a.md', '../unsafe'], ['---\ntitle: a\n---\n正文', '09-a.md', batch],
  ]) assert.throws(() => parseMarkdown(...args));
});

test('仅选择一级非隐藏文件，同名不同编号不去重，原文件不变化', async (t) => {
  const fixture = await localFiles(t, {
    '09-蓝笔.md': story, '84-蓝笔.md': story,
    '.hidden.md': '备份', '.versions/09-旧稿.md': '旧稿',
  });
  assert.deepEqual(fixture.books.map((book) => book.slug), [`${batch}-09`, `${batch}-84`]);
  assert.equal(await fs.readFile(path.join(fixture.booksDir, '09-蓝笔.md'), 'utf8'), story);
});

test('拒绝目录外文件、隐藏备份、符号链接和重复编号', async (t) => {
  const fixture = await localFiles(t);
  await fs.writeFile(path.join(fixture.root, '10-outside.md'), story);
  await fs.symlink(path.join(fixture.root, '10-outside.md'), path.join(fixture.booksDir, '10-link.md'));
  await fs.writeFile(path.join(fixture.booksDir, '.09-backup.md'), story);
  for (const name of ['../10-outside.md', '10-link.md', '.09-backup.md']) {
    await assert.rejects(readBooks({ booksDir: fixture.booksDir, batch, books: [name] }));
  }
  await fs.writeFile(path.join(fixture.booksDir, '009-另一篇.md'), story);
  await assert.rejects(readBooks({ booksDir: fixture.booksDir, batch, all: true }), /编号重复/);
});

test('接口地址拒绝凭据、路径、重定向式查询和非本机明文 HTTP', () => {
  assert.equal(normalizeBase('http://localhost:8001/'), 'http://localhost:8001');
  assert.equal(normalizeBase('https://example.com'), 'https://example.com');
  for (const url of ['http://example.com', 'https://u:p@example.com', 'https://example.com/api', 'https://example.com?token=x', 'file:///tmp']) {
    assert.throws(() => normalizeBase(url));
  }
});

test('CLI 必须明确选择范围，发布不支持 --all 或 --yes', () => {
  for (const args of [
    ['import'], ['import', '--all', '--book', '09-a.md'], ['publish', '--all'],
    ['publish', '--book', '09-a.md', '--yes'], ['preview', '--all', '--books-dir', '/tmp'],
  ]) assert.throws(() => parseArgs(args));
  assert.equal(parseArgs(['publish', '--book', '09-a.md', '--dry-run']).dryRun, true);
});

test('preview 完全离线，不需要凭据，不创建运行记录', async (t) => {
  const fixture = await localFiles(t);
  const child = spawnSync(process.execPath, [
    entry, 'preview', '--all', '--books-dir', fixture.booksDir, '--batch', batch,
    '--api-base', 'http://127.0.0.1:1', '--state-dir', fixture.stateDir,
  ], { encoding: 'utf8', env: { PATH: process.env.PATH }, cwd: fixture.root });
  assert.equal(child.status, 0, child.stderr);
  assert.match(child.stdout, /未联网/);
  await assert.rejects(fs.access(fixture.stateDir));
});

test('import --dry-run 只读远端，不写作品和本地日志', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t);
  const result = await executeBooks({ ...fixture, api: mock.api, command: 'import', dryRun: true });
  assert.equal(result[0].action, 'create');
  assert.equal(writes(mock.calls).length, 0);
  await assert.rejects(fs.access(fixture.stateDir));
});

test('创建草稿并回读验证；重复导入跳过，日志无正文或凭据', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t);
  const options = { ...fixture, api: mock.api, command: 'import' };
  assert.equal((await executeBooks(options))[0].action, 'created');
  const created = [...mock.works.values()][0];
  assert.equal(created.status, 'draft');
  assert.equal(created.work_type, 'article');
  assert.equal(created.content, fixture.books[0].content);
  assert.equal(created.cover_url, null);
  assert.equal((await executeBooks(options))[0].action, 'skip');
  assert.equal(writes(mock.calls).length, 1);
  const directory = path.join(fixture.stateDir, (await fs.readdir(fixture.stateDir))[0]);
  const log = await fs.readFile(path.join(directory, 'events.jsonl'), 'utf8');
  assert.match(log, /create-intent/);
  assert.match(log, /created/);
  for (const secret of ['test-token-private', 'test-password-private', 'never-save-this', '第一段，']) assert.ok(!log.includes(secret));
  assert.equal((await fs.stat(path.join(directory, 'events.jsonl'))).mode & 0o777, 0o600);
  assert.deepEqual(await fs.readdir(directory), ['events.jsonl']);
});

test('已有相同正文的公开作品保留公开状态，不调用更新', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t, { initial: [remoteBook(fixture.books[0], { status: 'published' })] });
  assert.equal((await executeBooks({ ...fixture, api: mock.api, command: 'import' }))[0].action, 'skip');
  assert.equal(writes(mock.calls).length, 0);
});

test('同 slug 不同正文报告冲突，无论草稿还是公开均不覆盖', async (t) => {
  const fixture = await localFiles(t);
  for (const status of ['draft', 'published']) {
    const mock = await mockApi(t, { initial: [remoteBook(fixture.books[0], { content: '远端人工修改', status })] });
    assert.equal((await executeBooks({ ...fixture, api: mock.api, command: 'import' }))[0].action, 'conflict');
    assert.equal(writes(mock.calls).length, 0);
    assert.equal([...mock.works.values()][0].content, '远端人工修改');
  }
});

test('并发创建返回 409 时按 slug 对账，内容不同则冲突', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t, {
    hook({ method, route, body, works, json }) {
      if (method !== 'POST' || route !== '/api/v1/works') return false;
      works.set(body.slug, remoteBook(fixture.books[0], { content: '其他人的正文' }));
      json(409, { detail: 'exists' });
      return true;
    },
  });
  assert.equal((await executeBooks({ ...fixture, api: mock.api, command: 'import' }))[0].action, 'conflict');
  assert.equal(writes(mock.calls).length, 1);
});

test('POST 已提交但连接断开时对账，不重复创建；再次导入跳过', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t, {
    hook({ method, route, body, works, req }) {
      if (method !== 'POST' || route !== '/api/v1/works') return false;
      works.set(body.slug, { id: randomUUID(), ...body });
      req.socket.destroy();
      return true;
    },
  });
  const options = { ...fixture, api: mock.api, command: 'import' };
  assert.equal((await executeBooks(options))[0].action, 'reconciled');
  assert.equal((await executeBooks(options))[0].action, 'skip');
  assert.equal(writes(mock.calls).length, 1);
});

test('201 响应损坏或 500 发生在提交后时回读对账，不重发 POST', async (t) => {
  const fixture = await localFiles(t);
  for (const status of [201, 500, 409]) {
    const mock = await mockApi(t, {
      hook({ method, route, body, works, res }) {
        if (method !== 'POST' || route !== '/api/v1/works') return false;
        works.set(body.slug, { id: randomUUID(), ...body });
        res.writeHead(status);
        res.end('not-json');
        return true;
      },
    });
    const result = await executeBooks({ ...fixture, api: mock.api, command: 'import' });
    assert.equal(result[0].action, 'reconciled');
    assert.equal(writes(mock.calls).length, 1);
  }
});

test('超时且无法确认写入时停止，不重试，也不继续导入下一篇', async (t) => {
  const fixture = await localFiles(t, { '09-蓝笔.md': story, '84-旧钢笔.md': story });
  const mock = await mockApi(t, {
    timeoutMs: 80,
    hook({ method, route }) { return method === 'POST' && route === '/api/v1/works'; },
  });
  await assert.rejects(executeBooks({ ...fixture, api: mock.api, command: 'import' }), /回读核验/);
  assert.equal(writes(mock.calls).length, 1);
  assert.equal(mock.works.size, 0);
});

test('写入后回读不可用时记录 uncertain 并停止', async (t) => {
  const fixture = await localFiles(t);
  let wrote = false;
  const mock = await mockApi(t, {
    hook({ method, route, json }) {
      if (method === 'POST') wrote = true;
      if (wrote && method === 'GET' && route === '/api/v1/works/admin/all') {
        json(503, { detail: 'private-debug' });
        return true;
      }
      return false;
    },
  });
  await assert.rejects(executeBooks({ ...fixture, api: mock.api, command: 'import' }), /无法回读核验/);
  assert.equal(writes(mock.calls).length, 1);
  const directory = path.join(fixture.stateDir, (await fs.readdir(fixture.stateDir))[0]);
  assert.match(await fs.readFile(path.join(directory, 'events.jsonl'), 'utf8'), /create-uncertain/);
});

test('缺少凭据、401 和 403 均停止，不泄漏服务器详情', async (t) => {
  const fixture = await localFiles(t);
  const noCredentials = await mockApi(t, { env: {} });
  await assert.rejects(executeBooks({ ...fixture, api: noCredentials.api, command: 'import' }), /HUANGGAI_TOKEN/);
  assert.equal(noCredentials.calls.length, 0);
  for (const code of [401, 403]) {
    const mock = await mockApi(t, {
      hook({ json }) { json(code, { detail: 'SECRET-DEBUG-DO-NOT-PRINT' }); return true; },
    });
    await assert.rejects(executeBooks({ ...fixture, api: mock.api, command: 'import' }), (error) =>
      error instanceof ApiError && error.status === code && !error.message.includes('SECRET'));
    assert.equal(writes(mock.calls).length, 0);
  }
});

test('写入时出现 401/403/422，立即停止，不重试、不处理下一篇', async (t) => {
  const fixture = await localFiles(t, { '09-蓝笔.md': story, '84-旧钢笔.md': story });
  for (const code of [401, 403, 422]) {
    const mock = await mockApi(t, {
      hook({ method, route, json }) {
        if (method !== 'POST' || route !== '/api/v1/works') return false;
        json(code, { detail: 'private-debug' });
        return true;
      },
    });
    await assert.rejects(executeBooks({ ...fixture, api: mock.api, command: 'import' }), (error) => error.status === code);
    assert.equal(writes(mock.calls).length, 1);
    assert.equal(mock.works.size, 0);
  }
});

test('管理员账号密码登录后导入，不持久化登录响应', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t, { env: { HUANGGAI_ACCOUNT: 'admin', HUANGGAI_PASSWORD: 'test-password-private' } });
  assert.equal((await executeBooks({ ...fixture, api: mock.api, command: 'import' }))[0].action, 'created');
  assert.equal(mock.calls[0].route, '/api/v1/auth/login');
  const directory = path.join(fixture.stateDir, (await fs.readdir(fixture.stateDir))[0]);
  assert.ok(!(await fs.readFile(path.join(directory, 'events.jsonl'), 'utf8')).includes('test-password-private'));
});

test('重定向不跟随，避免把管理员 token 发往其他地址', async (t) => {
  const mock = await mockApi(t, {
    hook({ res }) { res.writeHead(302, { Location: '/somewhere-else' }); res.end(); return true; },
  });
  await mock.api.authenticate();
  await assert.rejects(mock.api.listWorks(), /被重定向/);
  assert.equal(mock.calls.length, 1);
});

test('发布必须确认；拒绝确认时零作品写入', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t, { initial: [remoteBook(fixture.books[0])] });
  for (const confirmPublish of [undefined, async () => false]) {
    await assert.rejects(executeBooks({ ...fixture, api: mock.api, command: 'publish', confirmPublish }), /未明确确认/);
  }
  assert.equal(writes(mock.calls).length, 0);
  assert.equal([...mock.works.values()][0].status, 'draft');
});

test('发布请求只含 status，回读验证；重复发布不重复更新', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t, { initial: [remoteBook(fixture.books[0])] });
  let confirmations = 0;
  const options = { ...fixture, api: mock.api, command: 'publish', confirmPublish: async () => { confirmations++; return true; } };
  assert.equal((await executeBooks(options))[0].action, 'published');
  assert.deepEqual(writes(mock.calls)[0].body, { status: 'published' });
  assert.equal([...mock.works.values()][0].content, fixture.books[0].content);
  assert.equal((await executeBooks(options))[0].action, 'skip');
  assert.equal(confirmations, 1);
  assert.equal(writes(mock.calls).length, 1);
});

test('发布 dry-run 不确认、不写入、不创建状态目录', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t, { initial: [remoteBook(fixture.books[0])] });
  assert.equal((await executeBooks({ ...fixture, api: mock.api, command: 'publish', dryRun: true }))[0].action, 'publish');
  assert.equal(writes(mock.calls).length, 0);
  await assert.rejects(fs.access(fixture.stateDir));
});

test('不存在、已归档或正文不匹配的作品不能发布', async (t) => {
  const fixture = await localFiles(t);
  for (const initial of [[], [remoteBook(fixture.books[0], { status: 'archived' })], [remoteBook(fixture.books[0], { content: '已修改' })]]) {
    const mock = await mockApi(t, { initial });
    const result = await executeBooks({ ...fixture, api: mock.api, command: 'publish', confirmPublish: async () => assert.fail('不应确认') });
    assert.equal(result[0].action, 'conflict');
    assert.equal(writes(mock.calls).length, 0);
  }
});

test('确认期间正文或作品 ID 改变时重新检查并拒绝发布', async (t) => {
  const fixture = await localFiles(t);
  for (const change of [{ content: '确认时有人编辑' }, { id: randomUUID() }]) {
    const mock = await mockApi(t, { initial: [remoteBook(fixture.books[0])] });
    const result = await executeBooks({
      ...fixture, api: mock.api, command: 'publish',
      confirmPublish: async () => { Object.assign([...mock.works.values()][0], change); return true; },
    });
    assert.equal(result[0].action, 'conflict');
    assert.equal(writes(mock.calls).length, 0);
  }
});

test('确认期间本地原稿改变时拒绝上传旧快照或发布', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t, { initial: [remoteBook(fixture.books[0])] });
  const result = await executeBooks({
    ...fixture, api: mock.api, command: 'publish',
    confirmPublish: async () => {
      await fs.writeFile(fixture.books[0].path, `${story}\n新增段落`);
      return true;
    },
  });
  assert.equal(result[0].action, 'conflict');
  assert.match(result[0].reason, /本地稿件/);
  assert.equal(writes(mock.calls).length, 0);
});

test('发布后正文出现并发变化时不覆盖正文，报告未核验结果', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t, {
    initial: [remoteBook(fixture.books[0])],
    hook({ method, body, works, json }) {
      if (method !== 'PUT') return false;
      const work = [...works.values()][0];
      Object.assign(work, body, { content: '请求期间他人修改的正文' });
      json(200, work);
      return true;
    },
  });
  await assert.rejects(executeBooks({
    ...fixture, api: mock.api, command: 'publish', confirmPublish: async () => true,
  }), /未通过回读核验/);
  assert.equal([...mock.works.values()][0].content, '请求期间他人修改的正文');
  assert.deepEqual(writes(mock.calls)[0].body, { status: 'published' });
  assert.equal(writes(mock.calls).length, 1);
});

test('PUT 已提交但连接断开时通过回读确认，不重发状态修改', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t, {
    initial: [remoteBook(fixture.books[0])],
    hook({ method, body, works, req }) {
      if (method !== 'PUT') return false;
      Object.assign([...works.values()][0], body);
      req.socket.destroy();
      return true;
    },
  });
  const result = await executeBooks({ ...fixture, api: mock.api, command: 'publish', confirmPublish: async () => true });
  assert.equal(result[0].action, 'reconciled');
  assert.equal(writes(mock.calls).length, 1);
  assert.deepEqual(writes(mock.calls)[0].body, { status: 'published' });
});

test('运行锁阻止同一接口并发写入，不修改已有锁', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t);
  const directory = path.join(fixture.stateDir, createHash('sha256').update(mock.base).digest('hex').slice(0, 16));
  await fs.mkdir(directory, { recursive: true });
  const lock = path.join(directory, 'run.lock');
  await fs.writeFile(lock, 'existing-lock');
  await assert.rejects(executeBooks({ ...fixture, api: mock.api, command: 'import' }), /已有运行锁/);
  assert.equal(await fs.readFile(lock, 'utf8'), 'existing-lock');
  assert.equal(writes(mock.calls).length, 0);
});

test('拒绝格式异常或重复 slug 的远端列表', async (t) => {
  const fixture = await localFiles(t);
  const work = remoteBook(fixture.books[0]);
  for (const data of [{ works: [] }, [work, work], [{ ...work, status: 'bad' }]]) {
    const mock = await mockApi(t, {
      hook({ json }) { json(200, data); return true; },
    });
    await assert.rejects(executeBooks({ ...fixture, api: mock.api, command: 'import' }), /格式无效|字段无效/);
    assert.equal(writes(mock.calls).length, 0);
  }
});

test('CLI 冲突以非零状态退出，不写入', async (t) => {
  const fixture = await localFiles(t);
  const mock = await mockApi(t, { initial: [remoteBook(fixture.books[0], { content: '不同' })] });
  // Async child is needed so the mock HTTP server can continue handling requests.
  const { spawn } = await import('node:child_process');
  const child = spawn(process.execPath, [
    entry, 'import', '--all', '--dry-run', '--books-dir', fixture.booksDir, '--batch', batch,
    '--api-base', mock.base, '--state-dir', fixture.stateDir,
  ], { env: { ...process.env, HUANGGAI_TOKEN: 'test-token-private' }, stdio: ['ignore', 'pipe', 'pipe'] });
  let output = '';
  child.stdout.on('data', (chunk) => { output += chunk; });
  const code = await new Promise((resolve) => child.on('close', resolve));
  assert.equal(code, 1);
  assert.match(output, /conflict/);
  assert.equal(writes(mock.calls).length, 0);
});
