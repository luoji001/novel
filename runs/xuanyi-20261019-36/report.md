# 纸条的背面 生成报告

slug：`xuanyi-20261019-36`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14171
LLM 调用：68 次，累计 221.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 裂缝中的低语 | 1447 | short | 99.5 | 0 |  | 1 |
| 2 | 怀表的指针 | 3984 | normal | 93.1 | 0 |  | 2 |
| 3 | 纸条的裂痕 | 3487 | normal | 89.7 | 0 |  | 3 |
| 4 | 石板上的日期 | 3309 | normal | 90.3 | 0 |  | 1 |
| 5 | 钥匙与石板的对话 | 1939 | short | 92.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈砚秋的」×4
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陆文澜的」×7、「“我不知道」×5、「沈砚秋的」×4
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈砚秋的」×6
  - [observe] attr_adv_pct 31.2 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「陆文澜的」×5、「为什么会」×3
- 第 5 章：
  - narration_para_pct 6.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13522
chapter_chars_mean: 2704
chapter_chars_median: 3179
chapter_chars_cv: 0.39
paragraphs_mean: 57.4
dialogue_chars_pct: 28.0
dialogue_para_pct: 64.7
interiority_para_pct: 13.4
narration_para_pct: 21.9
turn_under20_pct: 83.2
turn_over200_pct: 0.0
attr_say_pct: 27.6
attr_adv_pct: 10.8
scenes_per_chapter: 2.4
dialogue_run_mean: 3.4
turn_len_median: 11
```
