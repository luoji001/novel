#!/usr/bin/env node
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';
import { createInterface } from 'node:readline/promises';
import { HuanggaiApi, executeBooks, readBooks } from './core.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const HELP = `
黄盖小说导入助手（只读原稿，默认草稿）

  node tools/huanggai-import/publisher.mjs preview --all
  node tools/huanggai-import/publisher.mjs import --all --dry-run
  node tools/huanggai-import/publisher.mjs import --all
  node tools/huanggai-import/publisher.mjs publish --book 09-蓝笔.md

--all               选择目录一级非隐藏 .md；publish 禁用
--book <文件名>      明确选稿，可重复；不能与 --all 同用
--books-dir <目录>   默认 batches/20261019-xuanyi/codex-recommend
--batch <批次>       默认 20261019-xuanyi；slug 为批次加文件编号
--api-base <地址>    默认 http://127.0.0.1:8001；非本机须 HTTPS
--state-dir <目录>   默认 state/huanggai-import（按接口地址隔离）
--dry-run           import/publish 只读远端检查，不修改作品、不写运行记录
--help              显示帮助

preview 完全离线；import 只创建草稿，不更新已有正文。
publish 只改状态，必须逐项 --book 选稿，并在交互终端输入“发布”。
认证从进程环境读取 HUANGGAI_TOKEN，或 HUANGGAI_ACCOUNT/HUANGGAI_PASSWORD。
不会读取或修改 .env，不会保存或输出凭据。
`;

export function parseArgs(argv) {
  const args = { command: argv[0] ?? 'help', books: [], all: false, dryRun: false };
  const values = {
    '--book': 'book', '--books-dir': 'booksDir', '--batch': 'batch',
    '--api-base': 'apiBase', '--state-dir': 'stateDir',
  };
  for (let i = 1; i < argv.length; i++) {
    const flag = argv[i];
    if (flag === '--help' || flag === '-h') { args.command = 'help'; continue; }
    if (flag === '--all') { args.all = true; continue; }
    if (flag === '--dry-run') { args.dryRun = true; continue; }
    const key = values[flag];
    if (!key) throw new Error(`未知参数：${flag}`);
    const value = argv[++i];
    if (!value || value.startsWith('--')) throw new Error(`${flag} 缺少参数值`);
    if (key === 'book') args.books.push(value); else args[key] = value;
  }
  if (['--help', '-h'].includes(args.command)) args.command = 'help';
  if (!['help', 'preview', 'import', 'publish'].includes(args.command)) throw new Error('未知命令，使用 --help 查看帮助');
  if (args.command !== 'help') {
    if (args.all === Boolean(args.books.length)) throw new Error('请选择 --all 或 --book，不能同时使用');
    if (args.command === 'publish' && args.all) throw new Error('publish 禁用 --all，必须用 --book 明确选稿');
    if (args.command === 'preview' && args.dryRun) throw new Error('preview 本来就完全离线，无需 --dry-run');
    if (args.booksDir && !args.batch) throw new Error('更换小说目录时必须同时明确 --batch，避免与原批次混淆');
  }
  args.booksDir = path.resolve(args.booksDir ?? path.join(root, 'batches/20261019-xuanyi/codex-recommend'));
  args.batch ??= '20261019-xuanyi';
  args.apiBase ??= 'http://127.0.0.1:8001';
  args.stateDir = path.resolve(args.stateDir ?? path.join(root, 'state/huanggai-import'));
  return args;
}

function printBook(book) {
  console.log(`${book.file} → 《${book.title}》 | ${book.slug} | 正文 ${book.chars} 字`);
  console.log(`  摘要：${book.summary}`);
}

async function confirmPublish(items, base) {
  if (!process.stdin.isTTY || !process.stdout.isTTY) {
    throw new Error('公开发布必须在交互终端人工确认；非交互环境可用 publish --dry-run 检查');
  }
  console.log(`\n将向 ${base} 公开发布 ${items.length} 篇：`);
  for (const { book } of items) console.log(`  ${book.file} → ${book.slug}`);
  const readline = createInterface({ input: process.stdin, output: process.stdout });
  try { return (await readline.question('仅修改状态，不上传正文。输入“发布”继续：')) === '发布'; }
  finally { readline.close(); }
}

export async function main(argv = process.argv.slice(2)) {
  const args = parseArgs(argv);
  if (args.command === 'help') { console.log(HELP); return; }
  const books = await readBooks(args);
  if (args.command === 'preview') {
    for (const book of books) printBook(book);
    console.log(`\n共 ${books.length} 篇；未联网，未写入原稿或平台。`);
    return;
  }
  const api = new HuanggaiApi(args.apiBase);
  console.log(`目标：${api.base} | ${args.dryRun ? '只读检查' : args.command === 'import' ? '导入草稿' : '准备公开发布'}`);
  const results = await executeBooks({
    ...args, books, api, confirmPublish,
    onPlan(plans) {
      for (const item of plans) {
        printBook(item.book);
        console.log(`  计划：${item.action} — ${item.reason}`);
      }
    },
    onResult({ book, action, reason }) { console.log(`[${action}] ${book.file}：${reason}`); },
  });
  const counts = {};
  for (const { action } of results) counts[action] = (counts[action] ?? 0) + 1;
  console.log(`\n${args.dryRun ? '检查完成（未修改作品）' : '处理完成'}：${JSON.stringify(counts)}`);
  if (results.some((item) => item.action === 'conflict')) process.exitCode = 1;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch((error) => {
    console.error(`错误：${error.message}`);
    process.exitCode = 1;
  });
}
