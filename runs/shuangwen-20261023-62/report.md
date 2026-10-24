# 剪刀 生成报告

slug：`shuangwen-20261023-62`
档位：爽文　闸门模式：observe
章数：10　总字数：19001
LLM 调用：97 次，累计 405.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 档期被划去的瞬间 | 1828 | normal | 96.8 | 0 |  | 2 |
| 2 | 客户名单的核实 | 2384 | normal | 95.8 | 0 |  | 1 |
| 3 | 预算表的摊开 | 1786 | normal | 94.2 | 0 |  | 0 |
| 4 | 文件被翻开的瞬间 | 1856 | normal | 92.6 | 0 |  | 2 |
| 5 | 营业执照的审查 | 2068 | normal | 93.8 | 0 |  | 1 |
| 6 | 签字笔的落下 | 1384 | normal | 92.4 | 0 |  | 3 |
| 7 | 茶杯里的倒影 | 1520 | normal | 92.3 | 0 |  | 3 |
| 8 | 文件被翻开的瞬间 | 1739 | normal | 94.1 | 0 |  | 3 |
| 9 | 剪刀划过营业执照 | 1919 | normal | 95.4 | 0 |  | 1 |
| 10 | 文件被翻开的瞬间 | 2507 | long | 94.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道自己」×3
  - attr_adv_pct 22.2 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×4
- 第 4 章：
  - narration_para_pct 2.6 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「李振华的」×3
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 4.0 低于目标 5.0
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 21.4 高于目标 12.0
- 第 8 章：
  - 命中套话收尾句
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「文件被翻开的瞬间」已存在
- 第 9 章：
  - 命中套话收尾句
- 第 10 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「文件被翻开的瞬间」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18044
chapter_chars_mean: 1804
chapter_chars_median: 1748
chapter_chars_cv: 0.18
paragraphs_mean: 38.7
dialogue_chars_pct: 44.6
dialogue_para_pct: 80.8
interiority_para_pct: 6.1
narration_para_pct: 13.1
turn_under20_pct: 68.1
turn_over200_pct: 0.0
attr_say_pct: 24.9
attr_adv_pct: 9.2
scenes_per_chapter: 2.7
dialogue_run_mean: 6.1
turn_len_median: 14
```
