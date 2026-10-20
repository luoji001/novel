# 空驶 生成报告

slug：`xuanyi-20261019-170`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14578
LLM 调用：68 次，累计 220.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计价器的秘密角落 | 1899 | short | 77.7 | 0 |  | 2 |
| 2 | 计价器变零瞬间 | 3840 | normal | 89.7 | 0 |  | 2 |
| 3 | 录音卡顿的瞬间 | 3427 | normal | 84.8 | 0 |  | 2 |
| 4 | 触摸停车票的裂痕 | 3730 | normal | 34.3 | 0 |  | 4 |
| 5 | 触摸U盘的裂痕 | 1677 | short | 91.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 11.0 低于目标 20.0
  - dialogue_run_mean 1.2 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「为什么会」×3
  - narration_para_pct 18.2 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×4、「到了一个」×3
  - [observe] 章内自我复读 17 句（如「我知道你不应该来这里……但我已经知道了太多……如…」）
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3、「为什么会」×3
  - dialogue_chars_pct 10.8 低于目标 20.0
  - interiority_para_pct 22.4 高于目标 20.0
  - dialogue_run_mean 1.3 低于目标 1.5
- 第 5 章：
  - [observe] 标题与《触摸停车票的裂痕》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 14008
chapter_chars_mean: 2802
chapter_chars_median: 3280
chapter_chars_cv: 0.36
paragraphs_mean: 48.8
dialogue_chars_pct: 24.8
dialogue_para_pct: 53.1
interiority_para_pct: 14.3
narration_para_pct: 32.5
turn_under20_pct: 67.2
turn_over200_pct: 0.0
attr_say_pct: 22.6
attr_adv_pct: 5.0
scenes_per_chapter: 2.8
dialogue_run_mean: 2.4
turn_len_median: 15
```
