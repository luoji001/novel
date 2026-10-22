# 旧卡 生成报告

slug：`shuangwen-20261022-39`
档位：爽文　闸门模式：observe
章数：10　总字数：18490
LLM 调用：97 次，累计 367.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 五枚银元的代价 | 1967 | normal | 98.6 | 0 |  | 0 |
| 2 | 一枚银戒的标识 | 1929 | normal | 94.1 | 0 |  | 1 |
| 3 | 旧借书卡的重逢 | 1878 | normal | 92.8 | 0 |  | 1 |
| 4 | 旧借书卡的重逢 | 1720 | normal | 92.6 | 0 |  | 4 |
| 5 | 旧借书卡的重逢 | 1765 | normal | 91.0 | 0 |  | 3 |
| 6 | 借书卡上的签名 | 1657 | normal | 91.9 | 0 |  | 2 |
| 7 | 旧借书卡的重逢 | 1681 | normal | 37.0 | 0 |  | 3 |
| 8 | 旧借书卡的重逢 | 1721 | normal | 93.6 | 0 |  | 3 |
| 9 | 铜钱换新卡 | 1865 | normal | 93.0 | 0 |  | 0 |
| 10 | 手指抚过烫金文字 | 2297 | long | 36.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 15.4 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「周怀远的」×3
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈文渊的」×4、「周怀远的」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「旧借书卡的重逢」已存在
- 第 5 章：
  - 单条套路句式超限：「周怀远的」×4
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「旧借书卡的重逢」已存在
- 第 6 章：
  - 单条套路句式超限：「周怀远的」×3
  - attr_adv_pct 15.4 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「沈文渊的」×4
  - [observe] attr_adv_pct 66.7 > 25.0（结构塌缩）
  - [observe] 标题重复：「旧借书卡的重逢」已存在
- 第 8 章：
  - 单条套路句式超限：「周怀远的」×3
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「旧借书卡的重逢」已存在
- 第 10 章：
  - narration_para_pct 4.4 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 章内自我复读 3 句（如「是那位老爷——他在后院摔了一跤，现在昏迷不醒！…」）

## 整书结构指标

```
chapters: 10
total_chars: 17569
chapter_chars_mean: 1757
chapter_chars_median: 1720
chapter_chars_cv: 0.1
paragraphs_mean: 38.1
dialogue_chars_pct: 45.9
dialogue_para_pct: 84.2
interiority_para_pct: 4.9
narration_para_pct: 10.9
turn_under20_pct: 61.8
turn_over200_pct: 0.0
attr_say_pct: 15.3
attr_adv_pct: 18.3
scenes_per_chapter: 1.7
dialogue_run_mean: 6.6
turn_len_median: 15
```
