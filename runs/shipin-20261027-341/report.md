# 雨靴的归属 生成报告

slug：`shipin-20261027-341`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6521
LLM 调用：57 次，累计 130.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 雨靴的纹路 | 500 | short | 38.4 | 0 |  | 1 |
| 2 | 钥匙的震颤 | 1077 | normal | 37.5 | 0 |  | 1 |
| 3 | 房产证的折痕 | 1136 | normal | 36.7 | 0 |  | 1 |
| 4 | 铁牌的交锋 | 1169 | normal | 88.1 | 0 |  | 0 |
| 5 | 纸片的重量 | 1409 | normal | 89.3 | 0 |  | 1 |
| 6 | 钥匙的轨迹 | 1224 | normal | 92.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 451 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「赵德昌盯着那个盒子看了几秒，终于低头打开了它…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「你们两个，都给我站住…」）
- 第 5 章：
  - narration_para_pct 34.6 低于目标 35.0
- 第 6 章：
  - [observe] 标题与《钥匙的震颤》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6154
chapter_chars_mean: 1026
chapter_chars_median: 1093
chapter_chars_cv: 0.3
paragraphs_mean: 23.5
dialogue_chars_pct: 18.0
dialogue_para_pct: 50.0
interiority_para_pct: 0.0
narration_para_pct: 50.0
turn_under20_pct: 93.7
turn_over200_pct: 0.0
attr_say_pct: 48.7
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 2.0
turn_len_median: 8
```
