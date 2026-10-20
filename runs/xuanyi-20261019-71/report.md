# 铜笔 生成报告

slug：`xuanyi-20261019-71`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14170
LLM 调用：68 次，累计 227.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 墨迹与账本的对视 | 1523 | short | 71.9 | 0 |  | 2 |
| 2 | 指纹触碰地图边缘 | 3615 | normal | 89.8 | 0 |  | 3 |
| 3 | 符号与账本的对视 | 3774 | normal | 90.0 | 0 |  | 5 |
| 4 | 瓷器与日期的对视 | 3335 | normal | 88.4 | 0 |  | 3 |
| 5 | 锁舌上的刻痕 | 1918 | short | 90.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 6.5 低于目标 20.0
  - interiority_para_pct 26.7 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「不仅仅是」×4
  - dialogue_chars_pct 18.0 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「为了进一步确认这一点，他小心翼翼地翻阅起账本中的…」）
- 第 3 章：
  - 单条套路句式超限：「沈墨生的」×5、「不仅仅是」×4、「沈墨生站在」×3
  - narration_para_pct 7.4 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - dialogue_run_mean 11.8 高于目标 10.0
  - [observe] 标题与《墨迹与账本的对视》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「沈墨生的」×6、「变得更加」×4、「周怀瑾的」×3
  - narration_para_pct 16.7 低于目标 20.0
  - [observe] 章内自我复读 6 句（如「这正是保险柜第三次开启的日子，也是他最初怀疑问题…」）
- 第 5 章：
  - 单条套路句式超限：「周怀瑾的」×4
  - narration_para_pct 14.6 低于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13573
chapter_chars_mean: 2715
chapter_chars_median: 3198
chapter_chars_cv: 0.36
paragraphs_mean: 51.2
dialogue_chars_pct: 32.3
dialogue_para_pct: 66.6
interiority_para_pct: 12.8
narration_para_pct: 20.6
turn_under20_pct: 71.3
turn_over200_pct: 0.0
attr_say_pct: 22.2
attr_adv_pct: 7.7
scenes_per_chapter: 2.6
dialogue_run_mean: 4.5
turn_len_median: 13
```
