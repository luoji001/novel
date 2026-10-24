# 划线 生成报告

slug：`shuangwen-20261023-74`
档位：爽文　闸门模式：observe
章数：10　总字数：19182
LLM 调用：97 次，累计 414.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕碎合同条款 | 2023 | normal | 96.2 | 0 |  | 2 |
| 2 | 撕碎清单的较量 | 1881 | normal | 92.5 | 0 |  | 2 |
| 3 | 划破协议的签名笔 | 1746 | normal | 90.5 | 0 |  | 0 |
| 4 | 签字笔的较量 | 1736 | normal | 92.1 | 0 |  | 0 |
| 5 | 清单与转账单的对峙 | 1965 | normal | 90.1 | 0 |  | 1 |
| 6 | 签字笔的较量 | 1945 | normal | 89.5 | 0 |  | 3 |
| 7 | 签字笔的较量 | 1995 | normal | 36.8 | 0 |  | 3 |
| 8 | 签字笔的较量 | 1645 | normal | 36.4 | 0 |  | 3 |
| 9 | 签字笔的较量 | 1846 | normal | 35.8 | 0 |  | 4 |
| 10 | 旧清单的指痕 | 2390 | long | 36.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - attr_adv_pct 20.0 高于目标 12.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×4
- 第 5 章：
  - attr_adv_pct 18.2 高于目标 12.0
- 第 6 章：
  - narration_para_pct 2.9 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 7 章：
  - narration_para_pct 4.7 低于目标 5.0
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 8 章：
  - 单条套路句式超限：「深吸一口气」×3
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 9 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 10 章：
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）

## 整书结构指标

```
chapters: 10
total_chars: 18188
chapter_chars_mean: 1819
chapter_chars_median: 1834
chapter_chars_cv: 0.1
paragraphs_mean: 41.9
dialogue_chars_pct: 45.3
dialogue_para_pct: 79.7
interiority_para_pct: 7.5
narration_para_pct: 12.8
turn_under20_pct: 67.2
turn_over200_pct: 0.0
attr_say_pct: 32.7
attr_adv_pct: 18.7
scenes_per_chapter: 1.3
dialogue_run_mean: 5.8
turn_len_median: 16
```
