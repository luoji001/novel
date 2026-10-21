# 代码验证机 生成报告

slug：`aiyuce-20261021-91`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11696
LLM 调用：57 次，累计 210.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 薪资条上的试用期数字 | 1932 | normal | 38.2 | 0 |  | 3 |
| 2 | 代码导入系统的第一次尝试 | 2222 | normal | 90.4 | 0 |  | 1 |
| 3 | 绩效考核表上的数字 | 2136 | normal | 36.4 | 0 |  | 3 |
| 4 | 代码验证报告的数字波动 | 2224 | normal | 89.9 | 0 |  | 0 |
| 5 | 测试机器的错误提示 | 1902 | normal | 36.1 | 0 |  | 1 |
| 6 | 绩效考核表的数字波动 | 1274 | short | 90.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 21.3 高于目标 18.0
  - narration_para_pct 42.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 44.4 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 19.2 高于目标 18.0
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 24.5 高于目标 18.0
  - narration_para_pct 23.1 低于目标 45.0
  - [observe] 标题与《绩效考核表上的数字》近似 0.84 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11371
chapter_chars_mean: 1895
chapter_chars_median: 1978
chapter_chars_cv: 0.19
paragraphs_mean: 17.5
dialogue_chars_pct: 17.6
dialogue_para_pct: 49.9
interiority_para_pct: 9.4
narration_para_pct: 40.6
turn_under20_pct: 54.2
turn_over200_pct: 0.0
attr_say_pct: 12.4
attr_adv_pct: 4.6
scenes_per_chapter: 3.2
dialogue_run_mean: 2.0
turn_len_median: 18
```
