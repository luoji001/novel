# 胶片钥匙 生成报告

slug：`shipin-20261027-25`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5488
LLM 调用：57 次，累计 128.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触摸胶片 | 586 | short | 19.9 | 0 |  | 1 |
| 2 | 触碰泛黄照片 | 1016 | normal | 37.1 | 0 |  | 2 |
| 3 | 报纸与椅子 | 908 | normal | 22.3 | 0 |  | 3 |
| 4 | 触碰胶片 | 1194 | normal | 92.4 | 0 |  | 1 |
| 5 | 夺钥 | 1073 | normal | 91.1 | 0 |  | 0 |
| 6 | 报纸与椅子 | 705 | normal | 34.4 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 526 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - dialogue_chars_pct 3.8 低于目标 5.0
  - [observe] 章内自我复读 2 句（如「最醒目的那张《少林寺》海报已经被磨花了边，边缘还…」）
- 第 3 章：
  - dialogue_chars_pct 3.7 低于目标 5.0
  - [observe] 章内自我复读 8 句（如「他裹着红色毛线帽，怀里抱着一卷旧报纸，脚尖轻轻勾…」）
  - [observe] 章节过短 790 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - [observe] 标题与《触摸胶片》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 548 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「报纸与椅子」已存在

## 整书结构指标

```
chapters: 6
total_chars: 4957
chapter_chars_mean: 826
chapter_chars_median: 879
chapter_chars_cv: 0.3
paragraphs_mean: 31.5
dialogue_chars_pct: 9.7
dialogue_para_pct: 25.5
interiority_para_pct: 0.9
narration_para_pct: 73.7
turn_under20_pct: 98.9
turn_over200_pct: 0.0
attr_say_pct: 20.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.1
turn_len_median: 9
```
