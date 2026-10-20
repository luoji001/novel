# 铜钥匙 生成报告

slug：`xuanyi-20261019-161`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14488
LLM 调用：68 次，累计 228.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显影液的异样颜色 | 1815 | short | 95.4 | 0 |  | 2 |
| 2 | 登记簿的泛黄纸页 | 3418 | normal | 93.5 | 0 |  | 3 |
| 3 | 摩挲铜钥匙的指尖 | 3968 | normal | 88.4 | 0 |  | 2 |
| 4 | 显影机的嗡鸣 | 3391 | normal | 90.2 | 0 |  | 2 |
| 5 | 抚摸照片边缘的指尖 | 1891 | short | 92.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林振邦的」×3
  - dialogue_chars_pct 19.4 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「苏婉秋的」×5、「林振邦的」×4、「”苏婉秋轻」×3
  - narration_para_pct 4.6 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「苏婉秋的」×4、「他知道这」×4、「林振邦的」×4
  - attr_adv_pct 12.5 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「林振邦的」×12、「苏婉秋的」×7、「”苏婉秋低」×5
  - narration_para_pct 9.4 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「林振邦的」×4
  - narration_para_pct 6.2 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13746
chapter_chars_mean: 2749
chapter_chars_median: 3185
chapter_chars_cv: 0.35
paragraphs_mean: 63.4
dialogue_chars_pct: 34.7
dialogue_para_pct: 74.1
interiority_para_pct: 10.4
narration_para_pct: 15.5
turn_under20_pct: 83.1
turn_over200_pct: 0.0
attr_say_pct: 32.8
attr_adv_pct: 8.8
scenes_per_chapter: 2.8
dialogue_run_mean: 5.5
turn_len_median: 10
```
