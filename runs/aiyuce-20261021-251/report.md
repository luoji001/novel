# 模型复核页数 生成报告

slug：`aiyuce-20261021-251`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11255
LLM 调用：57 次，累计 205.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲预算表 | 1883 | normal | 95.3 | 0 |  | 1 |
| 2 | 划线标记调查报告 | 2205 | normal | 35.6 | 0 |  | 3 |
| 3 | 目光锁定统计表 | 1815 | normal | 34.2 | 0 |  | 4 |
| 4 | 目光锁定统计表 | 1893 | normal | 33.6 | 0 |  | 5 |
| 5 | 目光锁定统计表 | 2194 | normal | 90.4 | 0 |  | 2 |
| 6 | 摩挲调查报告 | 1259 | short | 35.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 33.3 低于目标 45.0
- 第 2 章：
  - interiority_para_pct 42.9 高于目标 40.0
  - narration_para_pct 35.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 51.6 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 17.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「一条推论会被什么推翻…」）
- 第 4 章：
  - 单条套路句式超限：「带着一丝」×3
  - dialogue_chars_pct 49.3 高于目标 18.0
  - narration_para_pct 10.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
  - [observe] 标题重复：「目光锁定统计表」已存在
- 第 5 章：
  - narration_para_pct 35.7 低于目标 45.0
  - [observe] 标题重复：「目光锁定统计表」已存在
- 第 6 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 10985
chapter_chars_mean: 1831
chapter_chars_median: 1843
chapter_chars_cv: 0.19
paragraphs_mean: 14.7
dialogue_chars_pct: 20.6
dialogue_para_pct: 47.7
interiority_para_pct: 24.4
narration_para_pct: 27.9
turn_under20_pct: 63.1
turn_over200_pct: 0.0
attr_say_pct: 4.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.4
turn_len_median: 14
```
