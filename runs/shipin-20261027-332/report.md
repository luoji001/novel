# 铜钥 生成报告

slug：`shipin-20261027-332`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6349
LLM 调用：57 次，累计 120.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙滑向凹槽 | 348 | short | 40.0 | 0 |  | 1 |
| 2 | 登记本第37页 | 1012 | normal | 92.2 | 0 |  | 0 |
| 3 | 监控屏上的车标 | 1258 | normal | 91.1 | 0 |  | 1 |
| 4 | 钥匙与银镯相碰 | 1076 | normal | 49.5 | 0 |  | 0 |
| 5 | 钥匙与登记本对峙 | 1284 | normal | 85.2 | 0 |  | 2 |
| 6 | 钥匙与银镯相碰 | 1365 | normal | 85.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

1. 第二章提到陈国强联系上一名女子，得知与一桩旧案有关；第三章周雨晴通过监控发现钥匙来源与一桩旧案有关。但未明确说明两者是否为同一桩旧案，存在信息来源不一致的矛盾。

2. 第四章提到林晓桐发现一把陌生钥匙，试图匹配房号未果；第五章提到陈国强发现一把陌生铜钥匙，与登记本中模糊记录有关。两处“陌生钥匙”是否为同一把钥匙未明确，存在指代不清的矛盾。

3. 第六章提到周雨晴与同事发现监控中出现神秘黑影，疑似与失踪钥匙有关，但前文并未明确说明“失踪钥匙”具体指哪把钥匙，导致信息不连贯。

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 312 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 29.4 低于目标 35.0
- 第 5 章：
  - narration_para_pct 10.0 低于目标 35.0
  - dialogue_run_mean 9 高于目标 4.0
- 第 6 章：
  - narration_para_pct 4.0 低于目标 35.0
  - dialogue_run_mean 12 高于目标 4.0
  - [observe] 标题重复：「钥匙与银镯相碰」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5989
chapter_chars_mean: 998
chapter_chars_median: 1093
chapter_chars_cv: 0.36
paragraphs_mean: 20.2
dialogue_chars_pct: 24.1
dialogue_para_pct: 68.8
interiority_para_pct: 0.0
narration_para_pct: 31.2
turn_under20_pct: 90.5
turn_over200_pct: 0.0
attr_say_pct: 53.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 4.7
turn_len_median: 10
```
