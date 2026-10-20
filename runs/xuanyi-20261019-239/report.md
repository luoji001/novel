# 铜印 生成报告

slug：`xuanyi-20261019-239`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13861
LLM 调用：68 次，累计 238.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 泛黄汇款单飘落 | 1653 | short | 99.1 | 0 |  | 0 |
| 2 | 铜印边缘的裂痕 | 3794 | normal | 93.1 | 0 |  | 3 |
| 3 | 信纸边缘的指纹 | 3000 | normal | 86.8 | 0 |  | 3 |
| 4 | 算盘珠轻颤 | 3794 | normal | 89.7 | 0 |  | 3 |
| 5 | 翻开账本的手指 | 1615 | short | 84.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「林振国的」×6、「陈素云的」×5、「林振国站在」×3
  - narration_para_pct 8.1 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×4、「陈素云点」×3、「林振国的」×3
  - narration_para_pct 14.9 低于目标 20.0
  - [observe] 章内自我复读 20 句（如「林振国站起身来，看着走进来的身影——正是每天清晨…」）
- 第 4 章：
  - 单条套路句式超限：「林振国的」×7、「陈素云的」×6、「”陈素云轻」×5
  - narration_para_pct 6.3 低于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0
- 第 5 章：
  - dialogue_chars_pct 11.5 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13273
chapter_chars_mean: 2655
chapter_chars_median: 2851
chapter_chars_cv: 0.39
paragraphs_mean: 51
dialogue_chars_pct: 36.8
dialogue_para_pct: 75.1
interiority_para_pct: 12.1
narration_para_pct: 12.7
turn_under20_pct: 77.3
turn_over200_pct: 0.0
attr_say_pct: 26.5
attr_adv_pct: 11.4
scenes_per_chapter: 1.8
dialogue_run_mean: 5.3
turn_len_median: 13
```
