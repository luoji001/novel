# 裂镜 生成报告

slug：`shipin-20261027-338`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6174
LLM 调用：57 次，累计 129.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 剪刀划破晨雾 | 536 | short | 38.3 | 0 |  | 1 |
| 2 | 修镜子 | 1397 | normal | 95.7 | 0 |  | 1 |
| 3 | 剪刀插入裂缝 | 1124 | normal | 92.6 | 0 |  | 0 |
| 4 | 剪刀擦亮晨光 | 1050 | normal | 91.7 | 0 |  | 0 |
| 5 | 修补镜子 | 936 | normal | 35.7 | 0 |  | 2 |
| 6 | 修镜子 | 1125 | normal | 90.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 478 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 34.6 低于目标 35.0
- 第 5 章：
  - [observe] 章节过短 838 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《修镜子》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题重复：「修镜子」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5738
chapter_chars_mean: 956
chapter_chars_median: 1012
chapter_chars_cv: 0.3
paragraphs_mean: 29.5
dialogue_chars_pct: 30.1
dialogue_para_pct: 50.3
interiority_para_pct: 0.7
narration_para_pct: 49.0
turn_under20_pct: 81.6
turn_over200_pct: 0.0
attr_say_pct: 57.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.8
turn_len_median: 11
```
