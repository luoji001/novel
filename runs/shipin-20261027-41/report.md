# 锁匙 生成报告

slug：`shipin-20261027-41`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6672
LLM 调用：57 次，累计 135.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 保温杯与钥匙相触 | 762 | short | 94.3 | 0 |  | 0 |
| 2 | 保温杯上的裂痕 | 1083 | normal | 91.2 | 0 |  | 2 |
| 3 | 钥匙与保温杯相触 | 1303 | normal | 92.5 | 0 |  | 1 |
| 4 | 保温杯里的血迹 | 1224 | normal | 35.8 | 0 |  | 1 |
| 5 | 纸币上的名字 | 1350 | normal | 93.3 | 0 |  | 1 |
| 6 | 保温杯坠入雪地 | 944 | normal | 54.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 25.0 低于目标 35.0
  - dialogue_run_mean 5 高于目标 4.0
- 第 3 章：
  - [observe] 标题与《保温杯与钥匙相触》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「林浩站在」×3

## 整书结构指标

```
chapters: 6
total_chars: 6233
chapter_chars_mean: 1039
chapter_chars_median: 1090
chapter_chars_cv: 0.2
paragraphs_mean: 28.5
dialogue_chars_pct: 18.0
dialogue_para_pct: 51.1
interiority_para_pct: 0.5
narration_para_pct: 48.4
turn_under20_pct: 99.0
turn_over200_pct: 0.0
attr_say_pct: 43.2
attr_adv_pct: 4.6
scenes_per_chapter: 1.7
dialogue_run_mean: 2.2
turn_len_median: 9
```
