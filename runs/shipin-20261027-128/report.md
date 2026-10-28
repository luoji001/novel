# 铜剪 生成报告

slug：`shipin-20261027-128`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6712
LLM 调用：57 次，累计 206.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜质推子 | 874 | short | 95.8 | 0 |  | 0 |
| 2 | 推子留痕 | 968 | normal | 89.1 | 0 |  | 0 |
| 3 | 镜子裂痕 | 1360 | normal | 36.3 | 0 |  | 2 |
| 4 | 推子与围裙 | 1032 | normal | 93.4 | 0 |  | 0 |
| 5 | 推子入账 | 1244 | normal | 90.1 | 0 |  | 0 |
| 6 | 铜推子入账 | 1228 | normal | 89.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 6 章：
  - [observe] 标题与《推子入账》近似 0.89 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6282
chapter_chars_mean: 1047
chapter_chars_median: 1044
chapter_chars_cv: 0.18
paragraphs_mean: 29.2
dialogue_chars_pct: 24.1
dialogue_para_pct: 48.4
interiority_para_pct: 1.3
narration_para_pct: 50.2
turn_under20_pct: 88.6
turn_over200_pct: 0.0
attr_say_pct: 72.7
attr_adv_pct: 9.7
scenes_per_chapter: 1.7
dialogue_run_mean: 2.1
turn_len_median: 12
```
