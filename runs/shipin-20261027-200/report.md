# 旧船票 生成报告

slug：`shipin-20261027-200`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6308
LLM 调用：57 次，累计 188.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙的温度 | 723 | short | 97.8 | 0 |  | 0 |
| 2 | 铜钥匙的重量 | 1333 | normal | 91.5 | 0 |  | 2 |
| 3 | 船票与吊坠的对峙 | 1211 | normal | 91.7 | 0 |  | 1 |
| 4 | 铜钥匙坠入尘埃 | 1056 | normal | 90.1 | 0 |  | 0 |
| 5 | 铜铃与雨丝 | 1084 | normal | 90.1 | 0 |  | 1 |
| 6 | 铜铃轻触栏杆 | 895 | normal | 36.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 32.1 低于目标 35.0
  - [observe] 标题与《铜钥匙的温度》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - narration_para_pct 28.0 低于目标 35.0
- 第 5 章：
  - dialogue_chars_pct 3.2 低于目标 5.0
- 第 6 章：
  - [observe] 章节过短 796 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5877
chapter_chars_mean: 980
chapter_chars_median: 1008
chapter_chars_cv: 0.23
paragraphs_mean: 26.2
dialogue_chars_pct: 24.5
dialogue_para_pct: 57.1
interiority_para_pct: 0.8
narration_para_pct: 42.1
turn_under20_pct: 94.7
turn_over200_pct: 0.0
attr_say_pct: 49.2
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 2.2
turn_len_median: 10
```
