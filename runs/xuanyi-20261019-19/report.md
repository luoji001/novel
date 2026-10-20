# 旧账 生成报告

slug：`xuanyi-20261019-19`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14829
LLM 调用：68 次，累计 242.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻动账本的手指 | 2005 | short | 98.1 | 0 |  | 1 |
| 2 | 掀开铁皮盒的瞬间 | 3775 | normal | 87.0 | 0 |  | 4 |
| 3 | 手指划过褪色地图 | 3573 | normal | 91.6 | 0 |  | 2 |
| 4 | 翻动账本的手指 | 3540 | normal | 91.3 | 0 |  | 2 |
| 5 | 手指划过褪色地图 | 1931 | short | 91.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 18.6 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林永年站在」×3、「点了点头」×3、「林永年的」×3
  - narration_para_pct 19.0 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「他慢慢伸手掀开了盒子一角，一阵潮湿的气息扑面而来…」）
  - [observe] attr_adv_pct 28.6 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「陈国强的」×4
  - narration_para_pct 16.7 低于目标 20.0
- 第 4 章：
  - narration_para_pct 14.8 低于目标 20.0
  - [observe] 标题重复：「翻动账本的手指」已存在
- 第 5 章：
  - 单条套路句式超限：「陈国强的」×4、「林永年的」×3
  - narration_para_pct 13.3 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 标题重复：「手指划过褪色地图」已存在

## 整书结构指标

```
chapters: 5
total_chars: 14197
chapter_chars_mean: 2839
chapter_chars_median: 3403
chapter_chars_cv: 0.32
paragraphs_mean: 54.6
dialogue_chars_pct: 31.1
dialogue_para_pct: 72.4
interiority_para_pct: 11.0
narration_para_pct: 16.7
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 30.9
attr_adv_pct: 11.2
scenes_per_chapter: 4
dialogue_run_mean: 4.3
turn_len_median: 12
```
