# 铜铃 生成报告

slug：`shipin-20261027-261`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5721
LLM 调用：57 次，累计 126.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红色指示灯的低语 | 552 | short | 38.4 | 0 |  | 1 |
| 2 | 钥匙与停摆的挂钟 | 1206 | normal | 43.3 | 0 |  | 1 |
| 3 | 扫帚杆撞窗声 | 1098 | normal | 92.3 | 0 |  | 0 |
| 4 | 钥匙撞钟 | 1042 | normal | 89.3 | 0 |  | 1 |
| 5 | 计时器砸向屏幕 | 851 | normal | 19.0 | 0 |  | 3 |
| 6 | 钥匙撞钟 | 966 | normal | 35.7 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 498 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - interiority_para_pct 11.1 高于目标 6.0
- 第 4 章：
  - interiority_para_pct 7.1 高于目标 6.0
- 第 5 章：
  - dialogue_chars_pct 3.1 低于目标 5.0
  - narration_para_pct 93.8 高于目标 90.0
  - [observe] 章节过短 654 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - 单条套路句式超限：「小林站在」×3
  - dialogue_chars_pct 3.7 低于目标 5.0
  - narration_para_pct 91.3 高于目标 90.0
  - [observe] 章节过短 862 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「钥匙撞钟」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5192
chapter_chars_mean: 865
chapter_chars_median: 932
chapter_chars_cv: 0.28
paragraphs_mean: 32
dialogue_chars_pct: 9.5
dialogue_para_pct: 28.8
interiority_para_pct: 4.4
narration_para_pct: 66.9
turn_under20_pct: 99.0
turn_over200_pct: 0.0
attr_say_pct: 13.1
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.1
turn_len_median: 7
```
