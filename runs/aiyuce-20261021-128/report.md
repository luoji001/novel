# 校对钟 生成报告

slug：`aiyuce-20261021-128`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11457
LLM 调用：57 次，累计 218.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻译报价单分析 | 1919 | normal | 37.6 | 0 |  | 1 |
| 2 | 核对工资表 | 2189 | normal | 36.6 | 0 |  | 1 |
| 3 | 核对测试数据 | 2392 | normal | 89.7 | 0 |  | 1 |
| 4 | 客户反馈报告的核查 | 1847 | normal | 36.0 | 0 |  | 1 |
| 5 | 预算表核对 | 1964 | normal | 89.7 | 0 |  | 0 |
| 6 | 核对测试数据 | 1140 | short | 35.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 27.3 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对测试数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11213
chapter_chars_mean: 1869
chapter_chars_median: 1898
chapter_chars_cv: 0.23
paragraphs_mean: 12.7
dialogue_chars_pct: 7.1
dialogue_para_pct: 24.9
interiority_para_pct: 13.1
narration_para_pct: 62.0
turn_under20_pct: 31.2
turn_over200_pct: 0.0
attr_say_pct: 18.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 2.0
turn_len_median: 27
```
