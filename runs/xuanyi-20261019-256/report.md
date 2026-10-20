# 铜板敲击声 生成报告

slug：`xuanyi-20261019-256`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14640
LLM 调用：68 次，累计 248.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜板上的血迹 | 1616 | short | 98.4 | 0 |  | 1 |
| 2 | 水面倒影晃动 | 4269 | normal | 93.6 | 0 |  | 4 |
| 3 | 摩挲欠条边缘 | 3421 | normal | 90.4 | 0 |  | 3 |
| 4 | 摩挲怀表外壳 | 3478 | normal | 88.2 | 0 |  | 3 |
| 5 | 摩挲铜板边缘 | 1851 | short | 87.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 17.6 低于目标 20.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈文远的」×6、「”周素娥轻」×3、「周素娥的」×3
  - narration_para_pct 7.2 低于目标 20.0
  - [observe] attr_adv_pct 24.0 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周素娥的」×7、「陈文远的」×4、「陈文远站在」×3
  - narration_para_pct 11.5 低于目标 20.0
  - [observe] 章内自我复读 4 句（如「陈文远盯着那份欠条看了许久，缓缓说道：“如果张三…」）
- 第 4 章：
  - 单条套路句式超限：「陈文远的」×6、「为什么会」×3
  - interiority_para_pct 21.7 高于目标 20.0
  - narration_para_pct 18.8 低于目标 20.0
- 第 5 章：
  - dialogue_chars_pct 16.9 低于目标 20.0
  - [observe] 标题与《摩挲欠条边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13951
chapter_chars_mean: 2790
chapter_chars_median: 3251
chapter_chars_cv: 0.39
paragraphs_mean: 61.4
dialogue_chars_pct: 34.2
dialogue_para_pct: 71.6
interiority_para_pct: 11.8
narration_para_pct: 16.5
turn_under20_pct: 83.2
turn_over200_pct: 0.0
attr_say_pct: 16.9
attr_adv_pct: 9.0
scenes_per_chapter: 3.4
dialogue_run_mean: 4.0
turn_len_median: 10
```
