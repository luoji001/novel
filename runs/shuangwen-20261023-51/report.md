# 铜锤 生成报告

slug：`shuangwen-20261023-51`
档位：爽文　闸门模式：observe
章数：10　总字数：19986
LLM 调用：97 次，累计 456.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧工单上镇长的字 | 1979 | normal | 98.8 | 0 |  | 1 |
| 2 | 钢尺划过旧工单 | 1958 | normal | 36.8 | 0 |  | 1 |
| 3 | 钢尺划过旧工单 | 1719 | normal | 92.9 | 0 |  | 3 |
| 4 | 铜锤敲铁器 | 1913 | normal | 92.4 | 0 |  | 1 |
| 5 | 铜锤敲铁器 | 1924 | normal | 92.9 | 0 |  | 1 |
| 6 | 旧工单画圆圈 | 1863 | normal | 94.6 | 0 |  | 1 |
| 7 | 钢尺点验台 | 1745 | normal | 91.9 | 0 |  | 1 |
| 8 | 铜锤敲响铁器 | 1596 | normal | 93.8 | 0 |  | 1 |
| 9 | 铜锤敲铁器 | 2415 | normal | 94.0 | 0 |  | 2 |
| 10 | 钢尺划过旧工单 | 2864 | long | 92.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×4
- 第 2 章：
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周国强的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - [observe] 标题重复：「钢尺划过旧工单」已存在
- 第 4 章：
  - attr_adv_pct 22.2 高于目标 12.0
- 第 5 章：
  - [observe] 标题重复：「铜锤敲铁器」已存在
- 第 6 章：
  - attr_adv_pct 18.2 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「周国强的」×4
- 第 8 章：
  - [observe] 标题与《铜锤敲铁器》近似 0.91 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 情节与已写章节重复 0.70 ≥ 0.7（撞上「陈永年因旧工单与周国强产生冲突，最终在人事科王主任介入下…」）
  - [observe] 标题重复：「铜锤敲铁器」已存在
- 第 10 章：
  - 单条套路句式超限：「周国强的」×3
  - attr_adv_pct 13.6 高于目标 12.0
  - [observe] 标题重复：「钢尺划过旧工单」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18963
chapter_chars_mean: 1896
chapter_chars_median: 1818
chapter_chars_cv: 0.19
paragraphs_mean: 43.6
dialogue_chars_pct: 46.7
dialogue_para_pct: 82.9
interiority_para_pct: 5.1
narration_para_pct: 12.0
turn_under20_pct: 69.3
turn_over200_pct: 0.0
attr_say_pct: 22.7
attr_adv_pct: 12.2
scenes_per_chapter: 1.4
dialogue_run_mean: 6.3
turn_len_median: 14
```
