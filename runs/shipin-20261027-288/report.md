# 鱼箱底的信 生成报告

slug：`shipin-20261027-288`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6702
LLM 调用：57 次，累计 147.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 信封与鱼箱对峙 | 877 | short | 37.9 | 0 |  | 2 |
| 2 | 信封坠入鱼箱裂痕 | 1208 | normal | 92.8 | 0 |  | 1 |
| 3 | 信封与鱼箱对峙 | 1151 | normal | 92.3 | 0 |  | 2 |
| 4 | 算盘滚落鱼箱边 | 1227 | normal | 90.3 | 0 |  | 0 |
| 5 | 鱼箱裂痕中的信封 | 1091 | normal | 92.0 | 0 |  | 1 |
| 6 | 信封与鱼箱对峙 | 1142 | normal | 88.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 28.0 低于目标 35.0
  - [observe] attr_adv_pct 28.6 > 18.0（结构塌缩）
- 第 2 章：
  - narration_para_pct 30.4 低于目标 35.0
- 第 3 章：
  - narration_para_pct 27.3 低于目标 35.0
  - [observe] 标题重复：「信封与鱼箱对峙」已存在
- 第 5 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 6 章：
  - [observe] 标题重复：「信封与鱼箱对峙」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6296
chapter_chars_mean: 1049
chapter_chars_median: 1078
chapter_chars_cv: 0.12
paragraphs_mean: 25.7
dialogue_chars_pct: 22.5
dialogue_para_pct: 61.4
interiority_para_pct: 1.8
narration_para_pct: 36.8
turn_under20_pct: 93.4
turn_over200_pct: 0.0
attr_say_pct: 47.1
attr_adv_pct: 3.7
scenes_per_chapter: 1
dialogue_run_mean: 2.8
turn_len_median: 10
```
