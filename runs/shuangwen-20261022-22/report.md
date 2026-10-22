# 库存清单 生成报告

slug：`shuangwen-20261022-22`
档位：爽文　闸门模式：observe
章数：10　总字数：21010
LLM 调用：97 次，累计 358.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字时刻 | 2176 | normal | 100.0 | 0 |  | 2 |
| 2 | 摩挲袖口 | 2627 | normal | 93.0 | 0 |  | 4 |
| 3 | 摩挲笔帽 | 1944 | normal | 93.5 | 0 |  | 0 |
| 4 | 摩挲纸张 | 1927 | normal | 93.9 | 0 |  | 1 |
| 5 | 摩挲账本 | 1862 | normal | 93.9 | 0 |  | 1 |
| 6 | 摩挲笔杆 | 1780 | normal | 91.7 | 0 |  | 1 |
| 7 | 摩挲库存清单 | 1928 | normal | 92.4 | 0 |  | 3 |
| 8 | 摩挲合同纸张 | 2165 | normal | 93.0 | 0 |  | 3 |
| 9 | 摩挲账本 | 2094 | normal | 93.9 | 0 |  | 2 |
| 10 | 签字笔的重量 | 2497 | long | 37.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李振国的」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 2 章：
  - 命中套话收尾句
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 13.6 高于目标 12.0
  - dialogue_run_mean 16.3 高于目标 14.0
- 第 4 章：
  - attr_adv_pct 12.5 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「为什么会」×3
- 第 6 章：
  - [observe] 标题与《摩挲笔帽》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 21.4 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「李振国的」×4
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题与《摩挲纸张》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「李振国的」×3
  - [observe] 标题重复：「摩挲账本」已存在
- 第 10 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 章内自我复读 6 句（如「周晓芸的目光在这张泛黄的纸页上游移，仿佛能看到某…」）

## 整书结构指标

```
chapters: 10
total_chars: 20029
chapter_chars_mean: 2003
chapter_chars_median: 1924
chapter_chars_cv: 0.13
paragraphs_mean: 42.2
dialogue_chars_pct: 52.7
dialogue_para_pct: 82.1
interiority_para_pct: 8.4
narration_para_pct: 9.5
turn_under20_pct: 58.6
turn_over200_pct: 0.0
attr_say_pct: 24.9
attr_adv_pct: 11.1
scenes_per_chapter: 1.7
dialogue_run_mean: 6.8
turn_len_median: 16
```
