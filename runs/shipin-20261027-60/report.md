# 船票 生成报告

slug：`shipin-20261027-60`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6505
LLM 调用：57 次，累计 139.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙与旧船票 | 624 | short | 38.8 | 0 |  | 1 |
| 2 | 铜钥匙的裂痕 | 1135 | normal | 94.3 | 0 |  | 0 |
| 3 | 烟斗与红绳 | 1003 | normal | 92.9 | 0 |  | 0 |
| 4 | 收音机的电流声 | 1357 | normal | 93.3 | 0 |  | 0 |
| 5 | 铜钥匙与旧船票 | 1203 | normal | 92.4 | 0 |  | 2 |
| 6 | 铜钥匙的重量 | 1177 | normal | 90.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 555 < 597（本章目标 1087 字的 55%）
- 第 5 章：
  - 单条套路句式超限：「林小满的」×3
  - [observe] 标题重复：「铜钥匙与旧船票」已存在
- 第 6 章：
  - [observe] 标题与《铜钥匙的裂痕》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6086
chapter_chars_mean: 1014
chapter_chars_median: 1078
chapter_chars_cv: 0.25
paragraphs_mean: 26.3
dialogue_chars_pct: 26.4
dialogue_para_pct: 54.2
interiority_para_pct: 0.0
narration_para_pct: 45.8
turn_under20_pct: 91.0
turn_over200_pct: 0.0
attr_say_pct: 55.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 1.6
turn_len_median: 10
```
