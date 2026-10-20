# 火车票 生成报告

slug：`xuanyi-20261019-152`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15588
LLM 调用：68 次，累计 235.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的涂改痕迹 | 2009 | short | 99.6 | 0 |  | 1 |
| 2 | 纸片上的陌生名字 | 4412 | normal | 88.3 | 0 |  | 5 |
| 3 | 摩挲火车票边缘 | 3789 | normal | 89.3 | 0 |  | 3 |
| 4 | 摩挲登记本边缘 | 3285 | normal | 90.0 | 0 |  | 2 |
| 5 | 摩挲纸张边缘 | 2088 | short | 90.4 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×7、「陈雪梅的」×6、「”陈雪梅低」×4
  - dialogue_chars_pct 59.6 高于目标 58.0
  - narration_para_pct 7.6 低于目标 20.0
  - dialogue_run_mean 10.6 高于目标 10.0
  - [observe] 章内自我复读 26 句（如「是网吧老板让我保存的，他说万一有什么事，可以用来…」）
- 第 3 章：
  - 单条套路句式超限：「林志远的」×12、「“我不知道」×4、「林志远站在」×3
  - narration_para_pct 18.5 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「林志远的心跳又加快了几分…」）
- 第 4 章：
  - 单条套路句式超限：「林志远的」×3
  - narration_para_pct 16.1 低于目标 20.0
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林志远站在」×3
  - dialogue_chars_pct 17.8 低于目标 20.0
  - [observe] 标题与《摩挲登记本边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 14771
chapter_chars_mean: 2954
chapter_chars_median: 3146
chapter_chars_cv: 0.34
paragraphs_mean: 73.6
dialogue_chars_pct: 38.9
dialogue_para_pct: 75.0
interiority_para_pct: 6.7
narration_para_pct: 18.3
turn_under20_pct: 79.2
turn_over200_pct: 0.0
attr_say_pct: 17.5
attr_adv_pct: 7.4
scenes_per_chapter: 2.8
dialogue_run_mean: 5.4
turn_len_median: 12
```
