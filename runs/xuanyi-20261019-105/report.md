# 维生素B12 生成报告

slug：`xuanyi-20261019-105`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15283
LLM 调用：68 次，累计 243.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 擦拭屏幕水渍 | 1912 | short | 95.0 | 0 |  | 1 |
| 2 | 指纹残留 | 3825 | normal | 92.9 | 0 |  | 2 |
| 3 | 摩挲处方单边缘 | 3727 | normal | 91.3 | 0 |  | 3 |
| 4 | 摩挲铁门把手 | 3895 | normal | 91.6 | 0 |  | 3 |
| 5 | 摩挲药盒边缘 | 1919 | short | 89.4 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 20.6 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈国强的」×6、「林雨桐站在」×5
  - narration_para_pct 9.6 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「林雨桐的」×5、「“我不知道」×4
  - narration_para_pct 6.0 低于目标 20.0
  - [observe] attr_adv_pct 21.1 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「陈国强的」×9、「林雨桐站在」×4、「林雨桐的」×4
  - narration_para_pct 13.0 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林雨桐站在」×3、「“我不知道」×3
  - [observe] attr_adv_pct 57.1 > 20.0（结构塌缩）
  - [observe] 标题与《摩挲处方单边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 14568
chapter_chars_mean: 2914
chapter_chars_median: 3544
chapter_chars_cv: 0.34
paragraphs_mean: 64
dialogue_chars_pct: 31.8
dialogue_para_pct: 73.1
interiority_para_pct: 13.7
narration_para_pct: 13.2
turn_under20_pct: 77.1
turn_over200_pct: 0.0
attr_say_pct: 24.7
attr_adv_pct: 15.5
scenes_per_chapter: 4.2
dialogue_run_mean: 3.7
turn_len_median: 12
```
