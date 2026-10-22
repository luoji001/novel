# 合同副本 生成报告

slug：`shuangwen-20261022-10`
档位：爽文　闸门模式：observe
章数：10　总字数：18593
LLM 调用：97 次，累计 357.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的较量 | 1843 | normal | 100.0 | 0 |  | 2 |
| 2 | 合同副本的裂痕 | 2273 | normal | 36.8 | 0 |  | 3 |
| 3 | 签字笔的较量 | 1569 | normal | 37.0 | 0 |  | 2 |
| 4 | 签字笔的较量 | 2001 | normal | 92.8 | 0 |  | 2 |
| 5 | 合同副本的裂缝 | 1809 | normal | 91.0 | 0 |  | 3 |
| 6 | 签字笔的较量 | 1457 | normal | 87.3 | 0 |  | 3 |
| 7 | 签字笔的较量 | 1920 | normal | 36.1 | 0 |  | 6 |
| 8 | 撕碎的合同副本 | 1693 | normal | 92.6 | 0 |  | 0 |
| 9 | 签字笔的较量 | 1551 | normal | 37.0 | 0 |  | 3 |
| 10 | 签字笔的较量 | 2467 | long | 88.8 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周建国的」×4
  - attr_adv_pct 25.0 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「周建国的」×5、「说道“我」×3
  - narration_para_pct 2.2 低于目标 5.0
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 3 章：
  - [observe] attr_adv_pct 44.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 4 章：
  - 单条套路句式超限：「周建国的」×5
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 5 章：
  - 单条套路句式超限：「周建国的」×8、「他知道自己」×3
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题与《合同副本的裂痕》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「周建国的」×5、「陈永福的」×3
  - dialogue_run_mean 32 高于目标 14.0
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 7 章：
  - 单条套路句式超限：「周建国的」×5
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 16.5 高于目标 14.0
  - [observe] 章内自我复读 4 句（如「你们以为这样就能解决问题吗？…」）
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 9 章：
  - 单条套路句式超限：「周建国的」×3
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 10 章：
  - 单条套路句式超限：「周建国的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 24.5 高于目标 14.0
  - [observe] 标题重复：「签字笔的较量」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17670
chapter_chars_mean: 1767
chapter_chars_median: 1742
chapter_chars_cv: 0.18
paragraphs_mean: 38.5
dialogue_chars_pct: 53.1
dialogue_para_pct: 86.3
interiority_para_pct: 4.5
narration_para_pct: 9.3
turn_under20_pct: 64.0
turn_over200_pct: 0.0
attr_say_pct: 30.4
attr_adv_pct: 20.8
scenes_per_chapter: 1.4
dialogue_run_mean: 11.0
turn_len_median: 15
```
