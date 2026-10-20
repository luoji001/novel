# 布鞋 生成报告

slug：`xuanyi-20261019-233`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13741
LLM 调用：68 次，累计 228.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲木纹的指尖 | 1725 | short | 85.0 | 0 |  | 3 |
| 2 | 铜锁轻触旧布鞋 | 3341 | normal | 91.8 | 0 |  | 4 |
| 3 | 摩挲银元的指尖 | 3559 | normal | 82.3 | 0 |  | 5 |
| 4 | 摩挲银元的指尖 | 3419 | normal | 91.7 | 0 |  | 4 |
| 5 | 摩挲账本的指尖 | 1692 | short | 90.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 17.5 低于目标 20.0
  - interiority_para_pct 26.9 高于目标 20.0
  - narration_para_pct 19.2 低于目标 20.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周怀瑾的」×5、「沈知远的」×4
  - narration_para_pct 16.2 低于目标 20.0
  - [observe] 章内自我复读 4 句（如「沈知远试着将它们连起来思考——如果这个铜锁真是某…」）
- 第 3 章：
  - 单条套路句式超限：「周怀瑾的」×6、「沈知远的」×6、「微微一笑」×3
  - dialogue_chars_pct 19.0 低于目标 20.0
  - interiority_para_pct 23.3 高于目标 20.0
  - [observe] 章内自我复读 11 句（如「沈知远抬头望去，只见外面的世界渐渐变得模糊不清，…」）
  - [observe] 标题与《摩挲木纹的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「沈知远的」×10、「周怀瑾的」×6
  - narration_para_pct 16.1 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 标题重复：「摩挲银元的指尖」已存在
- 第 5 章：
  - 单条套路句式超限：「周怀瑾的」×4
  - narration_para_pct 13.5 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 标题与《摩挲银元的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13143
chapter_chars_mean: 2629
chapter_chars_median: 3178
chapter_chars_cv: 0.35
paragraphs_mean: 51.8
dialogue_chars_pct: 29.2
dialogue_para_pct: 65.2
interiority_para_pct: 17.5
narration_para_pct: 17.2
turn_under20_pct: 73.8
turn_over200_pct: 0.0
attr_say_pct: 18.2
attr_adv_pct: 6.0
scenes_per_chapter: 2.8
dialogue_run_mean: 3.1
turn_len_median: 12
```
