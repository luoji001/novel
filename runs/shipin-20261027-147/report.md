# 血衣 生成报告

slug：`shipin-20261027-147`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6517
LLM 调用：57 次，累计 133.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 箱子上的铭牌 | 652 | short | 38.8 | 0 |  | 1 |
| 2 | 钥匙敲击登记簿 | 1389 | normal | 37.1 | 0 |  | 1 |
| 3 | 冻窗上的霜花痕迹 | 1096 | normal | 18.5 | 0 |  | 1 |
| 4 | 撕碎的火车票 | 1295 | normal | 36.6 | 0 |  | 1 |
| 5 | 钥匙敲击登记簿 | 1161 | normal | 91.1 | 0 |  | 1 |
| 6 | 铁门凹陷三指宽 | 918 | normal | 37.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 578 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 3 章：
  - [observe] 章内自我复读 3 句（如「G1236次列车即将恢复运行，请乘客注意听候车厅…」）
- 第 4 章：
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 5 章：
  - [observe] 标题重复：「钥匙敲击登记簿」已存在
- 第 6 章：
  - [observe] 章节过短 789 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 6040
chapter_chars_mean: 1007
chapter_chars_median: 1074
chapter_chars_cv: 0.27
paragraphs_mean: 31.8
dialogue_chars_pct: 21.3
dialogue_para_pct: 48.2
interiority_para_pct: 0.0
narration_para_pct: 51.8
turn_under20_pct: 79.0
turn_over200_pct: 0.0
attr_say_pct: 19.7
attr_adv_pct: 13.9
scenes_per_chapter: 2.5
dialogue_run_mean: 1.8
turn_len_median: 9
```
