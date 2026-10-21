# 听课记录表 生成报告

slug：`aiyuce-20261021-225`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11520
LLM 调用：57 次，累计 219.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对听课记录表 | 1922 | normal | 37.8 | 0 |  | 1 |
| 2 | 核对听课记录表 | 2023 | normal | 37.0 | 0 |  | 4 |
| 3 | 核对听课记录表 | 2264 | normal | 35.1 | 0 |  | 4 |
| 4 | 手指轻敲桌面 | 2037 | normal | 36.2 | 0 |  | 3 |
| 5 | 手指轻点表格 | 2112 | normal | 89.4 | 0 |  | 2 |
| 6 | 手指摩挲记录表边缘 | 1156 | short | 87.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - 命中套话收尾句
  - dialogue_chars_pct 18.3 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对听课记录表」已存在
- 第 3 章：
  - dialogue_chars_pct 21.5 高于目标 18.0
  - narration_para_pct 41.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的证据推翻…」）
  - [observe] 标题重复：「核对听课记录表」已存在
- 第 4 章：
  - 情节与已写章节重复 0.73 ≥ 0.72（撞上「教研组长与产品总监讨论AI作文批改系统的应用，权衡其效率…」）
  - narration_para_pct 41.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 20.7 高于目标 18.0
  - narration_para_pct 35.0 低于目标 45.0
- 第 6 章：
  - interiority_para_pct 50.0 高于目标 40.0
  - narration_para_pct 12.5 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11248
chapter_chars_mean: 1875
chapter_chars_median: 1984
chapter_chars_cv: 0.2
paragraphs_mean: 14.7
dialogue_chars_pct: 15.5
dialogue_para_pct: 40.0
interiority_para_pct: 14.2
narration_para_pct: 45.8
turn_under20_pct: 45.3
turn_over200_pct: 0.0
attr_say_pct: 29.1
attr_adv_pct: 2.5
scenes_per_chapter: 1.2
dialogue_run_mean: 2.1
turn_len_median: 22
```
