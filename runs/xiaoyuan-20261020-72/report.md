# 磁带的播放 生成报告

slug：`xiaoyuan-20261020-72`
档位：校园青春　闸门模式：observe
章数：9　总字数：19721
LLM 调用：100 次，累计 426.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 粉笔灰痕迹 | 1466 | short | 99.0 | 0 |  | 0 |
| 2 | 布料与月光 | 2494 | normal | 83.8 | 0 |  | 2 |
| 3 | 揉皱的课表 | 2393 | normal | 85.8 | 0 |  | 2 |
| 4 | 分科表的重量 | 2388 | normal | 91.8 | 0 |  | 1 |
| 5 | 分科表的重量 | 2410 | normal | 27.5 | 0 |  | 6 |
| 6 | 磁带的播放 | 2597 | normal | 89.0 | 0 |  | 1 |
| 7 | 分科表的重量 | 2060 | normal | 82.4 | 0 |  | 2 |
| 8 | 撕碎的课表边缘 | 2291 | normal | 91.9 | 0 |  | 1 |
| 9 | 分科表的重量 | 1613 | short | 86.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「点了点头」×3
  - [observe] 章内自我复读 37 句（如「周野看着手中的布料，想起那天晚上，他在广播站听到…」）
- 第 3 章：
  - dialogue_chars_pct 17.2 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「我最近一直在想，”他低声说，“如果我没有拿到那张…」）
- 第 4 章：
  - 单条套路句式超限：「教务处」×10、「林夏点点」×3
- 第 5 章：
  - dialogue_chars_pct 11.3 低于目标 20.0
  - interiority_para_pct 35.3 高于目标 35.0
  - attr_adv_pct 20.0 高于目标 12.0
  - dialogue_run_mean 1.3 低于目标 1.5
  - [observe] 章内自我复读 2 句（如「你是不是有什么话想说？…」）
  - [observe] 标题重复：「分科表的重量」已存在
- 第 6 章：
  - narration_para_pct 13.0 低于目标 15.0
- 第 7 章：
  - [observe] 章内自我复读 36 句（如「她终于问出了这句话，声音比平时轻了许多，“就是说…」）
  - [observe] 标题重复：「分科表的重量」已存在
- 第 8 章：
  - 单条套路句式超限：「林夏点点」×3
- 第 9 章：
  - interiority_para_pct 5.4 低于目标 8.0
  - [observe] 章内自我复读 16 句（如「林夏望着窗外，夜色正在一点点褪去，而他们之间的距…」）
  - [observe] 标题重复：「分科表的重量」已存在

## 整书结构指标

```
chapters: 9
total_chars: 18837
chapter_chars_mean: 2093
chapter_chars_median: 2284
chapter_chars_cv: 0.19
paragraphs_mean: 41.8
dialogue_chars_pct: 21.3
dialogue_para_pct: 56.6
interiority_para_pct: 20.1
narration_para_pct: 23.2
turn_under20_pct: 85.9
turn_over200_pct: 0.0
attr_say_pct: 45.2
attr_adv_pct: 5.5
scenes_per_chapter: 2.2
dialogue_run_mean: 2.6
turn_len_median: 11
```
