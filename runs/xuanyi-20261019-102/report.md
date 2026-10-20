# 当票 生成报告

slug：`xuanyi-20261019-102`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14071
LLM 调用：68 次，累计 227.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触碰当票的指尖 | 1715 | short | 93.1 | 0 |  | 2 |
| 2 | 触碰当票的指尖 | 3583 | normal | 88.9 | 0 |  | 5 |
| 3 | 铜钥匙的刻痕 | 3618 | normal | 91.2 | 0 |  | 4 |
| 4 | 触碰怀表的指尖 | 3377 | normal | 90.9 | 0 |  | 4 |
| 5 | 银元的刻痕 | 1773 | short | 93.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.0 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「沈墨生的」×3
  - dialogue_chars_pct 19.7 低于目标 20.0
  - interiority_para_pct 21.2 高于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 标题重复：「触碰当票的指尖」已存在
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈墨生的」×6
  - narration_para_pct 15.7 低于目标 20.0
  - [observe] 章内自我复读 8 句（如「他知道，自己正在接近某些重要的真相，而这趟旅程才…」）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周婉如的」×5、「周婉如点」×3、「不仅仅是」×3
  - narration_para_pct 9.8 低于目标 20.0
  - [observe] 标题与《触碰当票的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「周婉如的」×4
  - narration_para_pct 7.1 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13355
chapter_chars_mean: 2671
chapter_chars_median: 3198
chapter_chars_cv: 0.35
paragraphs_mean: 64
dialogue_chars_pct: 31.7
dialogue_para_pct: 70.8
interiority_para_pct: 11.8
narration_para_pct: 17.4
turn_under20_pct: 87.0
turn_over200_pct: 0.0
attr_say_pct: 16.6
attr_adv_pct: 10.1
scenes_per_chapter: 4.2
dialogue_run_mean: 4.3
turn_len_median: 10
```
