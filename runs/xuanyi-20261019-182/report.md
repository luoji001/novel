# 铜镜 生成报告

slug：`xuanyi-20261019-182`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13324
LLM 调用：68 次，累计 229.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜镜背面的日期 | 1522 | short | 95.1 | 0 |  | 2 |
| 2 | 钢笔未干的墨迹 | 3352 | normal | 89.5 | 0 |  | 3 |
| 3 | 铜镜上的划痕 | 3254 | normal | 90.5 | 0 |  | 2 |
| 4 | 触碰铜镜边缘 | 3399 | normal | 89.9 | 0 |  | 3 |
| 5 | 铜铃随镜摇晃 | 1792 | short | 90.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 21.4 高于目标 20.0
  - narration_para_pct 7.1 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×3、「陆文渊点」×3、「陆文渊的」×3
  - narration_para_pct 9.4 低于目标 20.0
  - [observe] 章内自我复读 21 句（如「他径直走向墙边的老式木桌，桌面斑驳暗沉，边缘还留…」）
- 第 3 章：
  - 单条套路句式超限：「沈慕云的」×3
  - [observe] 章内自我复读 1 句（如「1937年6月15日…」）
- 第 4 章：
  - 单条套路句式超限：「沈慕云的」×7、「陆文渊的」×5、「“我不知道」×3
  - narration_para_pct 9.0 低于目标 20.0
  - [observe] attr_adv_pct 26.7 > 20.0（结构塌缩）
- 第 5 章：
  - narration_para_pct 3.6 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 12658
chapter_chars_mean: 2532
chapter_chars_median: 3089
chapter_chars_cv: 0.34
paragraphs_mean: 56.8
dialogue_chars_pct: 41.6
dialogue_para_pct: 78.6
interiority_para_pct: 10.2
narration_para_pct: 11.2
turn_under20_pct: 75.3
turn_over200_pct: 0.0
attr_say_pct: 18.2
attr_adv_pct: 10.0
scenes_per_chapter: 2.2
dialogue_run_mean: 5.5
turn_len_median: 12
```
