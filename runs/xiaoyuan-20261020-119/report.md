# 座位票 生成报告

slug：`xiaoyuan-20261020-119`
档位：校园青春　闸门模式：observe
章数：9　总字数：20162
LLM 调用：100 次，累计 428.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 课表上的新座位 | 1552 | short | 97.2 | 0 |  | 2 |
| 2 | 座位票的消失 | 3220 | normal | 93.8 | 0 |  | 2 |
| 3 | 旧磁带的日期 | 2110 | normal | 89.3 | 0 |  | 3 |
| 4 | 纸片上的名字 | 2440 | normal | 90.6 | 0 |  | 1 |
| 5 | 分科表的折叠痕迹 | 2309 | normal | 90.6 | 0 |  | 2 |
| 6 | 袖口的墨水痕迹 | 2183 | normal | 88.5 | 0 |  | 1 |
| 7 | 磁带边缘的刻痕 | 2080 | normal | 92.3 | 0 |  | 2 |
| 8 | 窗边的横幅 | 2590 | normal | 88.0 | 0 |  | 2 |
| 9 | 磁带边缘的刻痕 | 1669 | short | 92.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「教务处」×6
  - [observe] 章内自我复读 4 句（如「因为你坐的位置，”陈默笑着说，“我一直以为你会坐…」）
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×3
  - attr_adv_pct 15.6 高于目标 12.0
- 第 3 章：
  - dialogue_chars_pct 19.8 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 章内自我复读 14 句（如「她的目光扫过桌角，那张被压得平平的纸片正躺在那里…」）
- 第 4 章：
  - 单条套路句式超限：「教务处」×8、「林夏站在」×3、「说道“你」×3
- 第 5 章：
  - 单条套路句式超限：「林夏站在」×4、「教务处」×4、「林夏点点」×3
  - narration_para_pct 14.3 低于目标 15.0
- 第 6 章：
  - [observe] 章内自我复读 19 句（如「她记得很清楚，那天下着小雨，陈默把自己的外套脱下…」）
- 第 7 章：
  - 单条套路句式超限：「”陈默低」×3
  - interiority_para_pct 6.4 低于目标 8.0
- 第 8 章：
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 章内自我复读 14 句（如「她知道，这样的安排不会有任何改变，就像她心中那个…」）
- 第 9 章：
  - interiority_para_pct 7.3 低于目标 8.0
  - [observe] 标题重复：「磁带边缘的刻痕」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19113
chapter_chars_mean: 2124
chapter_chars_median: 2090
chapter_chars_cv: 0.22
paragraphs_mean: 49.6
dialogue_chars_pct: 25.9
dialogue_para_pct: 65.9
interiority_para_pct: 13.8
narration_para_pct: 20.2
turn_under20_pct: 89.7
turn_over200_pct: 0.0
attr_say_pct: 36.8
attr_adv_pct: 6.4
scenes_per_chapter: 2.6
dialogue_run_mean: 3.0
turn_len_median: 9
```
