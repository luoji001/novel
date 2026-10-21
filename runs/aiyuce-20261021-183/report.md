# 初筛机 生成报告

slug：`aiyuce-20261021-183`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13163
LLM 调用：57 次，累计 227.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲绩效考核表边缘 | 2401 | normal | 38.6 | 0 |  | 1 |
| 2 | 翻阅运行日志 | 2174 | normal | 35.9 | 0 |  | 2 |
| 3 | 翻阅投入产出比报告 | 2469 | normal | 35.1 | 0 |  | 1 |
| 4 | 翻阅岗位招聘信息 | 2572 | normal | 35.5 | 0 |  | 3 |
| 5 | 摩挲绩效考核表边缘 | 2075 | normal | 90.4 | 0 |  | 1 |
| 6 | 摩挲文件夹标签 | 1466 | short | 85.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「他知道，自己虽然在这个领域摸爬滚打了这么多年，但…」）
- 第 2 章：
  - dialogue_chars_pct 20.6 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 20.6 高于目标 18.0
  - narration_para_pct 43.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 标题重复：「摩挲绩效考核表边缘」已存在
- 第 6 章：
  - dialogue_chars_pct 35.0 高于目标 18.0
  - narration_para_pct 16.7 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 12857
chapter_chars_mean: 2143
chapter_chars_median: 2241
chapter_chars_cv: 0.18
paragraphs_mean: 16.5
dialogue_chars_pct: 12.8
dialogue_para_pct: 32.4
interiority_para_pct: 12.0
narration_para_pct: 55.6
turn_under20_pct: 52.2
turn_over200_pct: 0.0
attr_say_pct: 18.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 1.7
turn_len_median: 23
```
