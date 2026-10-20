# 卡影 生成报告

slug：`xuanyi-20261019-20`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14347
LLM 调用：68 次，累计 235.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 指纹解锁的疑惑 | 1185 | short | 98.0 | 0 |  | 1 |
| 2 | 监控屏幕的蓝光 | 3472 | normal | 90.7 | 0 |  | 1 |
| 3 | 卡注销时间的矛盾 | 3698 | normal | 87.1 | 0 |  | 2 |
| 4 | 摩挲工牌边缘 | 4262 | normal | 87.4 | 0 |  | 3 |
| 5 | 便签纸上的日期 | 1725 | short | 91.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「林修远的」×3
- 第 3 章：
  - 单条套路句式超限：「周婉清的」×4
  - dialogue_chars_pct 19.6 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周婉清的」×6、「林修远的」×4、「他知道这」×3
  - attr_adv_pct 18.2 高于目标 10.0
  - [observe] 章内自我复读 14 句（如「李明的卡是在昨天下午三点注销的，可他最后一次进出…」）
- 第 5 章：
  - 单条套路句式超限：「周婉清的」×5、「林修远的」×3
  - narration_para_pct 17.5 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13727
chapter_chars_mean: 2745
chapter_chars_median: 3345
chapter_chars_cv: 0.47
paragraphs_mean: 54.4
dialogue_chars_pct: 24.4
dialogue_para_pct: 61.9
interiority_para_pct: 13.5
narration_para_pct: 24.7
turn_under20_pct: 72.4
turn_over200_pct: 0.0
attr_say_pct: 10.0
attr_adv_pct: 13.9
scenes_per_chapter: 3.6
dialogue_run_mean: 3.5
turn_len_median: 14
```
