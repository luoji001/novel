# 铜牌 生成报告

slug：`shipin-20261027-331`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6171
LLM 调用：57 次，累计 128.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红色光芒照向录像带 | 427 | short | 20.2 | 0 |  | 2 |
| 2 | 钥匙串落前的红光 | 1080 | normal | 93.7 | 0 |  | 2 |
| 3 | 遥控器按下的瞬间 | 785 | normal | 35.4 | 0 |  | 3 |
| 4 | 螺丝刀断成两截 | 1284 | normal | 92.4 | 0 |  | 3 |
| 5 | 工牌坠落的瞬间 | 1244 | normal | 94.4 | 0 |  | 0 |
| 6 | 遥控器倾斜十五度 | 1345 | normal | 93.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 6.2 高于目标 6.0
  - [observe] 章节过短 378 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「小林站在」×3
- 第 3 章：
  - 命中套话收尾句
  - 情节与已写章节重复 0.66 ≥ 0.62（撞上「小林在深夜便利店门口与神秘黑车司机对峙，阻止其获取公司录…」）
  - [observe] 章节过短 701 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×5
  - narration_para_pct 33.3 低于目标 35.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 6 章：
  - narration_para_pct 33.3 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 5712
chapter_chars_mean: 952
chapter_chars_median: 1068
chapter_chars_cv: 0.37
paragraphs_mean: 29.8
dialogue_chars_pct: 18.4
dialogue_para_pct: 49.5
interiority_para_pct: 2.5
narration_para_pct: 48.0
turn_under20_pct: 97.5
turn_over200_pct: 0.0
attr_say_pct: 52.8
attr_adv_pct: 2.7
scenes_per_chapter: 1.8
dialogue_run_mean: 1.6
turn_len_median: 8
```
