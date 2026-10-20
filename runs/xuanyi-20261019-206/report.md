# 铁皮文件夹 生成报告

slug：`xuanyi-20261019-206`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14014
LLM 调用：68 次，累计 214.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 剪断纸页的夜晚 | 1583 | short | 71.3 | 0 |  | 2 |
| 2 | 铁皮文件夹的异变 | 3346 | normal | 93.6 | 0 |  | 3 |
| 3 | 红印覆住真实姓名 | 3631 | normal | 91.9 | 0 |  | 2 |
| 4 | 揭开铁皮文件夹 | 3492 | normal | 90.4 | 0 |  | 3 |
| 5 | 钥匙牌上的陌生姓名 | 1957 | short | 91.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 6.5 低于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「周雪梅的」×6、「陈国栋的」×5、「“我不知道」×3
  - narration_para_pct 19.0 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「陈国栋的」×10
  - narration_para_pct 7.2 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「陈国栋的」×4、「他知道这」×3
  - [observe] attr_adv_pct 23.1 > 20.0（结构塌缩）
  - [observe] 标题与《铁皮文件夹的异变》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 16.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13384
chapter_chars_mean: 2677
chapter_chars_median: 3205
chapter_chars_cv: 0.34
paragraphs_mean: 54.8
dialogue_chars_pct: 35.8
dialogue_para_pct: 71.6
interiority_para_pct: 6.9
narration_para_pct: 21.5
turn_under20_pct: 80.8
turn_over200_pct: 0.0
attr_say_pct: 24.5
attr_adv_pct: 12.1
scenes_per_chapter: 3
dialogue_run_mean: 5.2
turn_len_median: 12
```
