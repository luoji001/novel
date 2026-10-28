# 铁门 生成报告

slug：`shipin-20261027-163`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5733
LLM 调用：57 次，累计 126.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 锁孔里的钥匙声 | 535 | short | 38.8 | 0 |  | 2 |
| 2 | 监控屏幕的嗡鸣声 | 1016 | normal | 58.4 | 0 |  | 1 |
| 3 | 钥匙与铁门的痕迹 | 1289 | normal | 91.7 | 0 |  | 0 |
| 4 | 钥匙摩擦车门声 | 949 | normal | 47.5 | 0 |  | 2 |
| 5 | 钥匙坠入垃圾桶声 | 753 | normal | 37.2 | 0 |  | 1 |
| 6 | 钥匙撬门的瞬间 | 1185 | normal | 45.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 4.9 低于目标 5.0
  - [observe] 章节过短 472 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - dialogue_chars_pct 4.6 低于目标 5.0
- 第 4 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
- 第 5 章：
  - [observe] 章节过短 673 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - interiority_para_pct 10.0 高于目标 6.0

## 整书结构指标

```
chapters: 6
total_chars: 5270
chapter_chars_mean: 878
chapter_chars_median: 912
chapter_chars_cv: 0.31
paragraphs_mean: 30.3
dialogue_chars_pct: 10.0
dialogue_para_pct: 19.8
interiority_para_pct: 3.1
narration_para_pct: 77.1
turn_under20_pct: 98.4
turn_over200_pct: 0.0
attr_say_pct: 14.1
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 1.6
turn_len_median: 8
```
