# 药房登记簿 生成报告

slug：`xuanyi-20261019-269`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13726
LLM 调用：68 次，累计 217.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记簿上的指纹 | 1318 | short | 97.7 | 0 |  | 1 |
| 2 | 抚摸旧处方单的指痕 | 3567 | normal | 91.5 | 0 |  | 2 |
| 3 | 墨迹与签名对峙 | 3452 | normal | 89.1 | 0 |  | 3 |
| 4 | 触摸处方单的指尖 | 3407 | normal | 87.5 | 0 |  | 4 |
| 5 | 登记簿上的日期不符 | 1977 | short | 91.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 13.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周玉兰的」×6、「沈文远站在」×3、「沈文远的」×3
  - narration_para_pct 7.5 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「沈文远的」×8、「周玉兰的」×7
  - narration_para_pct 7.3 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「周玉兰的」×10、「沈文远的」×3、「为什么会」×3
  - narration_para_pct 8.7 低于目标 20.0
  - dialogue_run_mean 10.3 高于目标 10.0
  - [observe] 标题与《抚摸旧处方单的指痕》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「沈文远站在」×3
  - [observe] 标题与《登记簿上的指纹》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13121
chapter_chars_mean: 2624
chapter_chars_median: 3253
chapter_chars_cv: 0.38
paragraphs_mean: 52
dialogue_chars_pct: 36.9
dialogue_para_pct: 80.9
interiority_para_pct: 8.8
narration_para_pct: 10.3
turn_under20_pct: 68.9
turn_over200_pct: 0.0
attr_say_pct: 26.7
attr_adv_pct: 4.7
scenes_per_chapter: 2.6
dialogue_run_mean: 6.7
turn_len_median: 13
```
