# 报价单 生成报告

slug：`aiyuce-20261021-122`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12934
LLM 调用：57 次，累计 242.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对显卡库存 | 1991 | normal | 37.5 | 0 |  | 2 |
| 2 | 电费单显示稳定能耗 | 2481 | normal | 35.0 | 0 |  | 1 |
| 3 | 核对显卡库存 | 2505 | normal | 90.4 | 0 |  | 2 |
| 4 | 核对显卡库存 | 2544 | normal | 88.5 | 0 |  | 1 |
| 5 | 核对显卡库存 | 1968 | normal | 33.6 | 0 |  | 5 |
| 6 | 核对显卡库存 | 1439 | short | 34.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 3 句（如「他之前拿到的那份报价单如今看来似乎有些滞后，毕竟…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - 命中套话收尾句
  - [observe] 标题重复：「核对显卡库存」已存在
- 第 4 章：
  - [observe] 标题重复：「核对显卡库存」已存在
- 第 5 章：
  - dialogue_chars_pct 32.3 高于目标 18.0
  - dialogue_run_mean 4.7 高于目标 4.0
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「听说最近市场上这种显卡的价格又涨了不少…」）
  - [observe] 标题重复：「核对显卡库存」已存在
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对显卡库存」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12632
chapter_chars_mean: 2105
chapter_chars_median: 2186
chapter_chars_cv: 0.21
paragraphs_mean: 17.2
dialogue_chars_pct: 9.0
dialogue_para_pct: 23.8
interiority_para_pct: 12.1
narration_para_pct: 64.1
turn_under20_pct: 46.1
turn_over200_pct: 0.0
attr_say_pct: 2.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.2
turn_len_median: 22
```
