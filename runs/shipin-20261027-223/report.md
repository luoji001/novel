# 铁锹与融雪剂 生成报告

slug：`shipin-20261027-223`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6781
LLM 调用：57 次，累计 138.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁锹与融雪剂 | 768 | short | 96.6 | 0 |  | 0 |
| 2 | 冰渣与红色停车牌 | 1026 | normal | 91.4 | 0 |  | 0 |
| 3 | 融雪剂与铁锹 | 1146 | normal | 89.0 | 0 |  | 0 |
| 4 | 融雪剂与铁锹 | 1291 | normal | 91.6 | 0 |  | 2 |
| 5 | 停车牌与融雪剂 | 1517 | normal | 36.8 | 0 |  | 2 |
| 6 | 铁锹劈开融雪剂 | 1027 | normal | 89.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 4 章：
  - 情节与已写章节重复 0.71 ≥ 0.62（撞上「李振与王强在停车场因争夺车位发生冲突，李振用铁锹阻止王强…」）
  - [observe] 标题重复：「融雪剂与铁锹」已存在
- 第 5 章：
  - [observe] attr_adv_pct 23.1 > 18.0（结构塌缩）
  - [observe] 标题与《铁锹与融雪剂》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题与《铁锹与融雪剂》近似 0.77 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6265
chapter_chars_mean: 1044
chapter_chars_median: 1011
chapter_chars_cv: 0.23
paragraphs_mean: 35.2
dialogue_chars_pct: 20.2
dialogue_para_pct: 48.6
interiority_para_pct: 1.5
narration_para_pct: 49.9
turn_under20_pct: 96.2
turn_over200_pct: 0.0
attr_say_pct: 18.4
attr_adv_pct: 5.1
scenes_per_chapter: 1
dialogue_run_mean: 2.0
turn_len_median: 8
```
