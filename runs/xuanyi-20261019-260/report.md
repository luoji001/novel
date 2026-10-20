# 注销卡 生成报告

slug：`xuanyi-20261019-260`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14913
LLM 调用：68 次，累计 240.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 异常刷卡时间点 | 1784 | short | 98.2 | 0 |  | 1 |
| 2 | 撕裂的门锁记录表 | 4126 | normal | 81.0 | 0 |  | 4 |
| 3 | 系统漏洞被发现 | 3181 | normal | 90.8 | 0 |  | 4 |
| 4 | 电话响起时的凝滞空气 | 3879 | normal | 89.3 | 0 |  | 2 |
| 5 | 绿萝叶片的触感 | 1938 | short | 93.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「他知道这」×4、「不仅仅是」×3、「沈婉如的」×3
  - dialogue_chars_pct 14.9 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「突然，他注意到一个微小的细节——在那个身影进入办…」）
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「沈婉如的」×4、「”沈婉如轻」×3、「带着一丝」×3
  - narration_para_pct 9.8 低于目标 20.0
  - [observe] 章内自我复读 5 句（如「她转身走向工作台，“如果你真想知道答案，或许应该…」）
  - [observe] attr_adv_pct 21.4 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「林振东的」×6
  - narration_para_pct 19.7 低于目标 20.0
- 第 5 章：
  - narration_para_pct 9.5 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14299
chapter_chars_mean: 2860
chapter_chars_median: 3044
chapter_chars_cv: 0.37
paragraphs_mean: 53
dialogue_chars_pct: 32.1
dialogue_para_pct: 64.3
interiority_para_pct: 14.3
narration_para_pct: 21.3
turn_under20_pct: 67.4
turn_over200_pct: 0.0
attr_say_pct: 22.3
attr_adv_pct: 15.0
scenes_per_chapter: 3
dialogue_run_mean: 3.6
turn_len_median: 14
```
