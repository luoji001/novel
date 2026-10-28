# 锁扣 生成报告

slug：`shipin-20261027-251`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6349
LLM 调用：57 次，累计 121.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 皮箱的重量 | 477 | short | 37.6 | 0 |  | 1 |
| 2 | 热饮杯的指纹痕迹 | 1143 | normal | 94.5 | 0 |  | 1 |
| 3 | 锁扣的裂痕 | 1196 | normal | 95.1 | 0 |  | 0 |
| 4 | 手机照亮的拉链 | 1443 | normal | 94.5 | 0 |  | 1 |
| 5 | 皮箱的裂纹 | 1097 | normal | 90.9 | 0 |  | 1 |
| 6 | 手机照亮的拉链 | 987 | normal | 36.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 412 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - attr_adv_pct 11.1 高于目标 10.0
- 第 4 章：
  - narration_para_pct 30.8 低于目标 35.0
- 第 5 章：
  - [observe] 标题与《皮箱的重量》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 章节过短 868 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「手机照亮的拉链」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5770
chapter_chars_mean: 962
chapter_chars_median: 1028
chapter_chars_cv: 0.32
paragraphs_mean: 40.7
dialogue_chars_pct: 20.8
dialogue_para_pct: 44.4
interiority_para_pct: 1.1
narration_para_pct: 54.6
turn_under20_pct: 99.3
turn_over200_pct: 0.0
attr_say_pct: 51.7
attr_adv_pct: 2.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.7
turn_len_median: 8
```
