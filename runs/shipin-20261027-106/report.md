# 冰台之争 生成报告

slug：`shipin-20261027-106`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6160
LLM 调用：57 次，累计 139.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 秤杆挑信 | 447 | short | 38.9 | 0 |  | 1 |
| 2 | 秤杆压信 | 1451 | normal | 36.2 | 0 |  | 2 |
| 3 | 秤杆压信 | 830 | normal | 21.0 | 0 |  | 4 |
| 4 | 秤杆压信 | 1059 | normal | 54.9 | 0 |  | 2 |
| 5 | 红钮与信封 | 1213 | normal | 91.2 | 0 |  | 0 |
| 6 | 秤杆压信 | 1154 | normal | 91.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 415 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 4 句（如「你要是敢碰，我就把你推车掀翻…」）
  - [observe] 标题与《秤杆挑信》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - dialogue_chars_pct 3.2 低于目标 5.0
  - [observe] 章内自我复读 2 句（如「监控员松开手指，红色按钮回到原位，屏幕依旧闪着细…」）
  - [observe] 章节过短 758 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「秤杆压信」已存在
- 第 4 章：
  - 情节与已写章节重复 0.63 ≥ 0.62（撞上「老张与阿珍争夺一封神秘信件，因信中隐藏的秘密引发激烈冲突…」）
  - [observe] 标题重复：「秤杆压信」已存在
- 第 6 章：
  - [observe] 标题重复：「秤杆压信」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5665
chapter_chars_mean: 944
chapter_chars_median: 1018
chapter_chars_cv: 0.35
paragraphs_mean: 34.7
dialogue_chars_pct: 12.1
dialogue_para_pct: 34.8
interiority_para_pct: 2.2
narration_para_pct: 63.0
turn_under20_pct: 100.0
turn_over200_pct: 0.0
attr_say_pct: 20.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.4
turn_len_median: 8
```
