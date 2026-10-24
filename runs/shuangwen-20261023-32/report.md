# 旧书卡 生成报告

slug：`shuangwen-20261023-32`
档位：爽文　闸门模式：observe
章数：10　总字数：18497
LLM 调用：97 次，累计 422.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙被锁住 | 1887 | normal | 98.6 | 0 |  | 1 |
| 2 | 借书卡在掌心浮现 | 1991 | normal | 93.8 | 0 |  | 1 |
| 3 | 借书卡在掌心浮现 | 1514 | normal | 37.0 | 0 |  | 5 |
| 4 | 钢笔划过卡片边缘 | 1772 | normal | 91.5 | 0 |  | 0 |
| 5 | 钢笔划过卡片边缘 | 1637 | normal | 93.1 | 0 |  | 2 |
| 6 | 押金交还是不交 | 2154 | normal | 93.4 | 0 |  | 2 |
| 7 | 钢笔划过卡片边缘 | 1743 | normal | 37.8 | 0 |  | 3 |
| 8 | 钢笔划过卡片边缘 | 1714 | normal | 36.2 | 0 |  | 3 |
| 9 | 钢笔划过卡片边缘 | 1672 | normal | 36.7 | 0 |  | 2 |
| 10 | 钥匙开启铁门瞬间 | 2403 | long | 93.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 22.9 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「档案室」×3
- 第 3 章：
  - 单条套路句式超限：「档案室」×3
  - narration_para_pct 2.5 低于目标 5.0
  - dialogue_run_mean 19 高于目标 14.0
  - [observe] attr_adv_pct 53.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「借书卡在掌心浮现」已存在
- 第 5 章：
  - narration_para_pct 3.1 低于目标 5.0
  - [observe] 标题重复：「钢笔划过卡片边缘」已存在
- 第 6 章：
  - 单条套路句式超限：「点了点头“」×3
  - attr_adv_pct 18.8 高于目标 12.0
- 第 7 章：
  - narration_para_pct 4.4 低于目标 5.0
  - [observe] attr_adv_pct 42.9 > 25.0（结构塌缩）
  - [observe] 标题重复：「钢笔划过卡片边缘」已存在
- 第 8 章：
  - 单条套路句式超限：「陆怀舟的」×3
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「钢笔划过卡片边缘」已存在
- 第 9 章：
  - [observe] 章内自我复读 2 句（如「那你最好准备好足够的押金…」）
  - [observe] 标题重复：「钢笔划过卡片边缘」已存在
- 第 10 章：
  - 单条套路句式超限：「档案室」×4、「沈知远站在」×3

## 整书结构指标

```
chapters: 10
total_chars: 17474
chapter_chars_mean: 1747
chapter_chars_median: 1668
chapter_chars_cv: 0.15
paragraphs_mean: 43.1
dialogue_chars_pct: 46.1
dialogue_para_pct: 81.9
interiority_para_pct: 7.0
narration_para_pct: 11.1
turn_under20_pct: 76.6
turn_over200_pct: 0.0
attr_say_pct: 24.3
attr_adv_pct: 17.2
scenes_per_chapter: 1.9
dialogue_run_mean: 7.7
turn_len_median: 14
```
