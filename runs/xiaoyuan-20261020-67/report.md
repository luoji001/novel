# 磁带 生成报告

slug：`xiaoyuan-20261020-67`
档位：校园青春　闸门模式：observe
章数：9　总字数：21237
LLM 调用：100 次，累计 457.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙藏在书包夹层 | 1542 | short | 96.6 | 0 |  | 2 |
| 2 | 钥匙挂成琴弦 | 2796 | normal | 91.4 | 0 |  | 2 |
| 3 | 钥匙摩挲书包夹层 | 2419 | normal | 87.6 | 0 |  | 2 |
| 4 | 钥匙摩挲书包夹层 | 2281 | normal | 90.5 | 0 |  | 3 |
| 5 | 钥匙摩挲书包夹层 | 2590 | normal | 91.6 | 0 |  | 3 |
| 6 | 钥匙摩挲书包夹层 | 2362 | normal | 90.2 | 0 |  | 4 |
| 7 | 钥匙摩挲书包夹层 | 2860 | normal | 92.7 | 0 |  | 3 |
| 8 | 钥匙摩挲书包夹层 | 2695 | normal | 89.4 | 0 |  | 3 |
| 9 | 钥匙摩挲书包夹层 | 1683 | short | 89.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×4、「林小满站在」×3、「林小满的」×3
  - [observe] 章内自我复读 2 句（如「他知道，这一切都是因为他不能说出真相，就像他一直…」）
- 第 2 章：
  - 单条套路句式超限：「林小满的」×4、「“我不知道」×3
  - narration_para_pct 13.8 低于目标 15.0
- 第 3 章：
  - dialogue_chars_pct 16.9 低于目标 20.0
  - [observe] 标题与《钥匙藏在书包夹层》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「”苏远低」×3
  - narration_para_pct 11.1 低于目标 15.0
  - [observe] 标题重复：「钥匙摩挲书包夹层」已存在
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 11.3 低于目标 15.0
  - [observe] 标题重复：「钥匙摩挲书包夹层」已存在
- 第 6 章：
  - 单条套路句式超限：「林小满站在」×3
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 章内自我复读 5 句（如「他知道，苏远一直在躲避某些事情，但现在看来，那份…」）
  - [observe] 标题重复：「钥匙摩挲书包夹层」已存在
- 第 7 章：
  - 单条套路句式超限：「“我不知道」×3、「林小满的」×3
  - narration_para_pct 11.9 低于目标 15.0
  - [observe] 标题重复：「钥匙摩挲书包夹层」已存在
- 第 8 章：
  - 单条套路句式超限：「林小满的」×3
  - narration_para_pct 12.5 低于目标 15.0
  - [observe] 标题重复：「钥匙摩挲书包夹层」已存在
- 第 9 章：
  - 单条套路句式超限：「林小满的」×5
  - [observe] attr_adv_pct 50.0 > 22.0（结构塌缩）
  - [observe] 标题重复：「钥匙摩挲书包夹层」已存在

## 整书结构指标

```
chapters: 9
total_chars: 20180
chapter_chars_mean: 2242
chapter_chars_median: 2313
chapter_chars_cv: 0.2
paragraphs_mean: 50.3
dialogue_chars_pct: 25.1
dialogue_para_pct: 64.9
interiority_para_pct: 17.6
narration_para_pct: 17.6
turn_under20_pct: 84.2
turn_over200_pct: 0.0
attr_say_pct: 26.8
attr_adv_pct: 8.6
scenes_per_chapter: 2.8
dialogue_run_mean: 3.1
turn_len_median: 10
```
