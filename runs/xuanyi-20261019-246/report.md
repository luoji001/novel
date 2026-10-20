# 钥牌 生成报告

slug：`xuanyi-20261019-246`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13920
LLM 调用：68 次，累计 215.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 擦拭门把手的疑云 | 1570 | short | 87.2 | 0 |  | 2 |
| 2 | 翻阅旧日志本 | 3771 | normal | 89.7 | 0 |  | 2 |
| 3 | 攥紧火车票的夜晚 | 3487 | normal | 80.5 | 0 |  | 4 |
| 4 | 揭开铁盒的秘密 | 3369 | normal | 90.3 | 0 |  | 4 |
| 5 | 摩挲钥匙牌刻痕 | 1718 | short | 90.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.2 低于目标 20.0
  - interiority_para_pct 24.1 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周文彬的」×7、「陈志远的」×6
  - attr_adv_pct 16.7 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3、「为什么会」×3
  - dialogue_chars_pct 16.9 低于目标 20.0
  - [observe] 章内自我复读 37 句（如「突然，他的目光落在一张旧报纸上，上面登载着一则新…」）
  - [observe] attr_adv_pct 23.5 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×4、「陈志远站在」×3
  - narration_para_pct 13.8 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「说完，他就离开了房间…」）
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「周文彬的」×4、「陈志远的」×4
  - attr_adv_pct 12.5 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13271
chapter_chars_mean: 2654
chapter_chars_median: 3194
chapter_chars_cv: 0.38
paragraphs_mean: 56.8
dialogue_chars_pct: 26.6
dialogue_para_pct: 61.9
interiority_para_pct: 15.4
narration_para_pct: 22.8
turn_under20_pct: 81.5
turn_over200_pct: 0.0
attr_say_pct: 24.4
attr_adv_pct: 17.3
scenes_per_chapter: 4.8
dialogue_run_mean: 3.6
turn_len_median: 13
```
