# 怀表 生成报告

slug：`xuanyi-20261019-261`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14798
LLM 调用：68 次，累计 244.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻开铁皮盒的秘密 | 1903 | short | 96.7 | 0 |  | 2 |
| 2 | 账本上的可疑日期 | 3926 | normal | 89.6 | 0 |  | 3 |
| 3 | 显影液中的陌生面孔 | 3131 | normal | 93.3 | 0 |  | 3 |
| 4 | 翻转怀表见姓名 | 3951 | normal | 84.3 | 0 |  | 3 |
| 5 | 照片边缘的旧车票 | 1882 | short | 91.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「苏婉清的」×4、「”苏婉清轻」×3
  - narration_para_pct 17.6 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林志远的」×8、「苏婉清的」×4、「”苏婉清低」×3
  - narration_para_pct 14.6 低于目标 20.0
  - [observe] 章内自我复读 20 句（如「他在脑海中迅速回想那个案子的情形，一个八岁的男孩…」）
- 第 3 章：
  - 单条套路句式超限：「林志远的」×6、「苏婉清的」×5、「林志远站在」×4
  - narration_para_pct 11.5 低于目标 20.0
  - attr_adv_pct 11.8 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「深吸一口气」×4、「苏婉清的」×4
  - dialogue_chars_pct 16.4 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「她说着，几乎是本能地伸手摸向胸前的位置——那里有…」）
- 第 5 章：
  - 单条套路句式超限：「苏婉清的」×7、「林志远的」×6

## 整书结构指标

```
chapters: 5
total_chars: 14147
chapter_chars_mean: 2829
chapter_chars_median: 2992
chapter_chars_cv: 0.35
paragraphs_mean: 56.6
dialogue_chars_pct: 31.2
dialogue_para_pct: 71.1
interiority_para_pct: 10.8
narration_para_pct: 18.1
turn_under20_pct: 82.6
turn_over200_pct: 0.0
attr_say_pct: 34.3
attr_adv_pct: 7.1
scenes_per_chapter: 2.8
dialogue_run_mean: 4.1
turn_len_median: 12
```
