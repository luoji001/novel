# 行李箱 生成报告

slug：`xuanyi-20261019-123`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14492
LLM 调用：68 次，累计 232.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 拖走箱子 | 1721 | short | 100.0 | 0 |  | 2 |
| 2 | 钥匙上的血迹 | 3570 | normal | 90.7 | 0 |  | 4 |
| 3 | 指纹触碰证件 | 4000 | normal | 89.9 | 0 |  | 2 |
| 4 | 翻阅笔记本 | 3432 | normal | 89.8 | 0 |  | 4 |
| 5 | 摩挲纸边 | 1764 | short | 92.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - narration_para_pct 9.4 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×5、「点了点头」×3
  - narration_para_pct 18.8 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「吴志远的心跳加快了几分…」）
  - [observe] attr_adv_pct 20.6 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×4、「陈美玲的」×3
  - narration_para_pct 7.5 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「南方电子厂」×17
  - narration_para_pct 5.4 低于目标 20.0
  - attr_adv_pct 19.4 高于目标 10.0
  - dialogue_run_mean 11 高于目标 10.0
- 第 5 章：
  - narration_para_pct 17.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13768
chapter_chars_mean: 2754
chapter_chars_median: 3271
chapter_chars_cv: 0.37
paragraphs_mean: 65.4
dialogue_chars_pct: 48.4
dialogue_para_pct: 81.4
interiority_para_pct: 7.4
narration_para_pct: 11.2
turn_under20_pct: 72.3
turn_over200_pct: 0.0
attr_say_pct: 30.0
attr_adv_pct: 11.8
scenes_per_chapter: 4.8
dialogue_run_mean: 7.2
turn_len_median: 12
```
