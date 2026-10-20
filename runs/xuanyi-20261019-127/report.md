# 铜印 生成报告

slug：`xuanyi-20261019-127`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14067
LLM 调用：68 次，累计 236.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 砚台的裂痕 | 1906 | short | 96.7 | 0 |  | 2 |
| 2 | 铜印与账单的对峙 | 3749 | normal | 93.3 | 0 |  | 2 |
| 3 | 账单与木牌的对峙 | 2937 | normal | 91.5 | 0 |  | 3 |
| 4 | 铜印摩挲 | 3789 | normal | 91.4 | 0 |  | 2 |
| 5 | 账单与铜印的对峙 | 1681 | short | 92.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈墨生的」×5
  - narration_para_pct 15.6 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陆怀瑾的」×8
  - narration_para_pct 8.9 低于目标 20.0
- 第 3 章：
  - narration_para_pct 4.7 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
  - [observe] 标题与《铜印与账单的对峙》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「沈墨生的」×5、「陆怀瑾的」×3、「微微一笑」×3
  - narration_para_pct 7.7 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「沈墨生站在」×3
  - narration_para_pct 11.8 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 标题与《账单与木牌的对峙》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13389
chapter_chars_mean: 2678
chapter_chars_median: 2793
chapter_chars_cv: 0.36
paragraphs_mean: 60
dialogue_chars_pct: 41.4
dialogue_para_pct: 81.1
interiority_para_pct: 9.9
narration_para_pct: 8.9
turn_under20_pct: 74.0
turn_over200_pct: 0.0
attr_say_pct: 17.7
attr_adv_pct: 10.8
scenes_per_chapter: 2.6
dialogue_run_mean: 5.7
turn_len_median: 13
```
