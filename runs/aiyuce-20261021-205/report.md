# 代写报价单 生成报告

slug：`aiyuce-20261021-205`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11579
LLM 调用：57 次，累计 214.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单 | 2017 | normal | 94.3 | 0 |  | 3 |
| 2 | 灯光忽明忽暗 | 2048 | normal | 91.9 | 0 |  | 2 |
| 3 | 核对电费单 | 1940 | normal | 35.9 | 0 |  | 3 |
| 4 | 核对折旧计算表 | 2154 | normal | 36.7 | 0 |  | 1 |
| 5 | 核对电费单 | 2147 | normal | 36.2 | 0 |  | 2 |
| 6 | 核对营业额报表 | 1267 | short | 35.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3
  - interiority_para_pct 46.7 高于目标 40.0
  - narration_para_pct 33.3 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 20.8 高于目标 18.0
  - narration_para_pct 21.1 低于目标 45.0
- 第 3 章：
  - interiority_para_pct 46.7 高于目标 40.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对电费单」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 2 句（如「然而这一切都建立在他能够稳定地保持较高的服务水平…」）
  - [observe] 标题重复：「核对电费单」已存在
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）

## 整书结构指标

```
chapters: 6
total_chars: 11318
chapter_chars_mean: 1886
chapter_chars_median: 1985
chapter_chars_cv: 0.17
paragraphs_mean: 14.3
dialogue_chars_pct: 5.6
dialogue_para_pct: 21.2
interiority_para_pct: 31.3
narration_para_pct: 47.5
turn_under20_pct: 69.7
turn_over200_pct: 0.0
attr_say_pct: 6.6
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.7
turn_len_median: 14
```
