# 报价单 生成报告

slug：`shuangwen-20261023-82`
档位：爽文　闸门模式：observe
章数：10　总字数：17796
LLM 调用：97 次，累计 384.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字的瞬间 | 1386 | normal | 98.2 | 0 |  | 2 |
| 2 | 签署最后一页名单 | 1945 | normal | 93.3 | 0 |  | 1 |
| 3 | 报价单上的指纹 | 2004 | normal | 37.2 | 0 |  | 3 |
| 4 | 报价单上的指纹 | 1465 | normal | 92.2 | 0 |  | 3 |
| 5 | 指认报价单上的名字 | 1723 | normal | 92.3 | 0 |  | 2 |
| 6 | 报价单上的指纹 | 2246 | normal | 35.5 | 0 |  | 2 |
| 7 | 指纹的博弈 | 1624 | normal | 91.0 | 0 |  | 0 |
| 8 | 指认旧照上的名字 | 1743 | normal | 91.0 | 0 |  | 3 |
| 9 | 翻动名册的瞬间 | 1552 | normal | 37.0 | 0 |  | 4 |
| 10 | 指纹的博弈 | 2098 | long | 93.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「市工商联」×6、「他知道这」×3
  - attr_adv_pct 18.2 高于目标 12.0
- 第 2 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - narration_para_pct 4.2 低于目标 5.0
  - dialogue_run_mean 15 高于目标 14.0
  - [observe] attr_adv_pct 53.3 > 25.0（结构塌缩）
- 第 4 章：
  - narration_para_pct 4.9 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「报价单上的指纹」已存在
- 第 5 章：
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题与《报价单上的指纹》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 章内自我复读 2 句（如「林海说，“我们一起面对接下来的一切…」）
  - [observe] 标题重复：「报价单上的指纹」已存在
- 第 8 章：
  - 单条套路句式超限：「市工商联」×3
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题与《指认报价单上的名字》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「市工商联」×5
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 16.5 高于目标 14.0
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
- 第 10 章：
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「指纹的博弈」已存在

## 整书结构指标

```
chapters: 10
total_chars: 16814
chapter_chars_mean: 1681
chapter_chars_median: 1660
chapter_chars_cv: 0.16
paragraphs_mean: 41.2
dialogue_chars_pct: 54.5
dialogue_para_pct: 89.3
interiority_para_pct: 3.3
narration_para_pct: 7.5
turn_under20_pct: 69.0
turn_over200_pct: 0.0
attr_say_pct: 36.4
attr_adv_pct: 20.8
scenes_per_chapter: 1.3
dialogue_run_mean: 10.2
turn_len_median: 12
```
