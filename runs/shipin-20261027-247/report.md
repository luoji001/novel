# 屏争 生成报告

slug：`shipin-20261027-247`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6980
LLM 调用：57 次，累计 135.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 监控屏幕的红光 | 633 | short | 39.3 | 0 |  | 1 |
| 2 | 钥匙串的寒光 | 1106 | normal | 41.7 | 0 |  | 2 |
| 3 | 监控屏幕的坠落 | 1404 | normal | 90.4 | 0 |  | 1 |
| 4 | 钥匙与荧光卡片 | 1106 | normal | 89.0 | 0 |  | 1 |
| 5 | 钥匙转动的瞬间 | 1425 | normal | 36.3 | 0 |  | 1 |
| 6 | 钥匙转动的瞬间 | 1300 | normal | 35.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 574 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
- 第 3 章：
  - [observe] 标题与《监控屏幕的红光》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_chars_pct 3.7 低于目标 5.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「那你最好祈祷，今晚没人想看你一眼…」）
- 第 6 章：
  - [observe] 章内自我复读 2 句（如「你得注意点，别让那些东西再进来…」）
  - [observe] 标题重复：「钥匙转动的瞬间」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6511
chapter_chars_mean: 1085
chapter_chars_median: 1130
chapter_chars_cv: 0.26
paragraphs_mean: 29
dialogue_chars_pct: 11.9
dialogue_para_pct: 34.8
interiority_para_pct: 0.9
narration_para_pct: 64.3
turn_under20_pct: 97.7
turn_over200_pct: 0.0
attr_say_pct: 41.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.6
turn_len_median: 9
```
