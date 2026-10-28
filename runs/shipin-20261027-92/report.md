# 信封的重量 生成报告

slug：`shipin-20261027-92`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5632
LLM 调用：57 次，累计 124.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 信封坠地 | 644 | short | 21.3 | 0 |  | 1 |
| 2 | 执法记录仪的蓝光 | 410 | normal | 36.7 | 0 |  | 1 |
| 3 | 鱼鳞入袋的响动 | 1152 | normal | 93.5 | 0 |  | 0 |
| 4 | 鱼鳞入袋的响动 | 1398 | normal | 91.1 | 0 |  | 2 |
| 5 | 鱼鳞入袋的响动 | 1260 | normal | 92.8 | 0 |  | 2 |
| 6 | 鱼鳞入袋的响动 | 764 | normal | 35.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 596 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 352 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 标题重复：「鱼鳞入袋的响动」已存在
- 第 5 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 标题重复：「鱼鳞入袋的响动」已存在
- 第 6 章：
  - [observe] 章节过短 709 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「鱼鳞入袋的响动」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5288
chapter_chars_mean: 881
chapter_chars_median: 901
chapter_chars_cv: 0.44
paragraphs_mean: 20.8
dialogue_chars_pct: 20.0
dialogue_para_pct: 54.6
interiority_para_pct: 0.0
narration_para_pct: 45.4
turn_under20_pct: 94.4
turn_over200_pct: 0.0
attr_say_pct: 50.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.8
turn_len_median: 10
```
