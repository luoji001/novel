# 表停 生成报告

slug：`xuanyi-20261019-175`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14274
LLM 调用：68 次，累计 235.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手表仍在走动 | 1550 | short | 97.0 | 0 |  | 2 |
| 2 | 手表仍在走动 | 4102 | normal | 90.8 | 0 |  | 5 |
| 3 | 手表仍在走动 | 3317 | normal | 87.4 | 0 |  | 3 |
| 4 | 身份证的反面秘密 | 3672 | normal | 89.6 | 0 |  | 3 |
| 5 | 手表仍走动 | 1628 | short | 90.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林婉如的」×3
  - narration_para_pct 17.5 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
  - 情节与已写章节重复 0.62 ≥ 0.62（撞上「李明发现林婉如丈夫的遗体手表仍在走动，质疑其是否真已去世…」）
  - narration_para_pct 18.4 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「你确定是你看到的吗？…」）
  - [observe] 标题重复：「手表仍在走动」已存在
- 第 3 章：
  - 单条套路句式超限：「点了点头」×3、「他知道这」×3
  - dialogue_chars_pct 18.9 低于目标 20.0
  - [observe] 标题重复：「手表仍在走动」已存在
- 第 4 章：
  - 单条套路句式超限：「林婉如的」×12、「“我不知道」×3
  - narration_para_pct 11.0 低于目标 20.0
  - [observe] 章内自我复读 4 句（如「你说你丈夫是在去年十月去世的？…」）
- 第 5 章：
  - narration_para_pct 16.2 低于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0
  - [observe] 标题与《手表仍在走动》近似 0.91 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13600
chapter_chars_mean: 2720
chapter_chars_median: 3175
chapter_chars_cv: 0.42
paragraphs_mean: 59.8
dialogue_chars_pct: 34.1
dialogue_para_pct: 73.3
interiority_para_pct: 9.0
narration_para_pct: 17.7
turn_under20_pct: 78.3
turn_over200_pct: 0.0
attr_say_pct: 26.7
attr_adv_pct: 7.1
scenes_per_chapter: 2.8
dialogue_run_mean: 4.0
turn_len_median: 12
```
