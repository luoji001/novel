# 蛇皮袋 生成报告

slug：`shipin-20261027-43`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6167
LLM 调用：57 次，累计 133.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 蛇皮袋与车票 | 757 | short | 94.6 | 0 |  | 0 |
| 2 | 铁钳撬开蛇皮袋 | 1043 | normal | 91.9 | 0 |  | 2 |
| 3 | 钥匙与蛇皮袋 | 1355 | normal | 94.8 | 0 |  | 1 |
| 4 | 手电筒照亮铜纽扣 | 1005 | normal | 93.2 | 0 |  | 0 |
| 5 | 铁钳与蛇皮袋 | 1179 | normal | 94.3 | 0 |  | 3 |
| 6 | 铁钳与青纹 | 822 | normal | 37.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「王翠兰的」×4
  - 情节与已写章节重复 0.65 ≥ 0.62（撞上「李建国与王翠兰争夺一个装有丈夫遗物的蛇皮袋，最终决定共同…」）
- 第 3 章：
  - 单条套路句式超限：「李建国站在」×3
- 第 5 章：
  - 单条套路句式超限：「李建国的」×3
  - 情节与已写章节重复 0.71 ≥ 0.62（撞上「李建国与王翠兰争夺一个装有丈夫遗物的蛇皮袋，最终决定共同…」）
  - [observe] 标题与《铁钳撬开蛇皮袋》近似 0.77 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 章节过短 737 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5685
chapter_chars_mean: 948
chapter_chars_median: 964
chapter_chars_cv: 0.21
paragraphs_mean: 32.3
dialogue_chars_pct: 20.0
dialogue_para_pct: 49.9
interiority_para_pct: 0.7
narration_para_pct: 49.4
turn_under20_pct: 94.5
turn_over200_pct: 0.0
attr_say_pct: 29.7
attr_adv_pct: 1.7
scenes_per_chapter: 1.2
dialogue_run_mean: 1.7
turn_len_median: 8
```
