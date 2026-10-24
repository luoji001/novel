# 旧账 生成报告

slug：`shuangwen-20261023-61`
档位：爽文　闸门模式：observe
章数：10　总字数：18550
LLM 调用：97 次，累计 420.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红笔划线 | 1784 | normal | 40.0 | 0 |  | 2 |
| 2 | 计算器清零 | 1785 | normal | 93.4 | 0 |  | 1 |
| 3 | 计算器清零 | 1647 | normal | 37.6 | 0 |  | 3 |
| 4 | 计算器清零 | 1780 | normal | 92.2 | 0 |  | 2 |
| 5 | 计算器清零 | 1816 | normal | 92.0 | 0 |  | 3 |
| 6 | 计算器清零 | 1893 | normal | 37.6 | 0 |  | 3 |
| 7 | 计算器清零 | 1507 | normal | 36.4 | 0 |  | 3 |
| 8 | 计算器清零 | 1734 | normal | 37.1 | 0 |  | 4 |
| 9 | 计算器清零 | 1857 | normal | 92.6 | 0 |  | 2 |
| 10 | 计算器清零 | 2737 | long | 93.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建军的」×4、「县供销社」×3
  - [observe] attr_adv_pct 52.9 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「李建军的」×6
- 第 3 章：
  - 单条套路句式超限：「县供销社」×4、「王德顺的」×3
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「计算器清零」已存在
- 第 4 章：
  - 单条套路句式超限：「县供销社」×3
  - [observe] 标题重复：「计算器清零」已存在
- 第 5 章：
  - 单条套路句式超限：「王德顺的」×6
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「计算器清零」已存在
- 第 6 章：
  - 单条套路句式超限：「王德顺的」×7、「县供销社」×6
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「计算器清零」已存在
- 第 7 章：
  - 单条套路句式超限：「王德顺的」×5、「李建军的」×3
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
  - [observe] 标题重复：「计算器清零」已存在
- 第 8 章：
  - 单条套路句式超限：「王德顺的」×5、「县供销社」×5
  - narration_para_pct 3.6 低于目标 5.0
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「计算器清零」已存在
- 第 9 章：
  - 单条套路句式超限：「王德顺的」×3
  - [observe] 标题重复：「计算器清零」已存在
- 第 10 章：
  - 单条套路句式超限：「县供销社」×16
  - attr_adv_pct 19.4 高于目标 12.0
  - [observe] 标题重复：「计算器清零」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17681
chapter_chars_mean: 1768
chapter_chars_median: 1702
chapter_chars_cv: 0.17
paragraphs_mean: 36.4
dialogue_chars_pct: 49.2
dialogue_para_pct: 85.5
interiority_para_pct: 5.6
narration_para_pct: 8.9
turn_under20_pct: 67.3
turn_over200_pct: 0.0
attr_say_pct: 28.4
attr_adv_pct: 22.6
scenes_per_chapter: 1.4
dialogue_run_mean: 7.2
turn_len_median: 14
```
