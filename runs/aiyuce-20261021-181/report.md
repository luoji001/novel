# 墨盒 生成报告

slug：`aiyuce-20261021-181`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11474
LLM 调用：57 次，累计 219.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单 | 2080 | normal | 95.8 | 0 |  | 1 |
| 2 | 张贴招聘JD | 2220 | normal | 90.3 | 0 |  | 0 |
| 3 | 核对报价单 | 1911 | normal | 37.5 | 0 |  | 2 |
| 4 | 调整折旧表 | 2077 | normal | 36.5 | 0 |  | 1 |
| 5 | 核对电费单 | 1828 | normal | 36.4 | 0 |  | 2 |
| 6 | 核对报价单 | 1352 | short | 89.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 16.7 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对电费单》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对电费单」已存在
- 第 6 章：
  - [observe] 标题重复：「核对报价单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11211
chapter_chars_mean: 1868
chapter_chars_median: 1950
chapter_chars_cv: 0.16
paragraphs_mean: 14.8
dialogue_chars_pct: 5.8
dialogue_para_pct: 33.6
interiority_para_pct: 17.6
narration_para_pct: 48.8
turn_under20_pct: 86.4
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 1.5
turn_len_median: 8
```
