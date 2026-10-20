# 行李箱 生成报告

slug：`xuanyi-20261019-03`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14454
LLM 调用：68 次，累计 263.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙的齿痕 | 1485 | short | 100.0 | 0 |  | 2 |
| 2 | 箱子消失的秘密 | 3509 | normal | 92.0 | 0 |  | 3 |
| 3 | 箱子的踪迹 | 3886 | normal | 89.1 | 0 |  | 3 |
| 4 | 钥匙的齿痕 | 3385 | normal | 91.2 | 0 |  | 4 |
| 5 | 火车票的终点 | 2184 | short | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林志远站在」×3、「陈美玲的」×3
  - narration_para_pct 5.3 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈美玲的」×7、「林志远的」×4、「林志远站在」×3
  - narration_para_pct 5.9 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×6、「陈美玲的」×5、「林志远站在」×4
  - narration_para_pct 10.5 低于目标 20.0
  - attr_adv_pct 10.2 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「陈美玲的」×6、「”陈美玲轻」×4、「林志远站在」×3
  - narration_para_pct 7.4 低于目标 20.0
  - attr_adv_pct 15.6 高于目标 10.0
  - [observe] 标题重复：「钥匙的齿痕」已存在
- 第 5 章：
  - 单条套路句式超限：「“我不知道」×5、「林志远的」×3
  - narration_para_pct 6.5 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13669
chapter_chars_mean: 2734
chapter_chars_median: 3208
chapter_chars_cv: 0.35
paragraphs_mean: 71
dialogue_chars_pct: 49.5
dialogue_para_pct: 88.8
interiority_para_pct: 3.7
narration_para_pct: 7.5
turn_under20_pct: 84.8
turn_over200_pct: 0.0
attr_say_pct: 29.6
attr_adv_pct: 12.2
scenes_per_chapter: 5.4
dialogue_run_mean: 8.7
turn_len_median: 10
```
