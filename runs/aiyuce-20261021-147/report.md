# 屏显 生成报告

slug：`aiyuce-20261021-147`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11838
LLM 调用：57 次，累计 217.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲统计表边缘 | 1684 | normal | 97.0 | 0 |  | 1 |
| 2 | 查看统计数据 | 2769 | normal | 34.3 | 0 |  | 4 |
| 3 | 摩挲统计表边缘 | 2241 | normal | 89.5 | 0 |  | 1 |
| 4 | 翻看维护费用清单 | 1748 | normal | 80.4 | 0 |  | 3 |
| 5 | 摩挲统计表边缘 | 2150 | normal | 90.5 | 0 |  | 1 |
| 6 | 摩挲统计表边缘 | 1240 | short | 90.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 20.0 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 67.7 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 12.2 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「主任接过纸条，心中已经有了主意…」）
- 第 3 章：
  - [observe] 标题重复：「摩挲统计表边缘」已存在
- 第 4 章：
  - dialogue_chars_pct 79.6 高于目标 18.0
  - dialogue_run_mean 21 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
- 第 5 章：
  - [observe] 标题重复：「摩挲统计表边缘」已存在
- 第 6 章：
  - narration_para_pct 18.2 低于目标 45.0
  - [observe] 标题重复：「摩挲统计表边缘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11474
chapter_chars_mean: 1912
chapter_chars_median: 1896
chapter_chars_cv: 0.26
paragraphs_mean: 20
dialogue_chars_pct: 30.2
dialogue_para_pct: 57.0
interiority_para_pct: 13.3
narration_para_pct: 29.7
turn_under20_pct: 71.9
turn_over200_pct: 0.0
attr_say_pct: 16.6
attr_adv_pct: 6.8
scenes_per_chapter: 1.2
dialogue_run_mean: 5.8
turn_len_median: 12
```
