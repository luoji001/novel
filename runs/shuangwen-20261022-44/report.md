# 旧房产证 生成报告

slug：`shuangwen-20261022-44`
档位：爽文　闸门模式：observe
章数：10　总字数：19223
LLM 调用：97 次，累计 362.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲门声的打断 | 1914 | normal | 98.1 | 0 |  | 2 |
| 2 | 签字笔的较量 | 2052 | normal | 91.9 | 0 |  | 1 |
| 3 | 公章的震动 | 1682 | normal | 92.0 | 0 |  | 3 |
| 4 | 旧房产证的现身 | 1912 | normal | 91.6 | 0 |  | 2 |
| 5 | 签字笔的较量 | 1756 | normal | 92.8 | 0 |  | 3 |
| 6 | 房产登记档案的现身 | 1875 | normal | 91.3 | 0 |  | 3 |
| 7 | 指纹与铅字的对峙 | 1738 | normal | 36.6 | 0 |  | 2 |
| 8 | 房产登记档案的现身 | 2209 | normal | 91.7 | 0 |  | 3 |
| 9 | 房产证的现身 | 1980 | normal | 91.6 | 0 |  | 2 |
| 10 | 房产证的现身 | 2095 | long | 85.0 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×3
  - dialogue_run_mean 18 高于目标 14.0
- 第 2 章：
  - 单条套路句式超限：「李建国的」×3
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李建国的」×4
  - attr_adv_pct 16.7 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「王小红的」×4
  - attr_adv_pct 20.0 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「李建国的」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 6 章：
  - 单条套路句式超限：「李建国的」×3
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题与《旧房产证的现身》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「王小红的」×4
  - [observe] attr_adv_pct 50.0 > 25.0（结构塌缩）
- 第 8 章：
  - 单条套路句式超限：「李建国的」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「房产登记档案的现身」已存在
- 第 9 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题与《旧房产证的现身》近似 0.92 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「李建国的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 23.1 高于目标 12.0
  - dialogue_run_mean 28 高于目标 14.0
  - [observe] 标题重复：「房产证的现身」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18377
chapter_chars_mean: 1838
chapter_chars_median: 1820
chapter_chars_cv: 0.09
paragraphs_mean: 34.4
dialogue_chars_pct: 50.4
dialogue_para_pct: 83.2
interiority_para_pct: 5.4
narration_para_pct: 11.4
turn_under20_pct: 56.5
turn_over200_pct: 0.0
attr_say_pct: 23.0
attr_adv_pct: 17.4
scenes_per_chapter: 1.8
dialogue_run_mean: 8.3
turn_len_median: 16
```
