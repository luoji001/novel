# 雨靴的归属 生成报告

slug：`shipin-20261027-383`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6172
LLM 调用：57 次，累计 129.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙串上的血迹 | 378 | short | 17.8 | 0 |  | 3 |
| 2 | 灯罩松了 | 1124 | normal | 96.5 | 0 |  | 0 |
| 3 | 雨靴上的裂痕 | 1194 | normal | 93.2 | 0 |  | 0 |
| 4 | 毛线帽的回音 | 1189 | normal | 92.0 | 0 |  | 1 |
| 5 | 雨靴与钥匙串对峙 | 1183 | normal | 90.9 | 0 |  | 0 |
| 6 | 拖鞋与钥匙串对峙 | 1098 | normal | 92.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 1.2 低于目标 5.0
  - narration_para_pct 93.3 高于目标 90.0
  - [observe] 章节过短 333 < 597（本章目标 1087 字的 55%）
- 第 4 章：
  - narration_para_pct 34.6 低于目标 35.0
- 第 6 章：
  - [observe] 标题与《雨靴与钥匙串对峙》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5754
chapter_chars_mean: 959
chapter_chars_median: 1074
chapter_chars_cv: 0.32
paragraphs_mean: 27.2
dialogue_chars_pct: 21.4
dialogue_para_pct: 52.8
interiority_para_pct: 1.6
narration_para_pct: 45.6
turn_under20_pct: 92.9
turn_over200_pct: 0.0
attr_say_pct: 38.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.8
turn_len_median: 10
```
