import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { fileURLToPath } from 'node:url';
import { selectorForElement, pickField } from '../calibration.mjs';
import { loadConfig } from '../core.mjs';

const execute = promisify(execFile);
const script = fileURLToPath(new URL('../publisher.mjs', import.meta.url));
const preset = fileURLToPath(new URL('../platforms/qimao.json', import.meta.url));

test('uses a unique id from the selected real element', () => {
  const element = {
    tagName: 'INPUT', getAttribute: (key) => key === 'id' ? 'story-title' : null,
    ownerDocument: { querySelectorAll: (selector) => selector === 'input[id="story-title"]' ? [element] : [] },
  };
  assert.equal(selectorForElement(element), 'input[id="story-title"]');
});

test('skips duplicate ids and uses a unique placeholder instead', () => {
  const element = {
    tagName: 'INPUT',
    getAttribute: (key) => ({ id: 'duplicate', placeholder: '请输入作品标题' })[key],
    ownerDocument: { querySelectorAll: (selector) => selector === 'input[id="duplicate"]' ? [element, {}] :
      selector === 'input[placeholder="请输入作品标题"]' ? [element] : [] },
  };
  assert.equal(selectorForElement(element), 'input[placeholder="请输入作品标题"]');
});

test('uses a unique structural selector when the element has no attributes', () => {
  const document = { querySelectorAll: (selector) => selector === 'div > textarea:nth-of-type(2)' ? [second] : [] };
  const parent = { tagName: 'DIV', parentElement: null, ownerDocument: document };
  const first = { tagName: 'TEXTAREA', parentElement: parent };
  const second = { tagName: 'TEXTAREA', parentElement: parent, getAttribute: () => null, ownerDocument: document };
  parent.children = [first, second];
  assert.equal(selectorForElement(second), 'div > textarea:nth-of-type(2)');
});

test('picker uses serializable binding arguments, retrieves element handle, cleans up', async () => {
  let callback;
  let handleDisposed = false;
  let bindingDisposed = false;
  let listenersCleaned = false;
  const element = {
    nodeType: 1, tagName: 'TEXTAREA', getAttribute: (key) => key === 'id' ? 'body' : null,
    ownerDocument: { querySelectorAll: () => [element] },
  };
  const frame = {
    evaluate: async (_fn, arg) => {
      if (typeof arg === 'object') queueMicrotask(() => callback({ frame }, true));
      else listenersCleaned = true;
    },
    evaluateHandle: async () => ({
      evaluate: async (fn) => fn(element),
      dispose: async () => { handleDisposed = true; },
    }),
  };
  const page = {
    once: () => {}, off: () => {}, mainFrame: () => frame, frames: () => [frame],
    exposeBinding: async (...args) => {
      assert.equal(args.length, 2, 'removed Playwright handle option must not be used');
      callback = args[1];
      return { dispose: async () => { bindingDisposed = true; } };
    },
  };
  assert.equal(await pickField(page, 'body', '正文'), 'textarea[id="body"]');
  assert.ok(handleDisposed && bindingDisposed && listenersCleaned);
});

test('Qimao preset has a login entry but no fabricated editor selectors', async () => {
  const config = await loadConfig(preset);
  assert.equal(config.loginUrl, 'https://zuozhe.qimao.com/');
  assert.equal(config.configured, false);
  assert.equal(config.fields, undefined);
  await assert.rejects(() => loadConfig(preset, true), /未校准/);
});

test('accepts calibrated manual confirmation, refuses unattended Qimao runs', async (t) => {
  const directory = await fs.mkdtemp(path.join(os.tmpdir(), 'qimao-test-'));
  t.after(() => fs.rm(directory, { recursive: true, force: true }));
  const file = path.join(directory, 'qimao.local.json');
  await fs.writeFile(file, JSON.stringify({
    id: 'qimao', configured: true, editorUrl: 'https://zuozhe.qimao.com/', manualNewEntry: true,
    fields: { title: '#selected-title', body: '#selected-body' },
    actions: { save: { button: '#selected-save', success: { manual: true } } },
  }));
  assert.equal((await loadConfig(file, true)).actions.save.success.manual, true);
  await assert.rejects(() => execute(process.execPath, [script, 'run', '--config', file, '--book', '09-蓝笔.md', '--save-draft', '--yes']),
    (error) => error.code === 1 && /不能使用 --yes/.test(error.stderr));
});

test('setup requires interactive terminal and never starts headless calibration', async () => {
  await assert.rejects(() => execute(process.execPath, [script, 'setup', '--config', preset, '--output', 'qimao.local.json', '--headless', '--yes']),
    (error) => error.code === 1 && /需要人工交互/.test(error.stderr));
  await assert.rejects(() => execute(process.execPath, [script, 'setup', '--config', preset, '--output', 'qimao.local.json']),
    (error) => error.code === 1 && /需要交互终端/.test(error.stderr));
});

test('setup requires an explicit destination, rejects unknown browser type', async () => {
  await assert.rejects(() => execute(process.execPath, [script, 'setup', '--config', preset]),
    (error) => error.code === 1 && /必须使用 --output/.test(error.stderr));
  await assert.rejects(() => execute(process.execPath, [script, 'list', '--browser', 'unknown']),
    (error) => error.code === 1 && /--browser 只能/.test(error.stderr));
});
