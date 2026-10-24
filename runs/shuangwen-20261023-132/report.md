# 旧借书条 生成报告

slug：`shuangwen-20261023-132`
档位：爽文　闸门模式：observe
章数：10　总字数：18537
LLM 调用：97 次，累计 437.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一纸旧借书条 | 1989 | normal | 39.1 | 0 |  | 3 |
| 2 | 一纸旧借书条 | 2206 | normal | 89.8 | 0 |  | 1 |
| 3 | 一张旧借书条 | 2098 | normal | 90.0 | 0 |  | 3 |
| 4 | 撕书对决 | 1572 | normal | 93.0 | 0 |  | 3 |
| 5 | 一纸旧借书条 | 1396 | normal | 37.6 | 0 |  | 3 |
| 6 | 铜钱换借书条 | 1612 | normal | 90.3 | 0 |  | 3 |
| 7 | 一纸旧借书条 | 1798 | normal | 92.0 | 0 |  | 2 |
| 8 | 一纸旧借书条 | 1578 | normal | 91.5 | 0 |  | 2 |
| 9 | 一纸旧借书条 | 1849 | normal | 92.3 | 0 |  | 2 |
| 10 | 灰烬显真章 | 2429 | long | 90.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陆怀远的」×3、「藏经阁」×3
  - dialogue_chars_pct 28.1 低于目标 30.0
  - [observe] attr_adv_pct 44.4 > 25.0（结构塌缩）
- 第 2 章：
  - [observe] 标题重复：「一纸旧借书条」已存在
- 第 3 章：
  - 单条套路句式超限：「陆怀远的」×5、「沈墨站在」×3、「雕花木屋」×3
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题与《一纸旧借书条》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陆怀远的」×4、「他知道这」×4、「藏经阁」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 5 章：
  - narration_para_pct 3.8 低于目标 5.0
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「一纸旧借书条」已存在
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陆怀远的」×5
  - attr_adv_pct 15.4 高于目标 12.0
- 第 7 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「一纸旧借书条」已存在
- 第 8 章：
  - 单条套路句式超限：「陆怀远的」×4
  - [observe] 标题重复：「一纸旧借书条」已存在
- 第 9 章：
  - 单条套路句式超限：「陆怀远的」×4
  - [observe] 标题重复：「一纸旧借书条」已存在
- 第 10 章：
  - attr_adv_pct 20.8 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17606
chapter_chars_mean: 1761
chapter_chars_median: 1730
chapter_chars_cv: 0.18
paragraphs_mean: 39.2
dialogue_chars_pct: 42.8
dialogue_para_pct: 79.5
interiority_para_pct: 7.9
narration_para_pct: 12.6
turn_under20_pct: 72.7
turn_over200_pct: 0.0
attr_say_pct: 32.1
attr_adv_pct: 18.3
scenes_per_chapter: 2.1
dialogue_run_mean: 5.8
turn_len_median: 12
```
