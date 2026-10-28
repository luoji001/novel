# 钥匙孔的微光 生成报告

slug：`shipin-20261027-164`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5398
LLM 调用：57 次，累计 120.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙孔的凹痕 | 341 | short | 38.2 | 0 |  | 1 |
| 2 | 登记簿的空白页 | 866 | normal | 35.9 | 0 |  | 4 |
| 3 | 钥匙坠地回响 | 623 | normal | 20.4 | 0 |  | 3 |
| 4 | 钥匙抵住纸张 | 1203 | normal | 90.2 | 0 |  | 1 |
| 5 | 铜铃系腕响 | 1009 | normal | 92.5 | 0 |  | 0 |
| 6 | 钥匙触碰铜匙 | 1350 | normal | 92.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 303 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 26.1 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
  - [observe] 章内自我复读 2 句（如「这是907房间的钥匙…」）
  - [observe] 章节过短 805 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 585 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - 单条套路句式超限：「周振国的」×3
- 第 6 章：
  - 单条套路句式超限：「周振国的」×3
  - 情节与已写章节重复 0.85 ≥ 0.62（撞上「林婉清发现一把无主钥匙，揭开二十年前的秘密，并与周振国展…」）

## 整书结构指标

```
chapters: 6
total_chars: 5036
chapter_chars_mean: 839
chapter_chars_median: 878
chapter_chars_cv: 0.42
paragraphs_mean: 22.7
dialogue_chars_pct: 21.7
dialogue_para_pct: 47.7
interiority_para_pct: 1.1
narration_para_pct: 51.2
turn_under20_pct: 94.2
turn_over200_pct: 0.0
attr_say_pct: 60.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.0
turn_len_median: 11
```
