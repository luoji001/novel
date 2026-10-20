# 卡影 生成报告

slug：`xuanyi-20261019-40`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15229
LLM 调用：68 次，累计 224.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲打印件边缘 | 1876 | short | 91.5 | 0 |  | 1 |
| 2 | 摩挲录像带边缘 | 4089 | normal | 89.0 | 0 |  | 3 |
| 3 | 摩挲值班日志边缘 | 3798 | normal | 91.1 | 0 |  | 2 |
| 4 | 摩挲指纹贴片边缘 | 3345 | normal | 90.8 | 0 |  | 3 |
| 5 | 摩挲卡面划痕 | 2116 | short | 81.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 16.7 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周正阳的」×5、「他知道这」×3、「为什么会」×3
  - narration_para_pct 19.8 低于目标 20.0
  - attr_adv_pct 10.3 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「为什么会」×4、「周正阳站在」×3、「带着一丝」×3
  - attr_adv_pct 10.7 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「周正阳的」×5
  - narration_para_pct 17.8 低于目标 20.0
  - attr_adv_pct 15.4 高于目标 10.0
- 第 5 章：
  - dialogue_chars_pct 16.2 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「画面里的男人走进来，胸前佩戴着公司的工牌，手里还…」）

## 整书结构指标

```
chapters: 5
total_chars: 14424
chapter_chars_mean: 2885
chapter_chars_median: 3183
chapter_chars_cv: 0.32
paragraphs_mean: 70
dialogue_chars_pct: 28.5
dialogue_para_pct: 62.7
interiority_para_pct: 11.1
narration_para_pct: 26.1
turn_under20_pct: 82.8
turn_over200_pct: 0.0
attr_say_pct: 12.2
attr_adv_pct: 8.8
scenes_per_chapter: 5.6
dialogue_run_mean: 3.1
turn_len_median: 12
```
