# 铜钥 生成报告

slug：`xuanyi-20261019-64`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：16225
LLM 调用：68 次，累计 247.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 掀开铁皮箱盖 | 2025 | short | 97.3 | 0 |  | 3 |
| 2 | 摩挲钥匙的指尖 | 4566 | normal | 89.8 | 0 |  | 3 |
| 3 | 摩挲粮票的指尖 | 3848 | normal | 85.1 | 0 |  | 4 |
| 4 | 摩挲账本的指尖 | 3547 | normal | 89.0 | 0 |  | 5 |
| 5 | 摩挲口袋的指尖 | 2234 | short | 91.3 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周淑芬的」×6、「陈志远的」×5
  - narration_para_pct 13.2 低于目标 20.0
  - [observe] attr_adv_pct 57.1 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周淑芬的」×8、「“我不知道」×5、「陈志远的」×4
  - narration_para_pct 10.5 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「有些事，知道了也无济于事…」）
- 第 3 章：
  - 单条套路句式超限：「陈志远的」×8、「”周淑芬低」×4、「周淑芬的」×4
  - narration_para_pct 1.1 低于目标 20.0
  - dialogue_run_mean 20.8 高于目标 10.0
  - [observe] 标题与《摩挲钥匙的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「周淑芬的」×8、「陈志远的」×6、「他知道这」×4
  - narration_para_pct 10.3 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「陈志远抬起头，直视着她的眼睛…」）
  - [observe] attr_adv_pct 30.8 > 20.0（结构塌缩）
  - [observe] 标题与《摩挲粮票的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「周淑芬的」×10、「“我不知道」×3、「陈志远的」×3
  - narration_para_pct 16.1 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 标题与《摩挲粮票的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 15398
chapter_chars_mean: 3080
chapter_chars_median: 3376
chapter_chars_cv: 0.33
paragraphs_mean: 74.8
dialogue_chars_pct: 41.3
dialogue_para_pct: 84.0
interiority_para_pct: 6.7
narration_para_pct: 9.3
turn_under20_pct: 82.5
turn_over200_pct: 0.0
attr_say_pct: 22.6
attr_adv_pct: 20.4
scenes_per_chapter: 2.8
dialogue_run_mean: 8.5
turn_len_median: 13
```
