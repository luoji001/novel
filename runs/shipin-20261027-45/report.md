# 二维码 生成报告

slug：`shipin-20261027-45`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6559
LLM 调用：57 次，累计 145.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 二维码的裂痕 | 458 | short | 13.8 | 0 |  | 3 |
| 2 | 二维码的争夺 | 1292 | normal | 35.8 | 0 |  | 2 |
| 3 | 钥匙的温度 | 1198 | normal | 95.5 | 0 |  | 1 |
| 4 | 炒粉锅的裂缝 | 1079 | normal | 95.0 | 0 |  | 0 |
| 5 | 二维码的裂痕 | 1327 | normal | 88.2 | 0 |  | 4 |
| 6 | 碗与伤疤的重逢 | 1199 | normal | 91.0 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 412 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 3 句（如「陈志远瞥了眼倒在地上的凳子，冷哼一声：“你怕是忘…」）
  - [observe] 标题与《二维码的裂痕》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×3
  - 情节与已写章节重复 0.62 ≥ 0.62（撞上「李大强与陈志远因一张二维码和一把钥匙争执，最终在周美玲调…」）
  - interiority_para_pct 7.1 高于目标 6.0
  - [observe] 标题重复：「二维码的裂痕」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6080
chapter_chars_mean: 1013
chapter_chars_median: 1104
chapter_chars_cv: 0.3
paragraphs_mean: 32.3
dialogue_chars_pct: 22.5
dialogue_para_pct: 48.4
interiority_para_pct: 1.5
narration_para_pct: 50.1
turn_under20_pct: 95.6
turn_over200_pct: 0.0
attr_say_pct: 13.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.3
turn_len_median: 10
```
