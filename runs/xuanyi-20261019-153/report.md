# 铜钱 生成报告

slug：`xuanyi-20261019-153`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14097
LLM 调用：68 次，累计 231.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钱上的年号 | 1827 | short | 57.9 | 0 |  | 2 |
| 2 | 铜秤上的红绳 | 3593 | normal | 92.1 | 0 |  | 3 |
| 3 | 铜钱入掌 | 3334 | normal | 90.7 | 0 |  | 3 |
| 4 | 红绳轻扬 | 3511 | normal | 90.2 | 0 |  | 3 |
| 5 | 灯芯映出铜钱纹 | 1827 | short | 71.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 13.8 低于目标 20.0
  - interiority_para_pct 26.9 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈文渊的」×7、「周怀瑾的」×6、「他知道这」×4
  - narration_para_pct 7.8 低于目标 20.0
  - attr_adv_pct 12.0 高于目标 10.0
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道自己」×4、「周怀瑾的」×3、「沈文渊的」×3
  - [observe] 章内自我复读 1 句（如「为什么这些事情偏偏出现在我这里？…」）
- 第 4 章：
  - 单条套路句式超限：「周怀瑾的」×11
  - narration_para_pct 19.2 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「他知道自己」×3
  - dialogue_chars_pct 13.7 低于目标 20.0
  - interiority_para_pct 30.0 高于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13487
chapter_chars_mean: 2697
chapter_chars_median: 3196
chapter_chars_cv: 0.32
paragraphs_mean: 53.8
dialogue_chars_pct: 26.3
dialogue_para_pct: 61.5
interiority_para_pct: 17.9
narration_para_pct: 20.6
turn_under20_pct: 83.9
turn_over200_pct: 0.0
attr_say_pct: 17.7
attr_adv_pct: 6.9
scenes_per_chapter: 2.2
dialogue_run_mean: 3.3
turn_len_median: 12
```
