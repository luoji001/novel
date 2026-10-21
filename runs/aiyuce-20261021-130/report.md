# 执业证书 生成报告

slug：`aiyuce-20261021-130`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11754
LLM 调用：53 次，累计 203.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单 | 2394 | normal | 38.9 | 0 |  | 2 |
| 2 | 核对报价单 | 2173 | normal | 35.0 | 0 |  | 2 |
| 3 | 核对招聘JD文件 | 2503 | normal | 35.0 | 0 |  | 1 |
| 4 | 核对折旧表 | 2204 | normal | 88.8 | 0 |  | 0 |
| 5 | 核对执业资格证书 | 1112 | normal | 59.9 | 0 |  | 1 |
| 6 | 核对执业资格证书 | 1362 | short | 58.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 35.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对电费单》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 44.4 低于目标 45.0
- 第 6 章：
  - interiority_para_pct 50.0 高于目标 40.0
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 标题重复：「核对执业资格证书」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11497
chapter_chars_mean: 1916
chapter_chars_median: 2144
chapter_chars_cv: 0.3
paragraphs_mean: 13.7
dialogue_chars_pct: 4.5
dialogue_para_pct: 25.6
interiority_para_pct: 28.9
narration_para_pct: 45.5
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.6
turn_len_median: 11
```
