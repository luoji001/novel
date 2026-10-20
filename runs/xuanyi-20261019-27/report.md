# 铜章 生成报告

slug：`xuanyi-20261019-27`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13875
LLM 调用：68 次，累计 234.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜壶与端砚对照 | 1326 | short | 80.1 | 0 |  | 2 |
| 2 | 账本边缘的指纹 | 3593 | normal | 97.0 | 0 |  | 2 |
| 3 | 旧照片的背面 | 3802 | normal | 93.4 | 0 |  | 2 |
| 4 | 铜章与端砚对话 | 3480 | normal | 92.3 | 0 |  | 3 |
| 5 | 木牌与砚台对视 | 1669 | short | 93.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_run_mean 1.1 低于目标 1.5
  - [observe] 章内自我复读 15 句（如「他决定去找陆文渊，看看这位文物局的鉴定员能否帮助…」）
- 第 2 章：
  - 单条套路句式超限：「他知道自己」×3、「沈怀瑾的」×3
  - attr_adv_pct 11.8 高于目标 10.0
- 第 3 章：
  - narration_para_pct 10.5 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「那你为什么现在才告诉我？…」）
- 第 4 章：
  - 单条套路句式超限：「陆文渊的」×7、「沈怀瑾的」×5
  - narration_para_pct 5.9 低于目标 20.0
  - [observe] 标题与《铜壶与端砚对照》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「沈怀瑾的」×3
  - narration_para_pct 0.0 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13224
chapter_chars_mean: 2645
chapter_chars_median: 3329
chapter_chars_cv: 0.43
paragraphs_mean: 57.2
dialogue_chars_pct: 36.1
dialogue_para_pct: 74.0
interiority_para_pct: 11.1
narration_para_pct: 14.9
turn_under20_pct: 78.9
turn_over200_pct: 0.0
attr_say_pct: 14.4
attr_adv_pct: 6.8
scenes_per_chapter: 2
dialogue_run_mean: 5.0
turn_len_median: 13
```
