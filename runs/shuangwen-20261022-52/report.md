# 令牌风云 生成报告

slug：`shuangwen-20261022-52`
档位：爽文　闸门模式：observe
章数：10　总字数：18972
LLM 调用：97 次，累计 451.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 令牌裂痕真相 | 2057 | normal | 98.8 | 0 |  | 2 |
| 2 | 令牌对峙 | 2628 | normal | 20.8 | 0 |  | 2 |
| 3 | 令牌对峙真相 | 1738 | normal | 94.6 | 0 |  | 3 |
| 4 | 登记簿裂痕真相 | 1953 | normal | 93.6 | 0 |  | 2 |
| 5 | 铜币交换令牌 | 1633 | normal | 93.8 | 0 |  | 1 |
| 6 | 铜牌显影术 | 1648 | normal | 88.2 | 0 |  | 3 |
| 7 | 令牌对峙真相 | 1932 | normal | 94.1 | 0 |  | 2 |
| 8 | 令牌交锋 | 1471 | normal | 91.6 | 0 |  | 1 |
| 9 | 契约现形 | 1711 | normal | 94.5 | 0 |  | 1 |
| 10 | 令牌换灵石 | 2191 | long | 92.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李文渊的」×3
  - attr_adv_pct 20.8 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「李文渊的」×3
  - [observe] 章内自我复读 2 句（如「你真的不需要我帮忙吗？…」）
- 第 3 章：
  - 单条套路句式超限：「李文渊的」×7
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题与《令牌对峙》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题与《令牌裂痕真相》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - attr_adv_pct 25.0 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「李文渊的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 31 高于目标 14.0
- 第 7 章：
  - attr_adv_pct 15.8 高于目标 12.0
  - [observe] 标题重复：「令牌对峙真相」已存在
- 第 8 章：
  - 单条套路句式超限：「藏书阁」×4
- 第 9 章：
  - 单条套路句式超限：「李文渊的」×5
- 第 10 章：
  - attr_adv_pct 25.0 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17789
chapter_chars_mean: 1779
chapter_chars_median: 1727
chapter_chars_cv: 0.16
paragraphs_mean: 52
dialogue_chars_pct: 51.2
dialogue_para_pct: 86.7
interiority_para_pct: 4.2
narration_para_pct: 9.1
turn_under20_pct: 82.5
turn_over200_pct: 0.0
attr_say_pct: 27.9
attr_adv_pct: 14.1
scenes_per_chapter: 1.6
dialogue_run_mean: 9.7
turn_len_median: 12
```
