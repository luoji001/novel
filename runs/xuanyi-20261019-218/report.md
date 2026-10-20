# 旧布鞋的印痕 生成报告

slug：`xuanyi-20261019-218`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13260
LLM 调用：68 次，累计 236.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 针脚的回声 | 1716 | short | 99.2 | 0 |  | 2 |
| 2 | 银针的重量 | 3197 | normal | 91.1 | 0 |  | 2 |
| 3 | 朱砂与紫草叶 | 3476 | normal | 91.5 | 0 |  | 3 |
| 4 | 缝入画中的锦缎 | 3194 | normal | 91.6 | 0 |  | 2 |
| 5 | 银针划破窗棂 | 1672 | short | 91.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈砚秋的」×4、「陆怀瑾的」×3
  - [observe] attr_adv_pct 66.7 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「沈砚秋的」×6、「陆怀瑾的」×4、「他知道这」×4
  - narration_para_pct 9.5 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「陆怀瑾的」×10、「沈砚秋的」×5
  - narration_para_pct 9.5 低于目标 20.0
  - attr_adv_pct 11.8 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「沈砚秋的」×6、「陆怀瑾的」×4
  - narration_para_pct 10.1 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「沈砚秋的」×9

## 整书结构指标

```
chapters: 5
total_chars: 12670
chapter_chars_mean: 2534
chapter_chars_median: 3041
chapter_chars_cv: 0.33
paragraphs_mean: 51.6
dialogue_chars_pct: 43.2
dialogue_para_pct: 79.9
interiority_para_pct: 6.7
narration_para_pct: 13.4
turn_under20_pct: 66.3
turn_over200_pct: 0.0
attr_say_pct: 9.7
attr_adv_pct: 13.0
scenes_per_chapter: 1.2
dialogue_run_mean: 5.5
turn_len_median: 14
```
