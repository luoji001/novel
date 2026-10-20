# log-01 生成报告

档位：纯文学　闸门模式：observe
章数：4　总字数：5646
LLM 调用：26 次，累计 75.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 报纸上的裂痕 | 997 | short | 51.6 | 0 |  | 2 |
| 2 | 账本上的日期不符 | 1858 | normal | 0.0 | 0 |  | 3 |
| 3 | 钢笔与笔记本的对峙 | 1814 | normal | 56.8 | 0 |  | 1 |
| 4 | 旧书的泛黄痕迹 | 973 | short | 75.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 3.1 低于目标 8.0
  - interiority_para_pct 40.0 高于目标 32.0
- 第 2 章：
  - narration_para_pct 21.9 低于目标 30.0
  - [observe] 章内自我复读 18 句（如「周永生摇了摇头，“不过我知道有很多人会来卖书，有…」）
  - [observe] attr_adv_pct 22.2 > 22.0（结构塌缩）
- 第 3 章：
  - narration_para_pct 5.9 低于目标 30.0
- 第 4 章：
  - narration_para_pct 0.0 低于目标 30.0

## 整书结构指标

```
chapters: 4
total_chars: 5380
chapter_chars_mean: 1345
chapter_chars_median: 1338
chapter_chars_cv: 0.34
paragraphs_mean: 23
dialogue_chars_pct: 29.0
dialogue_para_pct: 64.0
interiority_para_pct: 21.5
narration_para_pct: 14.5
turn_under20_pct: 66.7
turn_over200_pct: 0.0
attr_say_pct: 39.4
attr_adv_pct: 10.2
scenes_per_chapter: 1.8
dialogue_run_mean: 3.9
turn_len_median: 12
```
