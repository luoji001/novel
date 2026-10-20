# 药房门缝 生成报告

slug：`xuanyi-20261019-265`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14971
LLM 调用：68 次，累计 229.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 监控时间被篡改 | 2011 | short | 97.1 | 0 |  | 4 |
| 2 | 核对药品库存数量 | 4055 | normal | 84.7 | 0 |  | 2 |
| 3 | 撕裂的日志一角 | 3127 | normal | 88.8 | 0 |  | 2 |
| 4 | 擦拭玻璃板的手势 | 4056 | normal | 89.4 | 0 |  | 4 |
| 5 | 核对考勤记录 | 1717 | short | 93.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周婉如的」×3
  - narration_para_pct 12.2 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - dialogue_run_mean 14 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「周婉如的」×8、「他知道这」×3
  - [observe] 章内自我复读 54 句（如「他记得上周有一次，一个顾客询问过这种药，而且他说…」）
- 第 3 章：
  - 单条套路句式超限：「周婉如的」×4
  - [observe] 章内自我复读 19 句（如「这种疏漏并不常见，特别是在这个岗位上，每一次记录…」）
- 第 4 章：
  - 单条套路句式超限：「周婉如的」×4、「林修远的」×3
  - narration_para_pct 17.1 低于目标 20.0
  - [observe] 章内自我复读 22 句（如「周婉如转身准备离开，但在门口停下了脚步，“不过，…」）
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「周婉如的」×4
  - narration_para_pct 14.6 低于目标 20.0
  - dialogue_run_mean 10.7 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14274
chapter_chars_mean: 2855
chapter_chars_median: 3016
chapter_chars_cv: 0.37
paragraphs_mean: 59
dialogue_chars_pct: 32.8
dialogue_para_pct: 68.9
interiority_para_pct: 11.1
narration_para_pct: 20.1
turn_under20_pct: 79.1
turn_over200_pct: 0.0
attr_say_pct: 15.1
attr_adv_pct: 9.7
scenes_per_chapter: 5
dialogue_run_mean: 7.1
turn_len_median: 10
```
