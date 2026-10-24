# 铁皮盒 生成报告

slug：`shuangwen-20261023-21`
档位：爽文　闸门模式：observe
章数：10　总字数：18938
LLM 调用：97 次，累计 425.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 打印机吞吐账单 | 2138 | normal | 39.5 | 0 |  | 1 |
| 2 | 铁皮盒里的旧账单 | 1909 | normal | 89.1 | 0 |  | 1 |
| 3 | 纸片上的数字痕迹 | 1513 | normal | 92.3 | 0 |  | 1 |
| 4 | 手指划过纸页边缘 | 1688 | normal | 92.6 | 0 |  | 3 |
| 5 | 手指按在纸页上 | 1725 | normal | 92.7 | 0 |  | 0 |
| 6 | 旧账本的残页 | 2124 | normal | 91.2 | 0 |  | 0 |
| 7 | 打印机吞吐账单 | 1874 | normal | 91.9 | 0 |  | 1 |
| 8 | 手指按在纸页上 | 2011 | normal | 36.4 | 0 |  | 2 |
| 9 | 手指按在纸页上 | 1770 | normal | 90.8 | 0 |  | 2 |
| 10 | 手指按在纸页上 | 2176 | long | 86.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 2 章：
  - dialogue_chars_pct 28.8 低于目标 30.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
- 第 4 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 18.5 高于目标 12.0
  - dialogue_run_mean 14.3 高于目标 14.0
- 第 7 章：
  - [observe] 标题重复：「打印机吞吐账单」已存在
- 第 8 章：
  - [observe] attr_adv_pct 38.5 > 25.0（结构塌缩）
  - [observe] 标题重复：「手指按在纸页上」已存在
- 第 9 章：
  - 单条套路句式超限：「他知道自己」×4
  - [observe] 标题重复：「手指按在纸页上」已存在
- 第 10 章：
  - narration_para_pct 2.0 低于目标 5.0
  - attr_adv_pct 17.2 高于目标 12.0
  - dialogue_run_mean 50 高于目标 14.0
  - [observe] 标题重复：「手指按在纸页上」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17938
chapter_chars_mean: 1794
chapter_chars_median: 1816
chapter_chars_cv: 0.11
paragraphs_mean: 41.9
dialogue_chars_pct: 49.0
dialogue_para_pct: 84.4
interiority_para_pct: 5.5
narration_para_pct: 10.1
turn_under20_pct: 74.3
turn_over200_pct: 0.0
attr_say_pct: 24.8
attr_adv_pct: 15.3
scenes_per_chapter: 2
dialogue_run_mean: 11.5
turn_len_median: 12
```
