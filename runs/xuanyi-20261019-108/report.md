# 水表走动 生成报告

slug：`xuanyi-20261019-108`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15489
LLM 调用：68 次，累计 239.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表转动 | 2020 | short | 97.5 | 0 |  | 3 |
| 2 | 查看电费单 | 4073 | normal | 89.2 | 0 |  | 2 |
| 3 | 电饭煲余温 | 3520 | normal | 55.0 | 0 |  | 3 |
| 4 | 水表仍在转动 | 3863 | normal | 79.8 | 0 |  | 2 |
| 5 | 电饭锅余温 | 2008 | short | 83.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周美兰的」×3
  - narration_para_pct 8.9 低于目标 20.0
  - [observe] attr_adv_pct 26.7 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周美兰的」×4
  - attr_adv_pct 10.5 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「中带着一丝」×4
  - dialogue_chars_pct 13.7 低于目标 20.0
  - interiority_para_pct 24.1 高于目标 20.0
- 第 4 章：
  - [observe] 章内自我复读 41 句（如「水表还在走，电费单上的数字还在变，就像那串始终不…」）
  - [observe] 标题与《水表转动》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章内自我复读 17 句（如「桌面上那个旧电饭锅正在发出咕嘟咕嘟的声音，看起来…」）
  - [observe] 标题与《电饭煲余温》近似 0.80 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 14818
chapter_chars_mean: 2964
chapter_chars_median: 3399
chapter_chars_cv: 0.33
paragraphs_mean: 60
dialogue_chars_pct: 28.7
dialogue_para_pct: 56.0
interiority_para_pct: 15.6
narration_para_pct: 28.4
turn_under20_pct: 70.6
turn_over200_pct: 0.0
attr_say_pct: 20.4
attr_adv_pct: 6.2
scenes_per_chapter: 5.2
dialogue_run_mean: 3.7
turn_len_median: 13
```
