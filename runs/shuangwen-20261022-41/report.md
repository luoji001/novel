# 作废的收据 生成报告

slug：`shuangwen-20261022-41`
档位：爽文　闸门模式：observe
章数：2　总字数：4234
LLM 调用：97 次，累计 374.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 编号贴纸的真假较量 | 1918 | normal | 99.0 | 0 |  | 1 |
| 2 | 计算器上的指纹痕迹 | 1790 | normal | 93.6 | 0 |  | 1 |
| 3 | 计算器上的指纹痕迹 | 1833 | normal | 94.8 | 0 |  | 2 |
| 4 | 撕碎的收据边缘 | 2040 | normal | 91.0 | 0 |  | 1 |
| 5 | 对峙于收据边缘 | 1920 | normal | 90.2 | 0 |  | 2 |
| 6 | 对峙于收据边缘 | 2001 | normal | 90.8 | 0 |  | 2 |
| 7 | 对峙于收据边缘 | 1996 | normal | 91.1 | 0 |  | 2 |
| 8 | 计算器上的指纹痕迹 | 1720 | normal | 35.4 | 0 |  | 4 |
| 9 | 计算器上的指纹痕迹 | 1854 | normal | 98.3 | 0 |  | 1 |
| 10 | 计算器上的指纹痕迹 | 2378 | long | 92.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×3
- 第 2 章：
  - 单条套路句式超限：「王德发的」×4
- 第 3 章：
  - 单条套路句式超限：「王德发的」×3、「李国强的」×3
  - [observe] 标题重复：「计算器上的指纹痕迹」已存在
- 第 4 章：
  - 单条套路句式超限：「王德发的」×3、「李国强的」×3
- 第 5 章：
  - 单条套路句式超限：「王德发的」×9
  - attr_adv_pct 20.0 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「王德发的」×6、「李国强的」×3
  - [observe] 标题重复：「对峙于收据边缘」已存在
- 第 7 章：
  - 单条套路句式超限：「王德发的」×3
  - [observe] 标题重复：「对峙于收据边缘」已存在
- 第 8 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 35 高于目标 14.0
  - [observe] attr_adv_pct 35.7 > 25.0（结构塌缩）
  - [observe] 标题重复：「计算器上的指纹痕迹」已存在
- 第 9 章：
  - attr_adv_pct 22.2 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「计算器上的指纹痕迹」已存在

## 整书结构指标

```
chapters: 2
total_chars: 4050
chapter_chars_mean: 2025
chapter_chars_median: 2025
chapter_chars_cv: 0.18
paragraphs_mean: 37
dialogue_chars_pct: 53.8
dialogue_para_pct: 88.9
interiority_para_pct: 2.7
narration_para_pct: 8.4
turn_under20_pct: 65.7
turn_over200_pct: 0.0
attr_say_pct: 17.2
attr_adv_pct: 21.0
scenes_per_chapter: 1.5
dialogue_run_mean: 11
turn_len_median: 16
```
