# 课表碎片 生成报告

slug：`xiaoyuan-20261020-118`
档位：校园青春　闸门模式：observe
章数：9　总字数：20883
LLM 调用：100 次，累计 459.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 校服外套的油渍 | 1567 | short | 48.4 | 0 |  | 3 |
| 2 | 课表的夹层秘密 | 2582 | normal | 93.0 | 0 |  | 2 |
| 3 | 磁带的沙沙声 | 2085 | normal | 87.6 | 0 |  | 1 |
| 4 | 钥匙的重量 | 2097 | normal | 92.4 | 0 |  | 2 |
| 5 | 名字的圆圈 | 2662 | normal | 92.1 | 0 |  | 3 |
| 6 | 校服外套的雪痕 | 2679 | normal | 87.6 | 0 |  | 4 |
| 7 | 实习证明的复印件 | 2974 | normal | 90.8 | 0 |  | 1 |
| 8 | 签字笔的余温 | 2496 | normal | 89.0 | 0 |  | 0 |
| 9 | 实习证明的复印件 | 1732 | short | 86.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「发现自己」×3
  - dialogue_chars_pct 17.7 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「她终于明白，为什么这两天总能在公告栏前看到那个熟…」）
- 第 2 章：
  - 单条套路句式超限：「苏婉秋站在」×3
  - [observe] 章内自我复读 1 句（如「苏婉秋站在储物柜前，手指轻轻拂过抽屉边缘…」）
- 第 3 章：
  - [observe] 章内自我复读 15 句（如「他知道，有些话说不出口，有些情感藏不住，就像此刻…」）
- 第 4 章：
  - 单条套路句式超限：「苏婉秋的」×3
  - attr_adv_pct 14.3 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「点了点头」×3
  - narration_para_pct 9.1 低于目标 15.0
  - [observe] 章内自我复读 8 句（如「她知道现在说什么都没用，只有等他真的离开之后，才…」）
- 第 6 章：
  - 单条套路句式超限：「带着一丝」×3
  - narration_para_pct 4.7 低于目标 15.0
  - [observe] 章内自我复读 10 句（如「林小满抬起头，“我偷偷把你那份课表藏起来了，一直…」）
  - [observe] 标题与《校服外套的油渍》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - narration_para_pct 14.1 低于目标 15.0
- 第 9 章：
  - interiority_para_pct 6.1 低于目标 8.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「实习证明的复印件」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19763
chapter_chars_mean: 2196
chapter_chars_median: 2360
chapter_chars_cv: 0.2
paragraphs_mean: 52.6
dialogue_chars_pct: 27.4
dialogue_para_pct: 69.8
interiority_para_pct: 14.5
narration_para_pct: 15.7
turn_under20_pct: 91.0
turn_over200_pct: 0.0
attr_say_pct: 30.7
attr_adv_pct: 4.9
scenes_per_chapter: 2
dialogue_run_mean: 4.0
turn_len_median: 9
```
