# 蛇皮袋 生成报告

slug：`shipin-20261027-197`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7217
LLM 调用：57 次，累计 139.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 身份证在掌心 | 938 | short | 95.9 | 0 |  | 0 |
| 2 | 身份证在窗台 | 1276 | normal | 92.4 | 0 |  | 3 |
| 3 | 铁丝撬开蛇皮袋 | 1342 | normal | 37.2 | 0 |  | 3 |
| 4 | 车票在窗台 | 1109 | normal | 91.3 | 0 |  | 1 |
| 5 | 车票在掌心 | 1421 | normal | 91.0 | 0 |  | 2 |
| 6 | 铁丝缠绕蛇皮袋 | 1125 | normal | 93.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「王翠兰点」×3
  - narration_para_pct 27.6 低于目标 35.0
  - [observe] 标题与《身份证在掌心》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - narration_para_pct 21.9 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
  - [observe] 章内自我复读 2 句（如「这袋子是他丢下的，我知道他在等什么…」）
- 第 4 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 5 章：
  - 单条套路句式超限：「李建国点了点头」×3
  - [observe] 标题与《车票在窗台》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「王翠兰的」×3、「李建国的」×3
  - [observe] 标题与《铁丝撬开蛇皮袋》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6755
chapter_chars_mean: 1126
chapter_chars_median: 1134
chapter_chars_cv: 0.15
paragraphs_mean: 31
dialogue_chars_pct: 28.8
dialogue_para_pct: 62.8
interiority_para_pct: 0.7
narration_para_pct: 36.5
turn_under20_pct: 92.4
turn_over200_pct: 0.0
attr_say_pct: 28.2
attr_adv_pct: 0.0
scenes_per_chapter: 2.5
dialogue_run_mean: 2.6
turn_len_median: 11
```
