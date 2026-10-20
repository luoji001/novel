# 刷卡密码 生成报告

slug：`xuanyi-20261019-220`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14144
LLM 调用：68 次，累计 225.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 注销卡重现流通 | 1757 | short | 99.8 | 0 |  | 0 |
| 2 | 刷卡记录与监控冲突 | 3772 | normal | 86.6 | 0 |  | 2 |
| 3 | 擦拭大理石台面 | 3328 | normal | 90.4 | 0 |  | 3 |
| 4 | 刷卡记录疑云 | 3386 | normal | 89.8 | 0 |  | 3 |
| 5 | 折叠文件夹开启时刻 | 1896 | short | 93.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「林子安的」×5
  - [observe] 章内自我复读 18 句（如「林子安起身走向监控墙，指着一块屏幕说：“小王，帮…」）
- 第 3 章：
  - 单条套路句式超限：「周启明的」×3、「林子安的」×3、「为什么会」×3
  - narration_para_pct 17.7 低于目标 20.0
  - attr_adv_pct 13.0 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「周启明的」×8、「林子安的」×8
  - narration_para_pct 9.3 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 5 章：
  - narration_para_pct 13.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13466
chapter_chars_mean: 2693
chapter_chars_median: 3189
chapter_chars_cv: 0.33
paragraphs_mean: 59.4
dialogue_chars_pct: 39.5
dialogue_para_pct: 71.5
interiority_para_pct: 8.9
narration_para_pct: 19.6
turn_under20_pct: 74.0
turn_over200_pct: 0.0
attr_say_pct: 38.9
attr_adv_pct: 9.8
scenes_per_chapter: 3.6
dialogue_run_mean: 4.3
turn_len_median: 13
```
