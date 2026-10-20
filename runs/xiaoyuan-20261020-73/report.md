# 袖口上的名字 生成报告

slug：`xiaoyuan-20261020-73`
档位：校园青春　闸门模式：observe
章数：9　总字数：21056
LLM 调用：100 次，累计 456.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕碎的分科表 | 1174 | short | 37.0 | 0 |  | 2 |
| 2 | 缝补袖口的对话 | 2749 | normal | 93.8 | 0 |  | 2 |
| 3 | 磁带里的声音 | 2738 | normal | 90.9 | 0 |  | 2 |
| 4 | 缝补袖口的对话 | 2610 | normal | 91.4 | 0 |  | 3 |
| 5 | 缝补袖口的对话 | 2701 | normal | 90.5 | 0 |  | 2 |
| 6 | 缝补袖口的对话 | 2871 | normal | 86.8 | 0 |  | 3 |
| 7 | 缝补袖口的对话 | 2153 | normal | 91.4 | 0 |  | 3 |
| 8 | 缝补袖口的对话 | 2514 | normal | 90.2 | 0 |  | 3 |
| 9 | 缝补袖口的对话 | 1537 | short | 85.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「不仅仅是」×3
  - [observe] 章内自我复读 14 句（如「分科表上密密麻麻的名单旁，赫然印着一条通知：“因…」）
- 第 2 章：
  - 单条套路句式超限：「周予安的」×4
  - interiority_para_pct 5.2 低于目标 8.0
- 第 3 章：
  - 单条套路句式超限：「周予安点」×3
  - interiority_para_pct 7.6 低于目标 8.0
- 第 4 章：
  - 单条套路句式超限：「林知夏的」×3
  - narration_para_pct 14.5 低于目标 15.0
  - [observe] 标题重复：「缝补袖口的对话」已存在
- 第 5 章：
  - narration_para_pct 12.7 低于目标 15.0
  - [observe] 标题重复：「缝补袖口的对话」已存在
- 第 6 章：
  - 单条套路句式超限：「林知夏的」×5、「周予安的」×4、「林知夏点了点头」×3
  - [observe] 章内自我复读 17 句（如「她的注意力被分科表上的一行字吸引住了，那是关于公…」）
  - [observe] 标题重复：「缝补袖口的对话」已存在
- 第 7 章：
  - 单条套路句式超限：「林知夏的」×5、「周予安的」×4
  - narration_para_pct 12.5 低于目标 15.0
  - [observe] 标题重复：「缝补袖口的对话」已存在
- 第 8 章：
  - 单条套路句式超限：「周予安的」×5、「带着一丝」×3
  - narration_para_pct 13.2 低于目标 15.0
  - [observe] 标题重复：「缝补袖口的对话」已存在
- 第 9 章：
  - interiority_para_pct 2.9 低于目标 8.0
  - [observe] 章内自我复读 4 句（如「下周就要拆掉旧教学楼了，你也得搬过去…」）
  - [observe] 标题重复：「缝补袖口的对话」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19960
chapter_chars_mean: 2218
chapter_chars_median: 2485
chapter_chars_cv: 0.26
paragraphs_mean: 53
dialogue_chars_pct: 30.8
dialogue_para_pct: 70.9
interiority_para_pct: 9.5
narration_para_pct: 19.7
turn_under20_pct: 88.1
turn_over200_pct: 0.0
attr_say_pct: 26.8
attr_adv_pct: 3.7
scenes_per_chapter: 2
dialogue_run_mean: 3.7
turn_len_median: 11
```
