# 法器凭据 生成报告

slug：`shuangwen-20261022-55`
档位：爽文　闸门模式：observe
章数：10　总字数：18931
LLM 调用：97 次，累计 462.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 煤油灯下的旧账本 | 1701 | normal | 39.4 | 0 |  | 4 |
| 2 | 签字权的较量 | 1568 | normal | 94.6 | 0 |  | 1 |
| 3 | 法器凭据的指纹 | 1865 | normal | 94.4 | 0 |  | 1 |
| 4 | 法器凭据的指纹 | 1954 | normal | 93.0 | 0 |  | 2 |
| 5 | 掀账本见裂痕 | 1724 | normal | 94.7 | 0 |  | 1 |
| 6 | 铜牌与旧名册 | 1992 | normal | 94.2 | 0 |  | 2 |
| 7 | 掀账本见裂痕 | 1931 | normal | 93.9 | 0 |  | 3 |
| 8 | 揭桌下残凭一角 | 1689 | normal | 91.4 | 0 |  | 1 |
| 9 | 账本上的笔尖颤动 | 1994 | normal | 92.1 | 0 |  | 2 |
| 10 | 掀账本见裂痕 | 2503 | long | 37.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王掌柜的」×8
  - narration_para_pct 3.0 低于目标 5.0
  - dialogue_run_mean 15.5 高于目标 14.0
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「王掌柜的」×7
- 第 3 章：
  - 单条套路句式超限：「王掌柜的」×4、「验货台」×3
- 第 4 章：
  - 单条套路句式超限：「王掌柜的」×9
  - [observe] 标题重复：「法器凭据的指纹」已存在
- 第 5 章：
  - 单条套路句式超限：「王掌柜的」×3
- 第 6 章：
  - 单条套路句式超限：「王掌柜的」×4
  - attr_adv_pct 20.0 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「王掌柜的」×5、「李长生的」×3
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「掀账本见裂痕」已存在
- 第 8 章：
  - 单条套路句式超限：「王掌柜的」×3
- 第 9 章：
  - 单条套路句式超限：「王掌柜的」×3
  - attr_adv_pct 12.1 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「王掌柜的」×6
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「掀账本见裂痕」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17942
chapter_chars_mean: 1794
chapter_chars_median: 1804
chapter_chars_cv: 0.14
paragraphs_mean: 41.6
dialogue_chars_pct: 47.0
dialogue_para_pct: 82.5
interiority_para_pct: 4.4
narration_para_pct: 13.0
turn_under20_pct: 71.9
turn_over200_pct: 0.0
attr_say_pct: 22.9
attr_adv_pct: 13.2
scenes_per_chapter: 1.5
dialogue_run_mean: 7.1
turn_len_median: 13
```
