# 旧工牌 生成报告

slug：`shuangwen-20261023-130`
档位：爽文　闸门模式：observe
章数：10　总字数：19285
LLM 调用：97 次，累计 441.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧工牌的重量 | 1815 | normal | 96.7 | 0 |  | 0 |
| 2 | 旧工牌的摩挲 | 1937 | normal | 92.2 | 0 |  | 3 |
| 3 | 旧工牌的摩挲 | 1810 | normal | 91.2 | 0 |  | 4 |
| 4 | 旧工牌的摩挲 | 2224 | normal | 92.3 | 0 |  | 2 |
| 5 | 旧工牌的摩挲 | 1435 | normal | 92.1 | 0 |  | 1 |
| 6 | 签字的手指 | 1914 | normal | 90.2 | 0 |  | 1 |
| 7 | 旧工牌的摩挲 | 1869 | normal | 90.8 | 0 |  | 2 |
| 8 | 旧工牌的签字 | 1926 | normal | 90.2 | 0 |  | 3 |
| 9 | 旧工牌的摩挲 | 1907 | normal | 91.2 | 0 |  | 4 |
| 10 | 旧工牌的摩挲 | 2438 | long | 89.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「登记处」×5
  - narration_para_pct 2.5 低于目标 5.0
  - [observe] 标题与《旧工牌的重量》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「县林业局」×4、「林志远的」×3
  - narration_para_pct 4.8 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「旧工牌的摩挲」已存在
- 第 4 章：
  - 单条套路句式超限：「林志远的」×4、「登记处」×3
  - [observe] 标题重复：「旧工牌的摩挲」已存在
- 第 5 章：
  - [observe] 标题重复：「旧工牌的摩挲」已存在
- 第 6 章：
  - 单条套路句式超限：「他知道这」×4、「林志远的」×4
- 第 7 章：
  - 单条套路句式超限：「登记处」×4
  - [observe] 标题重复：「旧工牌的摩挲」已存在
- 第 8 章：
  - narration_para_pct 3.8 低于目标 5.0
  - dialogue_run_mean 16.7 高于目标 14.0
  - [observe] 标题与《旧工牌的摩挲》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「县林业局」×3
  - narration_para_pct 2.9 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「旧工牌的摩挲」已存在
- 第 10 章：
  - 单条套路句式超限：「登记处」×9
  - 情节与已写章节重复 0.73 ≥ 0.7（撞上「林志远为证明自己仍是青云山护林员，与王主任展开身份争议，…」）
  - attr_adv_pct 16.0 高于目标 12.0
  - [observe] 标题重复：「旧工牌的摩挲」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18330
chapter_chars_mean: 1833
chapter_chars_median: 1816
chapter_chars_cv: 0.14
paragraphs_mean: 40.3
dialogue_chars_pct: 44.1
dialogue_para_pct: 84.9
interiority_para_pct: 6.3
narration_para_pct: 8.8
turn_under20_pct: 76.2
turn_over200_pct: 0.0
attr_say_pct: 35.3
attr_adv_pct: 7.4
scenes_per_chapter: 1.8
dialogue_run_mean: 7.7
turn_len_median: 12
```
