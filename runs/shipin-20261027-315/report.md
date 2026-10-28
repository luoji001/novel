# 铁柜 生成报告

slug：`shipin-20261027-315`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6815
LLM 调用：57 次，累计 138.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙撞击柜门 | 595 | short | 38.2 | 0 |  | 1 |
| 2 | 登记本上的指纹 | 1183 | normal | 92.2 | 0 |  | 0 |
| 3 | 手电筒照出影子 | 1118 | normal | 90.3 | 0 |  | 0 |
| 4 | 钥匙触碰柜门 | 1205 | normal | 90.7 | 0 |  | 1 |
| 5 | 皮箱触碰柜门 | 1418 | normal | 89.7 | 0 |  | 2 |
| 6 | 红色钥匙触碰锁孔 | 1290 | normal | 56.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 543 < 597（本章目标 1087 字的 55%）
- 第 4 章：
  - [observe] 标题与《钥匙撞击柜门》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「李国强站在」×3
  - [observe] 标题与《钥匙触碰柜门》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 32.0 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 6313
chapter_chars_mean: 1052
chapter_chars_median: 1080
chapter_chars_cv: 0.26
paragraphs_mean: 32.2
dialogue_chars_pct: 24.2
dialogue_para_pct: 53.4
interiority_para_pct: 1.6
narration_para_pct: 45.0
turn_under20_pct: 93.1
turn_over200_pct: 0.0
attr_say_pct: 43.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.8
turn_len_median: 10
```
