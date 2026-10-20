# 未发的消息 生成报告

slug：`xiaoyuan-20261020-26`
档位：校园青春　闸门模式：observe
章数：9　总字数：20415
LLM 调用：100 次，累计 439.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指划过公告栏 | 1387 | short | 98.8 | 0 |  | 0 |
| 2 | 手指抚过笔记本边缘 | 2913 | normal | 92.6 | 0 |  | 3 |
| 3 | 抚摸袖口的裂痕 | 2585 | normal | 7.5 | 0 |  | 2 |
| 4 | 手指抚过笔记本边缘 | 2820 | normal | 90.1 | 0 |  | 5 |
| 5 | 抚摸袖口的裂痕 | 2204 | normal | 86.0 | 0 |  | 5 |
| 6 | 手指抚过分科表 | 2378 | normal | 56.7 | 0 |  | 3 |
| 7 | 摩挲分科表边缘 | 2161 | normal | 10.0 | 0 |  | 3 |
| 8 | 摩挲分科表边缘 | 2338 | normal | 90.6 | 0 |  | 3 |
| 9 | 抚摸袖口的裂痕 | 1620 | short | 81.8 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「周明远的」×7
  - narration_para_pct 8.9 低于目标 15.0
  - attr_adv_pct 15.8 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「周明远的」×5、「知道自己」×5、「林夏站在」×3
  - dialogue_chars_pct 8.9 低于目标 20.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「点了点头」×4、「林夏站在」×4
  - narration_para_pct 12.5 低于目标 15.0
  - [observe] 章内自我复读 11 句（如「她知道有些话说出来就不叫秘密了，就像那些藏在笔记…」）
  - [observe] 标题重复：「手指抚过笔记本边缘」已存在
- 第 5 章：
  - 单条套路句式超限：「带着一丝」×3、「知道自己」×3
  - dialogue_chars_pct 19.4 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 章内自我复读 20 句（如「她知道，自己已经不再是那个无忧无虑的女孩了，而是…」）
  - [observe] 标题重复：「抚摸袖口的裂痕」已存在
- 第 6 章：
  - 单条套路句式超限：「林夏站在」×4
  - dialogue_chars_pct 14.8 低于目标 20.0
  - narration_para_pct 13.5 低于目标 15.0
- 第 7 章：
  - dialogue_chars_pct 9.2 低于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5
  - [observe] 章内自我复读 1 句（如「那上面还沾着一点粉笔灰，可能是刚才有人路过时蹭上…」）
- 第 8 章：
  - 单条套路句式超限：「林夏点点」×4、「林夏站在」×3
  - narration_para_pct 12.8 低于目标 15.0
  - [observe] 标题重复：「摩挲分科表边缘」已存在
- 第 9 章：
  - 单条套路句式超限：「林夏站在」×3
  - dialogue_chars_pct 16.2 低于目标 20.0
  - narration_para_pct 10.3 低于目标 15.0
  - [observe] 章内自我复读 16 句（如「直到走到楼梯口，听见有人在议论什么，她才想起昨天…」）
  - [observe] 标题重复：「抚摸袖口的裂痕」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19505
chapter_chars_mean: 2167
chapter_chars_median: 2229
chapter_chars_cv: 0.22
paragraphs_mean: 42.3
dialogue_chars_pct: 19.6
dialogue_para_pct: 62.7
interiority_para_pct: 19.1
narration_para_pct: 18.1
turn_under20_pct: 87.7
turn_over200_pct: 0.0
attr_say_pct: 43.0
attr_adv_pct: 5.7
scenes_per_chapter: 2.4
dialogue_run_mean: 4.1
turn_len_median: 9
```
