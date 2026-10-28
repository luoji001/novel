# 铜币 生成报告

slug：`shipin-20261027-250`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5925
LLM 调用：57 次，累计 120.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币的反光 | 500 | short | 20.6 | 0 |  | 3 |
| 2 | 计时器的余温 | 1033 | normal | 93.9 | 0 |  | 0 |
| 3 | 练习本的凸起纹路 | 894 | normal | 19.7 | 0 |  | 3 |
| 4 | 钥匙的裂痕 | 1289 | normal | 92.2 | 0 |  | 0 |
| 5 | 硬币的反光 | 1053 | normal | 92.2 | 0 |  | 2 |
| 6 | 证件的裂痕 | 1150 | normal | 36.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 437 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 808 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 标题重复：「硬币的反光」已存在
- 第 6 章：
  - [observe] 章内自我复读 2 句（如「远处传来熟悉的响动——那是练车场里的车辆启动声…」）
  - [observe] 标题与《钥匙的裂痕》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5481
chapter_chars_mean: 914
chapter_chars_median: 992
chapter_chars_cv: 0.29
paragraphs_mean: 29.7
dialogue_chars_pct: 11.8
dialogue_para_pct: 33.1
interiority_para_pct: 0.8
narration_para_pct: 66.1
turn_under20_pct: 97.9
turn_over200_pct: 0.0
attr_say_pct: 42.6
attr_adv_pct: 3.9
scenes_per_chapter: 2
dialogue_run_mean: 1.9
turn_len_median: 8
```
