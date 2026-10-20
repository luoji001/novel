# 水表停滞 生成报告

slug：`xuanyi-20261019-68`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15550
LLM 调用：68 次，累计 241.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表指针在转动 | 2084 | short | 73.0 | 0 |  | 2 |
| 2 | 水表指针在转动 | 3883 | normal | 85.4 | 0 |  | 4 |
| 3 | 水表指针在转动 | 3913 | normal | 89.3 | 0 |  | 4 |
| 4 | 手表指针停在三点 | 3729 | normal | 89.7 | 0 |  | 2 |
| 5 | 投诉单上的指纹 | 1936 | short | 93.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 13.2 低于目标 20.0
  - interiority_para_pct 31.0 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周美兰的」×3
  - dialogue_chars_pct 16.1 低于目标 20.0
  - interiority_para_pct 21.4 高于目标 20.0
  - [observe] 标题重复：「水表指针在转动」已存在
- 第 3 章：
  - 单条套路句式超限：「周美兰的」×5、「为什么会」×4
  - narration_para_pct 10.6 低于目标 20.0
  - attr_adv_pct 17.4 高于目标 10.0
  - [observe] 标题重复：「水表指针在转动」已存在
- 第 4 章：
  - 单条套路句式超限：「陈国强的」×3、「为什么会」×3
  - narration_para_pct 11.8 低于目标 20.0
- 第 5 章：
  - narration_para_pct 18.9 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14820
chapter_chars_mean: 2964
chapter_chars_median: 3543
chapter_chars_cv: 0.32
paragraphs_mean: 63
dialogue_chars_pct: 29.3
dialogue_para_pct: 64.7
interiority_para_pct: 16.7
narration_para_pct: 18.5
turn_under20_pct: 75.9
turn_over200_pct: 0.0
attr_say_pct: 21.6
attr_adv_pct: 6.0
scenes_per_chapter: 4.6
dialogue_run_mean: 3.5
turn_len_median: 13
```
