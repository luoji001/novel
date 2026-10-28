# 撕凭证 生成报告

slug：`shipin-20261027-105`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6119
LLM 调用：57 次，累计 128.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 拖箱 | 766 | short | 99.6 | 0 |  | 1 |
| 2 | 敲杯 | 1318 | normal | 94.1 | 0 |  | 0 |
| 3 | 擦手 | 790 | normal | 37.1 | 0 |  | 2 |
| 4 | 摸蓝布条 | 1302 | normal | 85.9 | 0 |  | 2 |
| 5 | 撕凭证 | 947 | normal | 36.4 | 0 |  | 1 |
| 6 | 拖箱 | 990 | normal | 91.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 6.2 高于目标 6.0
- 第 3 章：
  - narration_para_pct 22.2 低于目标 35.0
  - [observe] 章节过短 744 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - interiority_para_pct 8.3 高于目标 6.0
  - narration_para_pct 25.0 低于目标 35.0
- 第 5 章：
  - [observe] attr_adv_pct 100.0 > 18.0（结构塌缩）
- 第 6 章：
  - [observe] 标题重复：「拖箱」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5704
chapter_chars_mean: 951
chapter_chars_median: 889
chapter_chars_cv: 0.24
paragraphs_mean: 28.8
dialogue_chars_pct: 19.5
dialogue_para_pct: 51.1
interiority_para_pct: 2.6
narration_para_pct: 46.3
turn_under20_pct: 98.0
turn_over200_pct: 0.0
attr_say_pct: 27.5
attr_adv_pct: 17.7
scenes_per_chapter: 1
dialogue_run_mean: 2.0
turn_len_median: 10
```
