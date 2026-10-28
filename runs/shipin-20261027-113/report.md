# 蛇皮袋的重量 生成报告

slug：`shipin-20261027-113`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6954
LLM 调用：57 次，累计 143.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手电筒的光柱延伸 | 885 | short | 93.9 | 0 |  | 0 |
| 2 | 报纸撕裂的瞬间 | 1487 | normal | 88.9 | 0 |  | 3 |
| 3 | 塑料凳的阴影 | 1061 | normal | 93.0 | 0 |  | 0 |
| 4 | 塑料凳的阴影 | 937 | normal | 36.0 | 0 |  | 3 |
| 5 | 蛇皮袋的裂痕 | 1296 | normal | 91.2 | 0 |  | 0 |
| 6 | 蛇皮袋的裂痕 | 1282 | normal | 90.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「王小红的」×3
  - narration_para_pct 12.8 低于目标 35.0
  - dialogue_run_mean 6.8 高于目标 4.0
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「我娘走的时候，就是坐这个凳子离开的…」）
  - [observe] 章节过短 819 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「塑料凳的阴影」已存在
- 第 6 章：
  - 单条套路句式超限：「李建国的」×3
  - [observe] 标题重复：「蛇皮袋的裂痕」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6361
chapter_chars_mean: 1060
chapter_chars_median: 1052
chapter_chars_cv: 0.22
paragraphs_mean: 38
dialogue_chars_pct: 24.3
dialogue_para_pct: 52.9
interiority_para_pct: 0.8
narration_para_pct: 46.4
turn_under20_pct: 97.4
turn_over200_pct: 0.0
attr_say_pct: 43.8
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 2.3
turn_len_median: 10
```
