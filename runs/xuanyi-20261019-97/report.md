# 双重标记 生成报告

slug：`xuanyi-20261019-97`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14614
LLM 调用：68 次，累计 222.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 包裹的双重标记 | 1909 | short | 98.6 | 0 |  | 3 |
| 2 | 重启失败的监控设备 | 3608 | normal | 91.1 | 0 |  | 2 |
| 3 | 代码闪烁的诡异时刻 | 3735 | normal | 89.7 | 0 |  | 2 |
| 4 | 箱子的神秘光泽 | 3414 | normal | 90.5 | 0 |  | 3 |
| 5 | 核心控制系统嗡鸣 | 1943 | short | 89.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 3.9 低于目标 20.0
  - attr_adv_pct 13.3 高于目标 10.0
  - dialogue_run_mean 11.8 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「周雪梅的」×4
  - attr_adv_pct 11.1 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「周雪梅的」×4、「他知道这」×4、「林浩然的」×4
  - dialogue_chars_pct 19.6 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「林浩然的」×9、「他知道这」×4
  - narration_para_pct 15.9 低于目标 20.0
  - [observe] 章内自我复读 4 句（如「李明意味深长地一笑，“有些人是不会让你轻易找到答…」）
- 第 5 章：
  - 单条套路句式超限：「林浩然的」×4、「杭州余杭分拣中心」×4
  - narration_para_pct 6.1 低于目标 20.0
  - [observe] 章内自我复读 20 句（如「林浩然的手指飞快地滑动着鼠标，试图恢复那些丢失的…」）

## 整书结构指标

```
chapters: 5
total_chars: 13938
chapter_chars_mean: 2788
chapter_chars_median: 3235
chapter_chars_cv: 0.32
paragraphs_mean: 59.2
dialogue_chars_pct: 34.2
dialogue_para_pct: 66.8
interiority_para_pct: 10.2
narration_para_pct: 22.9
turn_under20_pct: 70.1
turn_over200_pct: 0.0
attr_say_pct: 17.2
attr_adv_pct: 7.2
scenes_per_chapter: 3.6
dialogue_run_mean: 5.2
turn_len_median: 13
```
