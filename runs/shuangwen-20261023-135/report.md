# 验单风波 生成报告

slug：`shuangwen-20261023-135`
档位：爽文　闸门模式：observe
章数：10　总字数：19166
LLM 调用：97 次，累计 417.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字位置风波 | 1385 | normal | 100.0 | 0 |  | 1 |
| 2 | 清单交出时刻 | 1955 | normal | 94.4 | 0 |  | 1 |
| 3 | 财务报表核对 | 2040 | normal | 93.9 | 0 |  | 1 |
| 4 | 清单交出时刻 | 1973 | normal | 92.9 | 0 |  | 4 |
| 5 | 清单交出时刻 | 1947 | normal | 92.3 | 0 |  | 2 |
| 6 | 清单交出时刻 | 1791 | normal | 36.2 | 0 |  | 2 |
| 7 | 清单交出时刻 | 1771 | normal | 93.2 | 0 |  | 1 |
| 8 | 清单交出时刻 | 1821 | normal | 87.7 | 0 |  | 4 |
| 9 | 签字犹豫时刻 | 2030 | normal | 92.1 | 0 |  | 1 |
| 10 | 清单交出时刻 | 2443 | long | 35.2 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 2 章：
  - attr_adv_pct 12.5 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李国强的」×3
- 第 4 章：
  - narration_para_pct 3.0 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 16 高于目标 14.0
  - [observe] 标题重复：「清单交出时刻」已存在
- 第 5 章：
  - narration_para_pct 2.6 低于目标 5.0
  - [observe] 标题重复：「清单交出时刻」已存在
- 第 6 章：
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「清单交出时刻」已存在
- 第 7 章：
  - [observe] 标题重复：「清单交出时刻」已存在
- 第 8 章：
  - 单条套路句式超限：「李国强的」×4
  - narration_para_pct 2.4 低于目标 5.0
  - dialogue_run_mean 41 高于目标 14.0
  - [observe] 标题重复：「清单交出时刻」已存在
- 第 9 章：
  - 单条套路句式超限：「李国强的」×4
- 第 10 章：
  - narration_para_pct 1.9 低于目标 5.0
  - dialogue_run_mean 25.5 高于目标 14.0
  - [observe] attr_adv_pct 26.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「清单交出时刻」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18218
chapter_chars_mean: 1822
chapter_chars_median: 1858
chapter_chars_cv: 0.14
paragraphs_mean: 39.9
dialogue_chars_pct: 55.0
dialogue_para_pct: 90.3
interiority_para_pct: 1.8
narration_para_pct: 7.9
turn_under20_pct: 64.5
turn_over200_pct: 0.0
attr_say_pct: 29.3
attr_adv_pct: 12.3
scenes_per_chapter: 1.7
dialogue_run_mean: 13.7
turn_len_median: 14
```
