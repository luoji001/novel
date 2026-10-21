# 黄盖 Markdown 小说导入

无需安装依赖，使用 Node.js 20 或更高版本。在小说仓库根目录运行命令。

默认读取 `batches/20261019-xuanyi/codex-recommend` 一级的非隐藏 `.md` 文件，
不扫描 `.versions`，不修改、移动或覆盖原稿。与七猫浏览器发布工具相互独立。

## 1. 离线检查

```sh
node tools/huanggai-import/publisher.mjs preview --all
```

此命令不联网、不需要凭据、不写运行记录。输出标题、slug、字数和摘要。
只提取文件第一行 `# 标题`，保留正文中的 Markdown 结构；无一级标题时用文件名作为标题。
仅统一换行、去除 BOM 和正文外围的空白行。不自动处理 YAML 头部。
摘要取正文去除常见 Markdown 标记后的前 160 个可见字符。

## 2. 设置认证并检查远端

默认后端为 `http://127.0.0.1:8001`。先确保本机服务已运行，并确认它使用开发数据库。

凭据只从进程环境读取，不读取/修改项目 `.env`：

- `HUANGGAI_TOKEN`：管理员 access token，有值时优先使用。
- 或同时提供 `HUANGGAI_ACCOUNT`、`HUANGGAI_PASSWORD`：调用既有登录接口取得 token，仅存于内存。

不要把密码写进仓库文件、运行日志或命令历史。例如在本机 **zsh** 中：

```zsh
read -r "HUANGGAI_ACCOUNT?管理员账号: "
read -rs "HUANGGAI_PASSWORD?管理员密码（不回显）: "
echo
export HUANGGAI_ACCOUNT HUANGGAI_PASSWORD
node tools/huanggai-import/publisher.mjs import --all --dry-run
```

`--dry-run` 可以登录、查询，但不创建或更新作品，也不创建本地日志/锁。
非本机 API 必须使用 HTTPS；禁止跟随重定向，避免管理员凭据被转发。
脚本不会自动续期失效的 token，遇到 401/403 会停止。

## 3. 导入草稿

```sh
node tools/huanggai-import/publisher.mjs import --book 09-蓝笔.md
# 单篇核验通过后：
node tools/huanggai-import/publisher.mjs import --all
```

- 新作品固定为 `article` 类型和 `draft` 状态，排序为文件编号；封面、外链留空。
- slug 由批次和规范化编号组成，例如 `20261019-xuanyi-09`。
- 同名但不同编号的作品分别导入；同一批次的重复编号会在联网前报错。
- 同 slug、同标题和正文哈希：跳过，不改远端任何字段或状态。
- 同 slug、不同标题或正文：报告冲突并跳过，不覆盖，即使远端是草稿。
- 不同批次必须指定不同 `--batch`；同一编号的文件改名不改变 slug。

换目录时必须同时指定批次，不能用新目录意外覆盖原批次：

```sh
node tools/huanggai-import/publisher.mjs preview --all \
  --books-dir /path/to/books --batch 20261020-xuanyi
```

## 4. 审核与公开

打开本机前端 `/admin/works`，登录管理员后点击“预览”。
草稿预览不会触发保存或发布；公开接口仍只返回已发布作品。
后台支持多行 Markdown 编辑、阅读预览及状态/类型选择。

**本地稿件与后台正文必须一致，才能通过脚本发布。** 如果在后台人工改稿，
先自行核对并同步本地；脚本不会代为覆盖任意一侧。

```sh
node tools/huanggai-import/publisher.mjs publish --book 09-蓝笔.md --dry-run
node tools/huanggai-import/publisher.mjs publish --book 09-蓝笔.md
```

真实发布必须在交互终端输入“发布”。不提供 `--yes`，不支持 `publish --all`；
可以重复 `--book` 明确选择多篇。只发送 `{"status":"published"}`，不上传正文。
真实写入前再次读取源文件；预览/确认期间本地原稿变化时报告冲突，不上传旧快照。
正文不一致、不存在或已归档的作品拒绝发布；已经发布且内容一致的作品跳过。
检查通过后先改状态，再回读核验；公开地址是前端 `/works/<slug>`。

现有后端没有条件更新/乐观锁，因此发布期间不要同时在别处编辑、删除或更改作品状态。
脚本在确认后、每次请求前重新检查，并在请求后回读，但不能代替服务端原子条件更新。

## 5. 日志、失败恢复与测试

真实写入使用 `state/huanggai-import/<接口地址哈希>/` 的单实例锁与 JSONL 日志，
已加入 Git 忽略。日志仅包含时间、接口、源路径、slug、标题正文哈希、远端 ID、
动作及 HTTP 状态，不包含凭据或正文。可用 `--state-dir` 指定其他私有目录。

409、断线、超时、服务端错误或响应损坏后，脚本会查询 slug 对账，不自动重发写请求。
如果不能确认结果，则记录 `uncertain` 并停止。先在后台核对，再重新 dry-run；
重跑会根据远端真实内容决定跳过、创建或冲突，不依据旧日志盲目重试。
强制终止后可能残留 `run.lock`，必须先确认旧进程已结束，才能手动移除。
一批中已成功的草稿不会自动回滚或删除。

存在冲突或错误时进程非零退出。结束后可清理当前 shell 的凭据：

```sh
unset HUANGGAI_ACCOUNT HUANGGAI_PASSWORD HUANGGAI_TOKEN
node --test tools/huanggai-import/test/*.test.mjs
```

可选前端真实浏览器检查（使用临时模拟 API，不向真实后端写数据）：

```sh
node --test tools/huanggai-import/test/frontend.browser.mjs
```

此检查复用 `tools/novel-publisher` 中已安装的 Playwright，默认前端位于同级工作区的
`information-github/next-huanggai`，浏览器为本机 Chrome。可通过
`HUANGGAI_FRONTEND_DIR`、`HUANGGAI_TEST_CHROME` 覆盖路径。测试自行启动并关闭临时端口服务，
截图写入系统临时目录。

如果运行环境无法启动 Chrome，可明确设置 `HUANGGAI_SKIP_BROWSER=1` 仅执行真实 Next.js
HTTP/SSR 检查（公开列表、Markdown 安全输出、排版样式、草稿 404）。
此模式会标记浏览器交互检查为跳过，不代表手机视口或后台交互已经验收。

前端按 Markdown 渲染正文，禁用原始 HTML，不迁移已有数据库内容。
如果旧作品保存的是 HTML 而非模型约定的 Markdown，应另行人工整理，不能依赖旧的 HTML 直出行为。
