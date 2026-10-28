# 镜痕 生成报告

slug：`shipin-20261027-30`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6078
LLM 调用：57 次，累计 135.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 推子与镜子 | 745 | short | 95.3 | 0 |  | 1 |
| 2 | 镜子与账本 | 937 | normal | 56.2 | 0 |  | 0 |
| 3 | 搪瓷缸与旧照片 | 1179 | normal | 93.7 | 0 |  | 0 |
| 4 | 红布条与裂镜 | 991 | normal | 92.3 | 0 |  | 0 |
| 5 | 镜子与裂痕 | 1089 | normal | 91.3 | 0 |  | 1 |
| 6 | 镜子与裂痕 | 1131 | normal | 89.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 14.3 高于目标 10.0
- 第 5 章：
  - [observe] 标题与《镜子与账本》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题重复：「镜子与裂痕」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5649
chapter_chars_mean: 942
chapter_chars_median: 966
chapter_chars_cv: 0.17
paragraphs_mean: 28.5
dialogue_chars_pct: 26.9
dialogue_para_pct: 48.5
interiority_para_pct: 0.4
narration_para_pct: 51.2
turn_under20_pct: 92.5
turn_over200_pct: 0.0
attr_say_pct: 55.4
attr_adv_pct: 2.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.8
turn_len_median: 10
```
