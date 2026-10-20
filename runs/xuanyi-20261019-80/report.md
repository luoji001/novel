# 暗码 生成报告

slug：`xuanyi-20261019-80`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14405
LLM 调用：68 次，累计 239.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 系统记录的矛盾点 | 1822 | short | 97.6 | 0 |  | 2 |
| 2 | 员工卡深夜入楼 | 3671 | normal | 89.8 | 0 |  | 3 |
| 3 | 便签纸上的异常日期 | 3608 | normal | 89.5 | 0 |  | 1 |
| 4 | 触碰未完成的离职单 | 3472 | normal | 90.1 | 0 |  | 2 |
| 5 | 摩挲金属牌的疑云 | 1827 | short | 92.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周雪梅的」×4、「他知道这」×3
  - narration_para_pct 18.2 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周雪梅的」×4
  - narration_para_pct 15.9 低于目标 20.0
  - [observe] 章内自我复读 18 句（如「林嘉文摇摇头，神色依旧平静，“也有可能是他最后一…」）
- 第 3 章：
  - 单条套路句式超限：「林嘉文的」×6、「他知道这」×5、「他知道自己」×3
- 第 4 章：
  - 单条套路句式超限：「林嘉文的」×5、「带着一丝」×3、「周雪梅的」×3
  - narration_para_pct 10.8 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「林嘉文的」×3
  - narration_para_pct 3.6 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13749
chapter_chars_mean: 2750
chapter_chars_median: 3325
chapter_chars_cv: 0.33
paragraphs_mean: 57
dialogue_chars_pct: 42.1
dialogue_para_pct: 76.5
interiority_para_pct: 8.9
narration_para_pct: 14.7
turn_under20_pct: 66.3
turn_over200_pct: 0.0
attr_say_pct: 20.5
attr_adv_pct: 7.6
scenes_per_chapter: 3.4
dialogue_run_mean: 7.0
turn_len_median: 14
```
