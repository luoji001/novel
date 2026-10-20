# 旧笔 生成报告

slug：`xuanyi-20261019-249`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14057
LLM 调用：68 次，累计 227.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药瓶上的指纹 | 1673 | short | 97.5 | 0 |  | 1 |
| 2 | 药瓶上的指纹 | 3652 | normal | 91.3 | 0 |  | 3 |
| 3 | 木柜暗格的刻痕 | 3498 | normal | 83.3 | 0 |  | 3 |
| 4 | 签字笔的颤抖 | 3387 | normal | 90.0 | 0 |  | 2 |
| 5 | 药方与签字笔的对话 | 1842 | short | 90.2 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周玉兰的」×4
- 第 2 章：
  - 单条套路句式超限：「沈文远的」×5、「“我不知道」×4、「”周玉兰轻」×4
  - narration_para_pct 12.0 低于目标 20.0
  - [observe] 标题重复：「药瓶上的指纹」已存在
- 第 3 章：
  - 单条套路句式超限：「沈文远的」×5、「周玉兰的」×3
  - dialogue_chars_pct 17.3 低于目标 20.0
  - interiority_para_pct 23.0 高于目标 20.0
- 第 4 章：
  - narration_para_pct 15.2 低于目标 20.0
  - attr_adv_pct 15.4 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13376
chapter_chars_mean: 2675
chapter_chars_median: 3241
chapter_chars_cv: 0.35
paragraphs_mean: 60.2
dialogue_chars_pct: 36.0
dialogue_para_pct: 69.8
interiority_para_pct: 11.5
narration_para_pct: 18.8
turn_under20_pct: 75.3
turn_over200_pct: 0.0
attr_say_pct: 20.8
attr_adv_pct: 5.1
scenes_per_chapter: 4.4
dialogue_run_mean: 3.9
turn_len_median: 11
```
