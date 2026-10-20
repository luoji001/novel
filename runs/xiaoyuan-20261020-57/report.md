# 信笺 生成报告

slug：`xiaoyuan-20261020-57`
档位：校园青春　闸门模式：observe
章数：9　总字数：19613
LLM 调用：100 次，累计 419.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙孔的回音 | 1370 | short | 95.6 | 0 |  | 2 |
| 2 | 调试音效的指尖 | 2497 | normal | 93.7 | 0 |  | 2 |
| 3 | 手指摩挲纸边 | 2519 | normal | 91.7 | 0 |  | 4 |
| 4 | 手指摩挲纸边 | 2548 | normal | 92.2 | 0 |  | 2 |
| 5 | 手指摩挲磁带 | 2277 | normal | 58.3 | 0 |  | 3 |
| 6 | 摩挲信封边角 | 2434 | normal | 92.5 | 0 |  | 0 |
| 7 | 抽屉里的信封 | 2509 | normal | 87.4 | 0 |  | 3 |
| 8 | 检查单的边缘 | 2116 | normal | 89.0 | 0 |  | 2 |
| 9 | 手指摩挲袖口褶皱 | 1334 | short | 79.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 12.0 低于目标 15.0
  - [observe] 章内自我复读 3 句（如「她捡起来，却发现那是张空白的信笺，背面还留着几道…」）
- 第 2 章：
  - 单条套路句式超限：「他知道自己」×3
  - interiority_para_pct 6.2 低于目标 8.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×3、「点了点头」×3
  - interiority_para_pct 6.5 低于目标 8.0
  - narration_para_pct 11.3 低于目标 15.0
  - [observe] 章内自我复读 1 句（如「但我总觉得，如果我现在放弃了，可能会后悔一辈子…」）
- 第 4 章：
  - narration_para_pct 11.8 低于目标 15.0
  - [observe] 标题重复：「手指摩挲纸边」已存在
- 第 5 章：
  - dialogue_chars_pct 15.0 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「周老师走到她身边，低声说了几句什么，然后转向顾舟…」）
  - [observe] 标题与《手指摩挲纸边》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「点了点头」×3
  - dialogue_chars_pct 18.4 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「她的目光落在门缝里露出一角的纸张上，那是封没有邮…」）
- 第 8 章：
  - [observe] 章内自我复读 16 句（如「顾舟看着那些光影交错的样子，突然觉得这个世界变得…」）
  - [observe] attr_adv_pct 22.2 > 22.0（结构塌缩）
- 第 9 章：
  - dialogue_chars_pct 11.5 低于目标 20.0
  - [observe] 章内自我复读 10 句（如「她下意识地把身体往前凑了一点，几乎是不自觉的动作…」）

## 整书结构指标

```
chapters: 9
total_chars: 18578
chapter_chars_mean: 2064
chapter_chars_median: 2300
chapter_chars_cv: 0.22
paragraphs_mean: 47.1
dialogue_chars_pct: 23.8
dialogue_para_pct: 66.4
interiority_para_pct: 14.2
narration_para_pct: 19.4
turn_under20_pct: 88.7
turn_over200_pct: 0.0
attr_say_pct: 30.5
attr_adv_pct: 4.8
scenes_per_chapter: 3.1
dialogue_run_mean: 3.6
turn_len_median: 9
```
