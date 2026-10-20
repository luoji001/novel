# 钥匙牌 生成报告

slug：`xuanyi-20261019-66`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14951
LLM 调用：68 次，累计 232.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙牌的刻痕 | 1932 | short | 99.8 | 0 |  | 2 |
| 2 | 账本上的神秘数字 | 3779 | normal | 91.6 | 0 |  | 4 |
| 3 | 钥匙牌的异常日期 | 4131 | normal | 85.1 | 0 |  | 4 |
| 4 | 铁盒中的陌生车票 | 3284 | normal | 91.6 | 0 |  | 3 |
| 5 | 抚摸钥匙牌的凹凸 | 1820 | short | 92.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周振邦的」×4
  - narration_para_pct 12.1 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周振邦的」×9、「陈素云的」×4、「点了点头」×3
  - narration_para_pct 15.2 低于目标 20.0
  - attr_adv_pct 13.3 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「周振邦走近几步，目光落在账本上…」）
- 第 3 章：
  - 单条套路句式超限：「周振邦的」×4、「周振邦站在」×3、「陈素云的」×3
  - interiority_para_pct 21.6 高于目标 20.0
  - narration_para_pct 10.8 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「储物室不大，里面堆满了各种旧物，有些是行李箱、床…」）
- 第 4 章：
  - 单条套路句式超限：「你是谁？」×3
  - narration_para_pct 18.8 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「你怎么知道我会在这里？…」）
- 第 5 章：
  - narration_para_pct 11.4 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14315
chapter_chars_mean: 2863
chapter_chars_median: 3130
chapter_chars_cv: 0.36
paragraphs_mean: 55.4
dialogue_chars_pct: 35.6
dialogue_para_pct: 72.6
interiority_para_pct: 13.5
narration_para_pct: 13.9
turn_under20_pct: 75.5
turn_over200_pct: 0.0
attr_say_pct: 43.2
attr_adv_pct: 8.5
scenes_per_chapter: 4.4
dialogue_run_mean: 4.6
turn_len_median: 13
```
