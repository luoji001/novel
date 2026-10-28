# 锁孔深处的光 生成报告

slug：`shipin-20261027-10`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6413
LLM 调用：57 次，累计 131.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙脱手而出 | 560 | short | 36.4 | 0 |  | 2 |
| 2 | 登记表飘落桌面 | 1236 | normal | 88.3 | 0 |  | 3 |
| 3 | 钥匙轻触锁孔 | 837 | normal | 32.5 | 0 |  | 3 |
| 4 | 怀表磕桌声响 | 1013 | normal | 36.3 | 0 |  | 1 |
| 5 | 房卡对光细看 | 1521 | normal | 37.7 | 0 |  | 4 |
| 6 | 木牌坠地回响 | 1240 | normal | 35.4 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 3 句（如「钥匙已经插入锁孔三分之二的位置，金属发出细微摩擦…」）
  - [observe] 章节过短 489 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「林晓阳的」×5
  - interiority_para_pct 8.7 高于目标 6.0
  - narration_para_pct 34.8 低于目标 35.0
- 第 3 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 96.9 高于目标 90.0
  - [observe] 章节过短 638 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「你总是在偷看别人东西…」）
- 第 5 章：
  - 单条套路句式超限：「陈国强的」×7
  - dialogue_chars_pct 46.4 高于目标 45.0
  - narration_para_pct 22.7 低于目标 35.0
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 6 章：
  - dialogue_chars_pct 45.4 高于目标 45.0
  - narration_para_pct 5.3 低于目标 35.0
  - dialogue_run_mean 12 高于目标 4.0
  - [observe] 章内自我复读 1 句（如「周雨桐拿起钢笔，在登记簿上画了个圈…」）
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 5826
chapter_chars_mean: 971
chapter_chars_median: 1052
chapter_chars_cv: 0.36
paragraphs_mean: 35.8
dialogue_chars_pct: 27.5
dialogue_para_pct: 59.4
interiority_para_pct: 2.9
narration_para_pct: 37.7
turn_under20_pct: 92.5
turn_over200_pct: 0.0
attr_say_pct: 54.5
attr_adv_pct: 23.0
scenes_per_chapter: 2
dialogue_run_mean: 3.9
turn_len_median: 9
```
