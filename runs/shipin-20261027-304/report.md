# 铁皮箱 生成报告

slug：`shipin-20261027-304`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6512
LLM 调用：57 次，累计 132.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙贴上门缝 | 559 | short | 36.8 | 0 |  | 2 |
| 2 | 钥匙触碰疤痕 | 954 | normal | 91.4 | 0 |  | 0 |
| 3 | 钥匙触碰铁皮箱 | 1218 | normal | 90.3 | 0 |  | 1 |
| 4 | 剪刀划破铁皮箱 | 1073 | normal | 92.6 | 0 |  | 0 |
| 5 | 钥匙触碰龙纹刺青 | 1183 | normal | 88.9 | 0 |  | 0 |
| 6 | 钥匙触碰玻璃窗 | 1519 | normal | 91.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「她低头看向登记簿上的记录，眉头微皱…」）
  - [observe] 章节过短 501 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] 标题与《钥匙触碰疤痕》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 26.7 低于目标 35.0
  - [observe] 标题与《钥匙触碰疤痕》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6023
chapter_chars_mean: 1004
chapter_chars_median: 1050
chapter_chars_cv: 0.3
paragraphs_mean: 33
dialogue_chars_pct: 23.8
dialogue_para_pct: 55.5
interiority_para_pct: 1.7
narration_para_pct: 42.8
turn_under20_pct: 96.5
turn_over200_pct: 0.0
attr_say_pct: 38.9
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 2.1
turn_len_median: 8
```
