# 药瓶 生成报告

slug：`xuanyi-20261019-149`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13923
LLM 调用：68 次，累计 226.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药瓶上的签名 | 1408 | short | 99.5 | 0 |  | 1 |
| 2 | 药瓶上的签名 | 3705 | normal | 92.3 | 0 |  | 6 |
| 3 | 账簿上的模糊签名 | 3756 | normal | 88.8 | 0 |  | 4 |
| 4 | 签字笔的低语 | 2954 | normal | 90.4 | 0 |  | 1 |
| 5 | 药瓶上的签名 | 2095 | short | 90.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 16.7 高于目标 10.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈素云点」×4
  - narration_para_pct 10.0 低于目标 20.0
  - attr_adv_pct 17.9 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「但我总觉得事情没那么简单…」）
  - [observe] 标题重复：「药瓶上的签名」已存在
- 第 3 章：
  - 单条套路句式超限：「陈素云的」×7、「林文远的」×7、「陈素云点了点头」×3
  - narration_para_pct 19.7 低于目标 20.0
  - [observe] 章内自我复读 6 句（如「在这间小小的药房里，两人默默地工作着，彼此之间虽…」）
  - [observe] attr_adv_pct 26.3 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
- 第 5 章：
  - 单条套路句式超限：「林文远的」×4、「陈素云的」×3
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 标题重复：「药瓶上的签名」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13142
chapter_chars_mean: 2628
chapter_chars_median: 2782
chapter_chars_cv: 0.38
paragraphs_mean: 62.8
dialogue_chars_pct: 35.7
dialogue_para_pct: 69.8
interiority_para_pct: 11.4
narration_para_pct: 18.8
turn_under20_pct: 82.6
turn_over200_pct: 0.0
attr_say_pct: 30.1
attr_adv_pct: 15.7
scenes_per_chapter: 3.4
dialogue_run_mean: 3.7
turn_len_median: 11
```
