# 空白页 生成报告

slug：`xuanyi-20261019-165`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14628
LLM 调用：68 次，累计 234.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 监控画面重叠 | 2032 | short | 90.4 | 0 |  | 1 |
| 2 | 账册第17页消失 | 3868 | normal | 82.6 | 0 |  | 3 |
| 3 | 咖啡杯人影浮现 | 3606 | normal | 59.3 | 0 |  | 3 |
| 4 | 电子检测器启动 | 3305 | normal | 89.9 | 0 |  | 1 |
| 5 | 处方单边缘残影 | 1812 | short | 72.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 14.2 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈知远的」×5、「他知道这」×3
  - interiority_para_pct 24.3 高于目标 20.0
  - [observe] 章内自我复读 17 句（如「于是他开始回忆这段时间以来的工作内容，试图找出哪…」）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3、「沈知远的」×3
  - dialogue_chars_pct 14.3 低于目标 20.0
  - interiority_para_pct 20.3 高于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「沈知远的」×8、「周若雪的」×7、「沈知远点了点头」×3
- 第 5 章：
  - dialogue_chars_pct 7.6 低于目标 20.0
  - interiority_para_pct 20.7 高于目标 20.0
  - dialogue_run_mean 1.3 低于目标 1.5

## 整书结构指标

```
chapters: 5
total_chars: 13970
chapter_chars_mean: 2794
chapter_chars_median: 3136
chapter_chars_cv: 0.33
paragraphs_mean: 57.8
dialogue_chars_pct: 19.1
dialogue_para_pct: 48.0
interiority_para_pct: 18.5
narration_para_pct: 33.5
turn_under20_pct: 80.5
turn_over200_pct: 0.0
attr_say_pct: 22.4
attr_adv_pct: 1.2
scenes_per_chapter: 3.2
dialogue_run_mean: 2.6
turn_len_median: 11
```
