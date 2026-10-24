# 令牌风云 生成报告

slug：`shuangwen-20261023-145`
档位：爽文　闸门模式：observe
章数：10　总字数：19893
LLM 调用：97 次，累计 441.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 令牌上的纹路浮现 | 1862 | normal | 99.6 | 0 |  | 1 |
| 2 | 抚摸书脊的指尖 | 2646 | normal | 94.3 | 0 |  | 2 |
| 3 | 令牌对质 | 1745 | normal | 36.6 | 0 |  | 4 |
| 4 | 令牌对峙 | 2103 | normal | 37.5 | 0 |  | 3 |
| 5 | 令牌对峙 | 2025 | normal | 37.8 | 0 |  | 4 |
| 6 | 令牌对峙 | 1611 | normal | 91.1 | 0 |  | 2 |
| 7 | 令牌对峙 | 1689 | normal | 37.0 | 0 |  | 3 |
| 8 | 令牌对峙 | 1813 | normal | 94.3 | 0 |  | 3 |
| 9 | 令牌对峙 | 1993 | normal | 88.3 | 0 |  | 3 |
| 10 | 抚摸书脊的指尖 | 2396 | long | 92.6 | 0 |  | 6 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 22.7 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「李承泽的」×7、「藏书阁」×4
  - attr_adv_pct 25.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李承泽的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 章内自我复读 3 句（如「林远点了点头，“确实如此，但我不认为这就是全部真…」）
- 第 4 章：
  - 单条套路句式超限：「藏书阁」×5
  - [observe] attr_adv_pct 31.2 > 25.0（结构塌缩）
  - [observe] 标题与《令牌对质》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「林远站在」×3
  - narration_para_pct 4.2 低于目标 5.0
  - [observe] attr_adv_pct 31.2 > 25.0（结构塌缩）
  - [observe] 标题重复：「令牌对峙」已存在
- 第 6 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「令牌对峙」已存在
- 第 7 章：
  - 单条套路句式超限：「李承泽的」×4
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「令牌对峙」已存在
- 第 8 章：
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「令牌对峙」已存在
- 第 9 章：
  - 单条套路句式超限：「李承泽的」×5
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「令牌对峙」已存在
- 第 10 章：
  - 单条套路句式超限：「李承泽的」×5
  - dialogue_chars_pct 70.7 高于目标 70.0
  - narration_para_pct 3.8 低于目标 5.0
  - attr_adv_pct 23.1 高于目标 12.0
  - dialogue_run_mean 16.7 高于目标 14.0
  - [observe] 标题重复：「抚摸书脊的指尖」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18870
chapter_chars_mean: 1887
chapter_chars_median: 1825
chapter_chars_cv: 0.16
paragraphs_mean: 44.2
dialogue_chars_pct: 47.5
dialogue_para_pct: 84.4
interiority_para_pct: 6.4
narration_para_pct: 9.2
turn_under20_pct: 75.1
turn_over200_pct: 0.0
attr_say_pct: 25.0
attr_adv_pct: 23.0
scenes_per_chapter: 1.6
dialogue_run_mean: 7.9
turn_len_median: 12
```
