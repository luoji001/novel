# 皮箱的重量 生成报告

slug：`shipin-20261027-133`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6433
LLM 调用：57 次，累计 136.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记表上的名字 | 553 | short | 38.2 | 0 |  | 1 |
| 2 | 钥匙孔的微光 | 1182 | normal | 91.7 | 0 |  | 1 |
| 3 | 保温杯的敲击 | 1172 | normal | 92.0 | 0 |  | 1 |
| 4 | 保温杯的温度 | 1089 | normal | 91.7 | 0 |  | 1 |
| 5 | 钥匙与登记表 | 1141 | normal | 90.3 | 0 |  | 0 |
| 6 | 钥匙上的刻痕 | 1290 | normal | 27.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 500 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 命中套话收尾句
- 第 3 章：
  - narration_para_pct 28.0 低于目标 35.0
- 第 4 章：
  - [observe] 标题与《保温杯的敲击》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「陈志远的」×3
  - interiority_para_pct 12.5 高于目标 6.0

## 整书结构指标

```
chapters: 6
total_chars: 5938
chapter_chars_mean: 990
chapter_chars_median: 1054
chapter_chars_cv: 0.26
paragraphs_mean: 28.5
dialogue_chars_pct: 21.3
dialogue_para_pct: 51.1
interiority_para_pct: 3.8
narration_para_pct: 45.0
turn_under20_pct: 94.7
turn_over200_pct: 0.0
attr_say_pct: 26.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.8
turn_len_median: 10
```
