# 蛇皮袋 生成报告

slug：`shipin-20261027-393`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7112
LLM 调用：57 次，累计 145.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 蛇皮袋的争夺 | 711 | short | 46.1 | 0 |  | 3 |
| 2 | 钥匙的归属 | 1660 | normal | 91.2 | 0 |  | 0 |
| 3 | 蛇皮袋的争夺 | 1356 | normal | 90.0 | 0 |  | 2 |
| 4 | 蛇皮袋的争夺 | 1319 | normal | 91.1 | 0 |  | 1 |
| 5 | 硬币与蛇皮袋相遇 | 891 | normal | 36.8 | 0 |  | 1 |
| 6 | 铜铃与烧伤疤痕 | 1169 | normal | 90.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×4、「王翠兰的」×3
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
- 第 3 章：
  - 单条套路句式超限：「李建国的」×6
  - [observe] 标题重复：「蛇皮袋的争夺」已存在
- 第 4 章：
  - [observe] 标题重复：「蛇皮袋的争夺」已存在
- 第 5 章：
  - [observe] 章节过短 803 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - 单条套路句式超限：「李建国站在」×3

## 整书结构指标

```
chapters: 6
total_chars: 6638
chapter_chars_mean: 1106
chapter_chars_median: 1156
chapter_chars_cv: 0.31
paragraphs_mean: 30.8
dialogue_chars_pct: 16.5
dialogue_para_pct: 48.8
interiority_para_pct: 0.4
narration_para_pct: 50.8
turn_under20_pct: 96.5
turn_over200_pct: 0.0
attr_say_pct: 40.5
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 2.2
turn_len_median: 8
```
