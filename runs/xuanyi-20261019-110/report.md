# 空车 生成报告

slug：`xuanyi-20261019-110`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15342
LLM 调用：68 次，累计 229.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计费器的时间差 | 1689 | short | 89.4 | 0 |  | 4 |
| 2 | 玻璃碎片的低语 | 3985 | normal | 86.1 | 0 |  | 2 |
| 3 | 充电线的嗡鸣 | 4068 | normal | 26.4 | 0 |  | 6 |
| 4 | 后座座椅的痕迹 | 3385 | normal | 15.0 | 0 |  | 4 |
| 5 | 触摸后视镜的凉意 | 2210 | short | 60.6 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - dialogue_chars_pct 17.3 低于目标 20.0
  - interiority_para_pct 23.5 高于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 16.3 低于目标 20.0
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「为什么会」×4、「深吸一口气」×3、「他知道自己」×3
  - dialogue_chars_pct 9.7 低于目标 20.0
  - interiority_para_pct 26.4 高于目标 20.0
  - dialogue_run_mean 1.4 低于目标 1.5
  - [observe] 章内自我复读 16 句（如「他睁开眼看了看窗外漆黑一片的世界，脑海中浮现出一…」）
- 第 4 章：
  - dialogue_chars_pct 8.1 低于目标 20.0
  - interiority_para_pct 28.1 高于目标 20.0
  - dialogue_run_mean 1.2 低于目标 1.5
  - [observe] 章内自我复读 1 句（如「你一直在找的东西，就在你身边…」）
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 6.6 低于目标 20.0
  - interiority_para_pct 27.0 高于目标 20.0
  - dialogue_run_mean 1.2 低于目标 1.5
  - [observe] attr_adv_pct 50.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 14748
chapter_chars_mean: 2950
chapter_chars_median: 3256
chapter_chars_cv: 0.35
paragraphs_mean: 51.4
dialogue_chars_pct: 11.5
dialogue_para_pct: 39.9
interiority_para_pct: 24.7
narration_para_pct: 35.4
turn_under20_pct: 83.0
turn_over200_pct: 0.0
attr_say_pct: 24.1
attr_adv_pct: 11.6
scenes_per_chapter: 1.4
dialogue_run_mean: 1.4
turn_len_median: 12
```
