# 旧账本 生成报告

slug：`shuangwen-20261022-131`
档位：爽文　闸门模式：observe
章数：10　总字数：21084
LLM 调用：97 次，累计 459.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本交接 | 1889 | normal | 99.5 | 0 |  | 0 |
| 2 | 朱砂印泥 | 1998 | normal | 92.5 | 0 |  | 0 |
| 3 | 令牌压账本 | 2042 | normal | 93.5 | 0 |  | 1 |
| 4 | 揉碎账页 | 2124 | normal | 91.6 | 0 |  | 0 |
| 5 | 令牌压账本 | 1952 | normal | 91.4 | 0 |  | 3 |
| 6 | 印章覆账本 | 2277 | normal | 37.5 | 0 |  | 2 |
| 7 | 撕碎账页 | 2245 | normal | 37.7 | 0 |  | 3 |
| 8 | 账本压令牌 | 2033 | normal | 92.0 | 0 |  | 2 |
| 9 | 令牌压账本 | 1807 | normal | 93.9 | 0 |  | 3 |
| 10 | 签字盖印 | 2707 | long | 94.0 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - 单条套路句式超限：「李文远的」×3
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李文远的」×5
  - [observe] 标题重复：「令牌压账本」已存在
- 第 6 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] attr_adv_pct 35.0 > 25.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「他知道这」×5、「李文远的」×3
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
  - [observe] 标题与《揉碎账页》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「李文远的」×3
  - attr_adv_pct 13.3 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「李文远的」×4
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「令牌压账本」已存在

## 整书结构指标

```
chapters: 10
total_chars: 20097
chapter_chars_mean: 2010
chapter_chars_median: 1946
chapter_chars_cv: 0.12
paragraphs_mean: 42.6
dialogue_chars_pct: 46.7
dialogue_para_pct: 77.8
interiority_para_pct: 7.3
narration_para_pct: 15.0
turn_under20_pct: 63.5
turn_over200_pct: 0.0
attr_say_pct: 19.8
attr_adv_pct: 13.9
scenes_per_chapter: 2
dialogue_run_mean: 5.8
turn_len_median: 16
```
