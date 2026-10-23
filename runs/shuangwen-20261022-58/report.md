# 旧工单 生成报告

slug：`shuangwen-20261022-58`
档位：爽文　闸门模式：observe
章数：10　总字数：18439
LLM 调用：97 次，累计 427.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 木柜与红头文件 | 1797 | normal | 100.0 | 0 |  | 2 |
| 2 | 铅笔填新表 | 2251 | normal | 94.2 | 0 |  | 1 |
| 3 | 铜尺与刻度板对峙 | 1792 | normal | 92.5 | 0 |  | 1 |
| 4 | 旧工单在手 | 1727 | normal | 93.6 | 0 |  | 1 |
| 5 | 铜尺对红头文件 | 1867 | normal | 88.0 | 0 |  | 2 |
| 6 | 碎纸拼真相 | 1391 | normal | 93.8 | 0 |  | 0 |
| 7 | 旧工单摊开 | 1662 | normal | 93.2 | 0 |  | 3 |
| 8 | 铜尺对红头文件 | 1893 | normal | 92.5 | 0 |  | 4 |
| 9 | 铅笔写日期 | 1684 | normal | 94.4 | 0 |  | 1 |
| 10 | 刻刀磨桌边 | 2365 | long | 37.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈主任的」×4
  - narration_para_pct 2.9 低于目标 5.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×4
- 第 3 章：
  - 单条套路句式超限：「陈主任的」×3
- 第 4 章：
  - 单条套路句式超限：「陈主任的」×6
- 第 5 章：
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 34 高于目标 14.0
- 第 7 章：
  - attr_adv_pct 22.2 高于目标 12.0
  - dialogue_run_mean 14.5 高于目标 14.0
  - [observe] 标题与《旧工单在手》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - narration_para_pct 2.8 低于目标 5.0
  - attr_adv_pct 13.6 高于目标 12.0
  - dialogue_run_mean 17 高于目标 14.0
  - [observe] 标题重复：「铜尺对红头文件」已存在
- 第 9 章：
  - narration_para_pct 2.7 低于目标 5.0
- 第 10 章：
  - 单条套路句式超限：「陈主任的」×4、「他知道这」×3
  - [observe] attr_adv_pct 42.9 > 25.0（结构塌缩）

## 整书结构指标

```
chapters: 10
total_chars: 17524
chapter_chars_mean: 1752
chapter_chars_median: 1702
chapter_chars_cv: 0.15
paragraphs_mean: 38.1
dialogue_chars_pct: 51.8
dialogue_para_pct: 88.5
interiority_para_pct: 2.6
narration_para_pct: 8.9
turn_under20_pct: 71.0
turn_over200_pct: 0.0
attr_say_pct: 29.3
attr_adv_pct: 14.1
scenes_per_chapter: 1.5
dialogue_run_mean: 11.6
turn_len_median: 14
```
