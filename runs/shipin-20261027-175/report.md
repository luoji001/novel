# 蓝钥匙 生成报告

slug：`shipin-20261027-175`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6654
LLM 调用：57 次，累计 129.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 箱角的细小凹陷 | 740 | short | 93.4 | 0 |  | 3 |
| 2 | 指纹触碰箱角 | 1072 | normal | 36.6 | 0 |  | 1 |
| 3 | 钥匙与便签的对峙 | 1103 | normal | 91.9 | 0 |  | 1 |
| 4 | 指纹触碰箱角 | 1498 | normal | 89.6 | 0 |  | 3 |
| 5 | 手电筒的光 | 1132 | normal | 92.8 | 0 |  | 0 |
| 6 | 敲箱寻父 | 1103 | normal | 87.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×3
  - narration_para_pct 15.0 低于目标 35.0
  - dialogue_run_mean 5.7 高于目标 4.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「那你为什么现在才来？…」）
- 第 3 章：
  - 单条套路句式超限：「李建国的」×3
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李建国站在」×3
  - [observe] 标题重复：「指纹触碰箱角」已存在
- 第 6 章：
  - 单条套路句式超限：「李建国的」×3
  - narration_para_pct 12.0 低于目标 35.0
  - dialogue_run_mean 7.3 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 6074
chapter_chars_mean: 1012
chapter_chars_median: 1004
chapter_chars_cv: 0.23
paragraphs_mean: 36.8
dialogue_chars_pct: 33.1
dialogue_para_pct: 62.6
interiority_para_pct: 0.4
narration_para_pct: 36.9
turn_under20_pct: 86.3
turn_over200_pct: 0.0
attr_say_pct: 40.6
attr_adv_pct: 0.0
scenes_per_chapter: 2.3
dialogue_run_mean: 3.7
turn_len_median: 9
```
