# 折旧表 生成报告

slug：`aiyuce-20261021-242`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12251
LLM 调用：57 次，累计 222.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 查看显卡标签数据 | 2128 | normal | 94.1 | 0 |  | 0 |
| 2 | 查看折线图走势 | 2162 | normal | 89.9 | 0 |  | 0 |
| 3 | 手指划过表格数字 | 2331 | normal | 33.4 | 0 |  | 4 |
| 4 | 手指划过时间标记 | 2358 | normal | 35.4 | 0 |  | 1 |
| 5 | 手指划过表格数字 | 2085 | normal | 78.7 | 0 |  | 4 |
| 6 | 复核折旧表数据 | 1181 | short | 90.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - dialogue_chars_pct 39.5 高于目标 18.0
  - dialogue_run_mean 4.7 高于目标 4.0
  - narration_para_pct 10.5 低于目标 45.0
  - [observe] 章内自我复读 5 句（如「如果真的实施的话，”他低声说道，“我们的生意恐怕…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 5 章：
  - dialogue_chars_pct 32.6 高于目标 18.0
  - dialogue_run_mean 10 高于目标 4.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 标题重复：「手指划过表格数字」已存在
- 第 6 章：
  - 单条套路句式超限：「深圳华强北电子市场」×3

## 整书结构指标

```
chapters: 6
total_chars: 11963
chapter_chars_mean: 1994
chapter_chars_median: 2098
chapter_chars_cv: 0.21
paragraphs_mean: 14.8
dialogue_chars_pct: 16.3
dialogue_para_pct: 37.9
interiority_para_pct: 12.7
narration_para_pct: 49.4
turn_under20_pct: 52.2
turn_over200_pct: 0.0
attr_say_pct: 9.6
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 3.2
turn_len_median: 22
```
