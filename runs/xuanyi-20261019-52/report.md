# 火车票 生成报告

slug：`xuanyi-20261019-52`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14937
LLM 调用：68 次，累计 236.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登录记录的谜题 | 1783 | short | 99.8 | 0 |  | 2 |
| 2 | 小蓝的登录记录 | 4379 | normal | 88.1 | 0 |  | 4 |
| 3 | 摩挲火车票边缘 | 3423 | normal | 89.9 | 0 |  | 3 |
| 4 | 摩挲机器外壳 | 3486 | normal | 91.8 | 0 |  | 2 |
| 5 | 摩挲火车票边缘 | 1861 | short | 89.7 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林秀兰的」×5
  - narration_para_pct 10.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林秀兰的」×5、「“我不知道」×4、「”林秀兰轻」×3
  - narration_para_pct 5.5 低于目标 20.0
  - attr_adv_pct 12.8 高于目标 10.0
  - dialogue_run_mean 12.4 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「陈志远的」×7、「林秀兰的」×5
  - narration_para_pct 13.2 低于目标 20.0
  - [observe] attr_adv_pct 21.7 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×4
  - narration_para_pct 14.3 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×5、「林秀兰的」×3
  - narration_para_pct 16.7 低于目标 20.0
  - [observe] attr_adv_pct 60.0 > 20.0（结构塌缩）
  - [observe] 标题重复：「摩挲火车票边缘」已存在

## 整书结构指标

```
chapters: 5
total_chars: 14170
chapter_chars_mean: 2834
chapter_chars_median: 3256
chapter_chars_cv: 0.38
paragraphs_mean: 68
dialogue_chars_pct: 44.6
dialogue_para_pct: 81.0
interiority_para_pct: 7.8
narration_para_pct: 11.3
turn_under20_pct: 80.5
turn_over200_pct: 0.0
attr_say_pct: 24.8
attr_adv_pct: 19.2
scenes_per_chapter: 3.4
dialogue_run_mean: 7.1
turn_len_median: 12
```
