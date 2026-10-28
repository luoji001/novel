# 碎镜 生成报告

slug：`shipin-20261027-100`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5587
LLM 调用：57 次，累计 122.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 推子落回怀中 | 762 | short | 95.6 | 0 |  | 0 |
| 2 | 裂痕里的倒影 | 1184 | normal | 35.4 | 0 |  | 1 |
| 3 | 拼接碎镜的少年 | 907 | normal | 21.6 | 0 |  | 1 |
| 4 | 铜质推子碰撞声 | 892 | normal | 37.0 | 0 |  | 4 |
| 5 | 手指捡拾玻璃星 | 726 | normal | 36.0 | 0 |  | 1 |
| 6 | 指尖触碰碎镜光 | 1110 | normal | 90.3 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 12 句（如「陈师傅弯腰拾起一张纸，上面印着一则寻人启事，照片…」）
- 第 3 章：
  - [observe] 章节过短 854 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - narration_para_pct 20.8 低于目标 35.0
  - dialogue_run_mean 4.8 高于目标 4.0
  - [observe] 章内自我复读 6 句（如「就像你在镜子里看见的那样——”老周把账本轻轻放回…」）
  - [observe] 章节过短 829 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - [observe] 章节过短 687 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5218
chapter_chars_mean: 870
chapter_chars_median: 842
chapter_chars_cv: 0.19
paragraphs_mean: 21.8
dialogue_chars_pct: 23.0
dialogue_para_pct: 49.4
interiority_para_pct: 0.6
narration_para_pct: 50.1
turn_under20_pct: 89.4
turn_over200_pct: 0.0
attr_say_pct: 80.2
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 2.1
turn_len_median: 11
```
