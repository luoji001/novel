# 旧病历本 生成报告

slug：`shuangwen-20261022-83`
档位：爽文　闸门模式：observe
章数：10　总字数：19061
LLM 调用：97 次，累计 421.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字与病历对峙 | 1875 | normal | 38.9 | 0 |  | 2 |
| 2 | 签字与病历对峙 | 2516 | normal | 93.9 | 0 |  | 2 |
| 3 | 合同与病历对峙 | 1952 | normal | 94.0 | 0 |  | 2 |
| 4 | 病历本的对峙 | 1878 | normal | 90.6 | 0 |  | 4 |
| 5 | 病历本的对峙 | 2034 | normal | 87.9 | 0 |  | 4 |
| 6 | 签字与病历对峙 | 1655 | normal | 37.0 | 0 |  | 3 |
| 7 | 病历本的对峙 | 1937 | normal | 35.0 | 0 |  | 5 |
| 8 | 签字与验收单对峙 | 1930 | normal | 93.6 | 0 |  | 2 |
| 9 | 病历本上的签名 | 1397 | normal | 91.3 | 0 |  | 2 |
| 10 | 病历本上的签名 | 1877 | long | 93.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×8
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「李建国的」×5
  - [observe] 标题重复：「签字与病历对峙」已存在
- 第 3 章：
  - 命中套话收尾句
  - [observe] 标题与《签字与病历对峙》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - narration_para_pct 2.0 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - dialogue_run_mean 23.5 高于目标 14.0
  - [observe] 标题与《合同与病历对峙》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 16.1 高于目标 12.0
  - dialogue_run_mean 44 高于目标 14.0
  - [observe] 标题重复：「病历本的对峙」已存在
- 第 6 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 章内自我复读 1 句（如「他知道，这场较量才刚刚开始…」）
  - [observe] 标题重复：「签字与病历对峙」已存在
- 第 7 章：
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 43 高于目标 14.0
  - [observe] 章内自我复读 1 句（如「你是想借这个机会，来干涉我手里的事？…」）
  - [observe] 标题重复：「病历本的对峙」已存在
- 第 8 章：
  - 单条套路句式超限：「李建国的」×3
  - [observe] 标题与《签字与病历对峙》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - narration_para_pct 3.6 低于目标 5.0
  - [observe] 标题与《病历本的对峙》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「李建国的」×4
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「病历本上的签名」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18045
chapter_chars_mean: 1804
chapter_chars_median: 1808
chapter_chars_cv: 0.15
paragraphs_mean: 42
dialogue_chars_pct: 51.8
dialogue_para_pct: 86.0
interiority_para_pct: 4.6
narration_para_pct: 9.4
turn_under20_pct: 69.5
turn_over200_pct: 0.0
attr_say_pct: 24.6
attr_adv_pct: 13.0
scenes_per_chapter: 1.8
dialogue_run_mean: 15.4
turn_len_median: 14
```
