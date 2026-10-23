# 旧券 生成报告

slug：`shuangwen-20261022-79`
档位：爽文　闸门模式：observe
章数：10　总字数：17613
LLM 调用：97 次，累计 423.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧券与手令 | 1655 | normal | 39.4 | 0 |  | 2 |
| 2 | 暗格中的铜钱 | 1972 | normal | 93.2 | 0 |  | 0 |
| 3 | 轻抚铜架 | 1710 | normal | 92.1 | 0 |  | 1 |
| 4 | 轻抚旧券 | 1791 | normal | 37.6 | 0 |  | 3 |
| 5 | 轻抚登记簿 | 1703 | normal | 91.7 | 0 |  | 0 |
| 6 | 轻抚登记簿 | 1499 | normal | 93.5 | 0 |  | 2 |
| 7 | 轻抚旧券 | 1840 | normal | 92.1 | 0 |  | 1 |
| 8 | 轻抚登记簿 | 1688 | normal | 93.5 | 0 |  | 1 |
| 9 | 轻抚旧券 | 1727 | normal | 92.5 | 0 |  | 3 |
| 10 | 轻抚券面 | 2018 | long | 91.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「方守仁的」×4
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「方守仁的」×6
- 第 4 章：
  - 单条套路句式超限：「李怀安的」×3
  - 情节与已写章节重复 0.74 ≥ 0.7（撞上「李怀安用一张旧借书券挑战方守仁的权威，引发一场关于规则与…」）
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 6 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「轻抚登记簿」已存在
- 第 7 章：
  - [observe] 标题重复：「轻抚旧券」已存在
- 第 8 章：
  - [observe] 标题重复：「轻抚登记簿」已存在
- 第 9 章：
  - 单条套路句式超限：「方守仁的」×4
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题重复：「轻抚旧券」已存在
- 第 10 章：
  - 情节与已写章节重复 0.70 ≥ 0.7（撞上「李怀安凭借一张三十年前的借书券挑战图书馆管理员方守仁，试…」）
  - [observe] 标题与《轻抚旧券》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 16723
chapter_chars_mean: 1672
chapter_chars_median: 1634
chapter_chars_cv: 0.09
paragraphs_mean: 37.5
dialogue_chars_pct: 43.7
dialogue_para_pct: 83.5
interiority_para_pct: 6.6
narration_para_pct: 9.9
turn_under20_pct: 76.3
turn_over200_pct: 0.0
attr_say_pct: 23.9
attr_adv_pct: 12.7
scenes_per_chapter: 1.7
dialogue_run_mean: 6.5
turn_len_median: 12
```
