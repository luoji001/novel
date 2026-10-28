# 钥匙风波 生成报告

slug：`shipin-20261027-387`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7609
LLM 调用：57 次，累计 129.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 螺丝刀逼近便利店 | 652 | short | 39.0 | 0 |  | 1 |
| 2 | 钥匙锁住货架 | 1113 | normal | 94.3 | 0 |  | 0 |
| 3 | 螺丝刀抵住柜门 | 1203 | normal | 36.1 | 0 |  | 2 |
| 4 | 螺丝刀划破夜色 | 2047 | normal | 38.3 | 0 |  | 3 |
| 5 | 螺丝刀撬动柜门 | 1385 | normal | 92.9 | 0 |  | 1 |
| 6 | 螺丝刀挑起饮料瓶 | 1203 | normal | 36.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 586 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 2 句（如「黑色轿车引擎熄火，静止在远处，像一只等待猎食的野…」）
- 第 4 章：
  - narration_para_pct 22.0 低于目标 35.0
  - dialogue_run_mean 4.6 高于目标 4.0
  - [observe] 章内自我复读 1 句（如「他说，语气平静但带着一丝警惕…」）
- 第 5 章：
  - [observe] 标题与《螺丝刀抵住柜门》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「小林站在」×3
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 7066
chapter_chars_mean: 1178
chapter_chars_median: 1100
chapter_chars_cv: 0.38
paragraphs_mean: 37.2
dialogue_chars_pct: 19.6
dialogue_para_pct: 50.9
interiority_para_pct: 1.5
narration_para_pct: 47.6
turn_under20_pct: 92.0
turn_over200_pct: 0.0
attr_say_pct: 38.6
attr_adv_pct: 3.8
scenes_per_chapter: 1.8
dialogue_run_mean: 2.1
turn_len_median: 8
```
