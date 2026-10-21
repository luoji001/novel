# 磁带 生成报告

slug：`xiaoyuan-20261020-115`
档位：校园青春　闸门模式：observe
章数：9　总字数：20487
LLM 调用：100 次，累计 447.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 公告栏的空位 | 1348 | short | 97.8 | 0 |  | 1 |
| 2 | 储物柜的信件 | 2631 | normal | 94.6 | 0 |  | 2 |
| 3 | 磁带与麦克风 | 2600 | normal | 92.6 | 0 |  | 0 |
| 4 | 分科表的边缘 | 2370 | normal | 90.5 | 0 |  | 2 |
| 5 | 磁带与麦克风 | 2343 | normal | 90.8 | 0 |  | 2 |
| 6 | 磁带与折痕 | 2549 | normal | 91.0 | 0 |  | 2 |
| 7 | 磁带与折痕 | 2653 | normal | 81.9 | 0 |  | 3 |
| 8 | 课表的边缘 | 2508 | normal | 91.7 | 0 |  | 3 |
| 9 | 照片的空位 | 1476 | short | 85.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 14.3 低于目标 15.0
- 第 2 章：
  - narration_para_pct 11.1 低于目标 15.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「周朗点了点头」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「林夏站在」×3、「林夏点点」×3
  - [observe] 标题重复：「磁带与麦克风」已存在
- 第 6 章：
  - 单条套路句式超限：「林夏站在」×3
  - narration_para_pct 12.3 低于目标 15.0
- 第 7 章：
  - dialogue_chars_pct 19.7 低于目标 20.0
  - [observe] 章内自我复读 38 句（如「她突然想起昨天路过教务处门口时，看到公告栏上还贴…」）
  - [observe] 标题重复：「磁带与折痕」已存在
- 第 8 章：
  - 单条套路句式超限：「他知道自己」×3
  - [observe] 章内自我复读 3 句（如「那你去吧，但是小心点。她最近好像心情不太好…」）
  - [observe] 标题与《分科表的边缘》近似 0.73 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - [observe] 章内自我复读 21 句（如「她知道这意味着什么——再也不会有人坐在隔壁桌聊天…」）

## 整书结构指标

```
chapters: 9
total_chars: 19466
chapter_chars_mean: 2163
chapter_chars_median: 2389
chapter_chars_cv: 0.22
paragraphs_mean: 49.4
dialogue_chars_pct: 26.4
dialogue_para_pct: 64.3
interiority_para_pct: 14.9
narration_para_pct: 20.8
turn_under20_pct: 88.1
turn_over200_pct: 0.0
attr_say_pct: 29.6
attr_adv_pct: 6.3
scenes_per_chapter: 1.8
dialogue_run_mean: 2.7
turn_len_median: 10
```
