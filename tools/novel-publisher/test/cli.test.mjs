import test from 'node:test';
import assert from 'node:assert/strict';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { fileURLToPath } from 'node:url';

const execute = promisify(execFile);
const script = fileURLToPath(new URL('../publisher.mjs', import.meta.url));
const example = fileURLToPath(new URL('../platform.example.json', import.meta.url));

test('help is available without launching a browser', async () => {
  const result = await execute(process.execPath, [script, '--help']);
  assert.match(result.stdout, /默认只填稿/);
});

test('rejects mutually exclusive actions before launching a browser', async () => {
  await assert.rejects(() => execute(process.execPath, [script, 'run', '--save-draft', '--publish']),
    (error) => error.code === 1 && /不能同时/.test(error.stderr));
});

test('requires a value for each option', async () => {
  await assert.rejects(() => execute(process.execPath, [script, 'preview', '--book', '--all']),
    (error) => error.code === 1 && /缺少参数值/.test(error.stderr));
});

test('example config cannot run even in explicit publish mode', async () => {
  await assert.rejects(() => execute(process.execPath, [
    script, 'run', '--config', example, '--book', '09-蓝笔.md', '--publish', '--yes',
  ]), (error) => error.code === 1 && /未校准/.test(error.stderr));
});

test('preview reads all five recommended novels without browser dependencies', async () => {
  const result = await execute(process.execPath, [script, 'preview', '--all']);
  const books = JSON.parse(result.stdout);
  assert.equal(books.length, 5);
  assert.equal(books[0].title, '蓝笔');
  assert.ok(books.every((book) => book.bodyChars > 0 && book.hash.length === 64));
  assert.ok(books.every((book) => !book.path.includes('.versions')));
});
