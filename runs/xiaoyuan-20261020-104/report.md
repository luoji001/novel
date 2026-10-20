# 分科表 生成报告

slug：`xiaoyuan-20261020-104`
档位：校园青春　闸门模式：observe
章数：9　总字数：20339
LLM 调用：100 次，累计 434.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁门的轻响 | 1361 | short | 88.9 | 0 |  | 2 |
| 2 | 钥匙的沉默时刻 | 2522 | normal | 89.0 | 0 |  | 4 |
| 3 | 广播的余韵 | 2477 | normal | 93.9 | 0 |  | 2 |
| 4 | 钥匙的沉默时刻 | 2573 | normal | 82.4 | 0 |  | 2 |
| 5 | 纸飞机的轨迹 | 2359 | normal | 92.1 | 0 |  | 1 |
| 6 | 校服外套的褶皱 | 2636 | normal | 90.7 | 0 |  | 1 |
| 7 | 磁带的温度 | 2407 | normal | 91.9 | 0 |  | 2 |
| 8 | 擦拭公告栏的指纹 | 2463 | normal | 59.2 | 0 |  | 3 |
| 9 | 手指画圈 | 1532 | short | 84.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周子航的」×4
  - dialogue_chars_pct 14.9 低于目标 20.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周子航的」×4、「他知道这」×4、「林小满站在」×3
  - dialogue_chars_pct 18.6 低于目标 20.0
  - [observe] 章内自我复读 5 句（如「你知道吗？我一直都觉得，我们之间有一些特别的东西…」）
- 第 3 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 5 句（如「他知道，这不仅仅是一个关于音乐的选择，更像是一个…」）
- 第 4 章：
  - [observe] 章内自我复读 37 句（如「林小满望向教室后墙，那张分科表已经被钉在那里，上…」）
  - [observe] 标题重复：「钥匙的沉默时刻」已存在
- 第 5 章：
  - 单条套路句式超限：「周子航的」×4
- 第 6 章：
  - 单条套路句式超限：「林小满的」×6、「带着一丝」×3
- 第 7 章：
  - 单条套路句式超限：「林小满站在」×3
  - attr_adv_pct 15.8 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「林小满站在」×3、「他知道自己」×3、「周子航的」×3
  - dialogue_chars_pct 15.1 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 12.0
- 第 9 章：
  - dialogue_chars_pct 13.2 低于目标 20.0

## 整书结构指标

```
chapters: 9
total_chars: 19384
chapter_chars_mean: 2154
chapter_chars_median: 2347
chapter_chars_cv: 0.21
paragraphs_mean: 45.3
dialogue_chars_pct: 22.8
dialogue_para_pct: 60.7
interiority_para_pct: 15.3
narration_para_pct: 24.0
turn_under20_pct: 87.6
turn_over200_pct: 0.0
attr_say_pct: 22.7
attr_adv_pct: 6.2
scenes_per_chapter: 2.6
dialogue_run_mean: 2.8
turn_len_median: 9
```
