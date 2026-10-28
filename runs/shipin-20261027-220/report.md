# 蓝纹钥匙 生成报告

slug：`shipin-20261027-220`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6640
LLM 调用：57 次，累计 137.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙映出波纹 | 618 | short | 38.2 | 0 |  | 3 |
| 2 | 钥匙摩挲桌面 | 955 | normal | 91.4 | 0 |  | 0 |
| 3 | 贝壳映出海平面 | 1253 | normal | 36.5 | 0 |  | 2 |
| 4 | 钥匙映红漆痕 | 1233 | normal | 0.0 | 0 |  | 3 |
| 5 | 钥匙坠入茶杯 | 1279 | normal | 89.0 | 0 |  | 2 |
| 6 | 钥匙擦过疤痕 | 1296 | normal | 89.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈国强的」×3
  - narration_para_pct 26.7 低于目标 35.0
  - [observe] 章节过短 574 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 23.1 低于目标 35.0
  - [observe] 章内自我复读 3 句（如「因为我想找个人，告诉他我回来了…」）
- 第 4 章：
  - 单条套路句式超限：「陈国强的」×4
  - narration_para_pct 16.7 低于目标 35.0
  - [observe] interiority_para_pct 16.7 > 15.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「林晓棠的」×3
  - interiority_para_pct 6.9 高于目标 6.0
- 第 6 章：
  - 单条套路句式超限：「陈国强的」×3
  - narration_para_pct 34.1 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 6209
chapter_chars_mean: 1035
chapter_chars_median: 1178
chapter_chars_cv: 0.25
paragraphs_mean: 28.3
dialogue_chars_pct: 25.3
dialogue_para_pct: 63.0
interiority_para_pct: 5.4
narration_para_pct: 31.7
turn_under20_pct: 96.5
turn_over200_pct: 0.0
attr_say_pct: 41.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 2.5
turn_len_median: 10
```
