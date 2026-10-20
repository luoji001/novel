# 算珠 生成报告

slug：`xuanyi-20261019-264`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15354
LLM 调用：68 次，累计 224.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 算盘上的指纹 | 1524 | short | 52.9 | 0 |  | 3 |
| 2 | 算盘上的圈圈 | 4082 | normal | 90.1 | 0 |  | 4 |
| 3 | 纸条上的指纹 | 4032 | normal | 88.3 | 0 |  | 2 |
| 4 | 皮箱里的旧账本 | 4018 | normal | 85.8 | 0 |  | 3 |
| 5 | 翻动账本的手指 | 1693 | short | 83.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 16.1 低于目标 20.0
  - interiority_para_pct 20.8 高于目标 20.0
  - dialogue_run_mean 1.4 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「点了点头」×3
  - 情节与已写章节重复 0.75 ≥ 0.62（撞上「李建国发现妻子失踪前留下的数字竟出现在粮站账本中，引发他…」）
  - dialogue_chars_pct 19.6 低于目标 20.0
  - [observe] 标题与《算盘上的指纹》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「他知道自己」×3、「点了点头」×3、「他知道这」×3
  - [observe] 标题与《算盘上的指纹》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「周慧兰的」×5、「他知道这」×5、「点了点头」×3
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 章内自我复读 16 句（如「老赵今年已经五十多岁，经常独自一人待在这栋老房子…」）
- 第 5 章：
  - 单条套路句式超限：「周慧兰的」×3
  - interiority_para_pct 24.2 高于目标 20.0
  - narration_para_pct 12.1 低于目标 20.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 14702
chapter_chars_mean: 2940
chapter_chars_median: 3838
chapter_chars_cv: 0.44
paragraphs_mean: 55.6
dialogue_chars_pct: 21.9
dialogue_para_pct: 60.3
interiority_para_pct: 15.0
narration_para_pct: 24.7
turn_under20_pct: 76.5
turn_over200_pct: 0.0
attr_say_pct: 17.9
attr_adv_pct: 10.0
scenes_per_chapter: 7.2
dialogue_run_mean: 3.3
turn_len_median: 13
```
