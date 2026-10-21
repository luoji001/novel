# 电表 生成报告

slug：`aiyuce-20261021-52`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13051
LLM 调用：57 次，累计 214.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指划过电费单 | 2209 | normal | 38.4 | 0 |  | 2 |
| 2 | 手指敲桌面 | 2467 | normal | 90.3 | 0 |  | 1 |
| 3 | 电价波动与服务器温度 | 2298 | normal | 91.9 | 0 |  | 0 |
| 4 | 手指敲桌面 | 2542 | normal | 35.8 | 0 |  | 2 |
| 5 | 手指划过电费单 | 2019 | normal | 90.7 | 0 |  | 1 |
| 6 | 手指划过电费单 | 1510 | short | 34.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 38.1 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「就在思考之际，他又重新看了眼那份电费单，心中隐隐…」）
- 第 2 章：
  - narration_para_pct 40.0 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「手指敲桌面」已存在
- 第 5 章：
  - [observe] 标题重复：「手指划过电费单」已存在
- 第 6 章：
  - interiority_para_pct 45.5 高于目标 40.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「手指划过电费单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12761
chapter_chars_mean: 2127
chapter_chars_median: 2202
chapter_chars_cv: 0.17
paragraphs_mean: 16.3
dialogue_chars_pct: 6.7
dialogue_para_pct: 26.1
interiority_para_pct: 26.4
narration_para_pct: 47.5
turn_under20_pct: 45.7
turn_over200_pct: 0.0
attr_say_pct: 16.5
attr_adv_pct: 7.8
scenes_per_chapter: 1.2
dialogue_run_mean: 1.2
turn_len_median: 24
```
