# 药谱 生成报告

slug：`shuangwen-20261023-106`
档位：爽文　闸门模式：observe
章数：10　总字数：19280
LLM 调用：97 次，累计 444.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药包称重 | 1924 | normal | 39.6 | 0 |  | 2 |
| 2 | 铅笔划线 | 2008 | normal | 92.1 | 0 |  | 2 |
| 3 | 药秤倒出当归 | 1695 | normal | 93.0 | 0 |  | 1 |
| 4 | 药秤倒出当归 | 1767 | normal | 94.3 | 0 |  | 1 |
| 5 | 铅笔划线 | 1890 | normal | 93.3 | 0 |  | 2 |
| 6 | 药秤卡住 | 1552 | normal | 93.0 | 0 |  | 1 |
| 7 | 药秤倒出当归 | 1929 | normal | 91.4 | 0 |  | 3 |
| 8 | 药谱摊开 | 1558 | normal | 93.2 | 0 |  | 1 |
| 9 | 药秤倒出当归 | 1892 | normal | 92.1 | 0 |  | 2 |
| 10 | 药秤倒出当归 | 3055 | long | 91.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 章内自我复读 3 句（如「李三望着王怀远离去的身影，默默地收起那份药谱手抄…」）
- 第 2 章：
  - narration_para_pct 4.9 低于目标 5.0
  - dialogue_run_mean 19.5 高于目标 14.0
- 第 3 章：
  - 命中套话收尾句
- 第 4 章：
  - [observe] 标题重复：「药秤倒出当归」已存在
- 第 5 章：
  - 单条套路句式超限：「“李三你」×3、「李三点点」×3
  - [observe] 标题重复：「铅笔划线」已存在
- 第 6 章：
  - 单条套路句式超限：「王怀远的」×3
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×4、「“李三你」×4
  - [observe] 标题重复：「药秤倒出当归」已存在
- 第 8 章：
  - attr_adv_pct 15.4 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「“李三你」×3
  - [observe] 标题重复：「药秤倒出当归」已存在
- 第 10 章：
  - 单条套路句式超限：「王怀远的」×3、「他知道这」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「药秤倒出当归」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18280
chapter_chars_mean: 1828
chapter_chars_median: 1759
chapter_chars_cv: 0.22
paragraphs_mean: 42.6
dialogue_chars_pct: 44.6
dialogue_para_pct: 81.6
interiority_para_pct: 5.5
narration_para_pct: 12.9
turn_under20_pct: 70.9
turn_over200_pct: 0.0
attr_say_pct: 22.3
attr_adv_pct: 7.2
scenes_per_chapter: 2.1
dialogue_run_mean: 7.3
turn_len_median: 13
```
