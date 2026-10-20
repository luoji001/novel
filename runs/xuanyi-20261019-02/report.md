# 当票 生成报告

slug：`xuanyi-20261019-02`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13899
LLM 调用：68 次，累计 244.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 泛黄当票的疑点 | 1869 | short | 50.2 | 0 |  | 3 |
| 2 | 玉佩与怀表相逢 | 3246 | normal | 0.0 | 0 |  | 3 |
| 3 | 沈佩瑶的名字浮现 | 3396 | normal | 29.8 | 0 |  | 2 |
| 4 | 钥匙上的日期之谜 | 3471 | normal | 3.7 | 0 |  | 3 |
| 5 | 铁盒中的裂痕 | 1912 | short | 59.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道自己」×3
  - dialogue_chars_pct 9.5 低于目标 20.0
  - dialogue_run_mean 1.4 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「周慕云的」×5、「他知道这」×3
  - dialogue_chars_pct 10.6 低于目标 20.0
  - interiority_para_pct 22.9 高于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「沈佩瑶的」×6、「周慕云的」×3
  - narration_para_pct 13.2 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周慕云的」×8、「他知道这」×5、「深吸一口气」×3
  - attr_adv_pct 12.0 高于目标 10.0
  - [observe] 章内自我复读 8 句（如「至于这些纠葛是否真如眼前所见那样清晰明了，也许只…」）
- 第 5 章：
  - 单条套路句式超限：「他知道这」×4、「周慕云的」×3
  - dialogue_chars_pct 15.0 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 章内自我复读 6 句（如「他迅速将盒子收好，转身看见站门口的是个穿着灰布长…」）

## 整书结构指标

```
chapters: 5
total_chars: 13277
chapter_chars_mean: 2655
chapter_chars_median: 3135
chapter_chars_cv: 0.3
paragraphs_mean: 51.8
dialogue_chars_pct: 20.9
dialogue_para_pct: 54.7
interiority_para_pct: 16.3
narration_para_pct: 29.1
turn_under20_pct: 82.4
turn_over200_pct: 0.0
attr_say_pct: 19.3
attr_adv_pct: 6.0
scenes_per_chapter: 2.6
dialogue_run_mean: 2.3
turn_len_median: 10
```
