# 旧信 生成报告

slug：`xuanyi-20261019-59`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14087
LLM 调用：68 次，累计 229.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 凝视泛黄账本 | 1874 | short | 84.4 | 0 |  | 2 |
| 2 | 触摸锈蚀信箱锁孔 | 3311 | normal | 45.8 | 0 |  | 4 |
| 3 | 触摸泛黄信笺 | 3404 | normal | 92.1 | 0 |  | 2 |
| 4 | 摩挲裂痕算盘珠 | 3519 | normal | 90.9 | 0 |  | 1 |
| 5 | 触摸褪色统计图 | 1974 | short | 91.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 12.5 低于目标 20.0
  - dialogue_run_mean 1.4 低于目标 1.5
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林永年站在」×3、「他知道这」×3
  - dialogue_chars_pct 16.7 低于目标 20.0
  - interiority_para_pct 26.5 高于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「林永年的」×5、「“我不知道」×3、「”陈素梅轻」×3
  - [observe] attr_adv_pct 28.6 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「林永年的」×4、「陈素梅的」×3
- 第 5 章：
  - narration_para_pct 2.3 低于目标 20.0
  - dialogue_run_mean 13 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13537
chapter_chars_mean: 2707
chapter_chars_median: 3198
chapter_chars_cv: 0.29
paragraphs_mean: 47.2
dialogue_chars_pct: 22.8
dialogue_para_pct: 61.2
interiority_para_pct: 16.0
narration_para_pct: 22.8
turn_under20_pct: 81.1
turn_over200_pct: 0.0
attr_say_pct: 28.1
attr_adv_pct: 9.3
scenes_per_chapter: 2.2
dialogue_run_mean: 4.5
turn_len_median: 12
```
