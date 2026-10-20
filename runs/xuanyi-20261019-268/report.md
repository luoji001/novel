# 水表 生成报告

slug：`xuanyi-20261019-268`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15348
LLM 调用：68 次，累计 244.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表持续增长 | 1751 | short | 98.1 | 0 |  | 2 |
| 2 | 签合同的手指 | 4008 | normal | 90.3 | 0 |  | 3 |
| 3 | 纸箱里的人名 | 3875 | normal | 88.8 | 0 |  | 3 |
| 4 | 水表持续增长 | 3402 | normal | 86.3 | 0 |  | 6 |
| 5 | 木椅上的干树叶 | 2307 | short | 90.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 17.1 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「”陈玉兰轻」×4、「”陈玉兰低」×4、「陈玉兰的」×4
  - narration_para_pct 6.4 低于目标 20.0
  - attr_adv_pct 14.6 高于目标 10.0
- 第 3 章：
  - interiority_para_pct 21.7 高于目标 20.0
  - narration_para_pct 4.3 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「就在这时」×3
  - dialogue_chars_pct 58.6 高于目标 58.0
  - narration_para_pct 10.2 低于目标 20.0
  - attr_adv_pct 11.8 高于目标 10.0
  - [observe] 章内自我复读 20 句（如「目前来看，没有任何迹象表明这个水表存在故障或者被…」）
  - [observe] 标题重复：「水表持续增长」已存在
- 第 5 章：
  - 单条套路句式超限：「他知道这」×5
  - narration_para_pct 2.0 低于目标 20.0
  - [observe] 章内自我复读 10 句（如「好像有个人，名字叫王志远，以前住在隔壁那间房里。…」）

## 整书结构指标

```
chapters: 5
total_chars: 14622
chapter_chars_mean: 2924
chapter_chars_median: 3269
chapter_chars_cv: 0.32
paragraphs_mean: 64.6
dialogue_chars_pct: 47.0
dialogue_para_pct: 82.5
interiority_para_pct: 10.2
narration_para_pct: 7.3
turn_under20_pct: 69.7
turn_over200_pct: 0.0
attr_say_pct: 23.9
attr_adv_pct: 13.3
scenes_per_chapter: 3
dialogue_run_mean: 6.3
turn_len_median: 13
```
