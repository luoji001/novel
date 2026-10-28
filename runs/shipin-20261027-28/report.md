# 药瓶的归属 生成报告

slug：`shipin-20261027-28`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6153
LLM 调用：57 次，累计 130.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药瓶的归属 | 472 | short | 22.7 | 0 |  | 2 |
| 2 | 病历本摔落的回音 | 1258 | normal | 92.8 | 0 |  | 2 |
| 3 | 红袖章的缝线 | 1052 | normal | 91.1 | 0 |  | 1 |
| 4 | 体温计的倒影 | 959 | normal | 94.0 | 0 |  | 0 |
| 5 | 注射器的较量 | 1174 | normal | 90.8 | 0 |  | 3 |
| 6 | 药瓶的归属 | 1232 | normal | 36.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 411 < 597（本章目标 1087 字的 55%）
  - [observe] attr_adv_pct 100.0 > 18.0（结构塌缩）
- 第 2 章：
  - narration_para_pct 15.0 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
- 第 3 章：
  - narration_para_pct 30.8 低于目标 35.0
- 第 5 章：
  - 单条套路句式超限：「李娟站在」×4
  - 情节与已写章节重复 0.63 ≥ 0.62（撞上「李娟为争夺儿子的药物与护士长陈雪梅对峙，最终得知孩子在I…」）
  - dialogue_run_mean 4.8 高于目标 4.0
- 第 6 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
  - [observe] 标题重复：「药瓶的归属」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5725
chapter_chars_mean: 954
chapter_chars_median: 1035
chapter_chars_cv: 0.3
paragraphs_mean: 28.2
dialogue_chars_pct: 24.3
dialogue_para_pct: 59.3
interiority_para_pct: 1.2
narration_para_pct: 39.5
turn_under20_pct: 83.6
turn_over200_pct: 0.0
attr_say_pct: 35.2
attr_adv_pct: 19.3
scenes_per_chapter: 1.3
dialogue_run_mean: 2.9
turn_len_median: 8
```
