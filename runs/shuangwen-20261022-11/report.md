# 旧账本 生成报告

slug：`shuangwen-20261022-11`
档位：爽文　闸门模式：observe
章数：10　总字数：20757
LLM 调用：97 次，累计 392.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅旧账本 | 1721 | normal | 99.8 | 0 |  | 1 |
| 2 | 翻阅旧账本 | 2122 | normal | 90.8 | 0 |  | 2 |
| 3 | 翻阅账簿指玄机 | 2191 | normal | 93.0 | 0 |  | 0 |
| 4 | 翻阅账簿指玄机 | 2547 | normal | 91.4 | 0 |  | 2 |
| 5 | 翻阅旧账本寻真章 | 2326 | normal | 93.3 | 0 |  | 3 |
| 6 | 账本对敲桌 | 2104 | normal | 93.4 | 0 |  | 1 |
| 7 | 递账本 | 1981 | normal | 37.2 | 0 |  | 3 |
| 8 | 翻阅账簿指玄机 | 1651 | normal | 92.0 | 0 |  | 1 |
| 9 | 翻阅账簿指玄机 | 1902 | normal | 91.9 | 0 |  | 2 |
| 10 | 账本对敲桌 | 2202 | long | 36.8 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李修远的」×6
- 第 2 章：
  - 单条套路句式超限：「他知道自己」×4
  - [observe] 标题重复：「翻阅旧账本」已存在
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「翻阅账簿指玄机」已存在
- 第 5 章：
  - 单条套路句式超限：「李修远的」×3
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题与《翻阅旧账本》近似 0.77 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 命中套话收尾句
- 第 7 章：
  - 单条套路句式超限：「李修远的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - [observe] attr_adv_pct 27.8 > 25.0（结构塌缩）
- 第 8 章：
  - [observe] 标题重复：「翻阅账簿指玄机」已存在
- 第 9 章：
  - attr_adv_pct 23.5 高于目标 12.0
  - [observe] 标题重复：「翻阅账簿指玄机」已存在
- 第 10 章：
  - 单条套路句式超限：「李修远的」×5、「他知道这」×3
  - narration_para_pct 4.8 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「三天之后，我希望看到你的答案…」）
  - [observe] 标题重复：「账本对敲桌」已存在

## 整书结构指标

```
chapters: 10
total_chars: 19714
chapter_chars_mean: 1971
chapter_chars_median: 2018
chapter_chars_cv: 0.13
paragraphs_mean: 44.6
dialogue_chars_pct: 48.0
dialogue_para_pct: 82.4
interiority_para_pct: 7.3
narration_para_pct: 10.3
turn_under20_pct: 65.2
turn_over200_pct: 0.0
attr_say_pct: 17.7
attr_adv_pct: 12.2
scenes_per_chapter: 1.8
dialogue_run_mean: 6.6
turn_len_median: 14
```
