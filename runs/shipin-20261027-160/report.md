# 灯芯 生成报告

slug：`shipin-20261027-160`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6569
LLM 调用：57 次，累计 140.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水杯边缘的褐色污渍 | 676 | short | 94.3 | 0 |  | 0 |
| 2 | 应急灯开关上的红笔 | 1229 | normal | 36.8 | 0 |  | 2 |
| 3 | 应急灯下的数学试卷 | 1439 | normal | 35.3 | 0 |  | 1 |
| 4 | 水杯边缘的褐色污渍 | 1378 | normal | 91.0 | 0 |  | 2 |
| 5 | 应急灯下的橡皮擦 | 1069 | normal | 91.4 | 0 |  | 1 |
| 6 | 水杯坠入窗台凹槽 | 772 | normal | 35.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「李国强的」×4
  - [observe] attr_adv_pct 200.0 > 18.0（结构塌缩）
- 第 3 章：
  - [observe] 章内自我复读 2 句（如「你要是真的想学，我可以教你…」）
- 第 4 章：
  - 单条套路句式超限：「王小明点」×3
  - [observe] 标题重复：「水杯边缘的褐色污渍」已存在
- 第 5 章：
  - 命中套话收尾句
- 第 6 章：
  - [observe] 章内自我复读 2 句（如「水杯表面凝结的雾气缓缓消散，映出窗外灰蒙蒙的天空…」）
  - [observe] 章节过短 722 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 6117
chapter_chars_mean: 1020
chapter_chars_median: 1072
chapter_chars_cv: 0.3
paragraphs_mean: 28.8
dialogue_chars_pct: 20.1
dialogue_para_pct: 45.8
interiority_para_pct: 0.0
narration_para_pct: 54.2
turn_under20_pct: 93.4
turn_over200_pct: 0.0
attr_say_pct: 49.3
attr_adv_pct: 37.5
scenes_per_chapter: 2.2
dialogue_run_mean: 1.6
turn_len_median: 10
```
