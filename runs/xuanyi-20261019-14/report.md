# 铜铃 生成报告

slug：`xuanyi-20261019-14`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15658
LLM 调用：68 次，累计 240.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 布匹编号清单 | 1865 | short | 91.1 | 0 |  | 3 |
| 2 | 算盘珠上的磨痕 | 4100 | normal | 90.2 | 0 |  | 4 |
| 3 | 布匹背面的暗记 | 3569 | normal | 90.7 | 0 |  | 1 |
| 4 | 纸片飘落真相现 | 4127 | normal | 87.2 | 0 |  | 3 |
| 5 | 纸片飘落真相现 | 1992 | short | 91.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 20.5 高于目标 20.0
  - [observe] 章内自我复读 16 句（如「陈德昌迅速将编号清单放回原处，装作若无其事的样子…」）
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周素云的」×5、「点了点头」×3、「陈德昌的」×3
  - narration_para_pct 12.8 低于目标 20.0
  - attr_adv_pct 14.7 高于目标 10.0
  - [observe] 章内自我复读 21 句（如「这时，周素云忽然想起了一句往事，那是很久以前她在…」）
- 第 3 章：
  - narration_para_pct 19.2 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周素云的」×6、「周素云点了点头」×3、「周素云点」×3
  - narration_para_pct 19.8 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「赵文远接过那张纸，仔细看了看，然后叹了口气：“看…」）
- 第 5 章：
  - narration_para_pct 12.8 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 标题重复：「纸片飘落真相现」已存在

## 整书结构指标

```
chapters: 5
total_chars: 14867
chapter_chars_mean: 2973
chapter_chars_median: 3398
chapter_chars_cv: 0.36
paragraphs_mean: 71.2
dialogue_chars_pct: 40.0
dialogue_para_pct: 74.8
interiority_para_pct: 7.3
narration_para_pct: 17.9
turn_under20_pct: 72.6
turn_over200_pct: 0.0
attr_say_pct: 14.6
attr_adv_pct: 10.4
scenes_per_chapter: 3.4
dialogue_run_mean: 4.1
turn_len_median: 14
```
