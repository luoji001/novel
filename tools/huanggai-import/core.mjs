import fs from 'node:fs/promises';
import path from 'node:path';
import { createHash } from 'node:crypto';

export const contentHash = (title, content) =>
  createHash('sha256').update(`${title}\0${content ?? ''}`).digest('hex');

export function parseMarkdown(raw, filename, batch) {
  if (!/^[a-z0-9][a-z0-9-]*$/.test(batch)) throw new Error('批次只能包含小写字母、数字和连字符');
  const number = filename.match(/^(\d+)[-_].+\.md$/i)?.[1];
  if (!number || !Number.isSafeInteger(Number(number)) || Number(number) > 2147483647) {
    throw new Error(`${filename}：文件名须以有效编号和连字符开头`);
  }
  const text = raw.replace(/^\uFEFF/, '').replace(/\r\n?/g, '\n');
  if (text.startsWith('---\n')) throw new Error(`${filename}：暂不支持 YAML 头部，请先人工确认正文范围`);
  const heading = text.match(/^#[ \t]+([^\n]+)(?:\n|$)/);
  const title = (heading?.[1] ?? filename.replace(/^\d+[-_]/, '').replace(/\.md$/i, '')).trim();
  // Remove the extracted title and surrounding blank lines only. Never flatten Markdown.
  const content = (heading ? text.slice(heading[0].length) : text)
    .replace(/^(?:[ \t]*\n)+/, '').replace(/(?:\n[ \t]*)+$/, '');
  if (!title || !content.trim()) throw new Error(`${filename}：标题或正文为空`);
  const slug = `${batch}-${String(Number(number)).padStart(2, '0')}`;
  if ([...title].length > 255 || slug.length > 255) throw new Error(`${filename}：标题或 slug 超过 255 字符`);
  const plain = content
    .replace(/!\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/<[^>]*>/g, '')
    .replace(/^[ \t]*(?:#{1,6}[ \t]+|>[ \t]?|[-*_]{3,}[ \t]*$)/gm, '')
    .replace(/[*_`~]/g, '').replace(/\s+/gu, ' ').trim();
  return {
    file: filename, title, content, slug, batch,
    summary: [...plain].slice(0, 160).join(''),
    sort_order: Number(number),
    hash: contentHash(title, content),
    chars: [...content.replace(/\s/gu, '')].length,
  };
}

export async function readBooks({ booksDir, books = [], all = false, batch }) {
  if (all === Boolean(books.length)) throw new Error('请选择 --all 或 --book，不能同时使用');
  const directory = await fs.realpath(booksDir);
  const files = all
    ? (await fs.readdir(directory, { withFileTypes: true }))
      .filter((item) => item.isFile() && !item.name.startsWith('.') && /\.md$/i.test(item.name))
      .map((item) => path.join(directory, item.name))
    : books.map((file) => path.resolve(directory, file));
  if (!files.length) throw new Error('目录中没有可导入的 Markdown 小说');
  const seen = new Set();
  const result = [];
  for (const file of files) {
    const realPath = await fs.realpath(file);
    if (path.dirname(realPath) !== directory || path.basename(file).startsWith('.') ||
        !(await fs.lstat(file)).isFile()) {
      throw new Error('只允许读取指定小说目录一级的普通、非隐藏 Markdown 文件');
    }
    const book = { path: realPath, ...parseMarkdown(await fs.readFile(realPath, 'utf8'), path.basename(realPath), batch) };
    if (seen.has(book.slug)) throw new Error(`本地编号重复：${book.slug}`);
    seen.add(book.slug);
    result.push(book);
  }
  return result.sort((a, b) => a.sort_order - b.sort_order);
}

export function normalizeBase(value) {
  let url;
  try { url = new URL(value); } catch { throw new Error('接口地址不是有效 URL'); }
  if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password ||
      url.search || url.hash || url.pathname !== '/') {
    throw new Error('接口地址必须是无凭据、路径或查询参数的 HTTP(S) 站点地址');
  }
  if (url.protocol === 'http:' && !['127.0.0.1', 'localhost', '[::1]'].includes(url.hostname)) {
    throw new Error('非本机接口必须使用 HTTPS，避免明文发送管理员凭据');
  }
  return url.origin;
}

export class ApiError extends Error {
  constructor(message, status = 0) {
    super(message);
    this.status = status;
  }
}

export class HuanggaiApi {
  constructor(base, { env = process.env, fetchImpl = fetch, timeoutMs = 15000 } = {}) {
    this.base = normalizeBase(base);
    this.env = env;
    this.fetch = fetchImpl;
    this.timeoutMs = timeoutMs;
  }

  async authenticate() {
    if (this.token) return;
    if (this.env.HUANGGAI_TOKEN?.trim()) {
      this.token = this.env.HUANGGAI_TOKEN.trim();
      return;
    }
    const { HUANGGAI_ACCOUNT: account, HUANGGAI_PASSWORD: password } = this.env;
    if (!account || !password) {
      throw new Error('请通过进程环境设置 HUANGGAI_TOKEN，或 HUANGGAI_ACCOUNT 和 HUANGGAI_PASSWORD；不会读取或修改 .env');
    }
    const data = await this.request('POST', '/api/v1/auth/login', { account, password }, false);
    if (typeof data?.access_token !== 'string' || !data.access_token) throw new Error('登录响应缺少 access_token');
    this.token = data.access_token;
  }

  async request(method, route, body, authenticated = true) {
    if (authenticated && !this.token) throw new Error('尚未登录');
    let response;
    try {
      response = await this.fetch(`${this.base}${route}`, {
        method, redirect: 'error', signal: AbortSignal.timeout(this.timeoutMs),
        headers: {
          'Content-Type': 'application/json',
          ...(authenticated ? { Authorization: `Bearer ${this.token}` } : {}),
        },
        ...(body === undefined ? {} : { body: JSON.stringify(body) }),
      });
    } catch {
      // Do not expose fetch error details, which can include request credentials.
      throw new ApiError(`${method} ${route}：连接失败、超时或被重定向`);
    }
    if (!response.ok) {
      const hint = response.status === 401 ? '登录已失效' : response.status === 403 ? '需要管理员权限' : '请求失败';
      // Never print a server's debug/SQL response or login request body.
      throw new ApiError(`${method} ${route}：${hint}（HTTP ${response.status}）`, response.status);
    }
    try { return await response.json(); }
    catch { throw new ApiError(`${method} ${route}：响应不是完整 JSON`, response.status); }
  }

  async listWorks() {
    const works = await this.request('GET', '/api/v1/works/admin/all');
    if (!Array.isArray(works)) throw new Error('管理端作品列表格式无效');
    const map = new Map();
    for (const work of works) {
      if (!work || typeof work.id !== 'string' || !work.id ||
          typeof work.slug !== 'string' || typeof work.title !== 'string' ||
          (work.content !== null && typeof work.content !== 'string') ||
          !['draft', 'published', 'archived'].includes(work.status) || map.has(work.slug)) {
        throw new Error('远端作品字段无效或存在重复 slug，已停止');
      }
      map.set(work.slug, work);
    }
    return map;
  }
}

export function planAction(book, remote, command) {
  if (!remote) return command === 'import'
    ? { action: 'create', reason: '新建草稿' }
    : { action: 'conflict', reason: '远端不存在，请先导入草稿' };
  if (contentHash(remote.title, remote.content) !== book.hash) {
    return { action: 'conflict', reason: '同一 slug 的标题或正文不同，不覆盖' };
  }
  if (command === 'import') return { action: 'skip', reason: `内容一致，保留现有 ${remote.status} 状态` };
  if (remote.status === 'published') return { action: 'skip', reason: '已经发布' };
  if (remote.status === 'archived') return { action: 'conflict', reason: '归档作品不自动重新发布' };
  return { action: 'publish', reason: '仅将匹配的草稿状态改为 published' };
}

async function withState(directory, base, operation) {
  const target = path.join(directory, createHash('sha256').update(base).digest('hex').slice(0, 16));
  await fs.mkdir(target, { recursive: true, mode: 0o700 });
  const lockPath = path.join(target, 'run.lock');
  let lock;
  try { lock = await fs.open(lockPath, 'wx', 0o600); }
  catch (error) {
    if (error.code === 'EEXIST') throw new Error(`已有运行锁：${lockPath}。确认原进程结束后才能手动移除此锁`);
    throw error;
  }
  try {
    await lock.writeFile(JSON.stringify({ pid: process.pid, time: new Date().toISOString() }));
    const journal = async (book, action, remote, httpStatus = null) => {
      const handle = await fs.open(path.join(target, 'events.jsonl'), 'a', 0o600);
      try {
        await handle.writeFile(`${JSON.stringify({
          time: new Date().toISOString(), endpoint: base, source: book.path,
          slug: book.slug, hash: book.hash, remoteId: remote?.id ?? null,
          action, httpStatus,
        })}\n`);
        await handle.sync();
      } finally { await handle.close(); }
    };
    return await operation(journal);
  } finally {
    await lock.close();
    await fs.unlink(lockPath);
  }
}

export async function executeBooks({
  command, books, api, dryRun = false, stateDir,
  confirmPublish, onPlan = () => {}, onResult = () => {},
}) {
  if (!['import', 'publish'].includes(command)) throw new Error('无效操作');
  if (!books.length) throw new Error('没有选中的小说');
  const sourceSlugs = new Set();
  for (const book of books) {
    if (sourceSlugs.has(book.slug) || contentHash(book.title, book.content) !== book.hash) {
      throw new Error('本地小说编号重复或哈希无效');
    }
    sourceSlugs.add(book.slug);
  }
  await api.authenticate();
  const execute = async (journal) => {
    const existing = await api.listWorks();
    const plans = books.map((book) => ({
      book, remote: existing.get(book.slug), ...planAction(book, existing.get(book.slug), command),
    }));
    await onPlan(plans);
    if (dryRun) return plans;
    const publishing = plans.filter((item) => item.action === 'publish');
    if (publishing.length && (!confirmPublish || !await confirmPublish(publishing, api.base))) {
      throw new Error('未明确确认，已取消发布；没有修改作品状态');
    }
    const results = [];
    for (const item of plans) {
      const { book } = item;
      let { remote, action, reason } = item;
      if (['create', 'publish'].includes(action)) {
        const [currentSource] = await readBooks({
          booksDir: path.dirname(book.path), books: [book.path], batch: book.batch,
        });
        if (currentSource.hash !== book.hash) {
          action = 'conflict';
          reason = '本地稿件在检查后发生变化，请重新预览；不上传旧快照';
        } else {
          // Refresh after confirmation and before each write; never trust stale preflight data.
          remote = (await api.listWorks()).get(book.slug);
          ({ action, reason } = planAction(book, remote, command));
          if (action === 'publish' && remote.id !== item.remote?.id) {
            action = 'conflict';
            reason = '作品 ID 已改变，请重新检查后再发布';
          }
        }
      }
      if (['skip', 'conflict'].includes(action)) {
        await journal(book, action, remote);
        const result = { book, remote, action, reason };
        results.push(result);
        await onResult(result);
        continue;
      }
      await journal(book, `${action}-intent`, remote);
      let writeError;
      try {
        if (action === 'create') {
          await api.request('POST', '/api/v1/works', {
            title: book.title, slug: book.slug, content: book.content, summary: book.summary,
            work_type: 'article', status: 'draft', sort_order: book.sort_order,
            cover_url: null, external_url: null,
          });
        } else {
          await api.request('PUT', `/api/v1/works/${encodeURIComponent(remote.id)}`, { status: 'published' });
        }
      } catch (error) {
        await journal(book, `${action}-request-failed`, remote, error.status ?? null);
        // Auth/validation failures are terminal. An uncertain write is reconciled, never retried.
        if (!(error instanceof ApiError) || (error.status >= 400 && error.status < 500 && error.status !== 409)) {
          throw error;
        }
        writeError = error;
      }
      let observed;
      try {
        observed = (await api.listWorks()).get(book.slug);
      } catch {
        await journal(book, `${action}-uncertain`, remote);
        throw new Error(`${book.file}：写入后无法回读核验，已停止；请检查远端后再运行，不要盲目重试`);
      }
      const matches = observed && contentHash(observed.title, observed.content) === book.hash;
      if (writeError?.status === 409 && action === 'create' && observed && !matches) {
        const result = { book, remote: observed, action: 'conflict', reason: '并发创建了不同正文，不覆盖' };
        await journal(book, 'conflict', observed, 409);
        results.push(result);
        await onResult(result);
        continue;
      }
      if (!matches || (action === 'publish' && (observed.status !== 'published' || observed.id !== remote.id))) {
        await journal(book, `${action}-uncertain`, observed, writeError?.status ?? null);
        throw new Error(`${book.file}：远端状态或正文未通过回读核验，已停止；不会自动覆盖、撤回或重试`);
      }
      const result = {
        book, remote: observed,
        action: writeError ? 'reconciled' : action === 'create' ? 'created' : 'published',
        reason: `已回读核验，远端状态：${observed.status}${writeError ? '（请求异常后对账成功，未重复写入）' : ''}`,
      };
      await journal(book, result.action, observed, writeError?.status ?? (action === 'create' ? 201 : 200));
      results.push(result);
      await onResult(result);
    }
    return results;
  };
  if (dryRun) return execute(null);
  if (!stateDir) throw new Error('写入操作需要本地运行记录目录');
  return withState(stateDir, api.base, execute);
}
