# 充电器 生成报告

slug：`xuanyi-20261019-30`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14700
LLM 调用：68 次，累计 226.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 蓝色数字的疑惑 | 1680 | short | 92.0 | 0 |  | 2 |
| 2 | 后备箱里的红色纸袋 | 3730 | normal | 84.6 | 0 |  | 3 |
| 3 | 行程记录的矛盾 | 3506 | normal | 89.2 | 0 |  | 4 |
| 4 | 充电器的陌生品牌 | 3706 | normal | 90.9 | 0 |  | 2 |
| 5 | 寻找备用充电器 | 2073 | short | 92.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 16.6 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「深吸一口气」×3、「城郊公路317号路段」×3
  - dialogue_chars_pct 19.8 低于目标 20.0
  - [observe] 章内自我复读 31 句（如「更奇怪的是，当他查看车载GPS的历史记录时，那段…」）
- 第 3 章：
  - 单条套路句式超限：「周振华的」×7、「周振华点了点头」×3、「“我不知道」×3
  - dialogue_chars_pct 59.8 高于目标 58.0
  - narration_para_pct 6.2 低于目标 20.0
  - dialogue_run_mean 12.5 高于目标 10.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×5
- 第 5 章：
  - narration_para_pct 10.0 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14051
chapter_chars_mean: 2810
chapter_chars_median: 3329
chapter_chars_cv: 0.34
paragraphs_mean: 56.6
dialogue_chars_pct: 34.3
dialogue_para_pct: 67.9
interiority_para_pct: 9.7
narration_para_pct: 22.4
turn_under20_pct: 76.7
turn_over200_pct: 0.0
attr_say_pct: 36.7
attr_adv_pct: 8.2
scenes_per_chapter: 2.8
dialogue_run_mean: 5.6
turn_len_median: 12
```
