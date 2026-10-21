# 冻笔 生成报告

slug：`xiaoyuan-20261020-149`
档位：校园青春　闸门模式：observe
章数：9　总字数：20179
LLM 调用：100 次，累计 445.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 贴课表的手指 | 1064 | short | 34.9 | 0 |  | 3 |
| 2 | 磁带盒的缝隙 | 2272 | normal | 95.2 | 0 |  | 1 |
| 3 | 铅笔划破素描本 | 2434 | normal | 93.1 | 0 |  | 1 |
| 4 | 素描本上的指纹 | 2687 | normal | 89.0 | 0 |  | 3 |
| 5 | 素描纸上的蓝痕 | 2405 | normal | 87.8 | 0 |  | 2 |
| 6 | 素描纸上的蓝痕 | 2581 | normal | 91.8 | 0 |  | 1 |
| 7 | 素描纸上的蓝痕 | 2460 | normal | 89.4 | 0 |  | 2 |
| 8 | 磁带盒的缝隙 | 2663 | normal | 87.0 | 0 |  | 2 |
| 9 | 素描纸上的蓝痕 | 1604 | short | 86.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林夏站在」×3
  - dialogue_chars_pct 11.8 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「那上面写着“美术班”的字样，旁边还有一排小字：“…」）
- 第 2 章：
  - narration_para_pct 13.7 低于目标 15.0
- 第 3 章：
  - attr_adv_pct 15.0 高于目标 12.0
- 第 4 章：
  - 命中套话收尾句
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 章内自我复读 13 句（如「他知道，这只是一个开始，就像那些被风吹散的雪片，…」）
- 第 5 章：
  - interiority_para_pct 7.5 低于目标 8.0
  - [observe] 章内自我复读 16 句（如「她的视线停留在桌面上那一小块被墨迹晕染的地方，那…」）
- 第 6 章：
  - [observe] 标题重复：「素描纸上的蓝痕」已存在
- 第 7 章：
  - [observe] 章内自我复读 5 句（如「你怎么又一个人待在这里？…」）
  - [observe] 标题重复：「素描纸上的蓝痕」已存在
- 第 8 章：
  - [observe] 章内自我复读 16 句（如「画室里的空气似乎变得更加安静了一些，仿佛连时间也…」）
  - [observe] 标题重复：「磁带盒的缝隙」已存在
- 第 9 章：
  - dialogue_chars_pct 17.1 低于目标 20.0
  - [observe] 标题重复：「素描纸上的蓝痕」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19168
chapter_chars_mean: 2130
chapter_chars_median: 2319
chapter_chars_cv: 0.24
paragraphs_mean: 48.3
dialogue_chars_pct: 24.9
dialogue_para_pct: 63.9
interiority_para_pct: 13.0
narration_para_pct: 23.1
turn_under20_pct: 89.0
turn_over200_pct: 0.0
attr_say_pct: 43.1
attr_adv_pct: 4.5
scenes_per_chapter: 3.1
dialogue_run_mean: 3.2
turn_len_median: 10
```
