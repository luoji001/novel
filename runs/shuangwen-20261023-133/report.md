# 账本 生成报告

slug：`shuangwen-20261023-133`
档位：爽文　闸门模式：observe
章数：10　总字数：21085
LLM 调用：97 次，累计 459.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅名册 | 1907 | normal | 97.6 | 0 |  | 1 |
| 2 | 墨迹未干的账簿 | 2354 | normal | 92.0 | 0 |  | 0 |
| 3 | 朱砂印泥的签字 | 2221 | normal | 92.3 | 0 |  | 1 |
| 4 | 账簿在案头发亮 | 2056 | normal | 93.5 | 0 |  | 1 |
| 5 | 朱砂涂抹的名册 | 1829 | normal | 92.9 | 0 |  | 2 |
| 6 | 签字的墨迹未干 | 2281 | normal | 90.9 | 0 |  | 2 |
| 7 | 账簿上的凹痕 | 1852 | normal | 94.2 | 0 |  | 3 |
| 8 | 账本在掌心发烫 | 1925 | normal | 91.7 | 0 |  | 1 |
| 9 | 签字的墨迹未干 | 1837 | normal | 90.7 | 0 |  | 2 |
| 10 | 墨迹未干的账簿 | 2813 | long | 36.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「知道自己」×3
- 第 3 章：
  - 单条套路句式超限：「赵明远的」×7、「李怀安的」×3
- 第 4 章：
  - attr_adv_pct 20.7 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「赵明远的」×5、「李怀安的」×3
  - dialogue_run_mean 15.5 高于目标 14.0
- 第 6 章：
  - 单条套路句式超限：「李怀安的」×6
  - attr_adv_pct 23.1 高于目标 12.0
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李怀安的」×4
  - attr_adv_pct 13.0 高于目标 12.0
- 第 8 章：
  - attr_adv_pct 13.0 高于目标 12.0
- 第 9 章：
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「签字的墨迹未干」已存在
- 第 10 章：
  - 单条套路句式超限：「李怀安的」×12
  - [observe] attr_adv_pct 44.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「墨迹未干的账簿」已存在

## 整书结构指标

```
chapters: 10
total_chars: 19963
chapter_chars_mean: 1996
chapter_chars_median: 1870
chapter_chars_cv: 0.15
paragraphs_mean: 48.3
dialogue_chars_pct: 48.1
dialogue_para_pct: 84.9
interiority_para_pct: 4.6
narration_para_pct: 10.5
turn_under20_pct: 74.2
turn_over200_pct: 0.0
attr_say_pct: 26.3
attr_adv_pct: 17.4
scenes_per_chapter: 2.5
dialogue_run_mean: 8.1
turn_len_median: 12
```
