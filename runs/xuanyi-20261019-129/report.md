# 药瓶上的签名 生成报告

slug：`xuanyi-20261019-129`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13837
LLM 调用：68 次，累计 242.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触摸1972年的药瓶 | 1434 | short | 57.4 | 0 |  | 3 |
| 2 | 触摸1972年的药瓶 | 3791 | normal | 90.8 | 0 |  | 5 |
| 3 | 登记簿上的陌生签名 | 3156 | normal | 92.2 | 0 |  | 3 |
| 4 | 触碰旧药瓶的指尖 | 3599 | normal | 88.4 | 0 |  | 4 |
| 5 | 触摸1972年的药瓶 | 1852 | short | 86.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林振邦的」×4
  - dialogue_chars_pct 14.1 低于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「陈素云的」×5、「”陈素云轻」×3、「陈素云点」×3
  - narration_para_pct 7.0 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「你最好别再碰那个药瓶…」）
  - [observe] attr_adv_pct 25.7 > 20.0（结构塌缩）
  - [observe] 标题重复：「触摸1972年的药瓶」已存在
- 第 3 章：
  - 单条套路句式超限：「林振邦的」×3
  - narration_para_pct 19.3 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「陈素云的」×7、「陈素云点」×3、「林振邦的」×3
  - narration_para_pct 4.2 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - dialogue_run_mean 13.4 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「他知道这」×5
  - [observe] 章内自我复读 17 句（如「早在几年前，他就见过几次张医生在药房账本上签字的…」）
  - [observe] 标题重复：「触摸1972年的药瓶」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13134
chapter_chars_mean: 2627
chapter_chars_median: 3025
chapter_chars_cv: 0.38
paragraphs_mean: 55.8
dialogue_chars_pct: 41.5
dialogue_para_pct: 78.2
interiority_para_pct: 6.9
narration_para_pct: 15.0
turn_under20_pct: 74.2
turn_over200_pct: 0.0
attr_say_pct: 33.3
attr_adv_pct: 14.0
scenes_per_chapter: 3.8
dialogue_run_mean: 6.4
turn_len_median: 12
```
