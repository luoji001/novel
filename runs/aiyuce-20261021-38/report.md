# 显卡价目录 生成报告

slug：`aiyuce-20261021-38`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12366
LLM 调用：57 次，累计 226.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显卡销售报价单 | 1919 | normal | 39.1 | 0 |  | 1 |
| 2 | 显卡销售报价单 | 2578 | normal | 36.6 | 0 |  | 3 |
| 3 | 库存清单更新 | 2080 | normal | 34.6 | 0 |  | 1 |
| 4 | 交易流水账记录 | 2397 | normal | 34.7 | 0 |  | 1 |
| 5 | 手机震动通知 | 1987 | normal | 87.3 | 0 |  | 0 |
| 6 | 摩挲报价单边缘 | 1399 | short | 36.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 41.7 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「一个穿着西装的男人冷冷地开口道，“你们有没有考虑…」）
  - [observe] 标题重复：「显卡销售报价单」已存在
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12090
chapter_chars_mean: 2015
chapter_chars_median: 1988
chapter_chars_cv: 0.2
paragraphs_mean: 15.2
dialogue_chars_pct: 4.0
dialogue_para_pct: 19.3
interiority_para_pct: 7.4
narration_para_pct: 73.4
turn_under20_pct: 92.5
turn_over200_pct: 0.0
attr_say_pct: 9.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.5
turn_len_median: 5
```
