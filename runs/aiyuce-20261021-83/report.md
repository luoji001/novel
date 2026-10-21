# 页数 生成报告

slug：`aiyuce-20261021-83`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13317
LLM 调用：57 次，累计 235.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫描仪的首次启动 | 2474 | normal | 37.6 | 0 |  | 1 |
| 2 | 折旧表上的电力消耗 | 2506 | normal | 36.2 | 0 |  | 1 |
| 3 | 查看折旧表数据 | 2446 | normal | 87.3 | 0 |  | 1 |
| 4 | 年度计费明细表 | 2318 | normal | 36.4 | 0 |  | 3 |
| 5 | 合伙人翻阅年度计费明细表 | 2100 | normal | 35.4 | 0 |  | 2 |
| 6 | 扫描仪的首次启动 | 1467 | short | 94.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - 命中套话收尾句
- 第 4 章：
  - dialogue_chars_pct 20.7 高于目标 18.0
  - narration_para_pct 23.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的事实推翻呢…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《年度计费明细表》近似 0.74 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题重复：「扫描仪的首次启动」已存在

## 整书结构指标

```
chapters: 6
total_chars: 13034
chapter_chars_mean: 2172
chapter_chars_median: 2333
chapter_chars_cv: 0.18
paragraphs_mean: 14.8
dialogue_chars_pct: 6.3
dialogue_para_pct: 29.4
interiority_para_pct: 13.0
narration_para_pct: 57.6
turn_under20_pct: 60.6
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.9
turn_len_median: 12
```
