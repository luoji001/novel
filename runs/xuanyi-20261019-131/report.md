# 锁痕 生成报告

slug：`xuanyi-20261019-131`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14279
LLM 调用：68 次，累计 227.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 锁痕暗藏账本秘密 | 1650 | short | 98.6 | 0 |  | 3 |
| 2 | 纸张边缘的时光褶皱 | 3604 | normal | 88.8 | 0 |  | 1 |
| 3 | 纸张边缘的时光褶皱 | 3789 | normal | 89.7 | 0 |  | 5 |
| 4 | 钥匙上的刻痕之谜 | 3268 | normal | 91.1 | 0 |  | 3 |
| 5 | 摩挲存单边缘 | 1963 | short | 91.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周慕云的」×4
  - narration_para_pct 8.3 低于目标 20.0
  - [observe] attr_adv_pct 30.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周慕云的」×5、「沈怀瑾站在」×3
- 第 3 章：
  - 单条套路句式超限：「周慕云点」×6、「周慕云的」×5、「沈怀瑾的」×5
  - narration_para_pct 8.6 低于目标 20.0
  - attr_adv_pct 13.2 高于目标 10.0
  - [observe] 章内自我复读 2 句（如「那你为什么不早告诉我？…」）
  - [observe] 标题重复：「纸张边缘的时光褶皱」已存在
- 第 4 章：
  - 单条套路句式超限：「沈怀瑾的」×6、「周慕云的」×4、「他知道这」×3
  - narration_para_pct 16.4 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 5 章：
  - narration_para_pct 13.2 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13569
chapter_chars_mean: 2714
chapter_chars_median: 3130
chapter_chars_cv: 0.34
paragraphs_mean: 62.4
dialogue_chars_pct: 40.9
dialogue_para_pct: 77.2
interiority_para_pct: 8.7
narration_para_pct: 14.1
turn_under20_pct: 75.1
turn_over200_pct: 0.0
attr_say_pct: 19.5
attr_adv_pct: 9.8
scenes_per_chapter: 2.4
dialogue_run_mean: 5.7
turn_len_median: 14
```
