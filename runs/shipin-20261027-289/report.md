# 录像带的最终归属 生成报告

slug：`shipin-20261027-289`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6947
LLM 调用：57 次，累计 136.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摸油渍的手指 | 482 | short | 17.0 | 0 |  | 2 |
| 2 | 录像带坠地瞬间 | 1437 | normal | 92.3 | 0 |  | 2 |
| 3 | 录像带与门禁卡对峙 | 1166 | normal | 89.0 | 0 |  | 0 |
| 4 | 触碰屏幕的指尖 | 1239 | normal | 89.4 | 0 |  | 1 |
| 5 | 摸油渍的手指 | 1162 | normal | 90.3 | 0 |  | 1 |
| 6 | 逆转的录像带 | 1455 | normal | 89.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 3.8 低于目标 5.0
  - [observe] 章节过短 450 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 16.7 低于目标 35.0
  - dialogue_run_mean 6.2 高于目标 4.0
- 第 4 章：
  - interiority_para_pct 6.7 高于目标 6.0
- 第 5 章：
  - [observe] 标题重复：「摸油渍的手指」已存在
- 第 6 章：
  - 单条套路句式超限：「小林站在」×3

## 整书结构指标

```
chapters: 6
total_chars: 6544
chapter_chars_mean: 1091
chapter_chars_median: 1128
chapter_chars_cv: 0.31
paragraphs_mean: 25.7
dialogue_chars_pct: 23.4
dialogue_para_pct: 55.9
interiority_para_pct: 1.2
narration_para_pct: 43.0
turn_under20_pct: 89.2
turn_over200_pct: 0.0
attr_say_pct: 33.8
attr_adv_pct: 0.0
scenes_per_chapter: 2.3
dialogue_run_mean: 2.4
turn_len_median: 10
```
