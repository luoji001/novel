# 雨靴 生成报告

slug：`shipin-20261027-33`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6914
LLM 调用：57 次，累计 148.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 靴子上的裂痕 | 676 | short | 95.5 | 0 |  | 0 |
| 2 | 电梯门上的鞋带 | 1258 | normal | 38.3 | 0 |  | 1 |
| 3 | 摩挲雨靴的指尖 | 1083 | normal | 92.2 | 0 |  | 0 |
| 4 | 摩挲雨靴的指尖 | 1445 | normal | 47.8 | 0 |  | 3 |
| 5 | 摩挲雨靴的指尖 | 1229 | normal | 36.0 | 0 |  | 2 |
| 6 | 摩挲拐杖的指尖 | 1217 | normal | 90.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「李素芬的」×4
  - interiority_para_pct 10.7 高于目标 6.0
  - [observe] 标题重复：「摩挲雨靴的指尖」已存在
- 第 5 章：
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）
  - [observe] 标题重复：「摩挲雨靴的指尖」已存在
- 第 6 章：
  - [observe] 标题与《摩挲雨靴的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6467
chapter_chars_mean: 1078
chapter_chars_median: 1140
chapter_chars_cv: 0.24
paragraphs_mean: 29.3
dialogue_chars_pct: 17.8
dialogue_para_pct: 44.2
interiority_para_pct: 4.2
narration_para_pct: 51.5
turn_under20_pct: 95.4
turn_over200_pct: 0.0
attr_say_pct: 49.5
attr_adv_pct: 8.1
scenes_per_chapter: 1.2
dialogue_run_mean: 1.7
turn_len_median: 9
```
