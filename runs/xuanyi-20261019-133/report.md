# 铜钱 生成报告

slug：`xuanyi-20261019-133`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14031
LLM 调用：68 次，累计 232.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻查账本的指尖 | 1565 | short | 97.1 | 0 |  | 3 |
| 2 | 铜钱与凹陷痕迹 | 3763 | normal | 90.3 | 0 |  | 4 |
| 3 | 触摸怀表凹陷处 | 3424 | normal | 90.4 | 0 |  | 2 |
| 4 | 触摸铜钱凹痕 | 3512 | normal | 91.5 | 0 |  | 3 |
| 5 | 摸铜钱看账本 | 1762 | short | 89.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈文远的」×4
  - attr_adv_pct 20.0 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「沈文远的」×8、「沈文远感到」×3、「”周玉兰轻」×3
  - narration_para_pct 13.9 低于目标 20.0
  - [observe] 章内自我复读 20 句（如「沈文远感到一阵晕眩，脑海中浮现出一个模糊的画面：…」）
  - [observe] attr_adv_pct 28.6 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周玉兰的」×4、「沈文远的」×4、「”周玉兰轻」×3
  - narration_para_pct 6.2 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周玉兰的」×7、「沈文远的」×6、「周玉兰点了点头」×3
  - narration_para_pct 6.7 低于目标 20.0
  - [observe] 标题与《铜钱与凹陷痕迹》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - interiority_para_pct 20.6 高于目标 20.0
  - narration_para_pct 17.6 低于目标 20.0
  - [observe] attr_adv_pct 27.3 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13401
chapter_chars_mean: 2680
chapter_chars_median: 3279
chapter_chars_cv: 0.38
paragraphs_mean: 55.2
dialogue_chars_pct: 38.1
dialogue_para_pct: 77.0
interiority_para_pct: 11.0
narration_para_pct: 12.1
turn_under20_pct: 72.7
turn_over200_pct: 0.0
attr_say_pct: 21.6
attr_adv_pct: 16.3
scenes_per_chapter: 3.4
dialogue_run_mean: 5.1
turn_len_median: 12
```
