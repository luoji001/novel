# 签名瓶 生成报告

slug：`xuanyi-20261019-229`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15026
LLM 调用：68 次，累计 239.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 玻璃瓶里的二十粒药 | 1870 | short | 97.6 | 0 |  | 3 |
| 2 | 登记簿的消失痕迹 | 3840 | normal | 92.1 | 0 |  | 1 |
| 3 | 处方单上的陌生名字 | 3509 | normal | 86.2 | 0 |  | 4 |
| 4 | 钢笔的磨损处 | 3486 | normal | 91.3 | 0 |  | 3 |
| 5 | 怀表与处方单相遇 | 2316 | short | 80.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林素云的」×3
  - narration_para_pct 5.6 低于目标 20.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周启明的」×3
- 第 3 章：
  - 单条套路句式超限：「林素云的」×4
  - narration_para_pct 19.0 低于目标 20.0
  - [observe] 章内自我复读 21 句（如「她记得那天，整个医院都在忙，好像是某个重要的会议…」）
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「周启明的」×9、「林素云的」×8、「“我不知道」×3
  - narration_para_pct 9.5 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「林素云的心跳加快了几分…」）
- 第 5 章：
  - dialogue_chars_pct 15.9 低于目标 20.0
  - interiority_para_pct 22.5 高于目标 20.0
  - [observe] 章内自我复读 16 句（如「虽然她知道这样做可能会引起某些人的不满，但对于真…」）

## 整书结构指标

```
chapters: 5
total_chars: 14376
chapter_chars_mean: 2875
chapter_chars_median: 3304
chapter_chars_cv: 0.29
paragraphs_mean: 56.6
dialogue_chars_pct: 29.6
dialogue_para_pct: 69.2
interiority_para_pct: 12.9
narration_para_pct: 17.9
turn_under20_pct: 80.3
turn_over200_pct: 0.0
attr_say_pct: 38.0
attr_adv_pct: 13.6
scenes_per_chapter: 4.8
dialogue_run_mean: 3.8
turn_len_median: 11
```
