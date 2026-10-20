# 账本上的名字 生成报告

slug：`xuanyi-20261019-119`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14498
LLM 调用：68 次，累计 238.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜铃惊起麻雀 | 1814 | short | 91.5 | 0 |  | 3 |
| 2 | 铜铃摇晃的手势 | 3491 | normal | 92.2 | 0 |  | 3 |
| 3 | 照片背面的指纹 | 3846 | normal | 89.8 | 0 |  | 3 |
| 4 | 算盘上的光斑 | 3438 | normal | 90.5 | 0 |  | 2 |
| 5 | 摩挲账本边缘 | 1904 | short | 90.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「”陈秀兰轻」×3、「陈秀兰的」×3
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 章内自我复读 19 句（如「他说这话的时候声音有些发抖，“汇款单上写的收款人…」）
- 第 2 章：
  - 单条套路句式超限：「陈秀兰的」×6、「林永年的」×6、「”陈秀兰轻」×4
  - narration_para_pct 6.9 低于目标 20.0
  - attr_adv_pct 13.6 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×6、「林永年的」×4、「林永年点点」×3
  - narration_para_pct 10.3 低于目标 20.0
  - attr_adv_pct 12.8 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「陈秀兰的」×9、「林永年的」×8、「林永年站在」×4
  - narration_para_pct 19.2 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「林永年的」×3
  - narration_para_pct 9.1 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13839
chapter_chars_mean: 2768
chapter_chars_median: 3257
chapter_chars_cv: 0.33
paragraphs_mean: 56
dialogue_chars_pct: 42.0
dialogue_para_pct: 79.4
interiority_para_pct: 7.4
narration_para_pct: 13.1
turn_under20_pct: 72.1
turn_over200_pct: 0.0
attr_say_pct: 26.3
attr_adv_pct: 11.6
scenes_per_chapter: 3
dialogue_run_mean: 5.3
turn_len_median: 13
```
