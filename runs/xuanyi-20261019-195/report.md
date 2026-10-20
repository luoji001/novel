# 银表 生成报告

slug：`xuanyi-20261019-195`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14310
LLM 调用：68 次，累计 234.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触摸银色机械表 | 1831 | short | 99.8 | 0 |  | 1 |
| 2 | 敲击登记簿的指尖 | 3372 | normal | 93.1 | 0 |  | 2 |
| 3 | 抚摸旧存折的指尖 | 4040 | normal | 87.8 | 0 |  | 3 |
| 4 | 翻开登记簿的指尖 | 3196 | normal | 90.4 | 0 |  | 3 |
| 5 | 触摸银色机械表 | 1866 | short | 90.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 12.5 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「陈文远的」×7
  - narration_para_pct 12.5 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×6、「陈文远的」×5、「”林婉如低」×3
  - narration_para_pct 3.4 低于目标 20.0
  - dialogue_run_mean 13.6 高于目标 10.0
- 第 4 章：
  - narration_para_pct 9.0 低于目标 20.0
  - attr_adv_pct 15.0 高于目标 10.0
  - [observe] 标题与《敲击登记簿的指尖》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 标题重复：「触摸银色机械表」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13541
chapter_chars_mean: 2708
chapter_chars_median: 3046
chapter_chars_cv: 0.34
paragraphs_mean: 68.6
dialogue_chars_pct: 42.3
dialogue_para_pct: 80.7
interiority_para_pct: 5.3
narration_para_pct: 14.1
turn_under20_pct: 82.9
turn_over200_pct: 0.0
attr_say_pct: 41.6
attr_adv_pct: 8.5
scenes_per_chapter: 3.2
dialogue_run_mean: 7.3
turn_len_median: 10
```
