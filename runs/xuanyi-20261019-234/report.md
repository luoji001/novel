# 蓝布 生成报告

slug：`xuanyi-20261019-234`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13421
LLM 调用：68 次，累计 219.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记簿缺了一页 | 1465 | short | 96.4 | 0 |  | 2 |
| 2 | 算珠映出的疑云 | 3788 | normal | 84.9 | 0 |  | 1 |
| 3 | 印章坠入抽屉的一瞬 | 2893 | normal | 92.3 | 0 |  | 2 |
| 4 | 布料上的暗纹 | 3306 | normal | 91.1 | 0 |  | 3 |
| 5 | 摸蓝布见铜印 | 1964 | short | 87.7 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周玉兰的」×3
  - narration_para_pct 19.2 低于目标 20.0
- 第 2 章：
  - dialogue_chars_pct 14.8 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「周玉兰的」×3
  - narration_para_pct 12.5 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周玉兰的」×3、「陈德昌的」×3
  - narration_para_pct 17.2 低于目标 20.0
  - attr_adv_pct 15.4 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「周玉兰的」×3
  - narration_para_pct 18.9 低于目标 20.0
  - [observe] 章内自我复读 18 句（如「桌上躺着几件零碎的东西，一卷未拆封的蓝布静静躺在…」）
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 12810
chapter_chars_mean: 2562
chapter_chars_median: 2747
chapter_chars_cv: 0.36
paragraphs_mean: 52.8
dialogue_chars_pct: 27.5
dialogue_para_pct: 65.0
interiority_para_pct: 12.0
narration_para_pct: 23.0
turn_under20_pct: 82.8
turn_over200_pct: 0.0
attr_say_pct: 18.8
attr_adv_pct: 9.2
scenes_per_chapter: 3.4
dialogue_run_mean: 3.8
turn_len_median: 12
```
