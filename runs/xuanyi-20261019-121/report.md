# 显影液 生成报告

slug：`xuanyi-20261019-121`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14369
LLM 调用：68 次，累计 233.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显影液中的孩子 | 1673 | short | 100.0 | 0 |  | 2 |
| 2 | 登记簿上的名字 | 3682 | normal | 89.2 | 0 |  | 4 |
| 3 | 打开小门 | 3601 | normal | 89.2 | 0 |  | 4 |
| 4 | 摩挲纸边的手指 | 3812 | normal | 90.0 | 0 |  | 3 |
| 5 | 摩挲纸边的手指 | 1596 | short | 92.2 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈志远的」×7、「林素云的」×3
  - narration_para_pct 5.4 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈志远的」×9、「”林素云低」×4、「林素云点了点头」×3
  - narration_para_pct 11.0 低于目标 20.0
  - attr_adv_pct 18.4 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「他知道，要想弄清楚真相，他还得继续寻找更多的答案…」）
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林素云的」×6、「他知道这」×5、「沈志远站在」×3
  - narration_para_pct 11.0 低于目标 20.0
  - attr_adv_pct 10.7 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「林素云的」×8、「沈志远的」×6、「他知道这」×4
  - narration_para_pct 4.2 低于目标 20.0
  - attr_adv_pct 10.5 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「林素云的」×3
  - narration_para_pct 12.5 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 章内自我复读 2 句（如「林素云微微皱眉，语气里透着一种不容置疑的力量…」）
  - [observe] 标题重复：「摩挲纸边的手指」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13663
chapter_chars_mean: 2733
chapter_chars_median: 3425
chapter_chars_cv: 0.4
paragraphs_mean: 62.8
dialogue_chars_pct: 37.8
dialogue_para_pct: 79.3
interiority_para_pct: 12.0
narration_para_pct: 8.7
turn_under20_pct: 79.9
turn_over200_pct: 0.0
attr_say_pct: 32.1
attr_adv_pct: 13.5
scenes_per_chapter: 2.8
dialogue_run_mean: 5.7
turn_len_median: 13
```
