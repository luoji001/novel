# 磁带的重量 生成报告

slug：`xiaoyuan-20261020-101`
档位：校园青春　闸门模式：observe
章数：9　总字数：20782
LLM 调用：100 次，累计 435.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 分科表的光点 | 1568 | short | 82.6 | 0 |  | 3 |
| 2 | 打开盒子的一刻 | 2714 | normal | 58.3 | 0 |  | 2 |
| 3 | 校服外套的褶皱 | 2449 | normal | 47.5 | 0 |  | 3 |
| 4 | 课表被水流浸湿 | 2530 | normal | 91.6 | 0 |  | 2 |
| 5 | 磁带的主人 | 2517 | normal | 92.6 | 0 |  | 1 |
| 6 | 钥匙转动的瞬间 | 2528 | normal | 89.4 | 0 |  | 2 |
| 7 | 磁带的主人 | 2304 | normal | 32.5 | 0 |  | 3 |
| 8 | 光斑的分割线 | 2527 | normal | 87.6 | 0 |  | 3 |
| 9 | 成绩单的褶皱 | 1636 | short | 91.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周远舟的」×5
  - dialogue_chars_pct 15.5 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「他们就这样站着，像两个并排的影子，中间隔着一条看…」）
- 第 2 章：
  - dialogue_chars_pct 15.0 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「她终于明白，有些人即使不在同一个班级，也能在某个…」）
- 第 3 章：
  - 单条套路句式超限：「周远舟的」×4
  - dialogue_chars_pct 13.7 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「外面的天色渐渐明亮起来，阳光透过走廊尽头的窗户照…」）
- 第 4 章：
  - 单条套路句式超限：「周远舟的」×3
  - [observe] 章内自我复读 15 句（如「他低头看着手中的课表，上面密密麻麻地写着各种课程…」）
- 第 5 章：
  - 单条套路句式超限：「林小满的」×4
- 第 6 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 12 句（如「陈老师笑了笑：“下次如果你感兴趣，可以来找我聊聊…」）
- 第 7 章：
  - 单条套路句式超限：「他知道这」×3、「林小满的」×3
  - dialogue_chars_pct 11.9 低于目标 20.0
  - [observe] 标题重复：「磁带的主人」已存在
- 第 8 章：
  - 单条套路句式超限：「周远舟的」×4
  - narration_para_pct 11.8 低于目标 15.0
  - [observe] 章内自我复读 22 句（如「林小满忽然觉得，这光斑似乎也在悄悄挪动，像是在寻…」）
- 第 9 章：
  - 单条套路句式超限：「林小满的」×6
  - interiority_para_pct 6.9 低于目标 8.0
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）

## 整书结构指标

```
chapters: 9
total_chars: 19825
chapter_chars_mean: 2203
chapter_chars_median: 2368
chapter_chars_cv: 0.18
paragraphs_mean: 45.6
dialogue_chars_pct: 22.8
dialogue_para_pct: 61.2
interiority_para_pct: 15.8
narration_para_pct: 23.0
turn_under20_pct: 87.7
turn_over200_pct: 0.0
attr_say_pct: 31.2
attr_adv_pct: 2.9
scenes_per_chapter: 3.8
dialogue_run_mean: 3.4
turn_len_median: 11
```
