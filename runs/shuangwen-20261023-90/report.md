# 账单 生成报告

slug：`shuangwen-20261023-90`
档位：爽文　闸门模式：observe
章数：10　总字数：20074
LLM 调用：97 次，累计 443.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指摩挲登记簿 | 1840 | normal | 98.0 | 0 |  | 0 |
| 2 | 账单背面的签名 | 2274 | normal | 92.0 | 0 |  | 1 |
| 3 | 摩挲凭牌边缘 | 1707 | normal | 93.4 | 0 |  | 1 |
| 4 | 账单边缘的摩挲 | 2071 | normal | 36.7 | 0 |  | 2 |
| 5 | 墨迹晕染的承诺 | 1732 | normal | 92.8 | 0 |  | 0 |
| 6 | 账单边缘的摩挲 | 2102 | normal | 92.9 | 0 |  | 2 |
| 7 | 账单边缘的摩挲 | 1885 | normal | 91.1 | 0 |  | 2 |
| 8 | 账单边缘的摩挲 | 1819 | normal | 92.7 | 0 |  | 2 |
| 9 | 摩挲账单边缘 | 2028 | normal | 92.9 | 0 |  | 1 |
| 10 | 摩挲账单边缘 | 2606 | long | 89.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「陆长青的」×6
- 第 3 章：
  - 单条套路句式超限：「陆长青的」×6、「“我不知道」×3
- 第 4 章：
  - 单条套路句式超限：「陆长青的」×9
  - [observe] attr_adv_pct 41.7 > 25.0（结构塌缩）
- 第 6 章：
  - narration_para_pct 3.7 低于目标 5.0
  - [observe] 标题重复：「账单边缘的摩挲」已存在
- 第 7 章：
  - 单条套路句式超限：「陆长青的」×4
  - [observe] 标题重复：「账单边缘的摩挲」已存在
- 第 8 章：
  - 单条套路句式超限：「陆长青的」×5、「微微一笑」×3
  - [observe] 标题重复：「账单边缘的摩挲」已存在
- 第 9 章：
  - [observe] 标题与《摩挲凭牌边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「陆长青的」×6
  - narration_para_pct 1.8 低于目标 5.0
  - dialogue_run_mean 17.3 高于目标 14.0
  - [observe] 标题重复：「摩挲账单边缘」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18989
chapter_chars_mean: 1899
chapter_chars_median: 1852
chapter_chars_cv: 0.14
paragraphs_mean: 46.4
dialogue_chars_pct: 52.7
dialogue_para_pct: 86.1
interiority_para_pct: 5.1
narration_para_pct: 8.8
turn_under20_pct: 75.3
turn_over200_pct: 0.0
attr_say_pct: 31.4
attr_adv_pct: 10.2
scenes_per_chapter: 1.6
dialogue_run_mean: 7.5
turn_len_median: 12
```
