# 借条 生成报告

slug：`shuangwen-20261023-83`
档位：爽文　闸门模式：observe
章数：10　总字数：19363
LLM 调用：97 次，累计 430.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的第三笔 | 1403 | normal | 39.2 | 0 |  | 3 |
| 2 | 签字笔的第三笔 | 1747 | normal | 93.7 | 0 |  | 2 |
| 3 | 一份借条复印件 | 2332 | normal | 91.4 | 0 |  | 1 |
| 4 | 一张泛黄的证书 | 2051 | normal | 37.1 | 0 |  | 3 |
| 5 | 一份借条复印件 | 2008 | normal | 90.6 | 0 |  | 4 |
| 6 | 一双手按在合同上 | 1573 | normal | 35.3 | 0 |  | 4 |
| 7 | 一双手按在合同上 | 1930 | normal | 92.3 | 0 |  | 2 |
| 8 | 一道红线 | 1837 | normal | 94.0 | 0 |  | 2 |
| 9 | 一份借条复印件 | 2154 | normal | 92.9 | 0 |  | 3 |
| 10 | 一份借条复印件 | 2318 | long | 91.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×3
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「我给你看过两遍，第三次再确认一遍是不是更稳妥？…」）
- 第 2 章：
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「签字笔的第三笔」已存在
- 第 3 章：
  - 单条套路句式超限：「他知道自己」×4
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「李建国的」×3
  - attr_adv_pct 23.1 高于目标 12.0
  - dialogue_run_mean 20.5 高于目标 14.0
  - [observe] 标题重复：「一份借条复印件」已存在
- 第 6 章：
  - 单条套路句式超限：「李建国的」×5
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 32 高于目标 14.0
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
- 第 7 章：
  - narration_para_pct 2.9 低于目标 5.0
  - [observe] 标题重复：「一双手按在合同上」已存在
- 第 8 章：
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 22.2 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「中带着一丝」×3
  - narration_para_pct 2.3 低于目标 5.0
  - [observe] 标题重复：「一份借条复印件」已存在
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李建国的」×5、「他知道这」×3
  - [observe] 标题重复：「一份借条复印件」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18366
chapter_chars_mean: 1837
chapter_chars_median: 1874
chapter_chars_cv: 0.16
paragraphs_mean: 41.9
dialogue_chars_pct: 53.0
dialogue_para_pct: 86.0
interiority_para_pct: 5.9
narration_para_pct: 8.2
turn_under20_pct: 69.4
turn_over200_pct: 0.0
attr_say_pct: 25.4
attr_adv_pct: 17.7
scenes_per_chapter: 2.1
dialogue_run_mean: 11.0
turn_len_median: 14
```
