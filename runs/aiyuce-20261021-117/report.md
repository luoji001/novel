# 记录本 生成报告

slug：`aiyuce-20261021-117`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11865
LLM 调用：57 次，累计 221.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 记录本的使用与管理 | 2188 | normal | 95.3 | 0 |  | 0 |
| 2 | 记录本折旧表 | 2463 | normal | 88.6 | 0 |  | 0 |
| 3 | 记录本消耗异常 | 2183 | normal | 85.3 | 0 |  | 0 |
| 4 | 核对折旧表 | 1914 | normal | 33.5 | 0 |  | 1 |
| 5 | 核对折旧表 | 1719 | normal | 33.4 | 0 |  | 2 |
| 6 | 核对折旧表 | 1392 | short | 90.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被最终采用的新纪录管理系统所推翻…」）
  - [observe] 标题重复：「核对折旧表」已存在
- 第 6 章：
  - narration_para_pct 14.3 低于目标 45.0
  - [observe] 标题重复：「核对折旧表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11626
chapter_chars_mean: 1938
chapter_chars_median: 2006
chapter_chars_cv: 0.19
paragraphs_mean: 12.3
dialogue_chars_pct: 1.9
dialogue_para_pct: 14.6
interiority_para_pct: 17.9
narration_para_pct: 67.5
turn_under20_pct: 84.8
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 18.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.8
turn_len_median: 10
```
