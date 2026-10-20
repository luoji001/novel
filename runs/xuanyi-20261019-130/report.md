# 数据备份 生成报告

slug：`xuanyi-20261019-130`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14022
LLM 调用：68 次，累计 225.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 行车记录仪的黑影 | 1715 | short | 96.3 | 0 |  | 0 |
| 2 | 拆开金属盒 | 3376 | normal | 88.3 | 0 |  | 3 |
| 3 | 密码箱的秘密 | 3813 | normal | 88.8 | 0 |  | 3 |
| 4 | 屏幕上的数据消失 | 3421 | normal | 93.0 | 0 |  | 4 |
| 5 | 工牌上的蓝光闪过 | 1692 | short | 94.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「他知道这」×4
  - dialogue_chars_pct 17.5 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「他没有回应，只是默默地看着眼前这个人，等待对方说…」）
- 第 3 章：
  - 单条套路句式超限：「林婉如的」×5、「陈子安点点」×4、「为什么会」×4
  - narration_para_pct 13.3 低于目标 20.0
  - [observe] 章内自我复读 27 句（如「然而，林婉如的眼神始终没有离开陈子安，仿佛她在等…」）
- 第 4 章：
  - 单条套路句式超限：「林婉如的」×6、「林婉如点」×3
  - narration_para_pct 11.4 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 章内自我复读 3 句（如「这上面写着‘禁止任何人擅自改动行车记录…」）
- 第 5 章：
  - narration_para_pct 7.5 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13308
chapter_chars_mean: 2662
chapter_chars_median: 3244
chapter_chars_cv: 0.36
paragraphs_mean: 63.6
dialogue_chars_pct: 41.8
dialogue_para_pct: 71.7
interiority_para_pct: 7.8
narration_para_pct: 20.5
turn_under20_pct: 75.4
turn_over200_pct: 0.0
attr_say_pct: 30.2
attr_adv_pct: 6.7
scenes_per_chapter: 2.6
dialogue_run_mean: 4.8
turn_len_median: 13
```
