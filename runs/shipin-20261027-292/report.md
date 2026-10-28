# 铜铃 生成报告

slug：`shipin-20261027-292`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6451
LLM 调用：57 次，累计 126.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜币与红绳的触碰 | 465 | short | 22.2 | 0 |  | 1 |
| 2 | 手机镜头对准铜币 | 1207 | normal | 92.8 | 0 |  | 0 |
| 3 | 登记簿边缘的指纹 | 1325 | normal | 93.2 | 0 |  | 1 |
| 4 | 铜铃铛的震颤 | 998 | normal | 89.3 | 0 |  | 2 |
| 5 | 手机屏幕的闪光 | 1120 | normal | 54.5 | 0 |  | 1 |
| 6 | 铜铃铛落地无声 | 1330 | normal | 37.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 433 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 4 章：
  - 命中套话收尾句
  - dialogue_chars_pct 3.9 低于目标 5.0
- 第 5 章：
  - dialogue_chars_pct 4.2 低于目标 5.0
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「林小满没有回应，只是继续盯着手机屏幕…」）

## 整书结构指标

```
chapters: 6
total_chars: 6013
chapter_chars_mean: 1002
chapter_chars_median: 1100
chapter_chars_cv: 0.3
paragraphs_mean: 28.3
dialogue_chars_pct: 16.0
dialogue_para_pct: 43.9
interiority_para_pct: 0.9
narration_para_pct: 55.1
turn_under20_pct: 96.7
turn_over200_pct: 0.0
attr_say_pct: 31.8
attr_adv_pct: 0.0
scenes_per_chapter: 2.7
dialogue_run_mean: 1.6
turn_len_median: 8
```
