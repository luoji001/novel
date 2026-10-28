# 红绳 生成报告

slug：`shipin-20261027-27`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5558
LLM 调用：57 次，累计 114.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 雪铲撬后备箱 | 402 | short | 38.8 | 0 |  | 1 |
| 2 | 扳手敲引擎盖 | 1036 | normal | 96.2 | 0 |  | 0 |
| 3 | 对讲机呼救援 | 1119 | normal | 94.0 | 0 |  | 0 |
| 4 | 轮胎滚落雪地 | 1056 | normal | 93.0 | 0 |  | 0 |
| 5 | 红绳缠手腕 | 1171 | normal | 92.4 | 0 |  | 0 |
| 6 | 手机屏幕亮起 | 768 | normal | 20.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 364 < 597（本章目标 1087 字的 55%）
- 第 6 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 562 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 4943
chapter_chars_mean: 824
chapter_chars_median: 948
chapter_chars_cv: 0.35
paragraphs_mean: 38.8
dialogue_chars_pct: 25.0
dialogue_para_pct: 42.1
interiority_para_pct: 0.5
narration_para_pct: 57.4
turn_under20_pct: 91.2
turn_over200_pct: 0.0
attr_say_pct: 35.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.7
turn_len_median: 9
```
