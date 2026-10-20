# 黑袋 生成报告

slug：`xuanyi-20261019-50`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14677
LLM 调用：68 次，累计 226.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手机震动的瞬间 | 1929 | short | 69.4 | 0 |  | 3 |
| 2 | 车辆倒影中的合同 | 3938 | normal | 39.3 | 0 |  | 2 |
| 3 | 黑色皮包的踪迹 | 3295 | normal | 84.0 | 0 |  | 3 |
| 4 | U盘里的监控视频 | 3688 | normal | 88.8 | 0 |  | 3 |
| 5 | 黑袋子的沉默时刻 | 1822 | short | 88.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 9.4 低于目标 20.0
  - interiority_para_pct 25.8 高于目标 20.0
  - dialogue_run_mean 1.3 低于目标 1.5
- 第 2 章：
  - dialogue_chars_pct 11.5 低于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「为什么会」×5、「点了点头“」×3
  - dialogue_chars_pct 15.7 低于目标 20.0
  - interiority_para_pct 20.3 高于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「沈婉如的」×5、「沈婉如点了点头」×3、「“我不知道」×3
  - narration_para_pct 9.3 低于目标 20.0
  - dialogue_run_mean 13.6 高于目标 10.0
- 第 5 章：
  - dialogue_chars_pct 71.0 高于目标 58.0
  - narration_para_pct 6.5 低于目标 20.0
  - dialogue_run_mean 14.5 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14108
chapter_chars_mean: 2822
chapter_chars_median: 3162
chapter_chars_cv: 0.34
paragraphs_mean: 48.6
dialogue_chars_pct: 31.0
dialogue_para_pct: 65.7
interiority_para_pct: 12.5
narration_para_pct: 21.8
turn_under20_pct: 76.7
turn_over200_pct: 0.0
attr_say_pct: 32.3
attr_adv_pct: 6.4
scenes_per_chapter: 3
dialogue_run_mean: 6.8
turn_len_median: 12
```
