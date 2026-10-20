# 红绸 生成报告

slug：`xuanyi-20261019-33`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14607
LLM 调用：68 次，累计 242.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 称绸记 | 1498 | short | 82.2 | 0 |  | 2 |
| 2 | 红绸与账本的对峙 | 3750 | normal | 89.5 | 0 |  | 3 |
| 3 | 触碰木柜的布料 | 4055 | normal | 35.0 | 0 |  | 4 |
| 4 | 撕碎的红绸 | 3537 | normal | 87.9 | 0 |  | 4 |
| 5 | 称绸时刻 | 1762 | short | 82.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 12.1 低于目标 20.0
  - interiority_para_pct 21.7 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈文渊的」×5、「周怀瑾的」×3
  - narration_para_pct 15.1 低于目标 20.0
  - attr_adv_pct 15.0 高于目标 10.0
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道自己」×5、「周怀瑾的」×5、「就在这时一」×4
  - dialogue_chars_pct 10.9 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「沈文渊的手指轻轻抚过账本边缘，那张被撕去的纸页留…」）
- 第 4 章：
  - 单条套路句式超限：「沈文渊的」×8、「周怀瑾的」×4、「沈文渊站在」×3
  - narration_para_pct 11.9 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「你是不是知道些什么？…」）
- 第 5 章：
  - dialogue_chars_pct 17.3 低于目标 20.0
  - interiority_para_pct 25.8 高于目标 20.0
  - narration_para_pct 12.9 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13973
chapter_chars_mean: 2795
chapter_chars_median: 3356
chapter_chars_cv: 0.41
paragraphs_mean: 56.2
dialogue_chars_pct: 23.5
dialogue_para_pct: 62.7
interiority_para_pct: 14.4
narration_para_pct: 22.9
turn_under20_pct: 88.2
turn_over200_pct: 0.0
attr_say_pct: 34.4
attr_adv_pct: 8.7
scenes_per_chapter: 3.4
dialogue_run_mean: 3.0
turn_len_median: 10
```
