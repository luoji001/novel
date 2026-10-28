# 可乐罐 生成报告

slug：`shipin-20261027-09`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6429
LLM 调用：57 次，累计 141.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 监控屏幕的晃动 | 466 | short | 38.8 | 0 |  | 1 |
| 2 | 钥匙串与可乐罐对峙 | 1299 | normal | 91.2 | 0 |  | 0 |
| 3 | 红色记号笔的痕迹 | 1091 | normal | 92.9 | 0 |  | 1 |
| 4 | 可乐罐与钥匙串对峙 | 1235 | normal | 36.8 | 0 |  | 1 |
| 5 | 钥匙串与可乐罐对峙 | 1022 | normal | 90.8 | 0 |  | 2 |
| 6 | 可乐罐与钥匙串对峙 | 1310 | normal | 90.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 405 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 4 章：
  - [observe] attr_adv_pct 28.6 > 18.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×3
  - [observe] 标题重复：「钥匙串与可乐罐对峙」已存在
- 第 6 章：
  - [observe] 标题重复：「可乐罐与钥匙串对峙」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5937
chapter_chars_mean: 990
chapter_chars_median: 1072
chapter_chars_cv: 0.31
paragraphs_mean: 29.5
dialogue_chars_pct: 20.8
dialogue_para_pct: 47.1
interiority_para_pct: 1.3
narration_para_pct: 51.6
turn_under20_pct: 92.1
turn_over200_pct: 0.0
attr_say_pct: 41.1
attr_adv_pct: 8.5
scenes_per_chapter: 1.7
dialogue_run_mean: 1.7
turn_len_median: 10
```
