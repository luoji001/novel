# 钥匙圈 生成报告

slug：`shipin-20261027-80`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5936
LLM 调用：57 次，累计 135.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙板上的刮痕 | 787 | short | 38.0 | 0 |  | 1 |
| 2 | 藏匿盐焗鸡包装袋 | 845 | normal | 37.6 | 0 |  | 2 |
| 3 | 钥匙盒的触感 | 1286 | normal | 93.2 | 0 |  | 0 |
| 4 | 钥匙圈在掌心发烫 | 610 | normal | 35.9 | 0 |  | 1 |
| 5 | 钥匙盒的触感 | 1181 | normal | 91.4 | 0 |  | 2 |
| 6 | 钥匙圈的凹陷 | 1221 | normal | 59.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 2 章：
  - narration_para_pct 34.5 低于目标 35.0
  - [observe] 章节过短 769 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - [observe] 章节过短 530 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - narration_para_pct 27.3 低于目标 35.0
  - [observe] 标题重复：「钥匙盒的触感」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5545
chapter_chars_mean: 924
chapter_chars_median: 946
chapter_chars_cv: 0.31
paragraphs_mean: 24.5
dialogue_chars_pct: 21.3
dialogue_para_pct: 54.6
interiority_para_pct: 1.7
narration_para_pct: 43.7
turn_under20_pct: 93.5
turn_over200_pct: 0.0
attr_say_pct: 23.3
attr_adv_pct: 4.4
scenes_per_chapter: 2
dialogue_run_mean: 2.1
turn_len_median: 10
```
