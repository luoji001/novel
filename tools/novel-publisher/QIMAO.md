# 七猫辅助发布

## 状态与边界

提供七猫作者后台入口、登录会话、**在真实页面点选字段的一次性校准**和填稿/草稿/发布命令。没有编造七猫后台的接口、编辑页路由、字段或保存成功提示。

**当前尚未用真实七猫账号完成联调，不能宣称全自动发布已可用。** 分类、封面、简介、平台声明、创建独立作品和提交结果仍需要人工检查。菜单名称、要求和发布步骤以登录后的实际页面为准。

## 首次运行：登录并点选字段

```bash
cd /Users/luoji/information-novel/novel/tools/novel-publisher
npm ci
npm run qimao:setup
```

1. 浏览器打开七猫作者后台，人工登录、处理验证码和必要的账号验证。
2. 找到短故事创作入口，进入一篇**新的独立短故事**的空白编辑页，不是已有作品/章节。
3. 在终端按回车，再依次在浏览器点击：**标题输入框 → 正文编辑框 → 保存草稿按钮**。
4. 点选期间脚本拦截点击，读取实际元素的选择器，不主动执行原按钮。不填写正文，不主动提交草稿或发布。
5. 配置写入 `qimao.local.json`，登录会话保存在项目的 `state/novel-publisher/qimao/profile/`。这两处均不加入 Git，请勿分享。

如果作品页面自动创建草稿，这是网站自身行为；请自行清理空白测试稿。首次不要使用重要的已有稿件校准。

仅登录、不校准：

```bash
npm run qimao:login
```

## 先试一篇

```bash
# 只填稿，脚本不点击保存或发布
npm run qimao -- --book 09-蓝笔.md

# 填稿并点击保存草稿，随后人工核对成功
npm run qimao -- --book 09-蓝笔.md --save-draft
```

脚本暂停时，请手工进入空白的新建页，并补全分类、简介等必填信息。按回车后填入标题/正文；只要原输入框有内容，就拒绝覆盖。

点击保存之后，**请在七猫页面确认已保存，再在终端输入 `已保存`**。直接回车表示失败或结果不确定，脚本会停止，避免重复提交。不要把“弹窗打开了”当成保存成功。

## 批量

```bash
npm run qimao -- --all --save-draft
```

每一篇开始前仍需手工进入独立作品的空白新建页；脚本不猜测七猫的多步创建流程。校准配置禁止 `--yes`/`--headless` 跳过这些检查。要做到无人值守，还需要根据真实账号后台补齐新建流程及机器可验证的成功信号。

本地日志会跳过已确认提交过的相同标题和正文；不会扫描或改动小说文件。

## 需要发布按钮时

首次校准不记录发布按钮。确实需要时，以新文件重新校准：

```bash
npm run qimao:setup -- --publish --output qimao-publish.local.json
node publisher.mjs run --config qimao-publish.local.json --book 09-蓝笔.md --publish
```

校准发布按钮本身不发布。运行发布命令后，终端会先要求输入 `发布`，脚本填稿并点击所选按钮；后续确认窗、声明或付费设置请人工处理，确认真实发布后才输入 `已发布`。

**已经保存为草稿的相同内容不会被重新创建。** 需要发布已有草稿时，请直接在七猫后台打开并发布，避免重复作品。签约或独家作品跨平台投稿前请检查自己的协议。

## Chrome 启动失败

可尝试安装 Playwright 自带的 Chromium，再指定浏览器：

```bash
npx playwright install chromium
npm run qimao:setup -- --browser chromium
npm run qimao -- --book 09-蓝笔.md --save-draft --browser chromium
```

这只能排查本机 Chrome 兼容问题，不能保证解决系统进程权限或网络问题。校准需要可交互的本机终端，不要在无 TTY 环境运行。

校准文件已存在时不会覆盖；需要重做请使用新的 `--output xxx.local.json`，运行时相应指定 `--config xxx.local.json`。异常提交记录和截图的处理见 [README.md](README.md)。
