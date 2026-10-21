# 红笔 生成报告

slug：`aiyuce-20261021-249`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12799
LLM 调用：57 次，累计 235.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指轻叩桌面 | 2244 | normal | 37.8 | 0 |  | 2 |
| 2 | 研组长摊开使用报告 | 2482 | normal | 86.7 | 0 |  | 2 |
| 3 | 手指轻叩桌面 | 1821 | normal | 32.3 | 0 |  | 5 |
| 4 | 手指轻触数据页面 | 2491 | normal | 36.4 | 0 |  | 2 |
| 5 | 手指轻触数据页面 | 2321 | normal | 35.1 | 0 |  | 5 |
| 6 | 手指轻触数据页面 | 1434 | short | 92.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「也许就是当某位教师的实际修改次数超过预设阈值之后…」）
- 第 2 章：
  - dialogue_chars_pct 35.7 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 24.7 高于目标 18.0
  - dialogue_run_mean 10 高于目标 4.0
  - narration_para_pct 15.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「手指轻叩桌面」已存在
- 第 4 章：
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - 命中套话收尾句
  - dialogue_chars_pct 20.7 高于目标 18.0
  - narration_para_pct 35.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「一条推论会被什么推翻…」）
  - [observe] 标题重复：「手指轻触数据页面」已存在
- 第 6 章：
  - [observe] 标题重复：「手指轻触数据页面」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12502
chapter_chars_mean: 2084
chapter_chars_median: 2232
chapter_chars_cv: 0.2
paragraphs_mean: 16.5
dialogue_chars_pct: 17.9
dialogue_para_pct: 58.5
interiority_para_pct: 9.0
narration_para_pct: 32.6
turn_under20_pct: 49.3
turn_over200_pct: 0.0
attr_say_pct: 9.0
attr_adv_pct: 3.7
scenes_per_chapter: 1
dialogue_run_mean: 3.5
turn_len_median: 22
```
