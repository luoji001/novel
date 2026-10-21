# 红笔 生成报告

slug：`aiyuce-20261021-153`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11150
LLM 调用：57 次，累计 207.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | AI作文批改报告 | 2100 | normal | 87.7 | 0 |  | 3 |
| 2 | 预算明细表 | 2078 | normal | 89.8 | 0 |  | 2 |
| 3 | 记录本的微表情 | 2060 | normal | 33.9 | 0 |  | 3 |
| 4 | 测试报告 | 1784 | normal | 33.2 | 0 |  | 3 |
| 5 | 数据备份的质疑 | 1861 | normal | 33.8 | 0 |  | 4 |
| 6 | 月度报告的微表情 | 1261 | short | 88.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 41.8 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 25.0 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 23.7 高于目标 18.0
  - narration_para_pct 28.6 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 36.2 高于目标 18.0
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 49.7 高于目标 18.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「假如在这个过程中，教研组长发现教师们对新引入的测…」）
- 第 5 章：
  - 命中套话收尾句
  - dialogue_chars_pct 39.2 高于目标 18.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 22.3 高于目标 18.0
  - narration_para_pct 44.4 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 10825
chapter_chars_mean: 1804
chapter_chars_median: 1904
chapter_chars_cv: 0.17
paragraphs_mean: 19.3
dialogue_chars_pct: 36.0
dialogue_para_pct: 66.6
interiority_para_pct: 3.5
narration_para_pct: 30.0
turn_under20_pct: 35.0
turn_over200_pct: 0.0
attr_say_pct: 26.2
attr_adv_pct: 2.1
scenes_per_chapter: 1.2
dialogue_run_mean: 3.2
turn_len_median: 26
```
