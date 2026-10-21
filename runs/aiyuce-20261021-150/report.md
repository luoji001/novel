# 报价单 生成报告

slug：`aiyuce-20261021-150`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13051
LLM 调用：57 次，累计 230.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计算器的按键声 | 2181 | normal | 94.8 | 0 |  | 1 |
| 2 | 折旧表上的数字 | 2213 | normal | 36.6 | 0 |  | 1 |
| 3 | 电费单上的数字增长 | 2362 | normal | 89.9 | 0 |  | 0 |
| 4 | 招聘JD的修改记录 | 2656 | normal | 36.1 | 0 |  | 1 |
| 5 | 合同条款变更通知 | 2245 | normal | 35.0 | 0 |  | 1 |
| 6 | 报价单的数字变动 | 1388 | short | 58.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 31.2 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「模型推理服务优化工程师…」）
- 第 5 章：
  - [observe] 章内自我复读 4 句（如「假设不久之后相关部门发布指导意见，宣布原先引入的…」）

## 整书结构指标

```
chapters: 6
total_chars: 12781
chapter_chars_mean: 2130
chapter_chars_median: 2180
chapter_chars_cv: 0.2
paragraphs_mean: 14
dialogue_chars_pct: 3.1
dialogue_para_pct: 20.4
interiority_para_pct: 10.8
narration_para_pct: 68.9
turn_under20_pct: 73.3
turn_over200_pct: 0.0
attr_say_pct: 16.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.1
turn_len_median: 12
```
