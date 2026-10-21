# 电表 生成报告

slug：`aiyuce-20261021-76`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13310
LLM 调用：57 次，累计 235.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 通知单张贴在墙上 | 2504 | normal | 37.1 | 0 |  | 2 |
| 2 | 文件堆叠在桌面 | 2344 | normal | 91.0 | 0 |  | 0 |
| 3 | 电费明细单 | 2157 | normal | 34.8 | 0 |  | 1 |
| 4 | 电费明细单 | 2191 | normal | 33.6 | 0 |  | 2 |
| 5 | 负荷率达标验证 | 2668 | normal | 33.2 | 0 |  | 1 |
| 6 | 负荷率达标验证 | 1440 | short | 85.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「某地级市供电局」×3
  - [observe] 章内自我复读 3 句（如「例如，若后来发现由于技术改进降低了发电成本，而电…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「电费明细单」已存在
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 标题重复：「负荷率达标验证」已存在

## 整书结构指标

```
chapters: 6
total_chars: 13063
chapter_chars_mean: 2177
chapter_chars_median: 2228
chapter_chars_cv: 0.2
paragraphs_mean: 12.8
dialogue_chars_pct: 1.1
dialogue_para_pct: 7.1
interiority_para_pct: 11.7
narration_para_pct: 81.2
turn_under20_pct: 80.7
turn_over200_pct: 0.0
attr_say_pct: 100.0
attr_adv_pct: 100.0
scenes_per_chapter: 1
dialogue_run_mean: 1
turn_len_median: 15
```
