# 灯罩 生成报告

slug：`shipin-20261027-132`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5747
LLM 调用：57 次，累计 134.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 黑板擦落回地面 | 538 | short | 22.7 | 0 |  | 1 |
| 2 | 铅笔戳开关 | 858 | normal | 21.1 | 0 |  | 1 |
| 3 | 竹竿卡落叶 | 728 | normal | 19.7 | 0 |  | 1 |
| 4 | 试卷卷成筒状 | 1179 | normal | 58.1 | 0 |  | 0 |
| 5 | 铅笔戳开关 | 1320 | normal | 91.6 | 0 |  | 3 |
| 6 | 电线绕树干 | 1118 | normal | 17.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 487 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 797 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - [observe] 章节过短 687 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - 单条套路句式超限：「李国强的」×3
  - narration_para_pct 31.0 低于目标 35.0
  - [observe] 标题重复：「铅笔戳开关」已存在
- 第 6 章：
  - dialogue_chars_pct 0.5 低于目标 5.0
  - narration_para_pct 93.6 高于目标 90.0
  - [observe] 章内自我复读 7 句（如「抬头看了眼天色，又低头看了看手里没缠完的电线…」）

## 整书结构指标

```
chapters: 6
total_chars: 5324
chapter_chars_mean: 887
chapter_chars_median: 892
chapter_chars_cv: 0.32
paragraphs_mean: 26
dialogue_chars_pct: 10.9
dialogue_para_pct: 32.3
interiority_para_pct: 1.6
narration_para_pct: 66.1
turn_under20_pct: 100.0
turn_over200_pct: 0.0
attr_say_pct: 100.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.6
turn_len_median: 9
```
