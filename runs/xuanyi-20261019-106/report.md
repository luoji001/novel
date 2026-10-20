# 铁门钥匙 生成报告

slug：`xuanyi-20261019-106`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13517
LLM 调用：68 次，累计 219.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙牌的温度变化 | 1674 | short | 96.4 | 0 |  | 1 |
| 2 | 挂钟与火车票的对峙 | 3529 | normal | 93.1 | 0 |  | 2 |
| 3 | 空白页的低语 | 3406 | normal | 89.6 | 0 |  | 3 |
| 4 | 钥匙传递的沉默 | 3192 | normal | 92.4 | 0 |  | 3 |
| 5 | 摩挲火车票边缘 | 1711 | short | 67.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.6 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈志远站在」×5、「周文彬的」×4、「陈志远的」×4
  - narration_para_pct 19.0 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「周文彬的」×8、「陈志远的」×5、「周文彬点」×3
  - narration_para_pct 13.4 低于目标 20.0
  - [observe] 章内自我复读 7 句（如「周文彬说着，脸上露出一种复杂的表情，似乎想要说什…」）
- 第 4 章：
  - 单条套路句式超限：「周文彬的」×9
  - narration_para_pct 4.2 低于目标 20.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 5 章：
  - dialogue_chars_pct 13.9 低于目标 20.0
  - interiority_para_pct 25.9 高于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5

## 整书结构指标

```
chapters: 5
total_chars: 12893
chapter_chars_mean: 2579
chapter_chars_median: 3035
chapter_chars_cv: 0.34
paragraphs_mean: 54.2
dialogue_chars_pct: 30.9
dialogue_para_pct: 69.9
interiority_para_pct: 11.6
narration_para_pct: 18.5
turn_under20_pct: 84.1
turn_over200_pct: 0.0
attr_say_pct: 9.7
attr_adv_pct: 9.1
scenes_per_chapter: 3
dialogue_run_mean: 4.3
turn_len_median: 11
```
