# 鱼钩 生成报告

slug：`shipin-20261027-50`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6208
LLM 调用：57 次，累计 155.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 鱼钩勾起信封 | 319 | short | 21.5 | 0 |  | 3 |
| 2 | 信封与鱼箱较量 | 1012 | normal | 91.9 | 0 |  | 0 |
| 3 | 信封坠入鱼箱缝隙 | 1331 | normal | 91.7 | 0 |  | 0 |
| 4 | 鱼钩勾住信封边缘 | 1287 | normal | 89.0 | 0 |  | 1 |
| 5 | 铜纽扣的寒光 | 1068 | normal | 90.3 | 0 |  | 0 |
| 6 | 鱼钩勾住信封边缘 | 1185 | normal | 37.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 3.2 低于目标 5.0
  - narration_para_pct 91.7 高于目标 90.0
  - [observe] 章节过短 281 < 597（本章目标 1087 字的 55%）
- 第 4 章：
  - [observe] 标题与《鱼钩勾起信封》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 29.6 低于目标 35.0
  - [observe] 章内自我复读 1 句（如「那是我爸最后的手迹！…」）
  - [observe] 标题重复：「鱼钩勾住信封边缘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5797
chapter_chars_mean: 966
chapter_chars_median: 1058
chapter_chars_cv: 0.37
paragraphs_mean: 26.2
dialogue_chars_pct: 16.5
dialogue_para_pct: 46.2
interiority_para_pct: 0.0
narration_para_pct: 53.8
turn_under20_pct: 93.9
turn_over200_pct: 0.0
attr_say_pct: 45.0
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.8
turn_len_median: 8
```
