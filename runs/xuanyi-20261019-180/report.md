# 刷卡残影 生成报告

slug：`xuanyi-20261019-180`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14931
LLM 调用：68 次，累计 237.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 暗夜追踪者 | 2227 | short | 99.6 | 0 |  | 1 |
| 2 | 打卡机屏幕停顿 | 3881 | normal | 89.4 | 0 |  | 5 |
| 3 | 注销卡深夜现身 | 3575 | normal | 90.2 | 0 |  | 2 |
| 4 | 工牌边缘摩挲痕迹 | 3640 | normal | 90.2 | 0 |  | 3 |
| 5 | 系统日志停顿瞬间 | 1603 | short | 91.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周启明的」×4、「“我不知道」×3
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周启明的」×5、「“我不知道」×3、「为什么会」×3
  - narration_para_pct 9.5 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 章内自我复读 23 句（如「陈志远抬起头看向他，“如果没有更多的证据，恐怕很…」）
- 第 3 章：
  - 单条套路句式超限：「周启明的」×10、「“我不知道」×4、「为什么会」×4
  - narration_para_pct 2.8 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「他知道这」×4、「带着一丝」×3
  - narration_para_pct 6.8 低于目标 20.0
  - attr_adv_pct 15.0 高于目标 10.0
- 第 5 章：
  - narration_para_pct 9.7 低于目标 20.0
  - [observe] 章内自我复读 9 句（如「那你能不能告诉我，系统日志缺失的具体时间范围？…」）

## 整书结构指标

```
chapters: 5
total_chars: 14202
chapter_chars_mean: 2840
chapter_chars_median: 3416
chapter_chars_cv: 0.33
paragraphs_mean: 59.6
dialogue_chars_pct: 45.4
dialogue_para_pct: 81.2
interiority_para_pct: 8.9
narration_para_pct: 9.8
turn_under20_pct: 65.3
turn_over200_pct: 0.0
attr_say_pct: 8.9
attr_adv_pct: 9.5
scenes_per_chapter: 4.6
dialogue_run_mean: 5.7
turn_len_median: 13
```
