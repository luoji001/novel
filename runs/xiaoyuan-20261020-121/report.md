# 红印章 生成报告

slug：`xiaoyuan-20261020-121`
档位：校园青春　闸门模式：observe
章数：9　总字数：20041
LLM 调用：100 次，累计 434.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 风铃与褪色分科表 | 1555 | short | 93.9 | 0 |  | 1 |
| 2 | 笔记本里的小猫 | 2609 | normal | 93.8 | 0 |  | 2 |
| 3 | 课表边缘的指纹 | 2576 | normal | 87.9 | 0 |  | 3 |
| 4 | 分科名单被揉皱 | 2236 | normal | 90.8 | 0 |  | 0 |
| 5 | 校服外套上的发丝 | 2309 | normal | 90.1 | 0 |  | 2 |
| 6 | 磁带头摩擦声 | 2292 | normal | 92.8 | 0 |  | 1 |
| 7 | 分科表的红印章 | 2424 | normal | 92.7 | 0 |  | 1 |
| 8 | 撕碎的分科名单 | 2456 | normal | 91.6 | 0 |  | 1 |
| 9 | 褪色名单的余温 | 1575 | short | 91.9 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 16.7 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林晓阳的」×5
  - narration_para_pct 13.0 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「林晓阳的」×3
  - dialogue_chars_pct 18.0 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「林晓阳的」×5
  - attr_adv_pct 12.5 高于目标 12.0
- 第 6 章：
  - narration_para_pct 14.5 低于目标 15.0
- 第 7 章：
  - 单条套路句式超限：「林晓阳点点」×3、「林晓阳的」×3
- 第 8 章：
  - 单条套路句式超限：「林晓阳站在」×3

## 整书结构指标

```
chapters: 9
total_chars: 19044
chapter_chars_mean: 2116
chapter_chars_median: 2213
chapter_chars_cv: 0.18
paragraphs_mean: 45.4
dialogue_chars_pct: 24.8
dialogue_para_pct: 64.5
interiority_para_pct: 14.8
narration_para_pct: 20.7
turn_under20_pct: 87.8
turn_over200_pct: 0.0
attr_say_pct: 40.7
attr_adv_pct: 4.4
scenes_per_chapter: 2
dialogue_run_mean: 2.9
turn_len_median: 10
```
