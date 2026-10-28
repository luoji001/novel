# 铜钥 生成报告

slug：`shipin-20261027-52`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5988
LLM 调用：57 次，累计 147.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙的微笑 | 583 | short | 38.5 | 0 |  | 1 |
| 2 | 钥匙的低语 | 983 | normal | 93.0 | 0 |  | 0 |
| 3 | 钥匙坠地回音 | 1060 | normal | 90.7 | 0 |  | 2 |
| 4 | 便签纸的潮气 | 1047 | normal | 2.2 | 0 |  | 1 |
| 5 | 钥匙与刻痕 | 1060 | normal | 49.2 | 0 |  | 1 |
| 6 | 钥匙的温度 | 1249 | normal | 37.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 529 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 25.9 低于目标 35.0
  - dialogue_run_mean 5 高于目标 4.0
- 第 4 章：
  - interiority_para_pct 14.8 高于目标 6.0
- 第 5 章：
  - dialogue_chars_pct 1.5 低于目标 5.0
- 第 6 章：
  - 单条套路句式超限：「林小满的」×4
  - [observe] 章内自我复读 2 句（如「你要是真要去看看那个房间，得先把钥匙交出来…」）
  - [observe] 标题与《钥匙的低语》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5559
chapter_chars_mean: 926
chapter_chars_median: 984
chapter_chars_cv: 0.23
paragraphs_mean: 27.5
dialogue_chars_pct: 17.0
dialogue_para_pct: 43.4
interiority_para_pct: 3.2
narration_para_pct: 53.4
turn_under20_pct: 94.5
turn_over200_pct: 0.0
attr_say_pct: 15.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.9
turn_len_median: 8
```
