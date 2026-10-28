# 冰裂 生成报告

slug：`shipin-20261027-246`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6441
LLM 调用：57 次，累计 140.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摸信封的指尖 | 586 | short | 37.7 | 0 |  | 1 |
| 2 | 撕信封的一角 | 1148 | normal | 94.5 | 0 |  | 0 |
| 3 | 信封上的铁丝 | 1286 | normal | 36.2 | 0 |  | 1 |
| 4 | 铁丝缠住信封一角 | 1039 | normal | 92.3 | 0 |  | 0 |
| 5 | 铁丝缠住信封一角 | 1210 | normal | 36.3 | 0 |  | 2 |
| 6 | 冰台裂痕中的信封 | 1166 | normal | 35.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 552 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 5 章：
  - [observe] 章内自我复读 2 句（如「你们是不是都想瞒着什么？…」）
  - [observe] 标题重复：「铁丝缠住信封一角」已存在
- 第 6 章：
  - 单条套路句式超限：「老张和阿强」×3
  - dialogue_chars_pct 4.9 低于目标 5.0
  - [observe] 章内自我复读 2 句（如「突然，一声巨响传来，冰台一角裂开一道缝，冰屑四溅…」）

## 整书结构指标

```
chapters: 6
total_chars: 5971
chapter_chars_mean: 995
chapter_chars_median: 1054
chapter_chars_cv: 0.23
paragraphs_mean: 31.2
dialogue_chars_pct: 16.4
dialogue_para_pct: 43.0
interiority_para_pct: 1.8
narration_para_pct: 55.2
turn_under20_pct: 95.8
turn_over200_pct: 0.0
attr_say_pct: 32.7
attr_adv_pct: 8.3
scenes_per_chapter: 1.5
dialogue_run_mean: 1.7
turn_len_median: 9
```
