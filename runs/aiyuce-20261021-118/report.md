# 证书名单 生成报告

slug：`aiyuce-20261021-118`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12969
LLM 调用：57 次，累计 223.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 提交工时记录表 | 2529 | normal | 38.0 | 0 |  | 1 |
| 2 | 调整报价单 | 2115 | normal | 35.7 | 0 |  | 2 |
| 3 | 修改招聘JD | 2294 | normal | 89.3 | 0 |  | 1 |
| 4 | 查看财务报表 | 2142 | normal | 35.8 | 0 |  | 1 |
| 5 | 核对证书复印件 | 2368 | normal | 88.3 | 0 |  | 3 |
| 6 | 核对证书复印件 | 1515 | short | 80.3 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「不过，这条推论会被什么推翻呢…」）
- 第 2 章：
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 30.8 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 18.7 高于目标 18.0
  - narration_para_pct 39.1 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 47.7 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 6.2 低于目标 45.0
  - [observe] 标题重复：「核对证书复印件」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12677
chapter_chars_mean: 2113
chapter_chars_median: 2176
chapter_chars_cv: 0.16
paragraphs_mean: 16.7
dialogue_chars_pct: 13.3
dialogue_para_pct: 47.0
interiority_para_pct: 6.9
narration_para_pct: 46.1
turn_under20_pct: 60.9
turn_over200_pct: 0.0
attr_say_pct: 40.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 2.7
turn_len_median: 14
```
