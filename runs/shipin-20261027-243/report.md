# 雨靴 生成报告

slug：`shipin-20261027-243`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7187
LLM 调用：57 次，累计 128.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙的归属 | 544 | short | 37.9 | 0 |  | 1 |
| 2 | 塑料袋的归宿 | 1425 | normal | 95.5 | 0 |  | 1 |
| 3 | 雨靴的归属 | 1144 | normal | 92.0 | 0 |  | 2 |
| 4 | 旧皮鞋的归属 | 1244 | normal | 92.3 | 0 |  | 3 |
| 5 | 交接旧皮鞋 | 1401 | normal | 91.2 | 0 |  | 0 |
| 6 | 钥匙与红绳的对话 | 1423 | normal | 93.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 485 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 3 章：
  - 单条套路句式超限：「李秀兰站在」×3、「点了点头」×3
  - [observe] 标题与《钥匙的归属》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - narration_para_pct 30.3 低于目标 35.0
  - attr_adv_pct 14.3 高于目标 10.0
  - dialogue_run_mean 4.6 高于目标 4.0
- 第 6 章：
  - 单条套路句式超限：「李秀兰站在」×3、「李秀兰的」×3
  - narration_para_pct 31.2 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 6644
chapter_chars_mean: 1107
chapter_chars_median: 1227
chapter_chars_cv: 0.3
paragraphs_mean: 37.8
dialogue_chars_pct: 26.3
dialogue_para_pct: 58.0
interiority_para_pct: 0.6
narration_para_pct: 41.3
turn_under20_pct: 95.7
turn_over200_pct: 0.0
attr_say_pct: 51.6
attr_adv_pct: 2.7
scenes_per_chapter: 2.2
dialogue_run_mean: 2.6
turn_len_median: 10
```
