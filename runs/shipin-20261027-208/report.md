# 硬币失踪记 生成报告

slug：`shipin-20261027-208`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6616
LLM 调用：57 次，累计 143.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币的震颤 | 608 | short | 37.8 | 0 |  | 1 |
| 2 | 水壶的碰撞声 | 1442 | normal | 88.2 | 0 |  | 3 |
| 3 | 身份证的磨损痕迹 | 981 | normal | 0.0 | 0 |  | 1 |
| 4 | 钥匙与木板的缝隙 | 1203 | normal | 91.9 | 0 |  | 0 |
| 5 | 水壶的裂痕 | 1228 | normal | 34.4 | 0 |  | 5 |
| 6 | 硬币与身份证的对峙 | 1148 | normal | 91.3 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 561 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「沈青梧的」×4
  - interiority_para_pct 8.3 高于目标 6.0
  - narration_para_pct 30.6 低于目标 35.0
- 第 3 章：
  - [observe] interiority_para_pct 16.7 > 15.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「沈青梧的」×3
  - narration_para_pct 8.3 低于目标 35.0
  - dialogue_run_mean 10.5 高于目标 4.0
  - [observe] 章内自我复读 3 句（如「你知道吗？每个人都会在这里找到属于自己的答案…」）
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 6253
chapter_chars_mean: 1042
chapter_chars_median: 1120
chapter_chars_cv: 0.26
paragraphs_mean: 22.3
dialogue_chars_pct: 18.1
dialogue_para_pct: 55.9
interiority_para_pct: 6.0
narration_para_pct: 38.1
turn_under20_pct: 89.4
turn_over200_pct: 0.0
attr_say_pct: 52.9
attr_adv_pct: 12.3
scenes_per_chapter: 2
dialogue_run_mean: 2.9
turn_len_median: 8
```
