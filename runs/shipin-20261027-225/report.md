# 钞票与火车票 生成报告

slug：`shipin-20261027-225`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6483
LLM 调用：57 次，累计 148.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 蛇皮袋与铁钳 | 597 | short | 39.0 | 0 |  | 1 |
| 2 | 铜铃与火车票 | 1055 | normal | 93.3 | 0 |  | 0 |
| 3 | 火车票与铜铃铛 | 1163 | normal | 21.6 | 0 |  | 1 |
| 4 | 火车票与铁钳 | 1307 | normal | 91.3 | 0 |  | 2 |
| 5 | 火车票与铜铃铛 | 1193 | normal | 85.2 | 0 |  | 4 |
| 6 | 铁钳与火车票 | 1162 | normal | 36.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 539 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] 章内自我复读 3 句（如「你拿走的钱，我一分钱都不要…」）
- 第 4 章：
  - narration_para_pct 30.4 低于目标 35.0
  - [observe] 标题与《火车票与铜铃铛》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「李小满的」×4
  - interiority_para_pct 9.5 高于目标 6.0
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 标题重复：「火车票与铜铃铛」已存在
- 第 6 章：
  - 单条套路句式超限：「李小满的」×3
  - [observe] 章内自我复读 1 句（如「远处传来几声犬吠，混着某个窗口飘来的炖菜香气…」）
  - [observe] 标题与《铜铃与火车票》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6129
chapter_chars_mean: 1022
chapter_chars_median: 1104
chapter_chars_cv: 0.24
paragraphs_mean: 21.8
dialogue_chars_pct: 15.4
dialogue_para_pct: 55.1
interiority_para_pct: 3.4
narration_para_pct: 41.5
turn_under20_pct: 98.6
turn_over200_pct: 0.0
attr_say_pct: 26.7
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 1.8
turn_len_median: 8
```
