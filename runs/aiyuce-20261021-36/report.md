# 模型图纸 生成报告

slug：`aiyuce-20261021-36`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12910
LLM 调用：57 次，累计 229.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 划线标出及格线 | 2321 | normal | 95.5 | 0 |  | 0 |
| 2 | 核对材料清单 | 1913 | normal | 90.3 | 0 |  | 0 |
| 3 | 用电量明细表更新 | 2353 | normal | 36.6 | 0 |  | 2 |
| 4 | 教师工资发放记录 | 2211 | normal | 91.1 | 0 |  | 2 |
| 5 | 实验报告数据对比 | 2513 | normal | 36.4 | 0 |  | 1 |
| 6 | 标出误差控制要点 | 1593 | short | 35.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - 单条套路句式超限：「石城县电力公司」×4
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 18.4 高于目标 18.0
  - narration_para_pct 29.4 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12621
chapter_chars_mean: 2104
chapter_chars_median: 2218
chapter_chars_cv: 0.16
paragraphs_mean: 15.8
dialogue_chars_pct: 6.7
dialogue_para_pct: 22.0
interiority_para_pct: 12.6
narration_para_pct: 65.5
turn_under20_pct: 59.7
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.8
turn_len_median: 20
```
