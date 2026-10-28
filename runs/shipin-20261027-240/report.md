# 铜推子 生成报告

slug：`shipin-20261027-240`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6914
LLM 调用：57 次，累计 138.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 推子与红袖章 | 600 | short | 37.9 | 0 |  | 1 |
| 2 | 推子与红袖章 | 1280 | normal | 36.4 | 0 |  | 4 |
| 3 | 推子与旧账本 | 1121 | normal | 91.0 | 0 |  | 0 |
| 4 | 推子贴镜面 | 1407 | normal | 36.6 | 0 |  | 1 |
| 5 | 推子与旧时光 | 1270 | normal | 91.0 | 0 |  | 2 |
| 6 | 推子贴镜面 | 1230 | normal | 89.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 564 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 19.0 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
  - [observe] 章内自我复读 8 句（如「他说着突然压低嗓门，“现在倒好，你们都想着把旧东…」）
  - [observe] 标题重复：「推子与红袖章」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「你还记得那个夏天吗？…」）
- 第 5 章：
  - narration_para_pct 29.0 低于目标 35.0
  - [observe] 标题与《推子与旧账本》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 34.8 低于目标 35.0
  - [observe] 标题重复：「推子贴镜面」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6552
chapter_chars_mean: 1092
chapter_chars_median: 1182
chapter_chars_cv: 0.25
paragraphs_mean: 22.8
dialogue_chars_pct: 28.6
dialogue_para_pct: 60.8
interiority_para_pct: 0.6
narration_para_pct: 38.6
turn_under20_pct: 84.5
turn_over200_pct: 0.0
attr_say_pct: 24.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.4
turn_len_median: 10
```
