# 绣针 生成报告

slug：`xuanyi-20261019-258`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13775
LLM 调用：68 次，累计 244.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 绣品上的水渍 | 1814 | short | 100.0 | 0 |  | 3 |
| 2 | 账本滑落的瞬间 | 3430 | normal | 91.3 | 0 |  | 2 |
| 3 | 绣针上的刻痕 | 3304 | normal | 91.2 | 0 |  | 2 |
| 4 | 绣绷上的针脚 | 3541 | normal | 91.2 | 0 |  | 2 |
| 5 | 绣针划破账页 | 1681 | short | 92.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈青梧的」×4
  - narration_para_pct 17.9 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「沈青梧的」×4
  - [observe] 章内自我复读 19 句（如「这张纸上记载的是最近一次采购丝绸的明细，日期明确…」）
- 第 3 章：
  - 单条套路句式超限：「沈青梧的」×10、「沈青梧站在」×3、「中带着一丝」×3
  - narration_para_pct 16.4 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「沈青梧的」×10
  - narration_para_pct 13.9 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「沈青梧的」×3
  - narration_para_pct 12.5 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13141
chapter_chars_mean: 2628
chapter_chars_median: 3144
chapter_chars_cv: 0.34
paragraphs_mean: 55.8
dialogue_chars_pct: 31.2
dialogue_para_pct: 69.2
interiority_para_pct: 13.5
narration_para_pct: 17.3
turn_under20_pct: 79.1
turn_over200_pct: 0.0
attr_say_pct: 13.3
attr_adv_pct: 8.5
scenes_per_chapter: 2.8
dialogue_run_mean: 3.1
turn_len_median: 12
```
