# 电表指针 生成报告

slug：`aiyuce-20261021-18`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12380
LLM 调用：53 次，累计 209.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单细节 | 2260 | normal | 96.3 | 0 |  | 1 |
| 2 | 核对折旧表细节 | 2683 | normal | 88.9 | 0 |  | 1 |
| 3 | 核对招聘JD与电费单 | 2373 | normal | 35.7 | 0 |  | 1 |
| 4 | 核对报价单修改痕迹 | 2402 | normal | 88.5 | 0 |  | 0 |
| 5 | 核对服务器运行时间 | 1226 | normal | 89.6 | 0 |  | 0 |
| 6 | 核对服务器运行时间 | 1430 | short | 90.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 44.4 低于目标 45.0
- 第 2 章：
  - narration_para_pct 37.5 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 标题重复：「核对服务器运行时间」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12103
chapter_chars_mean: 2017
chapter_chars_median: 2266
chapter_chars_cv: 0.29
paragraphs_mean: 14.3
dialogue_chars_pct: 4.2
dialogue_para_pct: 22.3
interiority_para_pct: 23.5
narration_para_pct: 54.2
turn_under20_pct: 62.2
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.1
turn_len_median: 14
```
