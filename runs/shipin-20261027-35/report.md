# 锈钥 生成报告

slug：`shipin-20261027-35`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6412
LLM 调用：57 次，累计 139.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕扯皮箱的锁扣 | 602 | short | 39.6 | 0 |  | 2 |
| 2 | 抚触泛黄纸片 | 1315 | normal | 90.4 | 0 |  | 1 |
| 3 | 摩挲锈迹的钥匙 | 1236 | normal | 92.5 | 0 |  | 1 |
| 4 | 摩挲锈迹的钥匙 | 1073 | normal | 56.8 | 0 |  | 1 |
| 5 | 摩挲清洁工具包 | 1003 | normal | 91.7 | 0 |  | 1 |
| 6 | 撕扯皮箱的锁扣 | 1177 | normal | 36.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×3
  - [observe] 章节过短 545 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 29.4 低于目标 35.0
- 第 3 章：
  - 单条套路句式超限：「李国强的」×3
- 第 4 章：
  - [observe] 标题重复：「摩挲锈迹的钥匙」已存在
- 第 5 章：
  - narration_para_pct 91.1 高于目标 90.0
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「铁锈味混着汗酸味冲进鼻腔，李国强感到有什么东西正…」）
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）
  - [observe] 标题重复：「撕扯皮箱的锁扣」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5919
chapter_chars_mean: 986
chapter_chars_median: 1064
chapter_chars_cv: 0.25
paragraphs_mean: 33.2
dialogue_chars_pct: 18.3
dialogue_para_pct: 40.3
interiority_para_pct: 1.6
narration_para_pct: 58.2
turn_under20_pct: 94.6
turn_over200_pct: 0.0
attr_say_pct: 13.8
attr_adv_pct: 9.4
scenes_per_chapter: 1.3
dialogue_run_mean: 1.6
turn_len_median: 10
```
