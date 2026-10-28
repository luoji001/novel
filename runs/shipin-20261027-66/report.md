# 钥匙套 生成报告

slug：`shipin-20261027-66`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6498
LLM 调用：57 次，累计 132.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙孔中的余温 | 705 | short | 95.4 | 0 |  | 0 |
| 2 | 钥匙板上的空位 | 1130 | normal | 90.5 | 0 |  | 1 |
| 3 | 登记本上的刻痕 | 1191 | normal | 88.7 | 0 |  | 2 |
| 4 | 钥匙套边缘的刻痕 | 1286 | normal | 90.9 | 0 |  | 2 |
| 5 | 钥匙贴近耳畔 | 1219 | normal | 89.1 | 0 |  | 2 |
| 6 | 钥匙板上的刻痕 | 961 | normal | 59.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「林晓阳站在」×3
- 第 3 章：
  - narration_para_pct 12.0 低于目标 35.0
  - dialogue_run_mean 7 高于目标 4.0
- 第 4 章：
  - 单条套路句式超限：「林晓阳站在」×3
  - narration_para_pct 29.6 低于目标 35.0
- 第 5 章：
  - 单条套路句式超限：「张德顺的」×5
  - narration_para_pct 27.5 低于目标 35.0
- 第 6 章：
  - [observe] 标题与《钥匙板上的空位》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6082
chapter_chars_mean: 1014
chapter_chars_median: 1094
chapter_chars_cv: 0.21
paragraphs_mean: 26.5
dialogue_chars_pct: 27.0
dialogue_para_pct: 63.7
interiority_para_pct: 1.2
narration_para_pct: 35.1
turn_under20_pct: 91.5
turn_over200_pct: 0.0
attr_say_pct: 41.3
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 3.2
turn_len_median: 10
```
