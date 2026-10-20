# 钥匙 生成报告

slug：`xuanyi-20261019-211`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13632
LLM 调用：68 次，累计 222.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 锁孔未闭的沉默 | 1719 | short | 99.7 | 0 |  | 2 |
| 2 | 钥匙转动的空响 | 3556 | normal | 93.2 | 0 |  | 3 |
| 3 | 信封轻触键盘声 | 3381 | normal | 91.6 | 0 |  | 3 |
| 4 | 钥匙边缘的划痕 | 3360 | normal | 91.2 | 0 |  | 3 |
| 5 | 铅笔碎裂的瞬间 | 1611 | short | 78.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈文远的」×3
  - narration_para_pct 10.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林素云的」×4、「带着一丝」×3
  - narration_para_pct 17.4 低于目标 20.0
  - [observe] attr_adv_pct 28.0 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×4
  - narration_para_pct 16.9 低于目标 20.0
  - [observe] 章内自我复读 4 句（如「主管接过信封，仔细端详了一会儿，然后抬起头来：“…」）
- 第 4 章：
  - 单条套路句式超限：「林素云的」×10、「沈文远的」×3
  - narration_para_pct 15.5 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 5 章：
  - interiority_para_pct 28.0 高于目标 20.0
  - narration_para_pct 12.0 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 12927
chapter_chars_mean: 2585
chapter_chars_median: 3155
chapter_chars_cv: 0.35
paragraphs_mean: 59.4
dialogue_chars_pct: 35.3
dialogue_para_pct: 75.9
interiority_para_pct: 8.9
narration_para_pct: 15.2
turn_under20_pct: 82.3
turn_over200_pct: 0.0
attr_say_pct: 23.7
attr_adv_pct: 13.2
scenes_per_chapter: 4
dialogue_run_mean: 5.0
turn_len_median: 11
```
