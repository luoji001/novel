# 二维码风波 生成报告

slug：`shipin-20261027-255`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7000
LLM 调用：57 次，累计 144.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 炒粉锅磕桌沿 | 611 | short | 37.6 | 0 |  | 1 |
| 2 | 二维码被替换 | 1151 | normal | 97.4 | 0 |  | 0 |
| 3 | 炒粉锅砸饭盒 | 1296 | normal | 92.0 | 0 |  | 0 |
| 4 | 炒粉锅撞饭盒 | 1158 | normal | 91.0 | 0 |  | 1 |
| 5 | 炒粉锅撞饭盒 | 1295 | normal | 94.3 | 0 |  | 2 |
| 6 | 铜钥匙悬红绳 | 1483 | normal | 90.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 563 < 597（本章目标 1087 字的 55%）
- 第 4 章：
  - [observe] 标题与《炒粉锅砸饭盒》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 31.0 低于目标 35.0
  - [observe] 标题重复：「炒粉锅撞饭盒」已存在
- 第 6 章：
  - 单条套路句式超限：「陈阿强站在」×3、「陈阿强的」×3
  - narration_para_pct 18.8 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 6590
chapter_chars_mean: 1098
chapter_chars_median: 1160
chapter_chars_cv: 0.26
paragraphs_mean: 26.7
dialogue_chars_pct: 24.3
dialogue_para_pct: 63.4
interiority_para_pct: 0.7
narration_para_pct: 35.9
turn_under20_pct: 92.0
turn_over200_pct: 0.0
attr_say_pct: 13.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.2
turn_len_median: 8
```
