# 铜推子 生成报告

slug：`shipin-20261027-352`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6811
LLM 调用：57 次，累计 145.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 推子落地声 | 521 | short | 38.8 | 0 |  | 1 |
| 2 | 推子抵裂镜 | 1497 | normal | 89.5 | 0 |  | 0 |
| 3 | 铜推子与裂镜对峙 | 1273 | normal | 90.8 | 0 |  | 2 |
| 4 | 红袖章与铜推子对峙 | 976 | normal | 90.4 | 0 |  | 1 |
| 5 | 铜推子与裂镜对峙 | 1251 | normal | 87.5 | 0 |  | 2 |
| 6 | 铜推子与红袖章对峙 | 1287 | normal | 55.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 480 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 31.0 低于目标 35.0
  - [observe] 标题与《推子抵裂镜》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「老张站在」×3
- 第 5 章：
  - interiority_para_pct 7.1 高于目标 6.0
  - [observe] 标题重复：「铜推子与裂镜对峙」已存在
- 第 6 章：
  - [observe] 标题与《铜推子与裂镜对峙》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6389
chapter_chars_mean: 1065
chapter_chars_median: 1189
chapter_chars_cv: 0.31
paragraphs_mean: 25.7
dialogue_chars_pct: 20.2
dialogue_para_pct: 46.9
interiority_para_pct: 2.5
narration_para_pct: 50.6
turn_under20_pct: 90.4
turn_over200_pct: 0.0
attr_say_pct: 54.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.5
turn_len_median: 10
```
