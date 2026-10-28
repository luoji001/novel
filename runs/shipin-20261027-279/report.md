# 锁扣 生成报告

slug：`shipin-20261027-279`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6330
LLM 调用：57 次，累计 134.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手电筒滚落冰面 | 768 | short | 95.9 | 0 |  | 0 |
| 2 | 保温杯底部的平安 | 947 | normal | 23.9 | 0 |  | 1 |
| 3 | 保温杯底部的平安 | 1222 | normal | 91.4 | 0 |  | 1 |
| 4 | 铁盒弹开的瞬间 | 1309 | normal | 93.8 | 0 |  | 0 |
| 5 | 手机屏幕的裂痕 | 950 | normal | 91.0 | 0 |  | 1 |
| 6 | 铁盒滚落的轨迹 | 1128 | normal | 36.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章节过短 865 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - [observe] 标题重复：「保温杯底部的平安」已存在
- 第 5 章：
  - 单条套路句式超限：「李岩和张强」×3
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「我在监控里看到了全过程…」）

## 整书结构指标

```
chapters: 6
total_chars: 5902
chapter_chars_mean: 984
chapter_chars_median: 966
chapter_chars_cv: 0.21
paragraphs_mean: 27.5
dialogue_chars_pct: 21.3
dialogue_para_pct: 51.2
interiority_para_pct: 1.2
narration_para_pct: 47.5
turn_under20_pct: 94.9
turn_over200_pct: 0.0
attr_say_pct: 59.3
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 2.0
turn_len_median: 8
```
