# 代码审查 生成报告

slug：`aiyuce-20261021-07`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12639
LLM 调用：57 次，累计 214.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 招聘JD的修改 | 2129 | normal | 94.3 | 0 |  | 0 |
| 2 | 调整模型参数 | 2359 | normal | 92.3 | 0 |  | 0 |
| 3 | 查看代码提交记录 | 2461 | normal | 36.4 | 0 |  | 1 |
| 4 | 查看代码提交记录 | 2270 | normal | 35.4 | 0 |  | 2 |
| 5 | 查阅绩效评估表 | 2028 | normal | 87.7 | 0 |  | 1 |
| 6 | 修改招聘JD条款 | 1386 | short | 35.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「查看代码提交记录」已存在
- 第 5 章：
  - narration_para_pct 38.5 低于目标 45.0
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12377
chapter_chars_mean: 2063
chapter_chars_median: 2155
chapter_chars_cv: 0.18
paragraphs_mean: 13.7
dialogue_chars_pct: 4.8
dialogue_para_pct: 25.8
interiority_para_pct: 16.9
narration_para_pct: 57.4
turn_under20_pct: 76.5
turn_over200_pct: 0.0
attr_say_pct: 6.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.4
turn_len_median: 12
```
