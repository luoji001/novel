# 合同副本 生成报告

slug：`shuangwen-20261022-110`
档位：爽文　闸门模式：observe
章数：10　总字数：19073
LLM 调用：97 次，累计 440.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一份合同 | 1790 | normal | 97.3 | 0 |  | 1 |
| 2 | 一份合同 | 1857 | normal | 91.4 | 0 |  | 3 |
| 3 | 一份合同 | 1822 | normal | 90.9 | 0 |  | 3 |
| 4 | 签合同 | 1900 | normal | 36.7 | 0 |  | 2 |
| 5 | 盖章风波 | 1698 | normal | 90.9 | 0 |  | 0 |
| 6 | 一张合同 | 1732 | normal | 91.1 | 0 |  | 3 |
| 7 | 敲铜板 | 2095 | normal | 92.7 | 0 |  | 2 |
| 8 | 盖章风波 | 1895 | normal | 91.7 | 0 |  | 1 |
| 9 | 盖章风波 | 1992 | normal | 36.7 | 0 |  | 3 |
| 10 | 敲铜板 | 2282 | long | 36.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周振国的」×7
- 第 2 章：
  - 单条套路句式超限：「周振国的」×4
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「一份合同」已存在
- 第 3 章：
  - 单条套路句式超限：「周振国的」×4
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「一份合同」已存在
- 第 4 章：
  - 单条套路句式超限：「周振国的」×7
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「周振国的」×8、「李大山的」×3
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题与《一份合同》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - narration_para_pct 3.8 低于目标 5.0
  - dialogue_run_mean 16.7 高于目标 14.0
- 第 8 章：
  - [observe] 标题重复：「盖章风波」已存在
- 第 9 章：
  - 单条套路句式超限：「周振国的」×4、「李大山的」×3
  - [observe] attr_adv_pct 31.2 > 25.0（结构塌缩）
  - [observe] 标题重复：「盖章风波」已存在
- 第 10 章：
  - 单条套路句式超限：「周振国的」×5
  - [observe] 章内自我复读 1 句（如「那我就让你看看，什么是真正的规则…」）
  - [observe] 标题重复：「敲铜板」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18136
chapter_chars_mean: 1814
chapter_chars_median: 1784
chapter_chars_cv: 0.09
paragraphs_mean: 40.5
dialogue_chars_pct: 48.1
dialogue_para_pct: 83.8
interiority_para_pct: 6.7
narration_para_pct: 9.5
turn_under20_pct: 69.6
turn_over200_pct: 0.0
attr_say_pct: 29.2
attr_adv_pct: 14.2
scenes_per_chapter: 1.7
dialogue_run_mean: 6.9
turn_len_median: 14
```
