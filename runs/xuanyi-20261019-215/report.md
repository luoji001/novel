# 表语 生成报告

slug：`xuanyi-20261019-215`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13707
LLM 调用：68 次，累计 226.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 机械表停摆时的光 | 1583 | short | 96.3 | 0 |  | 0 |
| 2 | 病历单的反面纹路 | 3115 | normal | 86.9 | 0 |  | 2 |
| 3 | 指纹与玻璃瓶的倒影 | 3441 | normal | 90.5 | 0 |  | 2 |
| 4 | 手表下的纸团 | 3512 | normal | 47.1 | 0 |  | 4 |
| 5 | 水中的气泡浮现 | 2051 | short | 89.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「不仅仅是」×3
  - dialogue_chars_pct 15.2 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 11.3 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「林婉清的」×3、「他知道这」×3
  - dialogue_chars_pct 12.6 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「张伟，男，死亡时间：凌晨两点零三分…」）
- 第 5 章：
  - narration_para_pct 12.8 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13117
chapter_chars_mean: 2623
chapter_chars_median: 2999
chapter_chars_cv: 0.32
paragraphs_mean: 50.2
dialogue_chars_pct: 25.4
dialogue_para_pct: 61.0
interiority_para_pct: 12.6
narration_para_pct: 26.4
turn_under20_pct: 80.1
turn_over200_pct: 0.0
attr_say_pct: 41.4
attr_adv_pct: 9.6
scenes_per_chapter: 3.2
dialogue_run_mean: 3.3
turn_len_median: 12
```
