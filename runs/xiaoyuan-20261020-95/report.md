# 公告栏的撤下 生成报告

slug：`xiaoyuan-20261020-95`
档位：校园青春　闸门模式：observe
章数：9　总字数：20447
LLM 调用：100 次，累计 421.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 公告栏的名单 | 1393 | short | 96.1 | 0 |  | 1 |
| 2 | 袖口的摩挲 | 2719 | normal | 84.2 | 0 |  | 2 |
| 3 | 磁带的回响 | 2587 | normal | 24.2 | 0 |  | 1 |
| 4 | 课桌边缘的摩挲 | 2561 | normal | 84.8 | 0 |  | 1 |
| 5 | 钥匙转动的瞬间 | 2294 | normal | 91.2 | 0 |  | 1 |
| 6 | 手指抚过名单 | 2410 | normal | 90.0 | 0 |  | 3 |
| 7 | 银杏叶上的余温 | 2594 | normal | 92.0 | 0 |  | 1 |
| 8 | 课表上的圆圈 | 2679 | normal | 89.5 | 0 |  | 1 |
| 9 | 照片背面的字 | 1201 | short | 91.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 9.4 低于目标 15.0
- 第 2 章：
  - dialogue_chars_pct 17.5 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「因为公告栏上的名单还在，按照规定，它会在明天早上…」）
- 第 3 章：
  - dialogue_chars_pct 10.9 低于目标 20.0
- 第 4 章：
  - [observe] 章内自我复读 22 句（如「她的目光落向窗外，那片金色的光斑正慢慢变暗，就像…」）
- 第 5 章：
  - 单条套路句式超限：「林夏站在」×3
- 第 6 章：
  - 单条套路句式超限：「林夏站在」×3
  - narration_para_pct 13.1 低于目标 15.0
  - [observe] 章内自我复读 5 句（如「如果你愿意的话，我可以陪你一起走完这段路…」）
- 第 7 章：
  - 单条套路句式超限：「林夏站在」×3
- 第 8 章：
  - 情节与已写章节重复 0.70 ≥ 0.65（撞上「林夏在公告栏前与周野重逢，两人终于坦白心意，决定一起面对…」）
- 第 9 章：
  - dialogue_chars_pct 18.8 低于目标 20.0

## 整书结构指标

```
chapters: 9
total_chars: 19449
chapter_chars_mean: 2161
chapter_chars_median: 2432
chapter_chars_cv: 0.25
paragraphs_mean: 47.9
dialogue_chars_pct: 22.0
dialogue_para_pct: 60.3
interiority_para_pct: 18.3
narration_para_pct: 21.5
turn_under20_pct: 90.6
turn_over200_pct: 0.0
attr_say_pct: 50.5
attr_adv_pct: 4.2
scenes_per_chapter: 1.4
dialogue_run_mean: 2.7
turn_len_median: 10
```
