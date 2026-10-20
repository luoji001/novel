# 红墨水 生成报告

slug：`xuanyi-20261019-34`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14047
LLM 调用：68 次，累计 235.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红墨水圈出的数字 | 1855 | short | 96.5 | 0 |  | 3 |
| 2 | 量布尺的裂痕 | 3399 | normal | 92.4 | 0 |  | 3 |
| 3 | 火车票与布料标签 | 3295 | normal | 90.9 | 0 |  | 2 |
| 4 | 揭开铁皮盒的秘密 | 3710 | normal | 90.2 | 0 |  | 4 |
| 5 | 抚摸布料标签的指尖 | 1783 | short | 91.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈德昌的」×4
  - narration_para_pct 9.4 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「微微一笑」×3
  - narration_para_pct 9.0 低于目标 20.0
  - [observe] attr_adv_pct 23.5 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「陈德昌的」×10
  - narration_para_pct 1.7 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周玉兰的」×7、「为什么会」×5、「”周玉兰轻」×4
  - narration_para_pct 6.8 低于目标 20.0
  - attr_adv_pct 15.8 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「那我们现在该怎么办？…」）
- 第 5 章：
  - 单条套路句式超限：「周玉兰的」×5
  - narration_para_pct 6.2 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13444
chapter_chars_mean: 2689
chapter_chars_median: 3163
chapter_chars_cv: 0.33
paragraphs_mean: 52.4
dialogue_chars_pct: 41.7
dialogue_para_pct: 84.4
interiority_para_pct: 9.2
narration_para_pct: 6.4
turn_under20_pct: 68.5
turn_over200_pct: 0.0
attr_say_pct: 30.2
attr_adv_pct: 12.8
scenes_per_chapter: 2.6
dialogue_run_mean: 6.6
turn_len_median: 15
```
