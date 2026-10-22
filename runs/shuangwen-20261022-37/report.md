# 旧工牌 生成报告

slug：`shuangwen-20261022-37`
档位：爽文　闸门模式：observe
章数：10　总字数：20162
LLM 调用：97 次，累计 384.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一纸入山凭牌的真相 | 1751 | normal | 40.0 | 0 |  | 2 |
| 2 | 旧工牌的磨损痕迹 | 2365 | normal | 94.4 | 0 |  | 0 |
| 3 | 旧工牌的签名时刻 | 1811 | normal | 92.2 | 0 |  | 2 |
| 4 | 旧工牌裂开细缝 | 1832 | normal | 36.2 | 0 |  | 2 |
| 5 | 旧工牌放在地上 | 2009 | normal | 92.3 | 0 |  | 3 |
| 6 | 旧工牌与新证件对峙 | 1824 | normal | 93.4 | 0 |  | 2 |
| 7 | 旧工牌与新凭牌对峙 | 1842 | normal | 92.5 | 0 |  | 1 |
| 8 | 盖章未干 | 1952 | normal | 92.9 | 0 |  | 1 |
| 9 | 旧工牌摩挲纸边 | 1960 | normal | 93.9 | 0 |  | 1 |
| 10 | 摩挲纸边 | 2806 | long | 91.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周怀安的」×4、「沈志远的」×3
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周怀安的」×3
  - attr_adv_pct 17.6 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「周怀安的」×4、「他知道这」×4、「沈志远的」×4
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「周怀安的」×3
  - narration_para_pct 2.8 低于目标 5.0
  - attr_adv_pct 22.2 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「周怀安的」×3
  - narration_para_pct 3.1 低于目标 5.0
- 第 7 章：
  - [observe] 标题与《旧工牌与新证件对峙》近似 0.78 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - dialogue_run_mean 17.5 高于目标 14.0
- 第 9 章：
  - attr_adv_pct 13.3 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「周怀安的」×6
  - [observe] 标题与《旧工牌摩挲纸边》近似 0.73 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 19175
chapter_chars_mean: 1918
chapter_chars_median: 1808
chapter_chars_cv: 0.16
paragraphs_mean: 41.2
dialogue_chars_pct: 48.7
dialogue_para_pct: 85.1
interiority_para_pct: 5.2
narration_para_pct: 9.7
turn_under20_pct: 73.1
turn_over200_pct: 0.0
attr_say_pct: 22.8
attr_adv_pct: 14.1
scenes_per_chapter: 1.3
dialogue_run_mean: 8.0
turn_len_median: 12
```
