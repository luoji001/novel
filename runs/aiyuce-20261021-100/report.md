# 电单 生成报告

slug：`aiyuce-20261021-100`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13840
LLM 调用：57 次，累计 244.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单核对过程 | 2473 | normal | 56.4 | 0 |  | 0 |
| 2 | 计算电费变化 | 2402 | normal | 35.2 | 0 |  | 1 |
| 3 | 折旧表核对过程 | 2583 | normal | 36.1 | 0 |  | 1 |
| 4 | 核对电价变化 | 2271 | normal | 87.2 | 0 |  | 2 |
| 5 | 盯住招聘JD | 2505 | normal | 35.8 | 0 |  | 1 |
| 6 | 核对电价变化 | 1600 | short | 88.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - 单条套路句式超限：「东莞某工业园区机房」×3
  - narration_para_pct 40.0 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 4 句（如「此外，由于新岗位对团队协作也有一定要求，这意味着…」）
- 第 6 章：
  - [observe] 标题重复：「核对电价变化」已存在

## 整书结构指标

```
chapters: 6
total_chars: 13570
chapter_chars_mean: 2262
chapter_chars_median: 2391
chapter_chars_cv: 0.16
paragraphs_mean: 14.8
dialogue_chars_pct: 3.4
dialogue_para_pct: 18.1
interiority_para_pct: 28.6
narration_para_pct: 53.4
turn_under20_pct: 76.2
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.4
turn_len_median: 10
```
