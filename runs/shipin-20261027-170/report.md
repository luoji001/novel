# 铜推子 生成报告

slug：`shipin-20261027-170`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6633
LLM 调用：57 次，累计 143.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜推子的低语 | 561 | short | 38.6 | 0 |  | 1 |
| 2 | 铜推子吻镜子 | 1411 | normal | 88.7 | 0 |  | 2 |
| 3 | 铜推子摩挲账本 | 1293 | normal | 90.8 | 0 |  | 2 |
| 4 | 铜推子与电推子对话 | 1179 | normal | 35.6 | 0 |  | 2 |
| 5 | 摩挲帽檐的午后 | 1105 | normal | 55.2 | 0 |  | 1 |
| 6 | 铜推子划过头顶 | 1078 | normal | 89.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 492 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 16.7 低于目标 35.0
  - dialogue_run_mean 6.7 高于目标 4.0
- 第 3 章：
  - narration_para_pct 27.8 低于目标 35.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 4 章：
  - narration_para_pct 32.4 低于目标 35.0
  - [observe] 章内自我复读 6 句（如「可这样大家都能更快剪好头发…」）
- 第 5 章：
  - interiority_para_pct 6.7 高于目标 6.0

## 整书结构指标

```
chapters: 6
total_chars: 6192
chapter_chars_mean: 1032
chapter_chars_median: 1077
chapter_chars_cv: 0.28
paragraphs_mean: 28.3
dialogue_chars_pct: 28.4
dialogue_para_pct: 64.9
interiority_para_pct: 1.7
narration_para_pct: 33.4
turn_under20_pct: 89.4
turn_over200_pct: 0.0
attr_say_pct: 43.5
attr_adv_pct: 3.3
scenes_per_chapter: 1.3
dialogue_run_mean: 2.8
turn_len_median: 12
```
