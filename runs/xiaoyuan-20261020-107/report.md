# 钥匙 生成报告

slug：`xiaoyuan-20261020-107`
档位：校园青春　闸门模式：observe
章数：9　总字数：20579
LLM 调用：100 次，累计 444.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙与未完成的诗 | 1525 | short | 97.0 | 0 |  | 2 |
| 2 | 分科表的张贴 | 2508 | normal | 89.5 | 0 |  | 1 |
| 3 | 磁带的整理 | 2793 | normal | 91.8 | 0 |  | 2 |
| 4 | 笔记本的边缘摩挲 | 2563 | normal | 92.2 | 0 |  | 2 |
| 5 | 课表的边缘摩挲 | 2501 | normal | 91.0 | 0 |  | 3 |
| 6 | 磁带盒的最后触碰 | 2498 | normal | 90.7 | 0 |  | 1 |
| 7 | 调令文件的边缘摩挲 | 2192 | normal | 86.0 | 0 |  | 4 |
| 8 | 铜钥匙的最后触碰 | 2479 | normal | 92.7 | 0 |  | 2 |
| 9 | 钥匙的最后触碰 | 1511 | short | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 19.8 低于目标 20.0
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
- 第 2 章：
  - dialogue_chars_pct 17.2 低于目标 20.0
- 第 3 章：
  - interiority_para_pct 4.9 低于目标 8.0
  - narration_para_pct 11.5 低于目标 15.0
- 第 4 章：
  - 单条套路句式超限：「周子墨的」×4、「林晓棠的」×3
  - narration_para_pct 11.5 低于目标 15.0
- 第 5 章：
  - 单条套路句式超限：「周子墨的」×3、「林晓棠的」×3
  - narration_para_pct 9.8 低于目标 15.0
  - [observe] 标题与《笔记本的边缘摩挲》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「林晓棠站在」×3
- 第 7 章：
  - 单条套路句式超限：「周子墨的」×5、「点了点头」×4、「周子墨点」×4
  - dialogue_chars_pct 18.9 低于目标 20.0
  - [observe] 章内自我复读 13 句（如「他知道这孩子一直藏着很多事情，就像那个总是躲在角…」）
  - [observe] 标题与《课表的边缘摩挲》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - narration_para_pct 7.0 低于目标 15.0
  - [observe] 标题与《磁带盒的最后触碰》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题与《铜钥匙的最后触碰》近似 0.93 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 9
total_chars: 19566
chapter_chars_mean: 2174
chapter_chars_median: 2384
chapter_chars_cv: 0.2
paragraphs_mean: 48.1
dialogue_chars_pct: 28.9
dialogue_para_pct: 69.6
interiority_para_pct: 13.2
narration_para_pct: 17.2
turn_under20_pct: 87.5
turn_over200_pct: 0.0
attr_say_pct: 29.6
attr_adv_pct: 5.0
scenes_per_chapter: 2.4
dialogue_run_mean: 3.9
turn_len_median: 10
```
