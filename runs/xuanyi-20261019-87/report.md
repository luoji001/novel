# 铜印 生成报告

slug：`xuanyi-20261019-87`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13741
LLM 调用：68 次，累计 233.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 砚台底款的暗纹 | 1867 | short | 97.7 | 0 |  | 0 |
| 2 | 翻阅拍卖目录 | 3327 | normal | 91.7 | 0 |  | 3 |
| 3 | 铜印的低语 | 3100 | normal | 91.4 | 0 |  | 2 |
| 4 | 纸条上的日期 | 3577 | normal | 88.6 | 0 |  | 4 |
| 5 | 砚台消失的雨天 | 1865 | short | 91.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「沈砚生的」×10、「周怀远的」×3、「瑞玉斋」×3
  - narration_para_pct 10.9 低于目标 20.0
  - attr_adv_pct 17.4 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「瑞玉斋」×8、「沈砚生的」×5
  - narration_para_pct 7.5 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「他知道这」×5、「沈砚生的」×5、「北平古玩协会」×3
  - narration_para_pct 19.7 低于目标 20.0
  - attr_adv_pct 15.4 高于目标 10.0
  - [observe] 章内自我复读 2 句（如「沈砚生没有回答，只是默默地注视着对方，眼中闪过一…」）
- 第 5 章：
  - 单条套路句式超限：「沈砚生的」×5、「周怀远的」×3
  - narration_para_pct 6.2 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13104
chapter_chars_mean: 2621
chapter_chars_median: 2952
chapter_chars_cv: 0.3
paragraphs_mean: 54.6
dialogue_chars_pct: 36.7
dialogue_para_pct: 75.2
interiority_para_pct: 11.7
narration_para_pct: 13.1
turn_under20_pct: 74.4
turn_over200_pct: 0.0
attr_say_pct: 10.2
attr_adv_pct: 15.8
scenes_per_chapter: 3.2
dialogue_run_mean: 4.8
turn_len_median: 14
```
