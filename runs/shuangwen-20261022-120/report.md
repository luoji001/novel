# 铜钱 生成报告

slug：`shuangwen-20261022-120`
档位：爽文　闸门模式：observe
章数：10　总字数：19530
LLM 调用：97 次，累计 446.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的签名 | 1970 | normal | 99.3 | 0 |  | 0 |
| 2 | 铜钱入炉成金水 | 1806 | normal | 92.6 | 0 |  | 1 |
| 3 | 签名摩挲的瞬间 | 1952 | normal | 92.9 | 0 |  | 3 |
| 4 | 朱砂印的低语 | 1636 | normal | 90.2 | 0 |  | 3 |
| 5 | 签名摩挲的瞬间 | 2192 | normal | 92.2 | 0 |  | 3 |
| 6 | 供奉交付记录的痕迹 | 1774 | normal | 92.1 | 0 |  | 1 |
| 7 | 铜钱跌落的回响 | 2141 | normal | 90.0 | 0 |  | 1 |
| 8 | 撕碎交付记录 | 2027 | normal | 92.7 | 0 |  | 1 |
| 9 | 铜钱跌落的回响 | 1668 | normal | 93.6 | 0 |  | 1 |
| 10 | 铜钱跌落的回响 | 2354 | long | 93.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「李怀安的」×5
- 第 3 章：
  - 单条套路句式超限：「李怀安的」×8
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 4 章：
  - narration_para_pct 2.2 低于目标 5.0
  - attr_adv_pct 22.2 高于目标 12.0
  - dialogue_run_mean 22 高于目标 14.0
- 第 5 章：
  - 单条套路句式超限：「李怀安的」×6、「供奉堂」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「签名摩挲的瞬间」已存在
- 第 6 章：
  - attr_adv_pct 15.8 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「李怀安的」×3、「供奉堂」×3
- 第 8 章：
  - attr_adv_pct 14.3 高于目标 12.0
- 第 9 章：
  - [observe] 标题重复：「铜钱跌落的回响」已存在
- 第 10 章：
  - 单条套路句式超限：「李怀安的」×5
  - narration_para_pct 4.3 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「铜钱跌落的回响」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18402
chapter_chars_mean: 1840
chapter_chars_median: 1846
chapter_chars_cv: 0.12
paragraphs_mean: 48.5
dialogue_chars_pct: 49.7
dialogue_para_pct: 82.6
interiority_para_pct: 5.2
narration_para_pct: 12.2
turn_under20_pct: 76.3
turn_over200_pct: 0.0
attr_say_pct: 32.8
attr_adv_pct: 13.0
scenes_per_chapter: 1.7
dialogue_run_mean: 7.7
turn_len_median: 12
```
