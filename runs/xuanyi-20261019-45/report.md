# 账本残页 生成报告

slug：`xuanyi-20261019-45`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15103
LLM 调用：68 次，累计 234.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 监控屏幕的静止画面 | 1968 | short | 88.1 | 0 |  | 3 |
| 2 | 账本边缘的烧焦痕迹 | 3717 | normal | 87.6 | 0 |  | 1 |
| 3 | 数字消失的瞬间 | 3879 | normal | 89.5 | 0 |  | 4 |
| 4 | 标签上的暗码疑云 | 3583 | normal | 89.2 | 0 |  | 3 |
| 5 | 工牌背面的日期异常 | 1951 | short | 92.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林雨桐的」×4
  - dialogue_chars_pct 14.5 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
- 第 2 章：
  - dialogue_chars_pct 17.7 低于目标 20.0
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈国强的」×8
  - narration_para_pct 12.7 低于目标 20.0
  - [observe] attr_adv_pct 23.5 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「陈国强的」×8
  - narration_para_pct 16.0 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「陈国强看了她一眼，又看了看手中的文件，“这些数据…」）
- 第 5 章：
  - 单条套路句式超限：「陈国强的」×4
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 14421
chapter_chars_mean: 2884
chapter_chars_median: 3405
chapter_chars_cv: 0.32
paragraphs_mean: 59.4
dialogue_chars_pct: 32.3
dialogue_para_pct: 65.3
interiority_para_pct: 10.1
narration_para_pct: 24.6
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 40.3
attr_adv_pct: 16.0
scenes_per_chapter: 4
dialogue_run_mean: 2.9
turn_len_median: 14
```
