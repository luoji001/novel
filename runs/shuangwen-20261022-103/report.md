# 验收单 生成报告

slug：`shuangwen-20261022-103`
档位：爽文　闸门模式：observe
章数：10　总字数：19334
LLM 调用：97 次，累计 435.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字的背面秘密 | 1656 | normal | 100.0 | 0 |  | 0 |
| 2 | 验收单的缺失 | 2062 | normal | 93.4 | 0 |  | 2 |
| 3 | 签字表的对峙 | 1778 | normal | 94.4 | 0 |  | 0 |
| 4 | 手指划过合同副本 | 1644 | normal | 92.7 | 0 |  | 2 |
| 5 | 签字表飘落 | 2187 | normal | 93.7 | 0 |  | 1 |
| 6 | 签字表飘落 | 1761 | normal | 37.0 | 0 |  | 2 |
| 7 | 签字笔的温度升高 | 2044 | normal | 37.6 | 0 |  | 2 |
| 8 | 手指划过验收单 | 1722 | normal | 93.7 | 0 |  | 1 |
| 9 | 手指划过验收单 | 1858 | normal | 91.4 | 0 |  | 4 |
| 10 | 手指划过验收单 | 2612 | long | 37.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 3.2 低于目标 5.0
  - dialogue_run_mean 14.5 高于目标 14.0
- 第 4 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 16.5 高于目标 14.0
- 第 5 章：
  - attr_adv_pct 23.5 高于目标 12.0
- 第 6 章：
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字表飘落」已存在
- 第 7 章：
  - narration_para_pct 2.0 低于目标 5.0
  - [observe] attr_adv_pct 27.8 > 25.0（结构塌缩）
- 第 8 章：
  - attr_adv_pct 18.8 高于目标 12.0
- 第 9 章：
  - narration_para_pct 4.9 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - dialogue_run_mean 19.5 高于目标 14.0
  - [observe] 标题重复：「手指划过验收单」已存在
- 第 10 章：
  - 单条套路句式超限：「市卫生局」×4
  - [observe] attr_adv_pct 36.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「手指划过验收单」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18365
chapter_chars_mean: 1836
chapter_chars_median: 1730
chapter_chars_cv: 0.16
paragraphs_mean: 39.4
dialogue_chars_pct: 55.4
dialogue_para_pct: 87.5
interiority_para_pct: 2.6
narration_para_pct: 9.9
turn_under20_pct: 63.6
turn_over200_pct: 0.0
attr_say_pct: 24.3
attr_adv_pct: 20.0
scenes_per_chapter: 1.8
dialogue_run_mean: 9.6
turn_len_median: 14
```
