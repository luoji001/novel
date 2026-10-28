# 冰台上的胎记 生成报告

slug：`shipin-20261027-148`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6013
LLM 调用：57 次，累计 136.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 鱼秤上的水珠 | 591 | short | 15.8 | 0 |  | 3 |
| 2 | 信与胎记的对峙 | 1243 | normal | 93.9 | 0 |  | 1 |
| 3 | 鱼尾撞破塑料袋 | 926 | normal | 91.6 | 0 |  | 0 |
| 4 | 鱼秤砸进塑料袋 | 1108 | normal | 90.3 | 0 |  | 0 |
| 5 | 冰台上的鱼鳞 | 1022 | normal | 91.1 | 0 |  | 0 |
| 6 | 信与铜镯的对峙 | 1117 | normal | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 529 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - attr_adv_pct 11.1 高于目标 10.0
- 第 6 章：
  - narration_para_pct 20.8 低于目标 35.0
  - [observe] 标题与《信与胎记的对峙》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5594
chapter_chars_mean: 932
chapter_chars_median: 996
chapter_chars_cv: 0.23
paragraphs_mean: 27
dialogue_chars_pct: 17.7
dialogue_para_pct: 52.1
interiority_para_pct: 0.0
narration_para_pct: 47.9
turn_under20_pct: 94.7
turn_over200_pct: 0.0
attr_say_pct: 36.1
attr_adv_pct: 2.5
scenes_per_chapter: 1
dialogue_run_mean: 2.1
turn_len_median: 9
```
