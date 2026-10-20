# 锁片 生成报告

slug：`xuanyi-20261019-126`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13679
LLM 调用：68 次，累计 220.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙牌的刻痕 | 1577 | short | 100.0 | 0 |  | 1 |
| 2 | 查看值班表记录 | 3886 | normal | 90.7 | 0 |  | 3 |
| 3 | 撬开铁皮柜门 | 3167 | normal | 91.6 | 0 |  | 2 |
| 4 | 翻阅黑色记事本 | 3199 | normal | 91.5 | 0 |  | 2 |
| 5 | 触摸墙面金属片 | 1845 | short | 47.1 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 17.6 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周慧兰的」×8、「陈志远的」×6、「三楼走廊尽头」×4
  - narration_para_pct 10.1 低于目标 20.0
  - attr_adv_pct 12.9 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×4
  - narration_para_pct 18.3 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周慧兰的」×4、「陈志远站在」×3、「陈志远的」×3
  - narration_para_pct 11.1 低于目标 20.0
- 第 5 章：
  - dialogue_chars_pct 5.8 低于目标 20.0
  - interiority_para_pct 32.3 高于目标 20.0
  - dialogue_run_mean 1 低于目标 1.5
  - [observe] 章内自我复读 11 句（如「回到值班室，他翻出那个破旧的记事本，仔细对照之前…」）

## 整书结构指标

```
chapters: 5
total_chars: 13045
chapter_chars_mean: 2609
chapter_chars_median: 3011
chapter_chars_cv: 0.36
paragraphs_mean: 55.6
dialogue_chars_pct: 33.8
dialogue_para_pct: 71.8
interiority_para_pct: 10.3
narration_para_pct: 17.8
turn_under20_pct: 81.1
turn_over200_pct: 0.0
attr_say_pct: 38.6
attr_adv_pct: 3.7
scenes_per_chapter: 3.6
dialogue_run_mean: 4.9
turn_len_median: 10
```
