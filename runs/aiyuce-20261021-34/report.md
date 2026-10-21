# 标价单 生成报告

slug：`aiyuce-20261021-34`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12577
LLM 调用：57 次，累计 223.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 调整员工数量 | 2389 | normal | 37.5 | 0 |  | 1 |
| 2 | 核对报价单数据 | 2153 | normal | 87.8 | 0 |  | 0 |
| 3 | 核对证书清单 | 2431 | normal | 35.0 | 0 |  | 1 |
| 4 | 核对折旧表数据 | 2159 | normal | 89.3 | 0 |  | 0 |
| 5 | 核对折旧表数据 | 2211 | normal | 23.5 | 0 |  | 2 |
| 6 | 核对证书清单 | 1228 | short | 90.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对折旧表数据」已存在
- 第 6 章：
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 标题重复：「核对证书清单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12316
chapter_chars_mean: 2053
chapter_chars_median: 2144
chapter_chars_cv: 0.21
paragraphs_mean: 14
dialogue_chars_pct: 4.0
dialogue_para_pct: 17.6
interiority_para_pct: 23.4
narration_para_pct: 59.0
turn_under20_pct: 43.1
turn_over200_pct: 0.0
attr_say_pct: 50.0
attr_adv_pct: 50.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.5
turn_len_median: 14
```
