# 磁带 生成报告

slug：`xiaoyuan-20261020-139`
档位：校园青春　闸门模式：observe
章数：9　总字数：21960
LLM 调用：100 次，累计 441.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 磁带与纸条的温度 | 1699 | short | 95.5 | 0 |  | 1 |
| 2 | 调频器上的指纹 | 2262 | normal | 88.7 | 0 |  | 2 |
| 3 | 抚触裂痕的手指 | 2995 | normal | 93.2 | 0 |  | 1 |
| 4 | 袖口里的纸条 | 2999 | normal | 85.8 | 0 |  | 4 |
| 5 | 课表上的重叠时间 | 2951 | normal | 86.3 | 0 |  | 2 |
| 6 | 袖口里的银杏叶 | 2399 | normal | 91.2 | 0 |  | 1 |
| 7 | 黑板上的函数图像 | 2224 | normal | 86.6 | 0 |  | 2 |
| 8 | 袖口里的红绳 | 2460 | normal | 0.0 | 0 |  | 3 |
| 9 | 撕碎的课表 | 1962 | short | 93.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 2 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 23 句（如「陈老师摘下眼镜擦拭起来，眉头皱成了一个疙瘩，“昨…」）
- 第 3 章：
  - 单条套路句式超限：「林夏站在」×4
- 第 4 章：
  - 单条套路句式超限：「林夏点了点头」×3、「说道“我」×3
  - dialogue_chars_pct 17.4 低于目标 20.0
  - attr_adv_pct 15.8 高于目标 12.0
  - [observe] 章内自我复读 21 句（如「而在这一刻，林夏的心中充满了对未来的期望和憧憬，…」）
- 第 5 章：
  - 单条套路句式超限：「林夏点点」×4
  - [observe] 章内自我复读 35 句（如「她的目光落在桌面上的一张纸条上，那是她在前几天偶…」）
- 第 6 章：
  - [observe] 标题与《袖口里的纸条》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - dialogue_chars_pct 17.4 低于目标 20.0
  - [observe] 章内自我复读 5 句（如「她轻声回应，虽然心里清楚这只是暂时的答应…」）
- 第 8 章：
  - [observe] 章内自我复读 17 句（如「她知道，有些事情已经无法改变了，就像分科表已经贴…」）
  - [observe] dialogue_chars_pct 5.3 < 8.0（结构塌缩）
  - [observe] 标题与《袖口里的纸条》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - narration_para_pct 7.3 低于目标 15.0
  - [observe] attr_adv_pct 42.9 > 22.0（结构塌缩）

## 整书结构指标

```
chapters: 9
total_chars: 20954
chapter_chars_mean: 2328
chapter_chars_median: 2278
chapter_chars_cv: 0.19
paragraphs_mean: 47.9
dialogue_chars_pct: 22.3
dialogue_para_pct: 60.0
interiority_para_pct: 16.3
narration_para_pct: 23.7
turn_under20_pct: 86.3
turn_over200_pct: 0.0
attr_say_pct: 38.3
attr_adv_pct: 7.3
scenes_per_chapter: 3.3
dialogue_run_mean: 3.0
turn_len_median: 10
```
