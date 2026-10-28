# 铜钥风波 生成报告

slug：`shipin-20261027-276`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7006
LLM 调用：57 次，累计 135.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙坠入水痕 | 392 | short | 38.2 | 0 |  | 1 |
| 2 | 钥匙坠入水痕 | 1461 | normal | 92.9 | 0 |  | 2 |
| 3 | 擦拭门牌的人 | 1719 | normal | 37.1 | 0 |  | 3 |
| 4 | 登记簿的空白处 | 1020 | normal | 90.1 | 0 |  | 0 |
| 5 | 钥匙与红丝巾 | 1368 | normal | 88.7 | 0 |  | 2 |
| 6 | 钥匙撞响门环 | 1040 | normal | 54.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 348 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 24.2 低于目标 35.0
  - [observe] 标题重复：「钥匙坠入水痕」已存在
- 第 3 章：
  - 单条套路句式超限：「苏婉清的」×4
  - narration_para_pct 29.4 低于目标 35.0
  - [observe] attr_adv_pct 22.2 > 18.0（结构塌缩）
- 第 5 章：
  - narration_para_pct 13.5 低于目标 35.0
  - dialogue_run_mean 6.2 高于目标 4.0
- 第 6 章：
  - 单条套路句式超限：「林晓阳站在」×3
  - dialogue_run_mean 4.3 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 6557
chapter_chars_mean: 1093
chapter_chars_median: 1132
chapter_chars_cv: 0.4
paragraphs_mean: 29.8
dialogue_chars_pct: 27.2
dialogue_para_pct: 67.9
interiority_para_pct: 0.5
narration_para_pct: 31.6
turn_under20_pct: 93.8
turn_over200_pct: 0.0
attr_say_pct: 37.5
attr_adv_pct: 5.7
scenes_per_chapter: 1.7
dialogue_run_mean: 3.3
turn_len_median: 10
```
