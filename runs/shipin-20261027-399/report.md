# 皮箱的重量 生成报告

slug：`shipin-20261027-399`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6707
LLM 调用：57 次，累计 135.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 柜门缓缓开启 | 424 | short | 18.4 | 0 |  | 3 |
| 2 | 登记本掉落瞬间 | 1308 | normal | 92.2 | 0 |  | 1 |
| 3 | 钥匙转动瞬间 | 1029 | normal | 91.4 | 0 |  | 1 |
| 4 | 警示牌撕开贴纸 | 1220 | normal | 92.8 | 0 |  | 1 |
| 5 | 箱子的重量 | 1333 | normal | 90.5 | 0 |  | 2 |
| 6 | 钥匙入锁孔的一瞬 | 1387 | normal | 21.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 382 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 31.0 低于目标 35.0
- 第 3 章：
  - 单条套路句式超限：「周振华站在」×3
- 第 4 章：
  - narration_para_pct 30.8 低于目标 35.0
- 第 5 章：
  - 单条套路句式超限：「周振华站在」×3
  - narration_para_pct 25.8 低于目标 35.0
- 第 6 章：
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 6200
chapter_chars_mean: 1033
chapter_chars_median: 1184
chapter_chars_cv: 0.33
paragraphs_mean: 30.2
dialogue_chars_pct: 21.9
dialogue_para_pct: 51.8
interiority_para_pct: 0.7
narration_para_pct: 47.5
turn_under20_pct: 92.4
turn_over200_pct: 0.0
attr_say_pct: 32.1
attr_adv_pct: 10.4
scenes_per_chapter: 2.3
dialogue_run_mean: 2.6
turn_len_median: 10
```
