# 黄铜钥匙 生成报告

slug：`shipin-20261027-374`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5473
LLM 调用：57 次，累计 118.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙滑落瞬间 | 480 | short | 22.8 | 0 |  | 1 |
| 2 | 钥匙与纸条的对峙 | 1021 | normal | 91.0 | 0 |  | 2 |
| 3 | 房卡与无名房间 | 1045 | normal | 89.9 | 0 |  | 0 |
| 4 | 钥匙与刻痕对望 | 783 | normal | 36.0 | 0 |  | 1 |
| 5 | 手机撞向钥匙板 | 931 | normal | 90.1 | 0 |  | 0 |
| 6 | 钥匙凹槽的秘密 | 1207 | normal | 85.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 434 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 15.0 低于目标 35.0
  - dialogue_run_mean 5.7 高于目标 4.0
- 第 4 章：
  - [observe] 章节过短 730 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - narration_para_pct 19.2 低于目标 35.0
  - dialogue_run_mean 7 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 5129
chapter_chars_mean: 855
chapter_chars_median: 918
chapter_chars_cv: 0.29
paragraphs_mean: 20.7
dialogue_chars_pct: 26.4
dialogue_para_pct: 61.4
interiority_para_pct: 0.8
narration_para_pct: 37.8
turn_under20_pct: 82.9
turn_over200_pct: 0.0
attr_say_pct: 33.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 3.2
turn_len_median: 10
```
