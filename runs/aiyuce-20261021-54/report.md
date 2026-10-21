# 成本表 生成报告

slug：`aiyuce-20261021-54`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12451
LLM 调用：57 次，累计 222.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 目光锁定报价单数字 | 2430 | normal | 94.2 | 0 |  | 1 |
| 2 | 核对电费单细节 | 2199 | normal | 88.3 | 0 |  | 0 |
| 3 | 目光锁定招聘JD | 2184 | normal | 89.8 | 0 |  | 0 |
| 4 | 目光锁定折旧表数字 | 2154 | normal | 36.0 | 0 |  | 3 |
| 5 | 目光锁定许可证条款 | 2218 | normal | 82.8 | 0 |  | 3 |
| 6 | 核对电费单细节 | 1260 | short | 34.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 28.6 低于目标 45.0
- 第 4 章：
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《目光锁定报价单数字》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - dialogue_chars_pct 49.3 高于目标 18.0
  - dialogue_run_mean 8 高于目标 4.0
  - narration_para_pct 11.1 低于目标 45.0
- 第 6 章：
  - [observe] 章内自我复读 2 句（如「如果后续审计结果显示，实际发生的成本并没有相应增…」）
  - [observe] 标题重复：「核对电费单细节」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12170
chapter_chars_mean: 2028
chapter_chars_median: 2147
chapter_chars_cv: 0.2
paragraphs_mean: 14.8
dialogue_chars_pct: 13.3
dialogue_para_pct: 40.2
interiority_para_pct: 21.1
narration_para_pct: 38.7
turn_under20_pct: 61.0
turn_over200_pct: 0.0
attr_say_pct: 18.0
attr_adv_pct: 1.6
scenes_per_chapter: 1.5
dialogue_run_mean: 2.7
turn_len_median: 19
```
