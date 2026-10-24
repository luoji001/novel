# 旧伤 生成报告

slug：`shuangwen-20261023-64`
档位：爽文　闸门模式：observe
章数：10　总字数：19140
LLM 调用：97 次，累计 451.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触碰疤痕的指尖 | 1813 | normal | 98.4 | 0 |  | 2 |
| 2 | 抚摸疤痕的手指 | 1928 | normal | 94.3 | 0 |  | 1 |
| 3 | 签字笔的刻痕 | 1849 | normal | 36.7 | 0 |  | 2 |
| 4 | 玉牌对账簿 | 2097 | normal | 94.6 | 0 |  | 0 |
| 5 | 玉牌对疤痕 | 1962 | normal | 88.3 | 0 |  | 4 |
| 6 | 账簿与旧伤的对话 | 1919 | normal | 37.5 | 0 |  | 1 |
| 7 | 玉牌对疤痕 | 2170 | normal | 91.6 | 0 |  | 4 |
| 8 | 钥匙与符咒的交锋 | 1548 | normal | 35.5 | 0 |  | 2 |
| 9 | 碎瓷片映月光 | 1612 | normal | 96.0 | 0 |  | 0 |
| 10 | 签字笔的刻痕 | 2232 | long | 93.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈长老的」×6
  - attr_adv_pct 25.0 高于目标 12.0
- 第 2 章：
  - dialogue_run_mean 14.7 高于目标 14.0
- 第 3 章：
  - 单条套路句式超限：「知道自己」×3
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「陈长老的」×6
  - narration_para_pct 2.6 低于目标 5.0
  - dialogue_run_mean 37 高于目标 14.0
  - [observe] 标题与《玉牌对账簿》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈长老的」×6
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「玉牌对疤痕」已存在
- 第 8 章：
  - dialogue_run_mean 28 高于目标 14.0
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 10 章：
  - [observe] 标题重复：「签字笔的刻痕」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18045
chapter_chars_mean: 1804
chapter_chars_median: 1785
chapter_chars_cv: 0.11
paragraphs_mean: 47.1
dialogue_chars_pct: 51.0
dialogue_para_pct: 83.6
interiority_para_pct: 4.7
narration_para_pct: 11.7
turn_under20_pct: 74.9
turn_over200_pct: 0.0
attr_say_pct: 28.4
attr_adv_pct: 15.7
scenes_per_chapter: 2.5
dialogue_run_mean: 12.3
turn_len_median: 12
```
