# 记录本 生成报告

slug：`aiyuce-20261021-189`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11906
LLM 调用：57 次，累计 231.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 预算表 | 1961 | normal | 95.9 | 0 |  | 0 |
| 2 | 使用报告 | 2030 | normal | 35.2 | 0 |  | 4 |
| 3 | 翻阅作文样本 | 2060 | normal | 35.7 | 0 |  | 2 |
| 4 | 翻阅作文样本 | 2405 | normal | 85.5 | 0 |  | 3 |
| 5 | 翻阅听课记录本 | 2177 | normal | 34.6 | 0 |  | 3 |
| 6 | 翻阅听课记录本 | 1267 | short | 34.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「李婉秋站在」×3
  - dialogue_chars_pct 23.5 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 35.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 45.5 高于目标 18.0
  - narration_para_pct 19.2 低于目标 45.0
  - [observe] 标题重复：「翻阅作文样本」已存在
- 第 5 章：
  - dialogue_chars_pct 28.6 高于目标 18.0
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 26.5 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「翻阅听课记录本」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11609
chapter_chars_mean: 1935
chapter_chars_median: 2000
chapter_chars_cv: 0.2
paragraphs_mean: 16.8
dialogue_chars_pct: 22.9
dialogue_para_pct: 50.0
interiority_para_pct: 15.7
narration_para_pct: 34.3
turn_under20_pct: 48.1
turn_over200_pct: 0.0
attr_say_pct: 18.6
attr_adv_pct: 4.8
scenes_per_chapter: 2
dialogue_run_mean: 2.2
turn_len_median: 26
```
