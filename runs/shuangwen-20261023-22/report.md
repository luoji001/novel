# 合同风波 生成报告

slug：`shuangwen-20261023-22`
档位：爽文　闸门模式：observe
章数：10　总字数：18976
LLM 调用：97 次，累计 414.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕碎的投诉记录 | 1647 | normal | 39.6 | 0 |  | 1 |
| 2 | 投诉记录的真相 | 1841 | normal | 90.9 | 0 |  | 2 |
| 3 | 签字权的争夺 | 1868 | normal | 93.7 | 0 |  | 2 |
| 4 | 红笔戳日期 | 1520 | normal | 95.0 | 0 |  | 0 |
| 5 | 签名的谎言 | 1857 | normal | 37.8 | 0 |  | 1 |
| 6 | 签字的真相 | 1683 | normal | 37.7 | 0 |  | 2 |
| 7 | 敲响合同的回音 | 2152 | normal | 94.3 | 0 |  | 1 |
| 8 | 签字的谎言 | 2074 | normal | 94.2 | 0 |  | 3 |
| 9 | 红笔戳日期 | 1848 | normal | 94.3 | 0 |  | 1 |
| 10 | 红笔戳日期 | 2476 | long | 91.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 2 章：
  - attr_adv_pct 15.4 高于目标 12.0
  - dialogue_run_mean 1.7 低于目标 2.0
- 第 3 章：
  - narration_para_pct 2.6 低于目标 5.0
  - attr_adv_pct 17.6 高于目标 12.0
- 第 5 章：
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 6 章：
  - narration_para_pct 3.3 低于目标 5.0
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
- 第 7 章：
  - attr_adv_pct 24.1 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「周子安点点」×3、「”林秋低」×3
  - attr_adv_pct 16.1 高于目标 12.0
  - [observe] 标题与《签名的谎言》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - [observe] 标题重复：「红笔戳日期」已存在
- 第 10 章：
  - 单条套路句式超限：「他知道这」×3、「周子安的」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「红笔戳日期」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18021
chapter_chars_mean: 1802
chapter_chars_median: 1770
chapter_chars_cv: 0.14
paragraphs_mean: 40.4
dialogue_chars_pct: 51.5
dialogue_para_pct: 81.7
interiority_para_pct: 7.3
narration_para_pct: 10.9
turn_under20_pct: 72.0
turn_over200_pct: 0.0
attr_say_pct: 33.4
attr_adv_pct: 19.5
scenes_per_chapter: 1.6
dialogue_run_mean: 5.8
turn_len_median: 13
```
