# 电表转动声 生成报告

slug：`aiyuce-20261021-228`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12929
LLM 调用：57 次，累计 224.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 预算表上的数字变动 | 2560 | normal | 38.4 | 0 |  | 2 |
| 2 | 核对用电记录单 | 2429 | normal | 36.7 | 0 |  | 2 |
| 3 | 预算表新增条目 | 2026 | normal | 33.8 | 0 |  | 4 |
| 4 | 核对成绩统计表 | 2659 | normal | 35.0 | 0 |  | 1 |
| 5 | 教师学历与职称档案的对比 | 2211 | normal | 36.4 | 0 |  | 1 |
| 6 | 设备采购延迟的影响 | 1038 | short | 33.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 2 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - 命中套话收尾句
  - dialogue_chars_pct 34.7 高于目标 18.0
  - narration_para_pct 39.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 50.8 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12630
chapter_chars_mean: 2105
chapter_chars_median: 2272
chapter_chars_cv: 0.28
paragraphs_mean: 16.2
dialogue_chars_pct: 11.6
dialogue_para_pct: 29.7
interiority_para_pct: 18.5
narration_para_pct: 51.7
turn_under20_pct: 56.7
turn_over200_pct: 0.0
attr_say_pct: 40.2
attr_adv_pct: 3.1
scenes_per_chapter: 1.2
dialogue_run_mean: 1.9
turn_len_median: 16
```
