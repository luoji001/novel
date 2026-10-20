# 铜铃 生成报告

slug：`xuanyi-20261019-253`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14811
LLM 调用：68 次，累计 241.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜铃与账本对话 | 1954 | short | 98.3 | 0 |  | 0 |
| 2 | 红绸下藏着小字 | 3748 | normal | 89.4 | 0 |  | 4 |
| 3 | 抚摸铜铃上的裂纹 | 3584 | normal | 91.3 | 0 |  | 2 |
| 4 | 摩挲铜钥匙棱线 | 3591 | normal | 89.6 | 0 |  | 3 |
| 5 | 抚纸条边角发脆 | 1929 | short | 90.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「周怀瑾的」×3、「他知道这」×3、「学徒房」×3
  - narration_para_pct 16.9 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「沈砚顺着他的目光望去，才发现红绸下方还有几行字，…」）
  - [observe] attr_adv_pct 21.4 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周怀瑾的」×3
  - narration_para_pct 15.6 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周怀瑾的」×4
  - narration_para_pct 12.7 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「“我不知道」×3
  - narration_para_pct 14.6 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14133
chapter_chars_mean: 2827
chapter_chars_median: 3411
chapter_chars_cv: 0.32
paragraphs_mean: 59.4
dialogue_chars_pct: 33.8
dialogue_para_pct: 71.2
interiority_para_pct: 12.9
narration_para_pct: 16.0
turn_under20_pct: 75.0
turn_over200_pct: 0.0
attr_say_pct: 13.4
attr_adv_pct: 12.0
scenes_per_chapter: 2.2
dialogue_run_mean: 3.5
turn_len_median: 12
```
