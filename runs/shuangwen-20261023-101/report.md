# 旧账单的签名 生成报告

slug：`shuangwen-20261023-101`
档位：爽文　闸门模式：observe
章数：10　总字数：19593
LLM 调用：97 次，累计 438.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计算器屏幕跳动数字 | 1754 | normal | 96.7 | 0 |  | 2 |
| 2 | 纸角摩挲的对峙 | 1953 | normal | 92.1 | 0 |  | 0 |
| 3 | 账单边缘的折痕 | 1897 | normal | 90.8 | 0 |  | 2 |
| 4 | 账单边缘的折痕 | 1714 | normal | 88.1 | 0 |  | 2 |
| 5 | 撕碎的供货单碎片 | 1696 | normal | 93.0 | 0 |  | 0 |
| 6 | 折痕下的身份较量 | 1807 | normal | 94.2 | 0 |  | 1 |
| 7 | 摩挲旧账单的对峙 | 1909 | normal | 86.7 | 0 |  | 4 |
| 8 | 摩挲旧账单的对峙 | 2084 | normal | 92.9 | 0 |  | 4 |
| 9 | 拍落老账单 | 1943 | normal | 94.3 | 0 |  | 0 |
| 10 | 摩挲旧账单的对峙 | 2826 | long | 36.7 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 12.5 高于目标 12.0
- 第 4 章：
  - dialogue_run_mean 24 高于目标 14.0
  - [observe] 标题重复：「账单边缘的折痕」已存在
- 第 6 章：
  - narration_para_pct 4.7 低于目标 5.0
- 第 7 章：
  - 单条套路句式超限：「李国强的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 42 高于目标 14.0
  - [observe] 标题与《纸角摩挲的对峙》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 15.0 高于目标 12.0
  - [observe] 标题重复：「摩挲旧账单的对峙」已存在
- 第 10 章：
  - narration_para_pct 3.3 低于目标 5.0
  - attr_adv_pct 19.5 高于目标 12.0
  - dialogue_run_mean 14.5 高于目标 14.0
  - [observe] 章内自我复读 1 句（如「按照市场规定，如果超过约定时间一年以上，就算作无…」）
  - [observe] 标题重复：「摩挲旧账单的对峙」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18547
chapter_chars_mean: 1855
chapter_chars_median: 1806
chapter_chars_cv: 0.17
paragraphs_mean: 44
dialogue_chars_pct: 55.3
dialogue_para_pct: 88.2
interiority_para_pct: 2.4
narration_para_pct: 9.4
turn_under20_pct: 71.3
turn_over200_pct: 0.0
attr_say_pct: 31.0
attr_adv_pct: 10.6
scenes_per_chapter: 1.4
dialogue_run_mean: 13.2
turn_len_median: 13
```
