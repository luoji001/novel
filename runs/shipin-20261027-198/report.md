# 裂镜 生成报告

slug：`shipin-20261027-198`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6919
LLM 调用：57 次，累计 174.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜质推子的震颤 | 627 | short | 38.2 | 0 |  | 1 |
| 2 | 铜质推子的震颤 | 1189 | normal | 92.3 | 0 |  | 1 |
| 3 | 触摸裂痕的掌心 | 1625 | normal | 36.0 | 0 |  | 1 |
| 4 | 镜子的裂痕 | 977 | normal | 90.2 | 0 |  | 0 |
| 5 | 争夺铜推子 | 1201 | normal | 90.2 | 0 |  | 0 |
| 6 | 传递铜推子的掌心 | 1294 | normal | 88.0 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 572 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 标题重复：「铜质推子的震颤」已存在
- 第 3 章：
  - [observe] 章内自我复读 3 句（如「他说，声音有些发颤，“这把推子，是我师父教我的…」）

## 整书结构指标

```
chapters: 6
total_chars: 6487
chapter_chars_mean: 1081
chapter_chars_median: 1123
chapter_chars_cv: 0.3
paragraphs_mean: 28.3
dialogue_chars_pct: 23.9
dialogue_para_pct: 52.5
interiority_para_pct: 2.2
narration_para_pct: 45.3
turn_under20_pct: 92.4
turn_over200_pct: 0.0
attr_say_pct: 48.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 2.0
turn_len_median: 10
```
