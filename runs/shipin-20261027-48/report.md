# 灯影 生成报告

slug：`shipin-20261027-48`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6895
LLM 调用：57 次，累计 143.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 应急灯下的对峙 | 410 | short | 11.4 | 0 |  | 3 |
| 2 | 铅笔划破黄昏 | 1229 | normal | 36.2 | 0 |  | 1 |
| 3 | 手电筒照亮试卷 | 1386 | normal | 90.3 | 0 |  | 0 |
| 4 | 铅笔划破黄昏 | 1304 | normal | 90.7 | 0 |  | 2 |
| 5 | 铅笔卡在灯罩缝 | 1193 | normal | 90.4 | 0 |  | 0 |
| 6 | 红领巾映雪夜 | 1367 | normal | 58.4 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 359 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 3 句（如「这道题我刚才已经讲过了，你怎么还在抄？…」）
- 第 4 章：
  - 单条套路句式超限：「李国强的」×4
  - [observe] 标题重复：「铅笔划破黄昏」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6352
chapter_chars_mean: 1059
chapter_chars_median: 1187
chapter_chars_cv: 0.33
paragraphs_mean: 34.5
dialogue_chars_pct: 17.7
dialogue_para_pct: 39.6
interiority_para_pct: 0.4
narration_para_pct: 60.0
turn_under20_pct: 97.1
turn_over200_pct: 0.0
attr_say_pct: 57.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.5
turn_len_median: 9
```
