# 账本残页 生成报告

slug：`shuangwen-20261023-93`
档位：爽文　闸门模式：observe
章数：10　总字数：19549
LLM 调用：97 次，累计 453.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本残页的指痕 | 1873 | normal | 98.7 | 0 |  | 1 |
| 2 | 签字权的较量 | 2299 | normal | 37.2 | 0 |  | 2 |
| 3 | 残页上的指纹痕迹 | 1750 | normal | 93.7 | 0 |  | 4 |
| 4 | 令牌与名册之争 | 2068 | normal | 88.5 | 0 |  | 2 |
| 5 | 红印揭开名册谜 | 1696 | normal | 88.0 | 0 |  | 4 |
| 6 | 残页轻触红印 | 2211 | normal | 93.6 | 0 |  | 1 |
| 7 | 残页轻触红印 | 1875 | normal | 87.3 | 0 |  | 5 |
| 8 | 残页轻触红印 | 1632 | normal | 92.8 | 0 |  | 4 |
| 9 | 残页轻触红印 | 1894 | normal | 92.2 | 0 |  | 4 |
| 10 | 残页轻触红印 | 2241 | long | 90.2 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李怀安的」×6、「供奉堂」×3
- 第 2 章：
  - dialogue_run_mean 15.7 高于目标 14.0
  - [observe] attr_adv_pct 41.4 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「供奉堂」×3
  - attr_adv_pct 14.3 高于目标 12.0
  - dialogue_run_mean 17 高于目标 14.0
  - [observe] 标题与《账本残页的指痕》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 40 高于目标 14.0
- 第 5 章：
  - 单条套路句式超限：「李怀安的」×5
  - narration_para_pct 2.6 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - dialogue_run_mean 37 高于目标 14.0
- 第 6 章：
  - 单条套路句式超限：「李怀安的」×3
- 第 7 章：
  - 单条套路句式超限：「李怀安的」×6
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 15.8 高于目标 12.0
  - dialogue_run_mean 40 高于目标 14.0
  - [observe] 标题重复：「残页轻触红印」已存在
- 第 8 章：
  - 单条套路句式超限：「李怀安的」×3、「供奉堂」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 15.5 高于目标 14.0
  - [observe] 标题重复：「残页轻触红印」已存在
- 第 9 章：
  - 单条套路句式超限：「供奉堂」×4
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 16.5 高于目标 14.0
  - [observe] 标题重复：「残页轻触红印」已存在
- 第 10 章：
  - 单条套路句式超限：「李怀安的」×4、「供奉堂」×4
  - narration_para_pct 2.3 低于目标 5.0
  - dialogue_run_mean 21.5 高于目标 14.0
  - [observe] 标题重复：「残页轻触红印」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18550
chapter_chars_mean: 1855
chapter_chars_median: 1796
chapter_chars_cv: 0.12
paragraphs_mean: 42.2
dialogue_chars_pct: 56.8
dialogue_para_pct: 92.0
interiority_para_pct: 2.5
narration_para_pct: 5.5
turn_under20_pct: 70.8
turn_over200_pct: 0.0
attr_say_pct: 24.9
attr_adv_pct: 13.7
scenes_per_chapter: 2.4
dialogue_run_mean: 21.9
turn_len_median: 14
```
