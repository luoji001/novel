# 折旧计算表 生成报告

slug：`aiyuce-20261021-110`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12410
LLM 调用：57 次，累计 231.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对显卡报价单 | 2205 | normal | 37.8 | 0 |  | 2 |
| 2 | 检查租金合同条款 | 2510 | normal | 35.7 | 0 |  | 1 |
| 3 | 核对显卡报价单 | 2107 | normal | 87.9 | 0 |  | 4 |
| 4 | 核对折旧计算表 | 2291 | normal | 36.8 | 0 |  | 1 |
| 5 | 核对显卡报价单 | 1931 | normal | 89.0 | 0 |  | 1 |
| 6 | 核对显卡报价单 | 1360 | short | 88.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 30.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 29.6 高于目标 18.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - narration_para_pct 26.3 低于目标 45.0
  - [observe] 标题重复：「核对显卡报价单」已存在
- 第 4 章：
  - [observe] 章内自我复读 3 句（如「如果AI模型开发进度报告显示需求下降，那么实际的…」）
- 第 5 章：
  - [observe] 标题重复：「核对显卡报价单」已存在
- 第 6 章：
  - narration_para_pct 22.2 低于目标 45.0
  - [observe] 标题重复：「核对显卡报价单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12137
chapter_chars_mean: 2023
chapter_chars_median: 2109
chapter_chars_cv: 0.19
paragraphs_mean: 14.2
dialogue_chars_pct: 12.0
dialogue_para_pct: 40.8
interiority_para_pct: 16.2
narration_para_pct: 43.0
turn_under20_pct: 60.1
turn_over200_pct: 0.0
attr_say_pct: 23.1
attr_adv_pct: 6.7
scenes_per_chapter: 1.2
dialogue_run_mean: 2.2
turn_len_median: 21
```
