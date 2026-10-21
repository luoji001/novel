# 磁带里的声音 生成报告

slug：`xiaoyuan-20261020-56`
档位：校园青春　闸门模式：observe
章数：9　总字数：18833
LLM 调用：100 次，累计 420.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 揉皱的纸片飘落 | 1239 | short | 77.2 | 0 |  | 3 |
| 2 | 袖口的字迹 | 2148 | normal | 94.5 | 0 |  | 2 |
| 3 | 磁带边缘的指纹 | 1953 | normal | 45.8 | 0 |  | 3 |
| 4 | 磁带盒里的声音 | 2384 | normal | 91.5 | 0 |  | 2 |
| 5 | 握紧的月考排名单 | 2735 | normal | 91.1 | 0 |  | 4 |
| 6 | 攥着挂号单的手 | 2341 | normal | 82.9 | 0 |  | 3 |
| 7 | 旧录音机的电流声 | 2371 | normal | 93.5 | 0 |  | 2 |
| 8 | 攥着挂号单的手 | 2047 | normal | 59.6 | 0 |  | 4 |
| 9 | 攥着挂号单的手 | 1606 | short | 84.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林修远的」×5
  - dialogue_chars_pct 14.2 低于目标 20.0
  - [observe] 章内自我复读 18 句（如「教室里其他同学似乎都没有注意到这件事，依旧忙着翻…」）
- 第 2 章：
  - narration_para_pct 9.2 低于目标 15.0
  - attr_adv_pct 14.3 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「苏晚晴的」×4
  - dialogue_chars_pct 13.5 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「希望你能找到更好的办法…」）
- 第 4 章：
  - 单条套路句式超限：「林修远的」×9
  - narration_para_pct 10.9 低于目标 15.0
- 第 5 章：
  - 单条套路句式超限：「苏晚晴的」×3
  - dialogue_chars_pct 18.0 低于目标 20.0
  - narration_para_pct 10.4 低于目标 15.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「林修远站在」×6、「苏晚晴的」×6、「他知道自己」×5
  - dialogue_chars_pct 16.9 低于目标 20.0
  - [observe] 章内自我复读 18 句（如「他想起之前看到的公告栏上的名单，想起老师说过的话…」）
- 第 7 章：
  - 单条套路句式超限：「林修远站在」×3、「”苏晚晴低」×3
  - narration_para_pct 6.5 低于目标 15.0
- 第 8 章：
  - 单条套路句式超限：「苏晚晴的」×4、「林修远点」×3、「知道自己」×3
  - dialogue_chars_pct 17.8 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「林修远盯着那张被撕碎的课表，想起上周苏晚晴还在那…」）
  - [observe] 标题重复：「攥着挂号单的手」已存在
- 第 9 章：
  - [observe] 章内自我复读 22 句（如「苏晚晴轻声说道，语气里有一种说不出的感觉，“可是…」）
  - [observe] 标题重复：「攥着挂号单的手」已存在

## 整书结构指标

```
chapters: 9
total_chars: 17902
chapter_chars_mean: 1989
chapter_chars_median: 2005
chapter_chars_cv: 0.22
paragraphs_mean: 43.8
dialogue_chars_pct: 20.7
dialogue_para_pct: 63.2
interiority_para_pct: 20.5
narration_para_pct: 16.4
turn_under20_pct: 93.3
turn_over200_pct: 0.0
attr_say_pct: 24.1
attr_adv_pct: 7.4
scenes_per_chapter: 2
dialogue_run_mean: 2.9
turn_len_median: 8
```
