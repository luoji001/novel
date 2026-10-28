# 铜钥 生成报告

slug：`shipin-20261027-150`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6542
LLM 调用：57 次，累计 131.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙上的凹痕 | 519 | short | 39.0 | 0 |  | 2 |
| 2 | 钥匙与铁盒对话 | 1330 | normal | 34.3 | 0 |  | 3 |
| 3 | 钥匙与便签纸较量 | 1189 | normal | 92.0 | 0 |  | 0 |
| 4 | 登记本边缘的褶皱 | 946 | normal | 54.4 | 0 |  | 0 |
| 5 | 钥匙与铁盒较量 | 1347 | normal | 90.5 | 0 |  | 1 |
| 6 | 钥匙落进铁盒 | 1205 | normal | 90.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「还是得找老张确认一下…」）
  - [observe] 章节过短 483 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 15.4 低于目标 35.0
  - dialogue_run_mean 7.3 高于目标 4.0
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）
- 第 5 章：
  - [observe] 标题与《钥匙与铁盒对话》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题与《钥匙与铁盒对话》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6164
chapter_chars_mean: 1027
chapter_chars_median: 1126
chapter_chars_cv: 0.29
paragraphs_mean: 21.8
dialogue_chars_pct: 22.4
dialogue_para_pct: 61.7
interiority_para_pct: 0.0
narration_para_pct: 38.3
turn_under20_pct: 94.6
turn_over200_pct: 0.0
attr_say_pct: 39.2
attr_adv_pct: 4.0
scenes_per_chapter: 1.5
dialogue_run_mean: 3.4
turn_len_median: 11
```
