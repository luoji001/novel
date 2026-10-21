# 折旧表 生成报告

slug：`aiyuce-20261021-13`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11532
LLM 调用：57 次，累计 224.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的数字 | 2033 | normal | 95.7 | 0 |  | 1 |
| 2 | 张贴招聘JD | 2252 | normal | 90.7 | 0 |  | 0 |
| 3 | 报价单上的数字 | 2133 | normal | 35.9 | 0 |  | 3 |
| 4 | 折旧表上的磨损处 | 2120 | normal | 36.5 | 0 |  | 3 |
| 5 | 打印纸上的数字 | 1803 | normal | 91.7 | 0 |  | 1 |
| 6 | 电费单上的数字 | 1185 | short | 35.7 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 30.8 低于目标 45.0
- 第 3 章：
  - narration_para_pct 44.4 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果有一天，周晓梅发现她的客户数量下降，而竞争对…」）
  - [observe] 标题与《电费单上的数字》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_chars_pct 21.4 高于目标 18.0
  - narration_para_pct 32.1 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「如果这台机器突然发生了重大故障，导致提前报废，那…」）
- 第 5 章：
  - narration_para_pct 35.7 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 25.8 高于目标 18.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「电费单上的数字」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11230
chapter_chars_mean: 1872
chapter_chars_median: 2020
chapter_chars_cv: 0.2
paragraphs_mean: 17.2
dialogue_chars_pct: 11.4
dialogue_para_pct: 41.5
interiority_para_pct: 20.6
narration_para_pct: 38.0
turn_under20_pct: 71.5
turn_over200_pct: 0.0
attr_say_pct: 17.4
attr_adv_pct: 2.6
scenes_per_chapter: 1.8
dialogue_run_mean: 1.9
turn_len_median: 12
```
