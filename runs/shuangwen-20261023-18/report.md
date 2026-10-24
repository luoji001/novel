# 转让协议 生成报告

slug：`shuangwen-20261023-18`
档位：爽文　闸门模式：observe
章数：10　总字数：18849
LLM 调用：97 次，累计 437.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔划破 | 1551 | normal | 100.0 | 0 |  | 1 |
| 2 | 雪落协议展 | 2054 | normal | 93.2 | 0 |  | 1 |
| 3 | 签字笔划破 | 1722 | normal | 92.3 | 0 |  | 1 |
| 4 | 账本核对 | 1809 | normal | 93.4 | 0 |  | 1 |
| 5 | 签字笔划破 | 1978 | normal | 36.6 | 0 |  | 2 |
| 6 | 签字笔划破 | 1815 | normal | 92.6 | 0 |  | 2 |
| 7 | 签字笔划破 | 1585 | normal | 92.8 | 0 |  | 1 |
| 8 | 结算单推到桌面 | 2108 | normal | 89.4 | 0 |  | 2 |
| 9 | 签字笔划破 | 1803 | normal | 92.3 | 0 |  | 2 |
| 10 | 雪落协议展 | 2414 | long | 93.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 3.0 低于目标 5.0
- 第 2 章：
  - attr_adv_pct 13.6 高于目标 12.0
- 第 3 章：
  - [observe] 标题重复：「签字笔划破」已存在
- 第 4 章：
  - narration_para_pct 3.2 低于目标 5.0
- 第 5 章：
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔划破」已存在
- 第 6 章：
  - 单条套路句式超限：「办公室」×3
  - [observe] 标题重复：「签字笔划破」已存在
- 第 7 章：
  - [observe] 标题重复：「签字笔划破」已存在
- 第 8 章：
  - 单条套路句式超限：「办公室」×3
  - attr_adv_pct 19.2 高于目标 12.0
- 第 9 章：
  - attr_adv_pct 17.6 高于目标 12.0
  - [observe] 标题重复：「签字笔划破」已存在
- 第 10 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「雪落协议展」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17884
chapter_chars_mean: 1788
chapter_chars_median: 1732
chapter_chars_cv: 0.14
paragraphs_mean: 41.1
dialogue_chars_pct: 49.1
dialogue_para_pct: 83.7
interiority_para_pct: 6.3
narration_para_pct: 9.9
turn_under20_pct: 74.5
turn_over200_pct: 0.0
attr_say_pct: 31.7
attr_adv_pct: 12.1
scenes_per_chapter: 1.8
dialogue_run_mean: 6.7
turn_len_median: 12
```
