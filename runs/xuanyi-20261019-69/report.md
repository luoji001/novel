# 药瓶上的签名 生成报告

slug：`xuanyi-20261019-69`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14112
LLM 调用：68 次，累计 219.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 印章的归属 | 1537 | short | 97.0 | 0 |  | 3 |
| 2 | 摩挲账本的指尖 | 3511 | normal | 88.8 | 0 |  | 2 |
| 3 | 摩挲处方单的指尖 | 3301 | normal | 87.8 | 0 |  | 6 |
| 4 | 摩挲印章的指尖 | 3794 | normal | 87.9 | 0 |  | 3 |
| 5 | 涂改的交接清单 | 1964 | short | 91.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈文远的」×4
  - narration_para_pct 12.9 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「周素云的」×6、「沈文远的」×6
  - narration_para_pct 13.5 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「沈文远的」×12、「周素云的」×7、「”周素云低」×5
  - dialogue_chars_pct 62.5 高于目标 58.0
  - narration_para_pct 5.0 低于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0
  - dialogue_run_mean 14 高于目标 10.0
  - [observe] 标题与《摩挲账本的指尖》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「沈文远的」×13、「周素云的」×7、「”周素云低」×5
  - narration_para_pct 7.9 低于目标 20.0
  - [observe] 标题与《摩挲账本的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「周素云的」×4、「沈文远的」×4
  - narration_para_pct 5.9 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13513
chapter_chars_mean: 2703
chapter_chars_median: 3165
chapter_chars_cv: 0.36
paragraphs_mean: 50.6
dialogue_chars_pct: 46.7
dialogue_para_pct: 86.4
interiority_para_pct: 4.8
narration_para_pct: 8.9
turn_under20_pct: 64.0
turn_over200_pct: 0.0
attr_say_pct: 19.1
attr_adv_pct: 8.5
scenes_per_chapter: 3.6
dialogue_run_mean: 8.3
turn_len_median: 15
```
