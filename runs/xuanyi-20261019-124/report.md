# 粮票 生成报告

slug：`xuanyi-20261019-124`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13558
LLM 调用：68 次，累计 222.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 抚摸账本边缘 | 1756 | short | 53.2 | 0 |  | 4 |
| 2 | 转动钥匙锁孔 | 3747 | normal | 86.6 | 0 |  | 4 |
| 3 | 触摸工资单边缘 | 3235 | normal | 91.0 | 0 |  | 2 |
| 4 | 对焦光斑 | 3166 | normal | 88.2 | 0 |  | 3 |
| 5 | 抚摸粮票边缘 | 1649 | short | 91.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈志远的」×3
  - dialogue_chars_pct 5.0 低于目标 20.0
  - interiority_para_pct 29.2 高于目标 20.0
  - dialogue_run_mean 1 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「点了点头」×4、「他知道这」×3
  - dialogue_chars_pct 17.6 低于目标 20.0
  - attr_adv_pct 11.8 高于目标 10.0
  - [observe] 章内自我复读 12 句（如「最靠边的位置，有一本厚重的账簿，封面已经褪色，纸…」）
- 第 3 章：
  - 单条套路句式超限：「陈志远的」×7、「”周淑芬轻」×5、「周淑芬的」×5
  - narration_para_pct 7.8 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「他知道这」×4
  - 情节与已写章节重复 0.76 ≥ 0.62（撞上「陈志远发现账本中出现已故同事李建国的工资记录，引发他对账…」）
  - [observe] 章内自我复读 4 句（如「李建国已经死了几年，可他的工资还在这里…」）
- 第 5 章：
  - narration_para_pct 6.2 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 标题与《抚摸账本边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 12948
chapter_chars_mean: 2590
chapter_chars_median: 3016
chapter_chars_cv: 0.35
paragraphs_mean: 53.6
dialogue_chars_pct: 27.4
dialogue_para_pct: 61.7
interiority_para_pct: 14.8
narration_para_pct: 23.6
turn_under20_pct: 81.7
turn_over200_pct: 0.0
attr_say_pct: 32.2
attr_adv_pct: 6.8
scenes_per_chapter: 1.8
dialogue_run_mean: 2.9
turn_len_median: 12
```
