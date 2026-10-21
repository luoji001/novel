# 代码审查 生成报告

slug：`aiyuce-20261021-199`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11164
LLM 调用：57 次，累计 209.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击键盘的招聘JD | 1822 | normal | 89.7 | 0 |  | 4 |
| 2 | 查看进度报告 | 2046 | normal | 36.2 | 0 |  | 1 |
| 3 | 审视代码审查记录 | 2342 | normal | 36.1 | 0 |  | 1 |
| 4 | 拨通内线电话 | 2080 | normal | 89.3 | 0 |  | 0 |
| 5 | 点击绩效评估表 | 1721 | normal | 88.8 | 0 |  | 2 |
| 6 | 点击绩效评估表 | 1147 | short | 35.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「不仅仅是」×3
  - dialogue_chars_pct 27.7 高于目标 18.0
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 27.3 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 5 章：
  - dialogue_chars_pct 22.3 高于目标 18.0
  - narration_para_pct 21.4 低于目标 45.0
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「点击绩效评估表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 10901
chapter_chars_mean: 1817
chapter_chars_median: 1884
chapter_chars_cv: 0.22
paragraphs_mean: 13.7
dialogue_chars_pct: 9.5
dialogue_para_pct: 31.8
interiority_para_pct: 14.9
narration_para_pct: 53.3
turn_under20_pct: 55.7
turn_over200_pct: 0.0
attr_say_pct: 8.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 2.4
turn_len_median: 20
```
