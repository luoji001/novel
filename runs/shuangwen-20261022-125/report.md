# 旧教案 生成报告

slug：`shuangwen-20261022-125`
档位：爽文　闸门模式：observe
章数：10　总字数：19542
LLM 调用：97 次，累计 437.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 教案本的触感 | 2013 | normal | 38.4 | 0 |  | 1 |
| 2 | 钥匙的重量 | 1946 | normal | 92.4 | 0 |  | 1 |
| 3 | 教案本的触感 | 1672 | normal | 94.4 | 0 |  | 2 |
| 4 | 教案本的页码 | 2122 | normal | 91.9 | 0 |  | 2 |
| 5 | 教案本的页码 | 1863 | normal | 92.1 | 0 |  | 2 |
| 6 | 教案本的页码 | 1834 | normal | 90.1 | 0 |  | 2 |
| 7 | 手指划过纸页 | 2014 | normal | 91.9 | 0 |  | 1 |
| 8 | 一页纸上的风声 | 1901 | normal | 37.6 | 0 |  | 2 |
| 9 | 树叶落在打印纸 | 2042 | normal | 94.5 | 0 |  | 1 |
| 10 | 手指拂过教案本封面 | 2125 | long | 93.3 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 35.7 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「微微一笑」×3
- 第 3 章：
  - 单条套路句式超限：「周正国的」×4
  - [observe] 标题重复：「教案本的触感」已存在
- 第 4 章：
  - 单条套路句式超限：「林婉秋的」×4
  - [observe] 标题与《教案本的触感》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「教案本的页码」已存在
- 第 6 章：
  - 命中套话收尾句
  - [observe] 标题重复：「教案本的页码」已存在
- 第 7 章：
  - narration_para_pct 2.4 低于目标 5.0
- 第 8 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 9 章：
  - attr_adv_pct 15.4 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「周正国的」×3
  - narration_para_pct 2.1 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - dialogue_run_mean 15.3 高于目标 14.0

## 整书结构指标

```
chapters: 10
total_chars: 18574
chapter_chars_mean: 1857
chapter_chars_median: 1882
chapter_chars_cv: 0.07
paragraphs_mean: 40.7
dialogue_chars_pct: 46.3
dialogue_para_pct: 84.7
interiority_para_pct: 4.7
narration_para_pct: 10.6
turn_under20_pct: 70.4
turn_over200_pct: 0.0
attr_say_pct: 32.9
attr_adv_pct: 16.0
scenes_per_chapter: 2
dialogue_run_mean: 6.8
turn_len_median: 14
```
