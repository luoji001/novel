# 校服外套的温度 生成报告

slug：`xiaoyuan-20261020-39`
档位：校园青春　闸门模式：observe
章数：9　总字数：21384
LLM 调用：100 次，累计 471.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 纸张的低语 | 1415 | short | 98.2 | 0 |  | 1 |
| 2 | 磁带的余音 | 3003 | normal | 80.9 | 0 |  | 4 |
| 3 | 外套的重量 | 2767 | normal | 91.7 | 0 |  | 2 |
| 4 | 笔记本的窃读者 | 2609 | normal | 89.3 | 0 |  | 1 |
| 5 | 课表的错位 | 2282 | normal | 89.5 | 0 |  | 1 |
| 6 | 贺卡的折痕 | 2419 | normal | 89.6 | 0 |  | 1 |
| 7 | 磁带的余音 | 2539 | normal | 85.6 | 0 |  | 2 |
| 8 | 摩挲照片的指尖 | 2531 | normal | 88.2 | 0 |  | 0 |
| 9 | 摩挲分科表的指尖 | 1810 | short | 84.4 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 11.8 低于目标 15.0
- 第 2 章：
  - dialogue_chars_pct 18.4 低于目标 20.0
  - interiority_para_pct 35.8 高于目标 35.0
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 章内自我复读 30 句（如「放学铃响起时，林小满依旧呆坐在座位上，手中紧握着…」）
- 第 3 章：
  - narration_para_pct 4.9 低于目标 15.0
  - attr_adv_pct 15.8 高于目标 12.0
- 第 4 章：
  - narration_para_pct 13.4 低于目标 15.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「陆老师的声音打断了她的思绪…」）
- 第 6 章：
  - attr_adv_pct 15.4 高于目标 12.0
- 第 7 章：
  - dialogue_chars_pct 16.2 低于目标 20.0
  - [observe] 标题重复：「磁带的余音」已存在
- 第 9 章：
  - 单条套路句式超限：「不仅仅是」×4、「心中充满了」×3
  - narration_para_pct 11.9 低于目标 15.0
  - [observe] 章内自我复读 16 句（如「林小满突然意识到，这不仅仅是一个座位的问题，而是…」）
  - [observe] 标题与《摩挲照片的指尖》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 9
total_chars: 20314
chapter_chars_mean: 2257
chapter_chars_median: 2414
chapter_chars_cv: 0.21
paragraphs_mean: 52
dialogue_chars_pct: 24.6
dialogue_para_pct: 65.0
interiority_para_pct: 17.7
narration_para_pct: 17.3
turn_under20_pct: 87.9
turn_over200_pct: 0.0
attr_say_pct: 28.4
attr_adv_pct: 7.4
scenes_per_chapter: 2.1
dialogue_run_mean: 3.9
turn_len_median: 8
```
