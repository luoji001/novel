# 二维码 生成报告

slug：`shipin-20261027-17`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6578
LLM 调用：57 次，累计 133.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 贴二维码 | 416 | short | 37.6 | 0 |  | 1 |
| 2 | 贴二维码 | 1019 | normal | 90.1 | 0 |  | 1 |
| 3 | 二维码贴纸摩擦声 | 1188 | normal | 89.5 | 0 |  | 2 |
| 4 | 二维码贴纸摩擦声 | 1251 | normal | 90.3 | 0 |  | 2 |
| 5 | 二维码撕扯声 | 1267 | normal | 89.5 | 0 |  | 3 |
| 6 | 二维码撕扯声 | 1431 | normal | 22.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 374 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 标题重复：「贴二维码」已存在
- 第 3 章：
  - 单条套路句式超限：「陈阿婆的」×4
  - narration_para_pct 21.1 低于目标 35.0
- 第 4 章：
  - 单条套路句式超限：「周志远的」×3
  - [observe] 标题重复：「二维码贴纸摩擦声」已存在
- 第 5 章：
  - narration_para_pct 25.0 低于目标 35.0
  - dialogue_run_mean 5 高于目标 4.0
  - [observe] 标题与《贴二维码》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - interiority_para_pct 7.3 高于目标 6.0
  - [observe] 章内自我复读 8 句（如「周志远沉默了一会儿，终于低声说道：“我知道你为什…」）
  - [observe] 标题重复：「二维码撕扯声」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6120
chapter_chars_mean: 1020
chapter_chars_median: 1146
chapter_chars_cv: 0.33
paragraphs_mean: 27.7
dialogue_chars_pct: 25.0
dialogue_para_pct: 54.1
interiority_para_pct: 2.5
narration_para_pct: 43.4
turn_under20_pct: 83.4
turn_over200_pct: 0.0
attr_say_pct: 7.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.5
turn_len_median: 10
```
