# 钢笔墨迹 生成报告

slug：`xuanyi-20261019-104`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14936
LLM 调用：68 次，累计 244.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲账本 | 1402 | short | 92.7 | 0 |  | 2 |
| 2 | 窥视账本秘密 | 4290 | normal | 92.3 | 0 |  | 4 |
| 3 | 粮票与颤抖手指 | 3550 | normal | 91.5 | 0 |  | 3 |
| 4 | 摩挲纸页边缘 | 3892 | normal | 91.1 | 0 |  | 3 |
| 5 | 摩挲钢笔外壳 | 1797 | short | 93.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈志远的」×3
  - interiority_para_pct 21.4 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈志远的」×10、「“我不知道」×5、「周美兰的」×5
  - narration_para_pct 17.8 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「陈志远站在会计室门口，手里握着一把生锈的钥匙…」）
- 第 3 章：
  - 单条套路句式超限：「周美兰的」×10、「陈志远的」×9、「“我不知道」×3
  - narration_para_pct 8.3 低于目标 20.0
  - [observe] attr_adv_pct 23.5 > 20.0（结构塌缩）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周美兰的」×7、「陈志远的」×6、「“我不知道」×3
  - narration_para_pct 15.2 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×4
  - narration_para_pct 3.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14250
chapter_chars_mean: 2850
chapter_chars_median: 3391
chapter_chars_cv: 0.43
paragraphs_mean: 61.2
dialogue_chars_pct: 38.2
dialogue_para_pct: 74.9
interiority_para_pct: 11.3
narration_para_pct: 13.8
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 17.9
attr_adv_pct: 10.5
scenes_per_chapter: 2.2
dialogue_run_mean: 3.8
turn_len_median: 13
```
