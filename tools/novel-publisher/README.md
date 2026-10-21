# 小说发布助手

**当前状态：通用浏览器工具，不是已验证的番茄、七猫或豆瓣适配器。** 这些平台登录后的实际字段、创建作品流程和成功信号需要先校准；示例域名和选择器不能直接用于发布。不使用猜测的接口或输入框，不绕过验证码，不修改小说文件。

## 七猫专用入口

已加入 `npm run qimao:setup`（登录并在真实页面点选标题、正文、保存按钮）以及 `npm run qimao -- --book 09-蓝笔.md --save-draft`。无需手工猜选择器；未预设不存在的编辑路由。使用步骤、人工确认和未联调的限制见 [QIMAO.md](QIMAO.md)。

## 已实现

- 默认读取 `batches/20261019-xuanyi/codex-recommend`，忽略 `.versions` 等子目录。
- Markdown 首行标题与正文分离；去掉章节标题的 `#` 和分隔线，保留段落及其余字符，不改写原稿。
- 本机 Chrome 保留登录会话，支持手工登录、检查字段、单篇填稿、批量保存草稿和显式发布。
- 默认只填稿，**不点击保存或发布**；平台编辑器自身可能自动保存。
- 拒绝覆盖已有内容、歧义字段、截断正文；每篇重新进入新建页面。
- 保存/发布后等待配置的成功信号，不把“点过按钮”当作成功。信号是否能代表真实提交成功，需要平台校准时确认。
- 本地记录内容摘要防止同一平台重复提交；提交结果未知则停止，不盲目重试。

## 安装和预览

```bash
cd /Users/luoji/information-novel/novel/tools/novel-publisher
npm ci
npm run list
npm run preview -- --all
npm run preview -- --book 09-蓝笔.md
```

本机没有 Chrome 时运行 `npx playwright install chromium` 并使用 `--browser chromium`，或者用环境变量 `NOVEL_PUBLISHER_CHROME` 指定浏览器可执行文件。

## 先校准目标平台

```bash
cp platform.example.json platform.local.json
```

1. 将 `id` 改成平台/账号的唯一标识，例如 `fanqie-myaccount`。**同一账号保持同一 id**，否则无法复用去重记录。
2. 设置 `loginUrl` 和 `editorUrl`。后者必须是**新建一篇独立作品的空白编辑页**，不能是已有稿件、已有书籍的章节编辑页或仅作者中心首页。无法直接进入空白页的平台还需补充创建作品流程，当前脚本不会替你猜测。
3. 运行下面命令，人工登录并进入编辑页：

   ```bash
   node publisher.mjs login --config platform.local.json
   node publisher.mjs inspect --config platform.local.json
   ```

4. 根据浏览器开发者工具及 `state/novel-publisher/<id>/fields.json` 设置 `fields.title`、`fields.body` 的精确选择器。`inspect` 不输出输入框值或会话信息。嵌入式编辑器支持：

   ```json
   { "selector": "body[contenteditable=true]", "frame": "iframe#editor" }
   ```

5. 若要自动保存，设置 `actions.save.button` 和 `actions.save.success`；发布同理。成功选择器应指向**操作后才出现、且确实表示成功的元素**。需要多步骤确认的发布流程暂不支持，不能把“下一步”配置成“发布成功”。
6. 将 `configured` 改成 `true`。先用一篇测试填稿，再检查正文、分类、简介、字数限制等；未配置的分类、封面、声明等由人工处理。

**不要把示例选择器当成任何平台的真实字段。** 特殊富文本编辑器若不能通过 `fill` 完整输入，脚本会报错停止，需要补充平台专用适配。

## 填稿、草稿和发布

仅填稿，检查后按回车关闭：

```bash
npm run run -- --config platform.local.json --book 09-蓝笔.md
```

批量保存草稿（每篇从空白页面开始）：

```bash
npm run run -- --config platform.local.json --all --save-draft
```

显式发布，终端还会要求输入“发布”确认：

```bash
npm run run -- --config platform.local.json --book 09-蓝笔.md --publish
```

已手动登录、测试过正确页面并确保所有必要字段可自动完成后，才可加 `--yes` 跳过人工等待。无界面模式还需 `--headless`。不自动处理验证码、实名、签约或平台协议。发布前自行检查内容权利、AI 内容标识要求和平台自动化规则。

## 状态和异常恢复

状态保存在 `state/novel-publisher/<id>/`，已加入 Git 忽略：

- `profile/`：登录会话，等同敏感凭证，不要分享。
- `publish-log.jsonl`：每次操作前写入 `intent`，收到成功信号后写入 `confirmed`。
- `error-*.png`：失败时的页面截图，可能包含账号信息。
- `run.lock`：避免两个进程同时操作同一平台配置。异常退出后，确认旧进程已结束才能删除残留锁。

相同内容已经保存为草稿后，再用 `--publish` 会跳过，**不会新建重复作品**；请在平台打开已有草稿手工发布。去重是本地的，不能发现其他电脑、其他工具或修改过内容后产生的重复稿件。

若有 `intent`/`uncertain` 而无 `confirmed`，先在平台人工核对，脚本不会重试。确认已保存/已发布后，可在日志末尾添加同一 `hash` 的 `confirmed` 记录；确认未提交后，备份日志再删除该 `hash` 的所有 `intent`/`uncertain` 记录才可重跑。**未核对前不要删除记录。** 损坏的日志同样会阻止提交。

## 测试

```bash
npm test
npm run test:browser
```

`npm test` 运行不依赖浏览器的读稿、配置、日志、点选选择器和 CLI 测试。`npm run test:browser` 需能启动 Chrome，使用临时目录和本地模拟发布页验证草稿/发布流程、正文回读、去重、覆盖保护和异常停止；不访问或发布到真实平台。若 Chrome 启动失败，会明确报错，不能视为网页流程已验证。
