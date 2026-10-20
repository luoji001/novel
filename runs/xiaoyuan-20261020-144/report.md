# 磁带的回响 生成报告

slug：`xiaoyuan-20261020-144`
档位：校园青春　闸门模式：observe
章数：9　总字数：20879
LLM 调用：100 次，累计 446.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 门锁的低语 | 1484 | short | 99.8 | 0 |  | 2 |
| 2 | 成绩单的重量 | 2437 | normal | 91.5 | 0 |  | 1 |
| 3 | 缴费单的边缘 | 2583 | normal | 92.4 | 0 |  | 1 |
| 4 | 工作证的阴影 | 2519 | normal | 91.0 | 0 |  | 0 |
| 5 | 成绩单的背面标签 | 2346 | normal | 89.4 | 0 |  | 2 |
| 6 | 纸条上的泪痕 | 2543 | normal | 93.0 | 0 |  | 3 |
| 7 | 麻雀的羽毛 | 2795 | normal | 89.8 | 0 |  | 4 |
| 8 | 校服外套的温度 | 2347 | normal | 90.3 | 0 |  | 4 |
| 9 | 缴费单的边缘 | 1816 | short | 90.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林小满站在」×3
  - narration_para_pct 8.8 低于目标 15.0
- 第 2 章：
  - 单条套路句式超限：「”周子安低」×4、「林小满的」×4、「林小满站在」×3
- 第 3 章：
  - 单条套路句式超限：「周子安的」×5、「林小满的」×5
- 第 5 章：
  - 单条套路句式超限：「林小满站在」×3
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「周子安的」×7、「林小满的」×7
  - narration_para_pct 12.1 低于目标 15.0
  - attr_adv_pct 18.2 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「周子安的」×7、「林小满站在」×5
  - narration_para_pct 11.3 低于目标 15.0
  - [observe] 章内自我复读 16 句（如「他知道，自己也许永远都无法真正了解周子安的想法，…」）
  - [observe] attr_adv_pct 40.0 > 22.0（结构塌缩）
- 第 8 章：
  - 单条套路句式超限：「林小满的」×3
  - [observe] 章内自我复读 4 句（如「周子安愣了一下，随即点了点头，“嗯，我刚想起来还…」）
  - [observe] 与历史章节逐字重复 3 句（如「他知道周子安一定知道些什么，但他不想说出来…」）
  - [observe] attr_adv_pct 37.5 > 22.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「林小满的」×3
  - interiority_para_pct 4.4 低于目标 8.0
  - [observe] 标题重复：「缴费单的边缘」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19814
chapter_chars_mean: 2202
chapter_chars_median: 2307
chapter_chars_cv: 0.18
paragraphs_mean: 51.6
dialogue_chars_pct: 25.1
dialogue_para_pct: 67.2
interiority_para_pct: 12.8
narration_para_pct: 20.0
turn_under20_pct: 90.7
turn_over200_pct: 0.0
attr_say_pct: 24.7
attr_adv_pct: 14.6
scenes_per_chapter: 3.9
dialogue_run_mean: 3.3
turn_len_median: 10
```
