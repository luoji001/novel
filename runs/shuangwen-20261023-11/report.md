# 旧标准副本 生成报告

slug：`shuangwen-20261023-11`
档位：爽文　闸门模式：observe
章数：10　总字数：17765
LLM 调用：97 次，累计 404.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 测试仪数字骤降 | 1806 | normal | 97.6 | 0 |  | 2 |
| 2 | 旧文件在桌上展开 | 1820 | normal | 92.1 | 0 |  | 2 |
| 3 | 纸屑堆积成堆 | 1545 | normal | 92.3 | 0 |  | 0 |
| 4 | 签字笔划破红印 | 1878 | normal | 92.2 | 0 |  | 3 |
| 5 | 旧标准副本被取出 | 1905 | normal | 93.0 | 0 |  | 0 |
| 6 | 旧验收单被递出 | 1399 | normal | 36.6 | 0 |  | 2 |
| 7 | 旧验收单被递出 | 1891 | normal | 90.9 | 0 |  | 2 |
| 8 | 旧验收单被递出 | 1429 | normal | 93.6 | 0 |  | 1 |
| 9 | 验单在桌上展开 | 1714 | normal | 91.2 | 0 |  | 1 |
| 10 | 旧验收单被递出 | 2368 | long | 93.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周振国的」×3
  - dialogue_chars_pct 29.9 低于目标 30.0
- 第 2 章：
  - 单条套路句式超限：「周振国的」×3
  - narration_para_pct 0.0 低于目标 5.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周振国的」×3
  - attr_adv_pct 21.4 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「周振国的」×4
  - [observe] 章内自我复读 2 句（如「可我手里还有当年的验收单…」）
- 第 7 章：
  - 单条套路句式超限：「周振国的」×3
  - [observe] 标题重复：「旧验收单被递出」已存在
- 第 8 章：
  - [observe] 标题重复：「旧验收单被递出」已存在
- 第 9 章：
  - [observe] 标题与《旧文件在桌上展开》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「林素梅的」×3
  - [observe] 标题重复：「旧验收单被递出」已存在

## 整书结构指标

```
chapters: 10
total_chars: 16912
chapter_chars_mean: 1691
chapter_chars_median: 1734
chapter_chars_cv: 0.16
paragraphs_mean: 34.6
dialogue_chars_pct: 40.7
dialogue_para_pct: 78.4
interiority_para_pct: 8.0
narration_para_pct: 13.6
turn_under20_pct: 70.5
turn_over200_pct: 0.0
attr_say_pct: 31.1
attr_adv_pct: 6.3
scenes_per_chapter: 1.7
dialogue_run_mean: 4.8
turn_len_median: 14
```
