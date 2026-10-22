# 登记簿 生成报告

slug：`shuangwen-20261022-17`
档位：爽文　闸门模式：observe
章数：10　总字数：19527
LLM 调用：97 次，累计 370.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指拂过泛黄登记簿 | 1973 | normal | 96.9 | 0 |  | 1 |
| 2 | 手指拂过泛黄登记簿 | 1933 | normal | 91.7 | 0 |  | 3 |
| 3 | 手指抚过旧登记簿 | 1722 | normal | 93.2 | 0 |  | 1 |
| 4 | 墨迹重显的纸张 | 1818 | normal | 94.1 | 0 |  | 0 |
| 5 | 手指拂过木桌刻痕 | 1976 | normal | 92.1 | 0 |  | 0 |
| 6 | 手指拂过木桌刻痕 | 1766 | normal | 91.3 | 0 |  | 3 |
| 7 | 手指拂过登记簿褶皱 | 2059 | normal | 93.4 | 0 |  | 1 |
| 8 | 手指拂过登记簿扉页 | 2034 | normal | 89.6 | 0 |  | 2 |
| 9 | 手指拂过登记簿扉页 | 1731 | normal | 35.5 | 0 |  | 2 |
| 10 | 手指抚过登记簿扉页 | 2505 | long | 91.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「带着一丝」×3
- 第 2 章：
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 15.5 高于目标 14.0
  - [observe] 标题重复：「手指拂过泛黄登记簿」已存在
- 第 3 章：
  - [observe] 标题与《手指拂过泛黄登记簿》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 3.3 低于目标 5.0
  - dialogue_run_mean 14.5 高于目标 14.0
  - [observe] 标题重复：「手指拂过木桌刻痕」已存在
- 第 7 章：
  - [observe] 标题与《手指拂过泛黄登记簿》近似 0.78 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 命中套话收尾句
  - [observe] 标题与《手指拂过登记簿褶皱》近似 0.78 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「手指拂过登记簿扉页」已存在
- 第 10 章：
  - [observe] 标题与《手指拂过登记簿扉页》近似 0.89 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18490
chapter_chars_mean: 1849
chapter_chars_median: 1850
chapter_chars_cv: 0.12
paragraphs_mean: 42.9
dialogue_chars_pct: 50.8
dialogue_para_pct: 85.8
interiority_para_pct: 5.1
narration_para_pct: 9.1
turn_under20_pct: 70.5
turn_over200_pct: 0.0
attr_say_pct: 42.6
attr_adv_pct: 6.8
scenes_per_chapter: 1.3
dialogue_run_mean: 8.7
turn_len_median: 13
```
