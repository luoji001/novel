# 纸条 生成报告

slug：`xuanyi-20261019-236`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13842
LLM 调用：68 次，累计 222.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 纸条上的陌生名字 | 1540 | short | 97.9 | 0 |  | 1 |
| 2 | 撕碎的纸页残影 | 3390 | normal | 87.7 | 0 |  | 3 |
| 3 | 摩挲怀表裂痕 | 3233 | normal | 92.0 | 0 |  | 2 |
| 4 | 摩挲铜钥匙纹路 | 3521 | normal | 88.5 | 0 |  | 3 |
| 5 | 摩挲纸条边缘 | 2153 | short | 91.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 12.5 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「苏婉秋点」×3、「不仅仅是」×3、「林子安的」×3
  - narration_para_pct 16.4 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「他开始重新审视眼前的一切，那个名字、那本书、还有…」）
- 第 3 章：
  - 单条套路句式超限：「林子安的」×6、「苏婉秋的」×3
  - narration_para_pct 11.9 低于目标 20.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林子安的」×7、「他知道这」×6、「林子安站在」×3
  - narration_para_pct 19.3 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 19.3 低于目标 20.0
  - narration_para_pct 17.1 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13193
chapter_chars_mean: 2639
chapter_chars_median: 3101
chapter_chars_cv: 0.32
paragraphs_mean: 57
dialogue_chars_pct: 30.8
dialogue_para_pct: 72.1
interiority_para_pct: 10.9
narration_para_pct: 17.0
turn_under20_pct: 85.4
turn_over200_pct: 0.0
attr_say_pct: 30.0
attr_adv_pct: 2.2
scenes_per_chapter: 2
dialogue_run_mean: 4.1
turn_len_median: 11
```
