# 标尺 生成报告

slug：`aiyuce-20261021-226`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12994
LLM 调用：57 次，累计 227.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 查看招聘JD的细节 | 2178 | normal | 95.9 | 0 |  | 1 |
| 2 | 核对工资单数据 | 1912 | normal | 89.5 | 0 |  | 0 |
| 3 | 核对报价单数据 | 2506 | normal | 36.4 | 0 |  | 2 |
| 4 | 核对工时统计报告 | 2294 | normal | 35.7 | 0 |  | 1 |
| 5 | 查看折旧记录 | 2596 | normal | 89.6 | 0 |  | 0 |
| 6 | 核对报价单数据 | 1502 | short | 89.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 31.2 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对工资单数据》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 标题重复：「核对报价单数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12736
chapter_chars_mean: 2123
chapter_chars_median: 2188
chapter_chars_cv: 0.19
paragraphs_mean: 13.3
dialogue_chars_pct: 2.6
dialogue_para_pct: 19.3
interiority_para_pct: 18.5
narration_para_pct: 62.1
turn_under20_pct: 84.2
turn_over200_pct: 0.0
attr_say_pct: 15.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.1
turn_len_median: 14
```
