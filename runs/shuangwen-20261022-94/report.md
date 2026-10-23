# 账本 生成报告

slug：`shuangwen-20261022-94`
档位：爽文　闸门模式：observe
章数：10　总字数：18120
LLM 调用：97 次，累计 435.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 裂痕中的账本 | 1442 | normal | 100.0 | 0 |  | 1 |
| 2 | 墨迹与字迹的对峙 | 2037 | normal | 93.1 | 0 |  | 2 |
| 3 | 账本上的焦痕 | 1633 | normal | 93.9 | 0 |  | 0 |
| 4 | 递账本 | 1845 | normal | 92.3 | 0 |  | 1 |
| 5 | 翻阅账本寻父名 | 1651 | normal | 37.5 | 0 |  | 2 |
| 6 | 递账本 | 1794 | normal | 93.5 | 0 |  | 3 |
| 7 | 递账本 | 1492 | normal | 93.5 | 0 |  | 2 |
| 8 | 递账本 | 2138 | normal | 92.7 | 0 |  | 5 |
| 9 | 翻账本寻父踪 | 1815 | normal | 88.3 | 0 |  | 4 |
| 10 | 递账本 | 2263 | long | 37.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈守仁的」×5
- 第 2 章：
  - 单条套路句式超限：「林秋实的」×3
  - attr_adv_pct 20.8 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「陈守仁的」×6、「林秋实的」×3
- 第 5 章：
  - 单条套路句式超限：「林秋实的」×3
  - [observe] 章内自我复读 1 句（如「这上面有一个人的名字，但是我在账本里没看到…」）
- 第 6 章：
  - 单条套路句式超限：「陈守仁的」×5
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「递账本」已存在
- 第 7 章：
  - narration_para_pct 3.6 低于目标 5.0
  - [observe] 标题重复：「递账本」已存在
- 第 8 章：
  - 单条套路句式超限：「陈守仁的」×4
  - 情节与已写章节重复 0.71 ≥ 0.7（撞上「林秋实拿出祖父留下的账本，揭露家族秘密，引发陈守仁等人对…」）
  - narration_para_pct 2.6 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「递账本」已存在
- 第 9 章：
  - narration_para_pct 1.9 低于目标 5.0
  - attr_adv_pct 17.4 高于目标 12.0
  - dialogue_run_mean 25 高于目标 14.0
  - [observe] 标题与《翻阅账本寻父名》近似 0.77 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「陈守仁的」×7
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「递账本」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17186
chapter_chars_mean: 1719
chapter_chars_median: 1696
chapter_chars_cv: 0.15
paragraphs_mean: 39.8
dialogue_chars_pct: 50.9
dialogue_para_pct: 86.0
interiority_para_pct: 5.8
narration_para_pct: 8.2
turn_under20_pct: 69.4
turn_over200_pct: 0.0
attr_say_pct: 23.9
attr_adv_pct: 12.9
scenes_per_chapter: 1.6
dialogue_run_mean: 8.8
turn_len_median: 13
```
