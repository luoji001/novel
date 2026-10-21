# 证书 生成报告

slug：`aiyuce-20261021-70`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12655
LLM 调用：57 次，累计 223.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对财务报表 | 2574 | normal | 94.8 | 0 |  | 0 |
| 2 | 修订版招聘JD文件 | 1991 | normal | 36.1 | 0 |  | 1 |
| 3 | 核对财务报表 | 2063 | normal | 34.4 | 0 |  | 2 |
| 4 | 扫描报告数据 | 2296 | normal | 34.3 | 0 |  | 2 |
| 5 | 核对持证员工名单 | 2544 | normal | 87.7 | 0 |  | 1 |
| 6 | 核对财务报表 | 1181 | short | 78.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对财务报表」已存在
- 第 4 章：
  - interiority_para_pct 43.8 高于目标 40.0
  - [observe] 章内自我复读 3 句（如「此外，如果市场对数据标注的需求下降，导致企业减少…」）
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
- 第 6 章：
  - dialogue_chars_pct 60.3 高于目标 18.0
  - dialogue_run_mean 8 高于目标 4.0
  - narration_para_pct 11.1 低于目标 45.0
  - [observe] 标题重复：「核对财务报表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12398
chapter_chars_mean: 2066
chapter_chars_median: 2138
chapter_chars_cv: 0.25
paragraphs_mean: 13.5
dialogue_chars_pct: 8.0
dialogue_para_pct: 27.4
interiority_para_pct: 24.9
narration_para_pct: 47.8
turn_under20_pct: 63.1
turn_over200_pct: 0.0
attr_say_pct: 6.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 2.2
turn_len_median: 12
```
