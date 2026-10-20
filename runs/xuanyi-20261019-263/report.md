# 行李箱标签 生成报告

slug：`xuanyi-20261019-263`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15183
LLM 调用：68 次，累计 249.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 箱子消失的夜晚 | 2153 | short | 93.4 | 0 |  | 4 |
| 2 | 铁皮柜锁舌卡住 | 3687 | normal | 90.5 | 0 |  | 3 |
| 3 | 箱子消失的夜晚 | 3788 | normal | 85.2 | 0 |  | 4 |
| 4 | 烟灰落在桌面 | 3617 | normal | 90.7 | 0 |  | 2 |
| 5 | 火车票上的站名 | 1933 | short | 88.3 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3、「林振华的」×3
  - interiority_para_pct 21.7 高于目标 20.0
  - narration_para_pct 15.2 低于目标 20.0
  - [observe] 章内自我复读 7 句（如「陈志远耸了耸肩，“不过我记得那个人好像有点像我们…」）
- 第 2 章：
  - 单条套路句式超限：「林振华的」×8、「林振华点」×3
  - narration_para_pct 8.0 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「他知道，按照规定，每晚都要登记巡视情况，可现在的…」）
- 第 3 章：
  - 单条套路句式超限：「苏婉如的」×14、「林振华的」×5、「“我不知道」×4
  - narration_para_pct 16.5 低于目标 20.0
  - [observe] 章内自我复读 26 句（如「他一直以为苏婉如是个冷漠的人，但现在看来，她似乎…」）
  - [observe] 标题重复：「箱子消失的夜晚」已存在
- 第 4 章：
  - 单条套路句式超限：「林振华站在」×3
  - [observe] 章内自我复读 1 句（如「你不觉得这些香烟有点奇怪吗？…」）
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 16.7 低于目标 20.0
  - [observe] 章内自我复读 20 句（如「壶身上印着工厂的标志，他忽然想起上周夜里巡逻时，…」）
  - [observe] attr_adv_pct 40.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 14398
chapter_chars_mean: 2880
chapter_chars_median: 3429
chapter_chars_cv: 0.3
paragraphs_mean: 70.6
dialogue_chars_pct: 32.9
dialogue_para_pct: 73.7
interiority_para_pct: 10.2
narration_para_pct: 16.1
turn_under20_pct: 87.2
turn_over200_pct: 0.0
attr_say_pct: 21.2
attr_adv_pct: 8.5
scenes_per_chapter: 6.6
dialogue_run_mean: 4.1
turn_len_median: 10
```
