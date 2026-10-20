# 泛黄的合影 生成报告

slug：`xuanyi-20261019-61`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14786
LLM 调用：68 次，累计 223.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显影液中的老照片 | 2062 | short | 98.7 | 0 |  | 2 |
| 2 | 摩挲纸边的手指 | 3766 | normal | 88.6 | 0 |  | 4 |
| 3 | 摩挲登记本的指尖 | 3297 | normal | 44.3 | 0 |  | 3 |
| 4 | 摩挲照片的指尖 | 3825 | normal | 88.3 | 0 |  | 4 |
| 5 | 摩挲相机的指尖 | 1831 | short | 92.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「苏婉秋的」×3
  - narration_para_pct 16.1 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「苏婉秋的」×6、「林永年的」×4、「为什么会」×4
  - interiority_para_pct 21.2 高于目标 20.0
  - narration_para_pct 15.2 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「苏婉秋的」×4
  - dialogue_chars_pct 12.2 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「苏婉秋的」×10、「林永年的」×5、「”苏婉秋轻」×4
  - narration_para_pct 10.8 低于目标 20.0
  - attr_adv_pct 15.8 高于目标 10.0
  - [observe] 标题与《摩挲登记本的指尖》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「苏婉秋的」×5
  - narration_para_pct 3.2 低于目标 20.0
  - [observe] attr_adv_pct 23.1 > 20.0（结构塌缩）
  - [observe] 标题与《摩挲照片的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 14188
chapter_chars_mean: 2838
chapter_chars_median: 3187
chapter_chars_cv: 0.32
paragraphs_mean: 51.6
dialogue_chars_pct: 29.4
dialogue_para_pct: 69.0
interiority_para_pct: 13.6
narration_para_pct: 17.4
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 20.3
attr_adv_pct: 15.7
scenes_per_chapter: 3.8
dialogue_run_mean: 5.1
turn_len_median: 13
```
