# 应急灯 生成报告

slug：`shipin-20261027-20`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6632
LLM 调用：57 次，累计 132.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 粉笔画出的弧线 | 564 | short | 18.4 | 0 |  | 3 |
| 2 | 扫帚与玻璃的碰撞 | 1131 | normal | 96.5 | 0 |  | 0 |
| 3 | 粉笔划出的光痕 | 1390 | normal | 90.5 | 0 |  | 0 |
| 4 | 铅笔盒的低语 | 1167 | normal | 22.1 | 0 |  | 1 |
| 5 | 书包砸地声 | 1194 | normal | 36.9 | 0 |  | 2 |
| 6 | 粉笔画出的光路 | 1180 | normal | 93.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 505 < 597（本章目标 1087 字的 55%）
- 第 4 章：
  - [observe] 章内自我复读 6 句（如「他愣了片刻，随即哈哈大笑，又将铅笔盒贴紧胸口，像…」）
- 第 5 章：
  - 单条套路句式超限：「王小满的」×3
  - [observe] 章内自我复读 2 句（如「我就不信你会一直这样…」）
- 第 6 章：
  - [observe] 标题与《粉笔划出的光痕》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6133
chapter_chars_mean: 1022
chapter_chars_median: 1076
chapter_chars_cv: 0.27
paragraphs_mean: 32.3
dialogue_chars_pct: 16.5
dialogue_para_pct: 38.0
interiority_para_pct: 1.4
narration_para_pct: 60.6
turn_under20_pct: 90.3
turn_over200_pct: 0.0
attr_say_pct: 51.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.5
turn_len_median: 10
```
