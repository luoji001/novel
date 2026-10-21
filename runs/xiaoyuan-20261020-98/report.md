# 铜铃 生成报告

slug：`xiaoyuan-20261020-98`
档位：校园青春　闸门模式：observe
章数：9　总字数：19755
LLM 调用：100 次，累计 424.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 校服上的褶皱 | 1273 | short | 90.8 | 0 |  | 2 |
| 2 | 校服里的磁带 | 2475 | normal | 93.8 | 0 |  | 3 |
| 3 | 名单边缘的指纹 | 2404 | normal | 91.4 | 0 |  | 3 |
| 4 | 磁带边缘的指纹 | 2398 | normal | 91.2 | 0 |  | 2 |
| 5 | 磁带边缘的指纹 | 2530 | normal | 90.5 | 0 |  | 3 |
| 6 | 铁盒里的借据 | 2168 | normal | 90.3 | 0 |  | 3 |
| 7 | 借条碎片的重量 | 2645 | normal | 89.2 | 0 |  | 2 |
| 8 | 借条碎片的重量 | 2384 | normal | 90.1 | 0 |  | 1 |
| 9 | 磁带盒里的落叶 | 1469 | short | 90.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 章内自我复读 17 句（如「而就在这个时候，他又想起了一件事，那就是那个隐藏…」）
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「苏雨桐的」×4
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「林晓阳的」×3
  - interiority_para_pct 5.6 低于目标 8.0
  - attr_adv_pct 15.8 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「林晓阳的」×4
  - [observe] 标题与《名单边缘的指纹》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「“我不知道」×3、「苏雨桐的」×3
  - narration_para_pct 14.6 低于目标 15.0
  - [observe] 标题重复：「磁带边缘的指纹」已存在
- 第 6 章：
  - 单条套路句式超限：「他知道这」×4
  - narration_para_pct 13.3 低于目标 15.0
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「林晓阳和苏雨桐」×4
  - attr_adv_pct 20.0 高于目标 12.0
- 第 8 章：
  - [observe] 标题重复：「借条碎片的重量」已存在
- 第 9 章：
  - interiority_para_pct 5.7 低于目标 8.0
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）

## 整书结构指标

```
chapters: 9
total_chars: 18794
chapter_chars_mean: 2088
chapter_chars_median: 2287
chapter_chars_cv: 0.22
paragraphs_mean: 45.6
dialogue_chars_pct: 29.1
dialogue_para_pct: 67.2
interiority_para_pct: 12.8
narration_para_pct: 20.0
turn_under20_pct: 82.5
turn_over200_pct: 0.0
attr_say_pct: 26.7
attr_adv_pct: 13.4
scenes_per_chapter: 2.9
dialogue_run_mean: 3.2
turn_len_median: 12
```
