# 旧籍 生成报告

slug：`shuangwen-20261023-29`
档位：爽文　闸门模式：observe
章数：10　总字数：19979
LLM 调用：97 次，累计 443.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记册的争夺 | 1913 | normal | 99.9 | 0 |  | 2 |
| 2 | 纸条对峙 | 2158 | normal | 36.9 | 0 |  | 3 |
| 3 | 签字划痕 | 1856 | normal | 94.4 | 0 |  | 1 |
| 4 | 裂痕中的传承 | 2402 | normal | 90.1 | 0 |  | 1 |
| 5 | 登记册的争执 | 2254 | normal | 37.6 | 0 |  | 3 |
| 6 | 登记册的对峙 | 1903 | normal | 85.6 | 0 |  | 4 |
| 7 | 飘落的职级证书 | 1383 | normal | 94.6 | 0 |  | 2 |
| 8 | 登记册的对峙 | 2226 | normal | 36.8 | 0 |  | 4 |
| 9 | 表决表上的签名 | 1640 | normal | 92.8 | 0 |  | 0 |
| 10 | 名册边缘的卷起 | 2234 | long | 92.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3、「林清河的」×3
  - attr_adv_pct 25.0 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「赵文远的」×3
  - dialogue_run_mean 15.7 高于目标 14.0
  - [observe] attr_adv_pct 26.3 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「赵文远的」×4
- 第 4 章：
  - 单条套路句式超限：「赵文远的」×4、「林清河的」×3
- 第 5 章：
  - 单条套路句式超限：「赵文远的」×5
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
  - [observe] 标题与《登记册的争夺》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「林清河的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 29 高于目标 14.0
  - [observe] 标题与《登记册的争夺》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「赵文远的」×4
  - narration_para_pct 0.0 低于目标 5.0
- 第 8 章：
  - 单条套路句式超限：「讲经堂堂前」×3
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 与历史章节逐字重复 3 句（如「赵文远站在讲经堂堂前，目光凌厉地看着林清河…」）
  - [observe] 标题重复：「登记册的对峙」已存在
- 第 10 章：
  - 单条套路句式超限：「赵文远的」×3

## 整书结构指标

```
chapters: 10
total_chars: 18994
chapter_chars_mean: 1899
chapter_chars_median: 1934
chapter_chars_cv: 0.15
paragraphs_mean: 41.8
dialogue_chars_pct: 46.4
dialogue_para_pct: 86.1
interiority_para_pct: 5.9
narration_para_pct: 8.1
turn_under20_pct: 66.3
turn_over200_pct: 0.0
attr_say_pct: 27.6
attr_adv_pct: 13.8
scenes_per_chapter: 1.8
dialogue_run_mean: 9.5
turn_len_median: 15
```
