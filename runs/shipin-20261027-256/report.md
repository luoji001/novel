# 船票 生成报告

slug：`shipin-20261027-256`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6780
LLM 调用：57 次，累计 134.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 暗格里的新船票 | 703 | short | 94.6 | 0 |  | 0 |
| 2 | 旧票落尘 | 1114 | normal | 91.6 | 0 |  | 0 |
| 3 | 触摸旧船票的指尖 | 1291 | normal | 91.5 | 0 |  | 3 |
| 4 | 触摸旧船票的指尖 | 1534 | normal | 92.1 | 0 |  | 1 |
| 5 | 抚摸帆布包的指腹 | 1291 | normal | 90.3 | 0 |  | 0 |
| 6 | 触摸铜徽的指腹 | 841 | normal | 36.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - 情节与已写章节重复 0.71 ≥ 0.62（撞上「小林持一张十年旧船票求老周购票，却被拒，最终得知船已停运…」）
  - narration_para_pct 21.4 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
- 第 4 章：
  - [observe] 标题重复：「触摸旧船票的指尖」已存在
- 第 6 章：
  - [observe] 章节过短 675 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 6259
chapter_chars_mean: 1043
chapter_chars_median: 1122
chapter_chars_cv: 0.31
paragraphs_mean: 31.7
dialogue_chars_pct: 20.7
dialogue_para_pct: 56.8
interiority_para_pct: 2.6
narration_para_pct: 40.5
turn_under20_pct: 92.7
turn_over200_pct: 0.0
attr_say_pct: 44.3
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 2.3
turn_len_median: 10
```
