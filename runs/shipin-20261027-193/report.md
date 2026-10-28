# 铜耳环的光 生成报告

slug：`shipin-20261027-193`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5516
LLM 调用：57 次，累计 116.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 胶片边缘的伤痕 | 427 | short | 37.2 | 0 |  | 1 |
| 2 | 砸向放映机的公文包 | 1094 | normal | 55.9 | 0 |  | 0 |
| 3 | 借阅卡的边缘 | 1079 | normal | 36.6 | 0 |  | 1 |
| 4 | 触摸光影的指尖 | 593 | normal | 17.9 | 0 |  | 3 |
| 5 | 耳环内侧的刻痕 | 1059 | normal | 36.0 | 0 |  | 1 |
| 6 | 胶片缓缓流淌的瞬间 | 1258 | normal | 90.4 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 380 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] 章内自我复读 2 句（如「林姐，这些档案需要您帮忙归档…」）
- 第 4 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 463 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - [observe] 章内自我复读 3 句（如「我……我在准备放最后一批胶片…」）

## 整书结构指标

```
chapters: 6
total_chars: 5062
chapter_chars_mean: 844
chapter_chars_median: 1006
chapter_chars_cv: 0.4
paragraphs_mean: 27
dialogue_chars_pct: 16.2
dialogue_para_pct: 39.9
interiority_para_pct: 1.2
narration_para_pct: 59.0
turn_under20_pct: 91.8
turn_over200_pct: 0.0
attr_say_pct: 51.8
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 1.3
turn_len_median: 12
```
