import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import { existsSync } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import http from 'node:http';
import { promisify } from 'node:util';
import { execFile } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright';
import { readJournal, parseMarkdown } from '../core.mjs';

const execute = promisify(execFile);
const script = fileURLToPath(new URL('../publisher.mjs', import.meta.url));
const chrome = process.env.NOVEL_PUBLISHER_CHROME ||
  ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/Applications/Chromium.app/Contents/MacOS/Chromium', chromium.executablePath()].find(existsSync);

test('browser flows on local mock website only', { skip: !chrome && '安装 Chrome 或 npx playwright install chromium 后运行' }, async (t) => {
  // Check the runtime once rather than spawning a failing browser for every case.
  let probe;
  try { probe = await chromium.launch({ executablePath: chrome, headless: true }); }
  catch (error) { throw new Error(`浏览器无法启动，网页测试尚未执行：${error.message}`); }
  finally { await probe?.close(); }
  const requests = [];
  const visits = [];
  const server = http.createServer(async (req, res) => {
    try {
      const url = new URL(req.url, 'http://localhost');
      if (url.pathname.startsWith('/record/')) {
        let data = '';
        for await (const chunk of req) data += chunk;
        requests.push({ token: url.pathname.split('/')[2], ...JSON.parse(data) });
        res.writeHead(200, { 'content-type': 'application/json' }).end('{"ok":true}');
        return;
      }
      if (!url.pathname.startsWith('/editor/')) { res.writeHead(404).end(); return; }
      const [, , token, scenario] = url.pathname.split('/');
      visits.push(token);
      const body = scenario === 'editable' ? '<div id="body" contenteditable="true" style="white-space:pre-wrap"></div>' :
        scenario === 'iframe' ? '<iframe id="editor" srcdoc="<body contenteditable=true></body>"></iframe>' :
        `<textarea id="body" ${scenario === 'truncated' ? 'maxlength="5"' : ''}></textarea>`;
      const initial = scenario === 'existing' ? 'value="已有作品"' : '';
      res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' }).end(`<!doctype html>
        <html><body><input id="title" class="title" ${initial}>
        ${scenario === 'ambiguous' ? '<input id="other-title" class="title">' : ''}
        ${body}
        <button id="save">保存草稿</button><button id="publish">发布</button>
        <p id="success" ${scenario === 'stale' ? '' : 'hidden'}>操作成功</p>
        <script>
          for (const action of ['save', 'publish']) {
            document.getElementById(action).onclick = async () => {
              const body = document.getElementById('body');
              const text = body ? ('value' in body ? body.value : body.innerText) :
                document.getElementById('editor').contentDocument.body.innerText;
              const response = await fetch('/record/${token}', {
                method: 'POST', headers: {'content-type':'application/json'},
                body: JSON.stringify({action, title: document.getElementById('title').value, body: text})
              });
              if (response.ok && ${JSON.stringify(scenario !== 'uncertain')}) document.getElementById('success').hidden = false;
            };
          }
        </script></body></html>`);
    } catch {
      res.writeHead(500).end();
    }
  });
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  t.after(() => new Promise((resolve) => server.close(resolve)));
  const origin = `http://127.0.0.1:${server.address().port}`;

  async function fixture(child, scenario = 'normal', count = 1) {
    const directory = await fs.mkdtemp(path.join(os.tmpdir(), 'novel-browser-'));
    child.after(() => fs.rm(directory, { recursive: true, force: true }));
    const token = path.basename(directory);
    const booksDir = path.join(directory, 'books');
    await fs.mkdir(booksDir);
    const originals = [];
    for (let i = 0; i < count; i++) {
      const raw = `# 小说${i + 1}\n\n第一段${i + 1}，保留 _、* 和😀。\n\n第二段，不能截断。\n`;
      const file = `${i + 1}-小说.md`;
      originals.push({ file, raw, ...parseMarkdown(raw, file) });
      await fs.writeFile(path.join(booksDir, file), raw);
    }
    await fs.mkdir(path.join(booksDir, '.versions'));
    await fs.writeFile(path.join(booksDir, '.versions/backup.md'), '# 不应发布\n\n备份');
    const config = {
      id: 'mock', configured: true, editorUrl: `${origin}/editor/${token}/${scenario}`, timeoutMs: 1500,
      fields: { title: scenario === 'ambiguous' ? '.title' : '#title', body: scenario === 'iframe' ? { frame: '#editor', selector: 'body[contenteditable]' } : '#body' },
      actions: { save: { button: '#save', success: '#success' }, publish: { button: '#publish', success: '#success' } },
    };
    const configPath = path.join(directory, 'config.json');
    await fs.writeFile(configPath, JSON.stringify(config));
    const state = path.join(directory, 'state');
    const journal = path.join(state, 'mock', 'publish-log.jsonl');
    async function run(...flags) {
      try {
        const result = await execute(process.execPath, [script, 'run', '--config', configPath,
          '--books-dir', booksDir, '--state-dir', state, '--all', '--yes', '--headless', ...flags], {
          timeout: 30000, env: { ...process.env, NOVEL_PUBLISHER_CHROME: chrome }, maxBuffer: 2 ** 20,
        });
        return { ...result, code: 0 };
      } catch (error) {
        if (error.killed) throw error;
        return { stdout: error.stdout, stderr: error.stderr, code: error.code };
      }
    }
    return {
      run, directory, booksDir, originals, journal, token,
      records: () => requests.filter((request) => request.token === token),
    };
  }

  await t.test('batch saves separate complete stories, skips backups and deduplicates retries', async (child) => {
    const f = await fixture(child, 'normal', 2);
    const first = await f.run('--save-draft');
    assert.equal(first.code, 0, first.stderr);
    assert.deepEqual(f.records().map(({ title, body, action }) => ({ title, body, action })),
      f.originals.map(({ title, body }) => ({ title, body, action: 'save' })));
    assert.equal(visits.filter((token) => token === f.token).length, 2);
    assert.equal((await readJournal(f.journal)).filter((event) => event.status === 'confirmed').length, 2);
    const second = await f.run('--save-draft');
    assert.equal(second.code, 0, second.stderr);
    assert.match(second.stdout, /跳过已确认/);
    assert.equal(f.records().length, 2);
    const publishExisting = await f.run('--publish');
    assert.equal(publishExisting.code, 0, publishExisting.stderr);
    assert.equal(f.records().length, 2);
    for (const book of f.originals) assert.equal(await fs.readFile(path.join(f.booksDir, book.file), 'utf8'), book.raw);
  });

  await t.test('explicit publish waits for its success signal', async (child) => {
    const f = await fixture(child);
    const result = await f.run('--publish');
    assert.equal(result.code, 0, result.stderr);
    assert.equal(f.records().length, 1);
    assert.equal(f.records()[0].action, 'publish');
    assert.equal((await readJournal(f.journal)).at(-1).status, 'confirmed');
  });

  await t.test('default fill mode never clicks save or publish', async (child) => {
    const f = await fixture(child);
    const result = await f.run();
    assert.equal(result.code, 0, result.stderr);
    assert.equal(f.records().length, 0);
    assert.equal((await readJournal(f.journal)).at(-1).status, 'filled');
  });

  for (const scenario of ['editable', 'iframe']) {
    await t.test(`fills ${scenario} editors without changing text`, async (child) => {
      const f = await fixture(child, scenario);
      const result = await f.run('--save-draft');
      assert.equal(result.code, 0, result.stderr);
      assert.equal(f.records()[0].body, f.originals[0].body);
    });
  }

  for (const [scenario, expected] of [
    ['existing', /已有内容，拒绝覆盖/],
    ['ambiguous', /匹配到多个/],
    ['truncated', /回读不一致/],
    ['stale', /点击前已出现/],
  ]) {
    await t.test(`refuses unsafe ${scenario} page before submit`, async (child) => {
      const f = await fixture(child, scenario);
      const result = await f.run('--save-draft');
      assert.equal(result.code, 1, result.stderr);
      assert.match(result.stderr, expected);
      assert.equal(f.records().length, 0);
      assert.equal((await readJournal(f.journal)).length, 0);
      await assert.rejects(() => fs.access(path.join(f.directory, 'state/mock/run.lock')), { code: 'ENOENT' });
    });
  }

  await t.test('unknown submit result stops batch and refuses automatic retry', async (child) => {
    const f = await fixture(child, 'uncertain', 2);
    const result = await f.run('--save-draft');
    assert.equal(result.code, 1, result.stderr);
    assert.match(result.stderr, /未确认提交结果/);
    assert.equal(f.records().length, 1);
    assert.equal((await readJournal(f.journal)).at(-1).status, 'uncertain');
    const retry = await f.run('--save-draft');
    assert.equal(retry.code, 1, retry.stderr);
    assert.match(retry.stderr, /上次提交结果不确定/);
    assert.equal(f.records().length, 1);
  });
});
