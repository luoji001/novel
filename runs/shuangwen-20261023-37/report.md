# 签章 生成报告

slug：`shuangwen-20261023-37`
档位：爽文　闸门模式：observe
章数：10　总字数：19875
LLM 调用：97 次，累计 427.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 文件夹的递出 | 1923 | normal | 99.0 | 0 |  | 1 |
| 2 | 工龄证明的摩擦 | 2195 | normal | 94.3 | 0 |  | 2 |
| 3 | 教学记录的出示 | 1715 | normal | 92.7 | 0 |  | 1 |
| 4 | 文件的摩擦 | 1989 | normal | 91.3 | 0 |  | 3 |
| 5 | 文件的摩擦 | 2155 | normal | 37.3 | 0 |  | 3 |
| 6 | 签字笔的使用 | 1836 | normal | 94.7 | 0 |  | 1 |
| 7 | 文件摩擦的真相 | 2177 | normal | 94.8 | 0 |  | 1 |
| 8 | 文件摩擦的真相 | 2051 | normal | 91.8 | 0 |  | 2 |
| 9 | 签字笔的摩擦 | 1623 | normal | 92.8 | 0 |  | 1 |
| 10 | 审批表的签署 | 2201 | long | 93.1 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×4
- 第 2 章：
  - 单条套路句式超限：「陈文娟的」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「陈文娟点点」×3
- 第 4 章：
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 15.8 高于目标 12.0
  - dialogue_run_mean 21 高于目标 14.0
- 第 5 章：
  - 单条套路句式超限：「李国强的」×9、「带着一丝」×3
  - [observe] attr_adv_pct 66.7 > 25.0（结构塌缩）
  - [observe] 标题重复：「文件的摩擦」已存在
- 第 6 章：
  - attr_adv_pct 13.3 高于目标 12.0
- 第 7 章：
  - [observe] 标题与《文件的摩擦》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「陈文娟的」×4
  - [observe] 标题重复：「文件摩擦的真相」已存在
- 第 9 章：
  - [observe] 标题与《签字笔的使用》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18849
chapter_chars_mean: 1885
chapter_chars_median: 1919
chapter_chars_cv: 0.1
paragraphs_mean: 42.8
dialogue_chars_pct: 50.4
dialogue_para_pct: 84.5
interiority_para_pct: 4.8
narration_para_pct: 10.6
turn_under20_pct: 67.1
turn_over200_pct: 0.0
attr_say_pct: 29.0
attr_adv_pct: 15.6
scenes_per_chapter: 2.3
dialogue_run_mean: 7.3
turn_len_median: 14
```
