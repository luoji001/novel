# 信中鱼鳞 生成报告

slug：`shipin-20261027-400`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6659
LLM 调用：57 次，累计 144.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁钳与冰台的对峙 | 658 | short | 96.9 | 0 |  | 0 |
| 2 | 鱼鳞擦过脸颊 | 1416 | normal | 92.5 | 0 |  | 0 |
| 3 | 信纸压冰台 | 1402 | normal | 91.3 | 0 |  | 0 |
| 4 | 铁钳砸冰台 | 931 | normal | 36.2 | 0 |  | 2 |
| 5 | 铁钳划破冰面 | 1079 | normal | 36.8 | 0 |  | 1 |
| 6 | 铁钳碾碎冰面 | 1167 | normal | 89.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 4 章：
  - [observe] 章节过短 852 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《铁钳与冰台的对峙》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）
- 第 6 章：
  - [observe] 标题与《铁钳划破冰面》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6203
chapter_chars_mean: 1034
chapter_chars_median: 1045
chapter_chars_cv: 0.27
paragraphs_mean: 30.5
dialogue_chars_pct: 18.8
dialogue_para_pct: 52.6
interiority_para_pct: 0.5
narration_para_pct: 46.9
turn_under20_pct: 96.3
turn_over200_pct: 0.0
attr_say_pct: 17.5
attr_adv_pct: 5.4
scenes_per_chapter: 1
dialogue_run_mean: 2.1
turn_len_median: 8
```
