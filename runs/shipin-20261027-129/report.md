# 二维码 生成报告

slug：`shipin-20261027-129`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6575
LLM 调用：57 次，累计 177.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫码五分钟后 | 623 | short | 38.0 | 0 |  | 1 |
| 2 | 扫码五分钟后 | 1287 | normal | 92.9 | 0 |  | 3 |
| 3 | 手机屏幕反光 | 1069 | normal | 89.9 | 0 |  | 0 |
| 4 | 手机屏幕反光 | 1356 | normal | 92.2 | 0 |  | 2 |
| 5 | 手机屏幕反光 | 1092 | normal | 90.0 | 0 |  | 3 |
| 6 | 手机屏幕反光 | 1142 | normal | 92.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 551 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「陈阿婆的」×5
  - narration_para_pct 26.1 低于目标 35.0
  - [observe] 标题重复：「扫码五分钟后」已存在
- 第 4 章：
  - narration_para_pct 20.0 低于目标 35.0
  - [observe] 标题重复：「手机屏幕反光」已存在
- 第 5 章：
  - 单条套路句式超限：「周志远的」×3
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 标题重复：「手机屏幕反光」已存在
- 第 6 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 标题重复：「手机屏幕反光」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6171
chapter_chars_mean: 1028
chapter_chars_median: 1044
chapter_chars_cv: 0.25
paragraphs_mean: 26.2
dialogue_chars_pct: 24.6
dialogue_para_pct: 64.7
interiority_para_pct: 0.0
narration_para_pct: 35.3
turn_under20_pct: 91.9
turn_over200_pct: 0.0
attr_say_pct: 23.3
attr_adv_pct: 3.0
scenes_per_chapter: 1.2
dialogue_run_mean: 2.8
turn_len_median: 8
```
