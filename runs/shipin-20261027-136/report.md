# 黑钥 生成报告

slug：`shipin-20261027-136`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6239
LLM 调用：57 次，累计 125.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙滑落底部 | 626 | short | 38.0 | 0 |  | 1 |
| 2 | 钥匙滑落底部 | 1247 | normal | 89.7 | 0 |  | 3 |
| 3 | 钥匙滑落底部 | 1117 | normal | 33.8 | 0 |  | 4 |
| 4 | 门禁卡贴上读卡器 | 1258 | normal | 92.6 | 0 |  | 0 |
| 5 | 钥匙擦过工牌边缘 | 1139 | normal | 36.2 | 0 |  | 2 |
| 6 | 钥匙顶开木门 | 846 | normal | 35.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 552 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「林小满的」×3
  - narration_para_pct 29.2 低于目标 35.0
  - [observe] 标题重复：「钥匙滑落底部」已存在
- 第 3 章：
  - interiority_para_pct 9.1 高于目标 6.0
  - narration_para_pct 31.8 低于目标 35.0
  - [observe] 章内自我复读 4 句（如「每个房间都有登记记录，你不该擅自开启…」）
  - [observe] 标题重复：「钥匙滑落底部」已存在
- 第 5 章：
  - narration_para_pct 29.6 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「规矩是为所有人制定的，不只是为了你一个人方便…」）
- 第 6 章：
  - [observe] 章节过短 762 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5809
chapter_chars_mean: 968
chapter_chars_median: 1064
chapter_chars_cv: 0.26
paragraphs_mean: 28
dialogue_chars_pct: 24.2
dialogue_para_pct: 54.8
interiority_para_pct: 3.6
narration_para_pct: 41.6
turn_under20_pct: 92.8
turn_over200_pct: 0.0
attr_say_pct: 39.6
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 2.3
turn_len_median: 12
```
