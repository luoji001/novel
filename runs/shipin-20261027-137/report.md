# 胶片 生成报告

slug：`shipin-20261027-137`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7173
LLM 调用：57 次，累计 138.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 胶片盒被守住 | 613 | short | 38.2 | 0 |  | 1 |
| 2 | 红围巾系沙发 | 1089 | normal | 94.4 | 0 |  | 1 |
| 3 | 胶片盒被守住 | 1241 | normal | 91.1 | 0 |  | 2 |
| 4 | 抚摸胶片的指尖 | 1558 | normal | 89.6 | 0 |  | 2 |
| 5 | 红围巾裹放映机 | 1387 | normal | 90.3 | 0 |  | 1 |
| 6 | 胶片盒被夺回 | 1279 | normal | 89.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 551 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 22.9 低于目标 35.0
- 第 3 章：
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 标题重复：「胶片盒被守住」已存在
- 第 4 章：
  - 单条套路句式超限：「周振国的」×3
  - 情节与已写章节重复 0.65 ≥ 0.62（撞上「老李为保护父亲遗留的胶片和电影票根与镇长周振国发生冲突，…」）
- 第 5 章：
  - narration_para_pct 32.0 低于目标 35.0
- 第 6 章：
  - narration_para_pct 28.6 低于目标 35.0
  - [observe] 标题与《胶片盒被守住》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6669
chapter_chars_mean: 1112
chapter_chars_median: 1184
chapter_chars_cv: 0.28
paragraphs_mean: 33.8
dialogue_chars_pct: 30.4
dialogue_para_pct: 65.4
interiority_para_pct: 1.1
narration_para_pct: 33.4
turn_under20_pct: 92.2
turn_over200_pct: 0.0
attr_say_pct: 51.7
attr_adv_pct: 2.1
scenes_per_chapter: 1.7
dialogue_run_mean: 2.8
turn_len_median: 10
```
