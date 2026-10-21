# 纸表 生成报告

slug：`aiyuce-20261021-101`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12789
LLM 调用：57 次，累计 229.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻看质检记录的纸质表格 | 2256 | normal | 94.3 | 0 |  | 0 |
| 2 | 翻看考勤表数字 | 2448 | normal | 35.1 | 0 |  | 1 |
| 3 | 翻看质检记录的纸质表格 | 2637 | normal | 34.6 | 0 |  | 2 |
| 4 | 翻看采购报价单 | 2112 | normal | 36.4 | 0 |  | 1 |
| 5 | 翻看采购报价单 | 1904 | normal | 87.4 | 0 |  | 1 |
| 6 | 翻看质检记录的纸质表格 | 1426 | short | 33.6 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 3 句（如「比如说一旦有哪家竞争对手率先实现了百分之九十以上…」）
  - [observe] 标题重复：「翻看质检记录的纸质表格」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 标题重复：「翻看采购报价单」已存在
- 第 6 章：
  - dialogue_chars_pct 34.4 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 23.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「翻看质检记录的纸质表格」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12511
chapter_chars_mean: 2085
chapter_chars_median: 2137
chapter_chars_cv: 0.2
paragraphs_mean: 14.2
dialogue_chars_pct: 6.9
dialogue_para_pct: 28.7
interiority_para_pct: 13.2
narration_para_pct: 58.1
turn_under20_pct: 76.9
turn_over200_pct: 0.0
attr_say_pct: 35.1
attr_adv_pct: 3.5
scenes_per_chapter: 1.5
dialogue_run_mean: 1.8
turn_len_median: 11
```
