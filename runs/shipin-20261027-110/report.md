# 硬币风波 生成报告

slug：`shipin-20261027-110`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6796
LLM 调用：57 次，累计 136.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币与掌心纹路 | 549 | short | 34.7 | 0 |  | 3 |
| 2 | 硬币与黑色手套 | 1307 | normal | 94.9 | 0 |  | 0 |
| 3 | 登记簿上的铅笔划痕 | 1137 | normal | 91.8 | 0 |  | 0 |
| 4 | 硬币与掌心纹路 | 1426 | normal | 90.2 | 0 |  | 3 |
| 5 | 硬币滚落至地面 | 1318 | normal | 36.6 | 0 |  | 4 |
| 6 | 硬币与红色袖章 | 1053 | normal | 89.2 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 2.5 低于目标 5.0
  - interiority_para_pct 9.1 高于目标 6.0
  - [observe] 章节过短 512 < 597（本章目标 1087 字的 55%）
- 第 4 章：
  - 单条套路句式超限：「王建国的」×4
  - narration_para_pct 30.8 低于目标 35.0
  - [observe] 标题重复：「硬币与掌心纹路」已存在
- 第 5 章：
  - 单条套路句式超限：「王建国站在」×3
  - narration_para_pct 25.7 低于目标 35.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 6406
chapter_chars_mean: 1068
chapter_chars_median: 1157
chapter_chars_cv: 0.28
paragraphs_mean: 24.3
dialogue_chars_pct: 24.1
dialogue_para_pct: 55.6
interiority_para_pct: 2.2
narration_para_pct: 42.3
turn_under20_pct: 80.7
turn_over200_pct: 0.0
attr_say_pct: 34.1
attr_adv_pct: 5.2
scenes_per_chapter: 1.3
dialogue_run_mean: 2.6
turn_len_median: 10
```
