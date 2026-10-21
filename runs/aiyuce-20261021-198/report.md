# 报价单 生成报告

slug：`aiyuce-20261021-198`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11591
LLM 调用：57 次，累计 206.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指敲击桌面 | 1727 | normal | 96.4 | 0 |  | 2 |
| 2 | 敲击桌面 | 2278 | normal | 88.0 | 0 |  | 3 |
| 3 | 手指敲击键盘 | 2485 | normal | 35.8 | 0 |  | 2 |
| 4 | 手指划过合同条款 | 2066 | normal | 84.5 | 0 |  | 3 |
| 5 | 手指划过报价单 | 1824 | normal | 33.5 | 0 |  | 3 |
| 6 | 手指划过报价单 | 1205 | short | 33.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×4
  - narration_para_pct 38.9 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 22.1 高于目标 18.0
  - narration_para_pct 31.6 低于目标 45.0
  - [observe] 标题与《手指敲击桌面》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《手指敲击桌面》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_chars_pct 40.5 高于目标 18.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - narration_para_pct 20.0 低于目标 45.0
- 第 5 章：
  - dialogue_chars_pct 41.2 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被采购主管向更高层汇报并请求进一步的信…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「手指划过报价单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11307
chapter_chars_mean: 1884
chapter_chars_median: 1894
chapter_chars_cv: 0.24
paragraphs_mean: 16
dialogue_chars_pct: 20.3
dialogue_para_pct: 40.5
interiority_para_pct: 15.8
narration_para_pct: 43.7
turn_under20_pct: 48.2
turn_over200_pct: 0.0
attr_say_pct: 13.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.6
turn_len_median: 25
```
