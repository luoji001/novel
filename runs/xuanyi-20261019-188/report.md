# 水表转动 生成报告

slug：`xuanyi-20261019-188`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14132
LLM 调用：68 次，累计 219.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表指针转动 | 1981 | short | 97.0 | 0 |  | 2 |
| 2 | 电费单 | 3400 | normal | 92.4 | 0 |  | 2 |
| 3 | 水表仍在转动 | 3574 | normal | 89.7 | 0 |  | 4 |
| 4 | 钥匙转动声 | 3384 | normal | 0.0 | 0 |  | 4 |
| 5 | 纸币静静躺着 | 1788 | short | 91.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「苏婉清的」×3、「林振东的」×3
  - narration_para_pct 17.1 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「”苏婉清轻」×3、「林振东的」×3、「为什么会」×3
  - narration_para_pct 18.7 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「林振东的」×7、「苏婉清的」×4、「他知道自己」×3
  - narration_para_pct 17.8 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「苏婉清回答道，“你怎么知道我会在这里…」）
  - [observe] 标题与《水表指针转动》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「林振东站在」×5
  - interiority_para_pct 25.5 高于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5
  - [observe] dialogue_chars_pct 4.7 < 6.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「林振东的」×3

## 整书结构指标

```
chapters: 5
total_chars: 13485
chapter_chars_mean: 2697
chapter_chars_median: 3239
chapter_chars_cv: 0.31
paragraphs_mean: 57.6
dialogue_chars_pct: 23.9
dialogue_para_pct: 57.9
interiority_para_pct: 14.2
narration_para_pct: 27.8
turn_under20_pct: 87.4
turn_over200_pct: 0.0
attr_say_pct: 17.5
attr_adv_pct: 2.5
scenes_per_chapter: 4
dialogue_run_mean: 3.3
turn_len_median: 10
```
