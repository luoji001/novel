# 蛇皮袋的坠落 生成报告

slug：`shipin-20261027-29`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6286
LLM 调用：57 次，累计 132.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 蛇皮袋的坠落 | 456 | short | 38.9 | 0 |  | 1 |
| 2 | 指纹印在身份证上 | 918 | normal | 37.4 | 0 |  | 1 |
| 3 | 蛇皮袋的坠落 | 1414 | normal | 93.5 | 0 |  | 1 |
| 4 | 蛇皮袋的坠落 | 1170 | normal | 21.8 | 0 |  | 4 |
| 5 | 身份证的裂痕 | 1025 | normal | 91.2 | 0 |  | 0 |
| 6 | 纸币洒满候车厅地板 | 1297 | normal | 91.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 394 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 858 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - [observe] 标题重复：「蛇皮袋的坠落」已存在
- 第 4 章：
  - 单条套路句式超限：「李国庆的」×8、「王德发的」×5
  - interiority_para_pct 6.1 高于目标 6.0
  - [observe] attr_adv_pct 100.0 > 18.0（结构塌缩）
  - [observe] 标题重复：「蛇皮袋的坠落」已存在
- 第 6 章：
  - 单条套路句式超限：「李国庆的」×3

## 整书结构指标

```
chapters: 6
total_chars: 5881
chapter_chars_mean: 980
chapter_chars_median: 1030
chapter_chars_cv: 0.34
paragraphs_mean: 25.8
dialogue_chars_pct: 15.1
dialogue_para_pct: 42.1
interiority_para_pct: 1.9
narration_para_pct: 56.0
turn_under20_pct: 97.6
turn_over200_pct: 0.0
attr_say_pct: 31.1
attr_adv_pct: 22.2
scenes_per_chapter: 1.3
dialogue_run_mean: 1.4
turn_len_median: 10
```
