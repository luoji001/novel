# 验货单 生成报告

slug：`shuangwen-20261022-23`
档位：爽文　闸门模式：observe
章数：10　总字数：18073
LLM 调用：97 次，累计 349.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一张验收单 | 1856 | normal | 98.9 | 0 |  | 1 |
| 2 | 一张验收单 | 1753 | normal | 91.8 | 0 |  | 2 |
| 3 | 一张验收单 | 1614 | normal | 92.1 | 0 |  | 4 |
| 4 | 碎纸机的咔嗒声 | 1733 | normal | 92.9 | 0 |  | 2 |
| 5 | 一张验收单 | 1736 | normal | 93.6 | 0 |  | 3 |
| 6 | 一张验收单 | 1472 | normal | 93.2 | 0 |  | 3 |
| 7 | 一张验收单 | 1823 | normal | 92.9 | 0 |  | 2 |
| 8 | 一张验收单 | 1978 | normal | 90.7 | 0 |  | 5 |
| 9 | 一张验收单 | 1711 | normal | 93.0 | 0 |  | 3 |
| 10 | 一张验收单 | 2387 | long | 36.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×4、「市卫健委」×3
- 第 2 章：
  - 单条套路句式超限：「市卫健委」×3
  - [observe] 标题重复：「一张验收单」已存在
- 第 3 章：
  - 单条套路句式超限：「李建国的」×4
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 15 高于目标 14.0
  - [observe] 标题重复：「一张验收单」已存在
- 第 4 章：
  - 单条套路句式超限：「李建国的」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「市卫健委」×4、「李建国的」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「一张验收单」已存在
- 第 6 章：
  - attr_adv_pct 15.4 高于目标 12.0
  - dialogue_run_mean 16.5 高于目标 14.0
  - [observe] 标题重复：「一张验收单」已存在
- 第 7 章：
  - 单条套路句式超限：「李建国的」×3
  - [observe] 标题重复：「一张验收单」已存在
- 第 8 章：
  - 单条套路句式超限：「市卫健委」×3
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - dialogue_run_mean 20.5 高于目标 14.0
  - [observe] 标题重复：「一张验收单」已存在
- 第 9 章：
  - 单条套路句式超限：「李建国的」×4
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「一张验收单」已存在
- 第 10 章：
  - narration_para_pct 2.4 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「李建国说完，转身走向办公桌，拿起了一张纸，开始填…」）
  - [observe] 标题重复：「一张验收单」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17207
chapter_chars_mean: 1721
chapter_chars_median: 1670
chapter_chars_cv: 0.14
paragraphs_mean: 36.2
dialogue_chars_pct: 53.5
dialogue_para_pct: 88.6
interiority_para_pct: 4.2
narration_para_pct: 7.2
turn_under20_pct: 63.8
turn_over200_pct: 0.0
attr_say_pct: 22.4
attr_adv_pct: 12.0
scenes_per_chapter: 1.6
dialogue_run_mean: 10.0
turn_len_median: 16
```
