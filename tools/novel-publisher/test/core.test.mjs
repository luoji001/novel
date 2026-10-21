import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { parseMarkdown, listBooks, readBooks, loadConfig, appendEvent, readJournal, submissionState, acquireLock } from '../core.mjs';

async function temporary(t) {
  const directory = await fs.mkdtemp(path.join(os.tmpdir(), 'novel-core-'));
  t.after(() => fs.rm(directory, { recursive: true, force: true }));
  return directory;
}

test('separates title, preserves paragraphs and literal punctuation', () => {
  const book = parseMarkdown('\uFEFF# 蓝笔\r\n\r\n他留下了 A_B、* 和 😀。\r\n\r\n## 二\r\n\r\n第二段。\r\n', '09-蓝笔.md');
  assert.equal(book.title, '蓝笔');
  assert.equal(book.body, '他留下了 A_B、* 和 😀。\n\n二\n\n第二段。');
  assert.equal(book.bodyChars, [...book.body.replace(/\s/gu, '')].length);
  assert.equal(book.hash.length, 64);
});

test('does not mistake story section dividers for YAML', () => {
  const book = parseMarkdown('# 旧物\n\n第一部分。\n\n---\n\n第二部分。\n\n---\n\n第三部分。', '01.md');
  assert.equal(book.body, '第一部分。\n\n第二部分。\n\n第三部分。');
});

test('strips only leading YAML, uses filename fallback, rejects empty content', () => {
  assert.equal(parseMarkdown('---\ncategory: fiction\n---\n# 小说\n\n正文', '01.md').title, '小说');
  assert.equal(parseMarkdown('没有标题的正文', '09-蓝笔.md').title, '蓝笔');
  assert.throws(() => parseMarkdown('# 空稿\n\n', '01.md'), /为空/);
  assert.throws(() => parseMarkdown('---\nnot closed', '01.md'), /未闭合/);
});

test('lists only first-level visible Markdown files, sorted numerically', async (t) => {
  const directory = await temporary(t);
  await fs.mkdir(path.join(directory, '.versions'));
  for (const file of ['09-蓝笔.md', '138-绣花针.md', '84-旧钢笔.md', '.hidden.md', 'notes.txt', '.versions/09.md']) {
    await fs.writeFile(path.join(directory, file), '# 题\n\n文');
  }
  assert.deepEqual((await listBooks(directory)).map((file) => path.basename(file)), ['09-蓝笔.md', '84-旧钢笔.md', '138-绣花针.md']);
});

test('deduplicates selection and never modifies sources', async (t) => {
  const directory = await temporary(t);
  const original = '# 蓝笔\n\n正文\n';
  await fs.writeFile(path.join(directory, '09-蓝笔.md'), original);
  const books = await readBooks({ booksDir: directory, books: ['09-蓝笔.md', '09-蓝笔.md'] });
  assert.equal(books.length, 1);
  assert.equal(await fs.readFile(path.join(directory, '09-蓝笔.md'), 'utf8'), original);
  await assert.rejects(() => readBooks({ booksDir: directory, books: ['09-蓝笔.md'], all: true }), /不能同时/);
});

test('example configuration cannot accidentally publish', async () => {
  const file = new URL('../platform.example.json', import.meta.url);
  // URL is accepted here as a filesystem path only after conversion.
  await assert.rejects(() => loadConfig(file.pathname, true), /未校准/);
  assert.equal((await loadConfig(file.pathname)).configured, false);
});

test('rejects missing confirmation selectors and equal field selectors', async (t) => {
  const directory = await temporary(t);
  const file = path.join(directory, 'config.json');
  const config = {
    id: 'test', configured: true, editorUrl: 'http://127.0.0.1/editor',
    fields: { title: '#title', body: '#body' }, actions: { save: { button: '#save' } },
  };
  await fs.writeFile(file, JSON.stringify(config));
  await assert.rejects(() => loadConfig(file, true), /success/);
  delete config.actions;
  config.fields.body = '#title';
  await fs.writeFile(file, JSON.stringify(config));
  await assert.rejects(() => loadConfig(file, true), /相同/);
});

test('journal distinguishes new, filled, confirmed and uncertain; malformed log blocks retry', async (t) => {
  const directory = await temporary(t);
  const file = path.join(directory, 'journal.jsonl');
  assert.deepEqual(await readJournal(file), []);
  await appendEvent(file, { hash: 'one', status: 'filled' });
  await appendEvent(file, { hash: 'two', status: 'intent' });
  await appendEvent(file, { hash: 'three', status: 'intent' });
  await appendEvent(file, { hash: 'three', status: 'confirmed' });
  const events = await readJournal(file);
  assert.equal(submissionState(events, 'one'), 'new');
  assert.equal(submissionState(events, 'two'), 'uncertain');
  assert.equal(submissionState(events, 'three'), 'confirmed');
  await fs.appendFile(file, '{broken');
  await assert.rejects(() => readJournal(file), /记录第 5 行损坏/);
});

test('lock prevents concurrent runs and can be released', async (t) => {
  const directory = await temporary(t);
  const file = path.join(directory, 'run.lock');
  const release = await acquireLock(file);
  try { await assert.rejects(() => acquireLock(file), /已有运行锁/); }
  finally { await release(); }
  const releaseAgain = await acquireLock(file);
  await releaseAgain();
});
