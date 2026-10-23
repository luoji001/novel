# 确权证 生成报告

slug：`shuangwen-20261022-104`
档位：爽文　闸门模式：observe
章数：10　总字数：19121
LLM 调用：97 次，累计 423.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一张碎纸机里的纸 | 1389 | normal | 38.2 | 0 |  | 2 |
| 2 | 确权证明 | 2089 | normal | 93.7 | 0 |  | 2 |
| 3 | 一张碎纸机里的纸 | 1912 | normal | 94.1 | 0 |  | 2 |
| 4 | 递出旧证件 | 1980 | normal | 93.6 | 0 |  | 0 |
| 5 | 递出旧证件 | 1821 | normal | 90.7 | 0 |  | 3 |
| 6 | 递出旧证件 | 1880 | normal | 90.9 | 0 |  | 2 |
| 7 | 递出旧证件 | 1740 | normal | 88.3 | 0 |  | 4 |
| 8 | 递出旧证件 | 2013 | normal | 94.5 | 0 |  | 3 |
| 9 | 递交户口本 | 2062 | normal | 93.1 | 0 |  | 1 |
| 10 | 递出户口本 | 2225 | long | 37.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×4
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「了自己的」×3
- 第 3 章：
  - 命中套话收尾句
  - [observe] 标题重复：「一张碎纸机里的纸」已存在
- 第 5 章：
  - narration_para_pct 2.4 低于目标 5.0
  - dialogue_run_mean 19.5 高于目标 14.0
  - [observe] 标题重复：「递出旧证件」已存在
- 第 6 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「递出旧证件」已存在
- 第 7 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 15.8 高于目标 12.0
  - dialogue_run_mean 34 高于目标 14.0
  - [observe] 标题重复：「递出旧证件」已存在
- 第 8 章：
  - 单条套路句式超限：「王小梅的」×3
  - attr_adv_pct 15.0 高于目标 12.0
  - [observe] 标题重复：「递出旧证件」已存在
- 第 9 章：
  - 单条套路句式超限：「李建国的」×4
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「王小梅的」×5
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题与《递交户口本》近似 0.80 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18168
chapter_chars_mean: 1817
chapter_chars_median: 1850
chapter_chars_cv: 0.12
paragraphs_mean: 40.4
dialogue_chars_pct: 49.7
dialogue_para_pct: 83.7
interiority_para_pct: 6.1
narration_para_pct: 10.3
turn_under20_pct: 70.1
turn_over200_pct: 0.0
attr_say_pct: 32.3
attr_adv_pct: 13.6
scenes_per_chapter: 1.6
dialogue_run_mean: 10.3
turn_len_median: 12
```
