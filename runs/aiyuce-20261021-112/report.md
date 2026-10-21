# 电表 生成报告

slug：`aiyuce-20261021-112`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12516
LLM 调用：57 次，累计 228.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电价调整通知单 | 1910 | normal | 96.7 | 0 |  | 0 |
| 2 | 核对电价调整通知单 | 2334 | normal | 92.7 | 0 |  | 1 |
| 3 | 核对方案草案 | 2163 | normal | 90.4 | 0 |  | 1 |
| 4 | 核对服务器折旧表 | 2251 | normal | 35.0 | 0 |  | 2 |
| 5 | 电价调整通知单 | 2404 | normal | 35.2 | 0 |  | 2 |
| 6 | 指尖划过日志表 | 1448 | short | 34.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 标题重复：「核对电价调整通知单」已存在
- 第 3 章：
  - narration_para_pct 30.8 低于目标 45.0
- 第 4 章：
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对电价调整通知单》近似 0.88 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 24.1 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12230
chapter_chars_mean: 2038
chapter_chars_median: 2161
chapter_chars_cv: 0.17
paragraphs_mean: 14.3
dialogue_chars_pct: 9.3
dialogue_para_pct: 34.6
interiority_para_pct: 19.3
narration_para_pct: 46.1
turn_under20_pct: 48.6
turn_over200_pct: 0.0
attr_say_pct: 11.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.4
turn_len_median: 26
```
