# 打印纸 生成报告

slug：`shuangwen-20261023-141`
档位：爽文　闸门模式：observe
章数：10　总字数：18640
LLM 调用：97 次，累计 425.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 打印机吞纸的一瞬 | 1502 | normal | 97.7 | 0 |  | 1 |
| 2 | 泛黄纸张的较量 | 1769 | normal | 93.7 | 0 |  | 0 |
| 3 | 打印机吞纸的一瞬 | 2275 | normal | 93.2 | 0 |  | 2 |
| 4 | 账本与供货单的对峙 | 2007 | normal | 91.6 | 0 |  | 3 |
| 5 | 账本页的较量 | 1930 | normal | 92.4 | 0 |  | 1 |
| 6 | 纸张的较量 | 1898 | normal | 37.1 | 0 |  | 2 |
| 7 | 账本条目被捏皱 | 1672 | normal | 92.4 | 0 |  | 2 |
| 8 | 账本条目被捏皱 | 1533 | normal | 93.2 | 0 |  | 1 |
| 9 | 账本条目被捏皱 | 1681 | normal | 93.1 | 0 |  | 3 |
| 10 | 账本条目被捏皱 | 2363 | long | 92.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李国强点了点头」×4、「就在这时」×3、「李国强的」×3
  - [observe] 标题重复：「打印机吞纸的一瞬」已存在
- 第 4 章：
  - 单条套路句式超限：「王德发的」×4、「李国强的」×3
  - narration_para_pct 4.2 低于目标 5.0
  - dialogue_run_mean 15.3 高于目标 14.0
- 第 5 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 6 章：
  - [observe] attr_adv_pct 27.8 > 25.0（结构塌缩）
  - [observe] 标题与《泛黄纸张的较量》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「王德发的」×4、「李国强的」×4
  - attr_adv_pct 13.3 高于目标 12.0
- 第 8 章：
  - [observe] 标题重复：「账本条目被捏皱」已存在
- 第 9 章：
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「账本条目被捏皱」已存在
- 第 10 章：
  - 单条套路句式超限：「王德发的」×3
  - [observe] 标题重复：「账本条目被捏皱」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17637
chapter_chars_mean: 1764
chapter_chars_median: 1734
chapter_chars_cv: 0.15
paragraphs_mean: 42.1
dialogue_chars_pct: 51.6
dialogue_para_pct: 85.6
interiority_para_pct: 3.6
narration_para_pct: 10.8
turn_under20_pct: 74.3
turn_over200_pct: 0.0
attr_say_pct: 35.2
attr_adv_pct: 11.9
scenes_per_chapter: 1.4
dialogue_run_mean: 7.3
turn_len_median: 12
```
