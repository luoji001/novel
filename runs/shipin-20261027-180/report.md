# 硬币的重量 生成报告

slug：`shipin-20261027-180`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6601
LLM 调用：57 次，累计 121.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币落地的瞬间 | 668 | short | 96.8 | 0 |  | 0 |
| 2 | 身份证的倒影 | 1527 | normal | 90.5 | 0 |  | 0 |
| 3 | 计时器的跳动数字 | 1019 | normal | 91.8 | 0 |  | 0 |
| 4 | 钥匙与硬币的对峙 | 1319 | normal | 91.0 | 0 |  | 0 |
| 5 | 身份证的倒影 | 867 | normal | 22.7 | 0 |  | 3 |
| 6 | 硬币跌落的瞬间 | 1195 | normal | 90.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 5 章：
  - dialogue_chars_pct 4.1 低于目标 5.0
  - [observe] 章节过短 789 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「身份证的倒影」已存在
- 第 6 章：
  - [observe] 标题与《硬币落地的瞬间》近似 0.86 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6141
chapter_chars_mean: 1024
chapter_chars_median: 1028
chapter_chars_cv: 0.3
paragraphs_mean: 30.3
dialogue_chars_pct: 15.2
dialogue_para_pct: 39.6
interiority_para_pct: 1.5
narration_para_pct: 58.9
turn_under20_pct: 100.0
turn_over200_pct: 0.0
attr_say_pct: 11.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.4
turn_len_median: 9
```
