# 红名单 生成报告

slug：`shuangwen-20261023-134`
档位：爽文　闸门模式：observe
章数：10　总字数：20255
LLM 调用：97 次，累计 434.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的重量 | 2043 | normal | 39.9 | 0 |  | 2 |
| 2 | 撕碎的报表 | 2147 | normal | 96.2 | 0 |  | 1 |
| 3 | 翻看采购数据表 | 1860 | normal | 94.3 | 0 |  | 1 |
| 4 | 翻看采购数据表 | 1793 | normal | 90.7 | 0 |  | 3 |
| 5 | 红笔点名 | 1926 | normal | 92.6 | 0 |  | 2 |
| 6 | 翻看采购数据表 | 1877 | normal | 37.2 | 0 |  | 3 |
| 7 | 翻看采购数据表 | 1941 | normal | 94.3 | 0 |  | 3 |
| 8 | 翻看采购数据表 | 2129 | normal | 93.2 | 0 |  | 2 |
| 9 | 翻看采购数据表 | 1703 | normal | 37.4 | 0 |  | 3 |
| 10 | 翻看采购数据表 | 2826 | long | 92.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「”陈浩坚定地说」×3、「李振强的」×3
  - [observe] attr_adv_pct 46.2 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「李振强的」×3
- 第 3 章：
  - narration_para_pct 0.0 低于目标 5.0
- 第 4 章：
  - narration_para_pct 3.3 低于目标 5.0
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「翻看采购数据表」已存在
- 第 5 章：
  - narration_para_pct 2.6 低于目标 5.0
  - dialogue_run_mean 18.5 高于目标 14.0
- 第 6 章：
  - 单条套路句式超限：「李振强的」×6
  - [observe] attr_adv_pct 36.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「翻看采购数据表」已存在
- 第 7 章：
  - 单条套路句式超限：「李振强的」×4
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「翻看采购数据表」已存在
- 第 8 章：
  - 单条套路句式超限：「李振强的」×6、「他知道这」×3
  - [observe] 标题重复：「翻看采购数据表」已存在
- 第 9 章：
  - 单条套路句式超限：「李振强的」×3
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「翻看采购数据表」已存在
- 第 10 章：
  - 单条套路句式超限：「李振强的」×4
  - [observe] 标题重复：「翻看采购数据表」已存在

## 整书结构指标

```
chapters: 10
total_chars: 19211
chapter_chars_mean: 1921
chapter_chars_median: 1832
chapter_chars_cv: 0.15
paragraphs_mean: 44.5
dialogue_chars_pct: 51.7
dialogue_para_pct: 85.9
interiority_para_pct: 4.1
narration_para_pct: 10.0
turn_under20_pct: 66.3
turn_over200_pct: 0.0
attr_say_pct: 19.9
attr_adv_pct: 17.0
scenes_per_chapter: 2
dialogue_run_mean: 9.0
turn_len_median: 14
```
