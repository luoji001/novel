# 冰台 生成报告

slug：`shipin-20261027-64`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6619
LLM 调用：57 次，累计 139.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 冰台碎裂 | 551 | short | 37.6 | 0 |  | 1 |
| 2 | 铁秤与信纸 | 1049 | normal | 90.8 | 0 |  | 0 |
| 3 | 冰台划痕 | 1105 | normal | 39.3 | 0 |  | 2 |
| 4 | 鱼肚里的信笺 | 1394 | normal | 37.8 | 0 |  | 1 |
| 5 | 信纸轻触冰台 | 1307 | normal | 90.4 | 0 |  | 1 |
| 6 | 信纸飘落 | 1207 | normal | 90.1 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

1. 第二章提到“信的内容竟与老张的账单有关”，但第四章提到“信件竟是李婶儿子所写”，两者信件来源和内容不一致，存在矛盾。

2. 第六章提到“信件落入李婶手中”，但第五章提到“老张决定归还信件”，前后信件归属不一致，存在矛盾。

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 495 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - dialogue_chars_pct 2.3 低于目标 5.0
  - narration_para_pct 95.7 高于目标 90.0
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「老张的手指无意识地摩挲着秤台边缘，那里留有一道浅…」）
- 第 5 章：
  - 单条套路句式超限：「老张站在」×3

## 整书结构指标

```
chapters: 6
total_chars: 6096
chapter_chars_mean: 1016
chapter_chars_median: 1063
chapter_chars_cv: 0.28
paragraphs_mean: 36.7
dialogue_chars_pct: 18.6
dialogue_para_pct: 43.5
interiority_para_pct: 1.5
narration_para_pct: 55.0
turn_under20_pct: 99.1
turn_over200_pct: 0.0
attr_say_pct: 72.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.7
turn_len_median: 9
```
