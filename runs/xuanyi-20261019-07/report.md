# 铜秤 生成报告

slug：`xuanyi-20261019-07`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：12178
LLM 调用：68 次，累计 216.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 砚台轻拂 | 1551 | short | 97.1 | 0 |  | 2 |
| 2 | 砚台轻拂 | 3167 | normal | 92.4 | 0 |  | 4 |
| 3 | 砚台轻拂 | 3474 | normal | 91.6 | 0 |  | 4 |
| 4 | 铜牌摩挲 | 2458 | normal | 86.1 | 0 |  | 4 |
| 5 | 纸条揭起 | 1523 | short | 92.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 14.7 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「陆知远的」×6、「微微一笑」×3
  - narration_para_pct 9.9 低于目标 20.0
  - dialogue_run_mean 10.5 高于目标 10.0
  - [observe] 标题重复：「砚台轻拂」已存在
- 第 3 章：
  - 单条套路句式超限：「沈怀瑾的」×4、「瑞玉斋」×3
  - narration_para_pct 12.9 低于目标 20.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
  - [observe] 标题重复：「砚台轻拂」已存在
- 第 4 章：
  - 单条套路句式超限：「瑞玉斋」×3
  - narration_para_pct 0.0 低于目标 20.0
  - dialogue_run_mean 25 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「这份资料是不是……有问题？…」）
- 第 5 章：
  - narration_para_pct 3.6 低于目标 20.0
  - dialogue_run_mean 12.5 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 11616
chapter_chars_mean: 2323
chapter_chars_median: 2342
chapter_chars_cv: 0.37
paragraphs_mean: 49.4
dialogue_chars_pct: 48.1
dialogue_para_pct: 86.8
interiority_para_pct: 4.6
narration_para_pct: 8.6
turn_under20_pct: 65.4
turn_over200_pct: 0.0
attr_say_pct: 30.4
attr_adv_pct: 9.0
scenes_per_chapter: 2
dialogue_run_mean: 11.8
turn_len_median: 14
```
