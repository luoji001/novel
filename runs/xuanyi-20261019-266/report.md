# 锈迹 生成报告

slug：`xuanyi-20261019-266`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14613
LLM 调用：68 次，累计 229.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙牌上的锈迹 | 1636 | short | 96.5 | 0 |  | 0 |
| 2 | 铁皮盒里的泛黄纸页 | 3779 | normal | 90.9 | 0 |  | 4 |
| 3 | 螺丝钉的微光 | 3806 | normal | 86.0 | 0 |  | 4 |
| 4 | 手电筒照亮值班表 | 3713 | normal | 82.4 | 0 |  | 2 |
| 5 | 锈迹蔓延的钥匙牌 | 1674 | short | 92.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×5、「中带着一丝」×3
  - narration_para_pct 10.1 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「我只是做了我能做的事情…」）
- 第 3 章：
  - 单条套路句式超限：「陈志远的」×8、「“我不知道」×4
  - narration_para_pct 16.0 低于目标 20.0
  - [observe] 章内自我复读 30 句（如「他想起前几天晚上，一个人拿着工具箱经过维修室时的…」）
  - [observe] attr_adv_pct 23.8 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「陈志远站在」×5、「他知道自己」×3
  - dialogue_chars_pct 15.1 低于目标 20.0
- 第 5 章：
  - narration_para_pct 6.7 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13910
chapter_chars_mean: 2782
chapter_chars_median: 3561
chapter_chars_cv: 0.4
paragraphs_mean: 62
dialogue_chars_pct: 31.2
dialogue_para_pct: 66.6
interiority_para_pct: 11.3
narration_para_pct: 22.0
turn_under20_pct: 81.6
turn_over200_pct: 0.0
attr_say_pct: 32.6
attr_adv_pct: 9.0
scenes_per_chapter: 3
dialogue_run_mean: 4.5
turn_len_median: 11
```
