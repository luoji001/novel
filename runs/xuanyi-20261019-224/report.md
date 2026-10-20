# 铜钥 生成报告

slug：`xuanyi-20261019-224`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14620
LLM 调用：68 次，累计 232.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 算盘珠上的影子 | 1537 | short | 85.8 | 0 |  | 2 |
| 2 | 攥住工资单的指尖 | 4213 | normal | 90.4 | 0 |  | 3 |
| 3 | 掀开铁皮盒的瞬间 | 3515 | normal | 90.6 | 0 |  | 2 |
| 4 | 摩挲铜钥匙的指尖 | 3469 | normal | 89.5 | 0 |  | 3 |
| 5 | 掀开木箱的瞬间 | 1881 | short | 91.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 16.1 低于目标 20.0
  - dialogue_run_mean 1.3 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「周秀兰的」×8、「“我不知道」×5、「陈国栋的」×5
  - attr_adv_pct 13.6 高于目标 10.0
  - [observe] 章内自我复读 19 句（如「挂断电话后，他坐回座位，拿出那张泛黄的工资单，轻…」）
- 第 3 章：
  - 单条套路句式超限：「陈国栋的」×3
  - narration_para_pct 18.6 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「他知道这」×4
  - dialogue_chars_pct 18.9 低于目标 20.0
  - narration_para_pct 19.7 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「周秀兰的」×5、「陈国栋的」×4
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 标题与《掀开铁皮盒的瞬间》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13959
chapter_chars_mean: 2792
chapter_chars_median: 3331
chapter_chars_cv: 0.39
paragraphs_mean: 57.8
dialogue_chars_pct: 28.0
dialogue_para_pct: 66.3
interiority_para_pct: 10.7
narration_para_pct: 23.1
turn_under20_pct: 80.7
turn_over200_pct: 0.0
attr_say_pct: 32.8
attr_adv_pct: 8.0
scenes_per_chapter: 3.2
dialogue_run_mean: 3.0
turn_len_median: 11
```
