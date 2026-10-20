# 银顶针 生成报告

slug：`xuanyi-20261019-38`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14201
LLM 调用：68 次，累计 245.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 银顶针的回响 | 1653 | short | 95.2 | 0 |  | 2 |
| 2 | 捻线寻踪 | 4103 | normal | 85.5 | 0 |  | 3 |
| 3 | 银顶针的刻痕 | 3221 | normal | 91.6 | 0 |  | 4 |
| 4 | 账本上的暗纹 | 3235 | normal | 86.3 | 0 |  | 3 |
| 5 | 指尖摩挲绣稿 | 1984 | short | 83.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈砚秋的」×3
  - attr_adv_pct 16.7 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×3
  - interiority_para_pct 22.6 高于目标 20.0
  - [observe] 章内自我复读 15 句（如「正当他对这件事感到更加疑惑之际，一个念头悄然浮现…」）
- 第 3 章：
  - 单条套路句式超限：「陆怀瑾的」×6、「沈砚秋的」×3
  - narration_para_pct 17.2 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「有些东西，有时候比人更诚实…」）
  - [observe] 标题与《银顶针的回响》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「沈砚秋的」×4
  - dialogue_chars_pct 16.7 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「陆怀瑾的」×3
  - interiority_para_pct 27.3 高于目标 20.0
  - narration_para_pct 3.0 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13601
chapter_chars_mean: 2720
chapter_chars_median: 3091
chapter_chars_cv: 0.35
paragraphs_mean: 53
dialogue_chars_pct: 25.1
dialogue_para_pct: 58.1
interiority_para_pct: 19.0
narration_para_pct: 22.9
turn_under20_pct: 76.9
turn_over200_pct: 0.0
attr_say_pct: 40.5
attr_adv_pct: 5.8
scenes_per_chapter: 2.8
dialogue_run_mean: 2.8
turn_len_median: 12
```
