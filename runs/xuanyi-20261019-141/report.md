# 显影液的温度 生成报告

slug：`xuanyi-20261019-141`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14232
LLM 调用：68 次，累计 234.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显影液中的陌生面孔 | 1709 | short | 94.3 | 0 |  | 2 |
| 2 | 擦拭玻璃上的水雾 | 3362 | normal | 91.3 | 0 |  | 4 |
| 3 | 触摸账本的指纹 | 3882 | normal | 90.2 | 0 |  | 2 |
| 4 | 触碰胶卷的指尖 | 3451 | normal | 91.5 | 0 |  | 3 |
| 5 | 擦拭照片的指纹 | 1823 | short | 92.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林婉秋的」×4
  - dialogue_run_mean 1.4 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×3、「”林婉秋轻」×3、「林婉秋点」×3
  - narration_para_pct 16.2 低于目标 20.0
  - attr_adv_pct 15.0 高于目标 10.0
  - [observe] 章内自我复读 23 句（如「林婉秋轻声说道，她的语气里有一种难以言说的情绪，…」）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×4、「周振邦的」×4、「林婉秋点」×3
  - narration_para_pct 16.7 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周振邦的」×12、「林婉秋的」×6、「周振邦点点」×3
  - narration_para_pct 6.2 低于目标 20.0
  - [observe] attr_adv_pct 20.8 > 20.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「周振邦的」×4
  - narration_para_pct 16.7 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13469
chapter_chars_mean: 2694
chapter_chars_median: 3198
chapter_chars_cv: 0.36
paragraphs_mean: 68
dialogue_chars_pct: 37.8
dialogue_para_pct: 72.2
interiority_para_pct: 9.5
narration_para_pct: 18.4
turn_under20_pct: 79.3
turn_over200_pct: 0.0
attr_say_pct: 33.8
attr_adv_pct: 10.6
scenes_per_chapter: 3.2
dialogue_run_mean: 4.3
turn_len_median: 12
```
