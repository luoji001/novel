# 箱中票 生成报告

slug：`shipin-20261027-91`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5900
LLM 调用：57 次，累计 122.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 黑皮箱的裂痕 | 442 | short | 38.0 | 0 |  | 1 |
| 2 | 箱子的裂痕 | 896 | normal | 38.1 | 0 |  | 3 |
| 3 | 身份证与箱子的对峙 | 1152 | normal | 90.7 | 0 |  | 0 |
| 4 | 火车票上的名字 | 1288 | normal | 91.5 | 0 |  | 2 |
| 5 | 红围巾的温度 | 1207 | normal | 13.3 | 0 |  | 2 |
| 6 | 钢笔坠地三响 | 909 | normal | 91.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 412 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 27.3 低于目标 35.0
  - [observe] 章节过短 837 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《黑皮箱的裂痕》近似 0.73 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 命中套话收尾句
  - narration_para_pct 25.5 低于目标 35.0
- 第 5 章：
  - interiority_para_pct 13.8 高于目标 6.0
  - narration_para_pct 31.0 低于目标 35.0
- 第 6 章：
  - dialogue_chars_pct 4.9 低于目标 5.0

## 整书结构指标

```
chapters: 6
total_chars: 5515
chapter_chars_mean: 919
chapter_chars_median: 976
chapter_chars_cv: 0.31
paragraphs_mean: 24.2
dialogue_chars_pct: 22.6
dialogue_para_pct: 56.6
interiority_para_pct: 4.2
narration_para_pct: 39.1
turn_under20_pct: 98.1
turn_over200_pct: 0.0
attr_say_pct: 35.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 2.3
turn_len_median: 9
```
