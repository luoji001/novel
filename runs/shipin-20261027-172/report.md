# 当票 生成报告

slug：`shipin-20261027-172`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6691
LLM 调用：57 次，累计 133.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撑伞的人 | 812 | short | 92.9 | 0 |  | 2 |
| 2 | 硬币与算盘 | 1621 | normal | 85.4 | 0 |  | 2 |
| 3 | 铜钥匙的光痕 | 989 | normal | 90.2 | 0 |  | 0 |
| 4 | 铜勺与纸片的对望 | 813 | normal | 14.4 | 0 |  | 3 |
| 5 | 铜钥匙的温度 | 1211 | normal | 92.2 | 0 |  | 1 |
| 6 | 算珠与旧照片 | 1239 | normal | 90.1 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 15.0 低于目标 35.0
  - dialogue_run_mean 5.3 高于目标 4.0
- 第 2 章：
  - narration_para_pct 18.8 低于目标 35.0
  - dialogue_run_mean 8.7 高于目标 4.0
- 第 4 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 97.7 高于目标 90.0
  - [observe] 章节过短 668 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - [observe] 标题与《铜钥匙的光痕》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6165
chapter_chars_mean: 1028
chapter_chars_median: 1027
chapter_chars_cv: 0.31
paragraphs_mean: 33
dialogue_chars_pct: 28.4
dialogue_para_pct: 58.8
interiority_para_pct: 0.9
narration_para_pct: 40.4
turn_under20_pct: 96.3
turn_over200_pct: 0.0
attr_say_pct: 55.3
attr_adv_pct: 0.0
scenes_per_chapter: 2.5
dialogue_run_mean: 3.8
turn_len_median: 10
```
