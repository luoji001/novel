# 铜炉 生成报告

slug：`shuangwen-20261022-98`
档位：爽文　闸门模式：observe
章数：10　总字数：18168
LLM 调用：97 次，累计 425.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击铜炉 | 1860 | normal | 100.0 | 0 |  | 1 |
| 2 | 焚纸对峙 | 1668 | normal | 37.2 | 0 |  | 2 |
| 3 | 焚纸对峙 | 1679 | normal | 91.8 | 0 |  | 5 |
| 4 | 旧版细则手抄本 | 1824 | normal | 90.3 | 0 |  | 0 |
| 5 | 铜炉上的云纹 | 1554 | normal | 94.0 | 0 |  | 2 |
| 6 | 焚纸对峙 | 1809 | normal | 36.7 | 0 |  | 3 |
| 7 | 焚纸对峙 | 1324 | normal | 94.1 | 0 |  | 2 |
| 8 | 焚纸对峙 | 1718 | normal | 89.0 | 0 |  | 3 |
| 9 | 签字权 | 2094 | normal | 94.3 | 0 |  | 0 |
| 10 | 铜炉压红头文件 | 2628 | long | 93.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 15.0 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「陈国栋的」×3
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「陈国栋的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 15 高于目标 14.0
  - [observe] 标题重复：「焚纸对峙」已存在
- 第 5 章：
  - narration_para_pct 3.7 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「陈国栋的」×4
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
  - [observe] 标题重复：「焚纸对峙」已存在
- 第 7 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「焚纸对峙」已存在
- 第 8 章：
  - narration_para_pct 3.2 低于目标 5.0
  - dialogue_run_mean 30 高于目标 14.0
  - [observe] 标题重复：「焚纸对峙」已存在
- 第 10 章：
  - attr_adv_pct 20.8 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17319
chapter_chars_mean: 1732
chapter_chars_median: 1688
chapter_chars_cv: 0.2
paragraphs_mean: 35.6
dialogue_chars_pct: 47.6
dialogue_para_pct: 83.4
interiority_para_pct: 5.8
narration_para_pct: 10.8
turn_under20_pct: 65.2
turn_over200_pct: 0.0
attr_say_pct: 25.1
attr_adv_pct: 16.3
scenes_per_chapter: 1.4
dialogue_run_mean: 8.8
turn_len_median: 14
```
