# 药瓶上的名字 生成报告

slug：`shipin-20261027-364`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5579
LLM 调用：57 次，累计 118.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 攥紧药瓶的指节 | 330 | short | 21.2 | 0 |  | 1 |
| 2 | 攥紧药瓶的手指 | 1381 | normal | 37.3 | 0 |  | 3 |
| 3 | 药盒里的枯叶 | 896 | normal | 36.3 | 0 |  | 1 |
| 4 | 攥紧输液架的指节 | 913 | normal | 37.8 | 0 |  | 2 |
| 5 | 胸牌坠地的瞬间 | 977 | normal | 35.6 | 0 |  | 3 |
| 6 | 保温杯里的沉默 | 1076 | normal | 37.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 291 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 25.7 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「这是处方单，不是你家人的名字…」）
  - [observe] 标题与《攥紧药瓶的指节》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章节过短 820 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - [observe] 章节过短 863 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《攥紧药瓶的指节》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×4
  - narration_para_pct 30.8 低于目标 35.0
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 6 章：
  - narration_para_pct 24.2 低于目标 35.0
  - dialogue_run_mean 5 高于目标 4.0
  - [observe] attr_adv_pct 28.6 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 5175
chapter_chars_mean: 862
chapter_chars_median: 886
chapter_chars_cv: 0.38
paragraphs_mean: 25.7
dialogue_chars_pct: 31.3
dialogue_para_pct: 64.6
interiority_para_pct: 0.7
narration_para_pct: 34.8
turn_under20_pct: 91.0
turn_over200_pct: 0.0
attr_say_pct: 13.9
attr_adv_pct: 11.4
scenes_per_chapter: 1.3
dialogue_run_mean: 2.5
turn_len_median: 10
```
