# 旧工牌 生成报告

slug：`shuangwen-20261022-108`
档位：爽文　闸门模式：observe
章数：10　总字数：18711
LLM 调用：97 次，累计 423.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 递出旧工牌 | 1546 | normal | 97.7 | 0 |  | 2 |
| 2 | 签字时的阴影 | 2043 | normal | 90.0 | 0 |  | 0 |
| 3 | 化肥袋的日期谜题 | 2099 | normal | 93.5 | 0 |  | 1 |
| 4 | 翻看工龄证明 | 1992 | normal | 90.6 | 0 |  | 0 |
| 5 | 旧工牌的反光 | 1587 | normal | 37.5 | 0 |  | 2 |
| 6 | 翻看工龄证明 | 2116 | normal | 92.3 | 0 |  | 1 |
| 7 | 递出旧工牌 | 1777 | normal | 91.4 | 0 |  | 3 |
| 8 | 递出旧工牌 | 1457 | normal | 90.1 | 0 |  | 1 |
| 9 | 旧工牌的反光 | 1878 | normal | 91.5 | 0 |  | 1 |
| 10 | 旧工牌的摩挲 | 2206 | long | 91.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「说道“我」×4、「点了点头」×3
  - attr_adv_pct 13.3 高于目标 12.0
- 第 3 章：
  - attr_adv_pct 17.6 高于目标 12.0
- 第 5 章：
  - 命中套话收尾句
  - [observe] attr_adv_pct 31.2 > 25.0（结构塌缩）
- 第 6 章：
  - [observe] 标题重复：「翻看工龄证明」已存在
- 第 7 章：
  - 命中套话收尾句
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「递出旧工牌」已存在
- 第 8 章：
  - [observe] 标题重复：「递出旧工牌」已存在
- 第 9 章：
  - [observe] 标题重复：「旧工牌的反光」已存在
- 第 10 章：
  - attr_adv_pct 20.8 高于目标 12.0
  - [observe] 标题与《旧工牌的反光》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 17710
chapter_chars_mean: 1771
chapter_chars_median: 1839
chapter_chars_cv: 0.14
paragraphs_mean: 42.6
dialogue_chars_pct: 45.4
dialogue_para_pct: 81.8
interiority_para_pct: 6.6
narration_para_pct: 11.6
turn_under20_pct: 72.0
turn_over200_pct: 0.0
attr_say_pct: 25.1
attr_adv_pct: 13.0
scenes_per_chapter: 2
dialogue_run_mean: 5.6
turn_len_median: 14
```
