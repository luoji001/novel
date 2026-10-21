# 筛片 生成报告

slug：`aiyuce-20261021-135`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13724
LLM 调用：57 次，累计 233.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对影像科工作量统计表 | 2465 | normal | 37.8 | 0 |  | 2 |
| 2 | AI初筛报价单 | 2611 | normal | 89.7 | 0 |  | 0 |
| 3 | 核对影像科工作量统计表 | 2922 | normal | 36.4 | 0 |  | 2 |
| 4 | 注视报告 | 2022 | normal | 36.3 | 0 |  | 1 |
| 5 | 核对预算报表数据 | 2429 | normal | 36.3 | 0 |  | 2 |
| 6 | 审视误诊案例报告 | 1269 | short | 34.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「他想起之前的一次会议上，一位年轻医生提到过，连续…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对影像科工作量统计表」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 42.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 13407
chapter_chars_mean: 2234
chapter_chars_median: 2392
chapter_chars_cv: 0.25
paragraphs_mean: 17.8
dialogue_chars_pct: 7.0
dialogue_para_pct: 26.7
interiority_para_pct: 19.4
narration_para_pct: 53.8
turn_under20_pct: 67.5
turn_over200_pct: 0.0
attr_say_pct: 10.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.5
turn_len_median: 12
```
