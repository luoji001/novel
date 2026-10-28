# 铜钥 生成报告

slug：`shipin-20261027-214`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6340
LLM 调用：57 次，累计 133.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙晃荡的清晨 | 822 | short | 18.3 | 0 |  | 3 |
| 2 | 触摸手机屏幕 | 969 | normal | 94.2 | 0 |  | 1 |
| 3 | 触摸金属扶手 | 982 | normal | 93.3 | 0 |  | 0 |
| 4 | 铜钥匙与旧信封 | 1379 | normal | 93.3 | 0 |  | 0 |
| 5 | 银镯子映出旧照片 | 1153 | normal | 92.7 | 0 |  | 0 |
| 6 | 木箱上的凹陷 | 1029 | normal | 91.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 16.0 高于目标 6.0
  - narration_para_pct 24.0 低于目标 35.0
  - [observe] 章内自我复读 10 句（如「那是十八年前的一天，有人留下这个箱子，里面就有这…」）
- 第 2 章：
  - narration_para_pct 30.0 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 5875
chapter_chars_mean: 979
chapter_chars_median: 948
chapter_chars_cv: 0.19
paragraphs_mean: 29.5
dialogue_chars_pct: 21.4
dialogue_para_pct: 52.7
interiority_para_pct: 3.4
narration_para_pct: 43.9
turn_under20_pct: 96.1
turn_over200_pct: 0.0
attr_say_pct: 38.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.2
turn_len_median: 10
```
