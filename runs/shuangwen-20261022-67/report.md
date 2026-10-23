# 皮重数据 生成报告

slug：`shuangwen-20261022-67`
档位：爽文　闸门模式：observe
章数：10　总字数：19646
LLM 调用：97 次，累计 419.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 打印纸上的数字 | 1782 | normal | 99.4 | 0 |  | 1 |
| 2 | 签字权的重量 | 1715 | normal | 94.5 | 0 |  | 2 |
| 3 | 递出纸张 | 1943 | normal | 36.6 | 0 |  | 1 |
| 4 | 签字权的重量 | 1899 | normal | 90.8 | 0 |  | 2 |
| 5 | 递出纸张 | 1614 | normal | 36.5 | 0 |  | 2 |
| 6 | 撕碎的签名纸 | 1706 | normal | 36.6 | 0 |  | 1 |
| 7 | 指尖触碰打印纸 | 1868 | normal | 90.8 | 0 |  | 2 |
| 8 | 递出纸张 | 1834 | normal | 93.2 | 0 |  | 1 |
| 9 | 签字权的重量 | 2758 | normal | 91.4 | 0 |  | 3 |
| 10 | 签字的圆圈 | 2517 | long | 93.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×3
- 第 2 章：
  - 单条套路句式超限：「他知道这」×5
  - attr_adv_pct 15.4 高于目标 12.0
- 第 3 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「过磅房」×3
  - [observe] 标题重复：「签字权的重量」已存在
- 第 5 章：
  - [observe] 章内自我复读 3 句（如「李国强说，“但我觉得，比起让一些人继续蒙混过关，…」）
  - [observe] 标题重复：「递出纸张」已存在
- 第 6 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 7 章：
  - 命中套话收尾句
  - dialogue_run_mean 16 高于目标 14.0
- 第 8 章：
  - [observe] 标题重复：「递出纸张」已存在
- 第 9 章：
  - 单条套路句式超限：「他知道自己」×5、「过磅房」×3
  - attr_adv_pct 22.5 高于目标 12.0
  - [observe] 标题重复：「签字权的重量」已存在
- 第 10 章：
  - 单条套路句式超限：「点了点头」×3

## 整书结构指标

```
chapters: 10
total_chars: 18507
chapter_chars_mean: 1851
chapter_chars_median: 1748
chapter_chars_cv: 0.19
paragraphs_mean: 49.7
dialogue_chars_pct: 46.2
dialogue_para_pct: 79.9
interiority_para_pct: 5.4
narration_para_pct: 14.8
turn_under20_pct: 74.8
turn_over200_pct: 0.0
attr_say_pct: 26.1
attr_adv_pct: 12.6
scenes_per_chapter: 3.5
dialogue_run_mean: 6.8
turn_len_median: 14
```
