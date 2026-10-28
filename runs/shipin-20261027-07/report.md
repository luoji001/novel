# 蓝箱 生成报告

slug：`shipin-20261027-07`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7033
LLM 调用：57 次，累计 137.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙串上的冰霜 | 571 | short | 17.6 | 0 |  | 3 |
| 2 | 蓝色皮箱的日期 | 1304 | normal | 95.2 | 0 |  | 1 |
| 3 | 敲打箱锁的节奏 | 1481 | normal | 90.6 | 0 |  | 3 |
| 4 | 红笔圈出的日期 | 1267 | normal | 33.1 | 0 |  | 2 |
| 5 | 敲击箱角的节奏 | 1097 | normal | 31.7 | 0 |  | 3 |
| 6 | 钥匙串坠入冰霜 | 1307 | normal | 92.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 2.0 低于目标 5.0
  - narration_para_pct 95.0 高于目标 90.0
  - [observe] 章节过短 500 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「李建国的」×3
- 第 3 章：
  - 单条套路句式超限：「李建国的」×3
  - narration_para_pct 19.0 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
- 第 4 章：
  - interiority_para_pct 8.8 高于目标 6.0
  - [observe] 章内自我复读 10 句（如「老周低头继续翻动记账本，纸页发出沙沙声，像风穿过…」）
- 第 5 章：
  - dialogue_chars_pct 1.6 低于目标 5.0
  - narration_para_pct 92.3 高于目标 90.0
  - [observe] 标题与《敲打箱锁的节奏》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 22.2 低于目标 35.0
  - [observe] 标题与《钥匙串上的冰霜》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6494
chapter_chars_mean: 1082
chapter_chars_median: 1181
chapter_chars_cv: 0.3
paragraphs_mean: 32.2
dialogue_chars_pct: 21.1
dialogue_para_pct: 49.3
interiority_para_pct: 2.3
narration_para_pct: 48.4
turn_under20_pct: 92.6
turn_over200_pct: 0.0
attr_say_pct: 44.8
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 2.2
turn_len_median: 8
```
