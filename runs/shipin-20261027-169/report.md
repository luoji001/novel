# 蛇皮袋 生成报告

slug：`shipin-20261027-169`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7388
LLM 调用：57 次，累计 146.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 蛇皮袋的争夺 | 574 | short | 37.6 | 0 |  | 1 |
| 2 | 红绳与蛇皮袋 | 1279 | normal | 89.1 | 0 |  | 0 |
| 3 | 蛇皮袋上的刘字 | 1259 | normal | 91.3 | 0 |  | 1 |
| 4 | 车票上的城市名 | 1330 | normal | 90.0 | 0 |  | 0 |
| 5 | 钥匙与照片的重逢 | 1507 | normal | 88.6 | 0 |  | 3 |
| 6 | 红绳缠绕蛇皮袋 | 1433 | normal | 87.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 516 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] 标题与《蛇皮袋的争夺》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「李红站在」×3
  - narration_para_pct 17.0 低于目标 35.0
  - dialogue_run_mean 5.6 高于目标 4.0
- 第 6 章：
  - narration_para_pct 21.2 低于目标 35.0
  - dialogue_run_mean 5.2 高于目标 4.0
  - [observe] 标题与《红绳与蛇皮袋》近似 0.77 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6853
chapter_chars_mean: 1142
chapter_chars_median: 1219
chapter_chars_cv: 0.28
paragraphs_mean: 36.7
dialogue_chars_pct: 25.8
dialogue_para_pct: 58.2
interiority_para_pct: 0.4
narration_para_pct: 41.4
turn_under20_pct: 94.3
turn_over200_pct: 0.0
attr_say_pct: 32.5
attr_adv_pct: 1.3
scenes_per_chapter: 1.3
dialogue_run_mean: 2.8
turn_len_median: 10
```
