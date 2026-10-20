# 药瓶指纹 生成报告

slug：`xuanyi-20261019-29`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14327
LLM 调用：68 次，累计 235.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药瓶上的名字 | 1583 | short | 98.0 | 0 |  | 2 |
| 2 | 药瓶上的名字 | 3931 | normal | 87.6 | 0 |  | 4 |
| 3 | 墨水与药瓶的相遇 | 3489 | normal | 90.9 | 0 |  | 3 |
| 4 | 钥匙转动的瞬间 | 3575 | normal | 87.8 | 0 |  | 2 |
| 5 | 指纹揭开的纸片 | 1744 | short | 65.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈文远的」×3
  - [observe] attr_adv_pct 66.7 > 20.0（结构塌缩）
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林素云的」×5、「他知道这」×3
  - [observe] 章内自我复读 27 句（如「每颗算珠都对应一种药物的存量，比如阿司匹林、黄连…」）
  - [observe] 标题重复：「药瓶上的名字」已存在
- 第 3 章：
  - 单条套路句式超限：「林素云的」×4、「陈文远站在」×3
  - narration_para_pct 19.0 低于目标 20.0
  - [observe] 章内自我复读 12 句（如「那是三天前被陈文远从药品架上取下来的，当时他正在…」）
- 第 4 章：
  - 单条套路句式超限：「陈文远的」×4
  - [observe] 章内自我复读 18 句（如「这把钥匙能打开这里的所有柜子，但唯独打不开那本登…」）
- 第 5 章：
  - dialogue_chars_pct 3.8 低于目标 20.0
  - interiority_para_pct 22.7 高于目标 20.0
  - dialogue_run_mean 1 低于目标 1.5

## 整书结构指标

```
chapters: 5
total_chars: 13697
chapter_chars_mean: 2739
chapter_chars_median: 3315
chapter_chars_cv: 0.39
paragraphs_mean: 55.2
dialogue_chars_pct: 25.2
dialogue_para_pct: 61.1
interiority_para_pct: 10.7
narration_para_pct: 28.2
turn_under20_pct: 85.6
turn_over200_pct: 0.0
attr_say_pct: 35.7
attr_adv_pct: 8.4
scenes_per_chapter: 3
dialogue_run_mean: 3.0
turn_len_median: 10
```
