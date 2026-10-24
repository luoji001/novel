# 旧合同 生成报告

slug：`shuangwen-20261023-60`
档位：爽文　闸门模式：observe
章数：10　总字数：19071
LLM 调用：97 次，累计 424.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻黄合同的较量 | 1658 | normal | 40.0 | 0 |  | 2 |
| 2 | 签署协议的炭笔 | 2288 | normal | 93.6 | 0 |  | 3 |
| 3 | 递出旧合同 | 1891 | normal | 91.9 | 0 |  | 2 |
| 4 | 钥匙的交易 | 1411 | normal | 95.6 | 0 |  | 2 |
| 5 | 指纹与合同的对峙 | 1837 | normal | 94.7 | 0 |  | 2 |
| 6 | 钥匙的交易 | 1750 | normal | 37.1 | 0 |  | 3 |
| 7 | 拍桌较量 | 2040 | normal | 36.3 | 0 |  | 1 |
| 8 | 拍桌较量 | 1996 | normal | 86.7 | 0 |  | 5 |
| 9 | 递出旧合同 | 1835 | normal | 91.7 | 0 |  | 3 |
| 10 | 翻黄合同的较量 | 2355 | long | 92.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王德昌的」×6
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 2 章：
  - narration_para_pct 3.3 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 14.5 高于目标 14.0
- 第 3 章：
  - 单条套路句式超限：「王德昌的」×6
  - attr_adv_pct 18.2 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「王德昌的」×5
  - attr_adv_pct 25.0 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「王德昌的」×8
  - attr_adv_pct 12.5 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「王德昌的」×3
  - [observe] attr_adv_pct 29.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「钥匙的交易」已存在
- 第 7 章：
  - [observe] 章内自我复读 1 句（如「你知道这意味着什么吗？…」）
- 第 8 章：
  - 单条套路句式超限：「王德昌的」×5
  - narration_para_pct 2.2 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 22.5 高于目标 14.0
  - [observe] 标题重复：「拍桌较量」已存在
- 第 9 章：
  - 单条套路句式超限：「王德昌的」×11
  - narration_para_pct 3.0 低于目标 5.0
  - [observe] 标题重复：「递出旧合同」已存在
- 第 10 章：
  - 单条套路句式超限：「王德昌的」×9
  - attr_adv_pct 15.0 高于目标 12.0
  - [observe] 标题重复：「翻黄合同的较量」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18064
chapter_chars_mean: 1806
chapter_chars_median: 1782
chapter_chars_cv: 0.14
paragraphs_mean: 43
dialogue_chars_pct: 49.5
dialogue_para_pct: 86.4
interiority_para_pct: 5.5
narration_para_pct: 8.1
turn_under20_pct: 75.9
turn_over200_pct: 0.0
attr_say_pct: 28.5
attr_adv_pct: 16.2
scenes_per_chapter: 1.7
dialogue_run_mean: 8.0
turn_len_median: 11
```
