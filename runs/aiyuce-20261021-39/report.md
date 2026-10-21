# 影像科的夜 生成报告

slug：`aiyuce-20261021-39`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12435
LLM 调用：57 次，累计 225.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 日志里的数字密码 | 1748 | normal | 98.7 | 0 |  | 2 |
| 2 | AI模型推理报价单 | 2262 | normal | 36.4 | 0 |  | 3 |
| 3 | 预算表上的百分比变化 | 2728 | normal | 90.1 | 0 |  | 0 |
| 4 | 敲击桌面的数据质疑 | 2031 | normal | 32.3 | 0 |  | 4 |
| 5 | 对比新旧招聘广告 | 2282 | normal | 88.3 | 0 |  | 0 |
| 6 | 敲击桌面的数据质疑 | 1378 | short | 34.7 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 19.0 高于目标 18.0
  - narration_para_pct 16.7 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 22.7 高于目标 18.0
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「如果有足够的数据显示AI模型对于某些特定类型的病…」）
- 第 4 章：
  - dialogue_chars_pct 57.9 高于目标 18.0
  - dialogue_run_mean 5.7 高于目标 4.0
  - narration_para_pct 10.5 低于目标 45.0
  - [observe] 章内自我复读 6 句（如「我理解你的意思，但我们不能忽视这样一个事实：如果…」）
- 第 6 章：
  - dialogue_chars_pct 27.8 高于目标 18.0
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「敲击桌面的数据质疑」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12120
chapter_chars_mean: 2020
chapter_chars_median: 2092
chapter_chars_cv: 0.23
paragraphs_mean: 16.2
dialogue_chars_pct: 21.3
dialogue_para_pct: 51.8
interiority_para_pct: 10.3
narration_para_pct: 37.9
turn_under20_pct: 57.6
turn_over200_pct: 0.0
attr_say_pct: 19.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 3.0
turn_len_median: 20
```
