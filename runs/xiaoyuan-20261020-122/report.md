# 磁带 生成报告

slug：`xiaoyuan-20261020-122`
档位：校园青春　闸门模式：observe
章数：9　总字数：20839
LLM 调用：100 次，累计 437.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 粉笔灰落在校服上 | 1629 | short | 92.9 | 0 |  | 3 |
| 2 | 揉皱的课表被拾起 | 2881 | normal | 93.1 | 0 |  | 4 |
| 3 | 课表上的名字被移走 | 2805 | normal | 88.4 | 0 |  | 2 |
| 4 | 磁带掉在地上 | 2225 | normal | 91.9 | 0 |  | 0 |
| 5 | 笔记本上的公式 | 2556 | normal | 90.6 | 0 |  | 1 |
| 6 | 笔记本上的公式 | 2361 | normal | 88.4 | 0 |  | 4 |
| 7 | 课表边缘被摩挲 | 2524 | normal | 92.8 | 0 |  | 1 |
| 8 | 纸飞机落在课桌上 | 2331 | normal | 91.5 | 0 |  | 2 |
| 9 | 纸条落在笔记本上 | 1518 | short | 48.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×4、「“林夏你」×3
  - narration_para_pct 11.4 低于目标 15.0
  - [observe] 章内自我复读 19 句（如「他知道，这样的日子恐怕还会继续下去，就像那些未完…」）
- 第 2 章：
  - 单条套路句式超限：「他知道这」×4
  - interiority_para_pct 5.4 低于目标 8.0
  - narration_para_pct 12.6 低于目标 15.0
  - [observe] 章内自我复读 1 句（如「我只是不想让别人担心…」）
- 第 3 章：
  - 单条套路句式超限：「带着一丝」×3、「林夏点点」×3
  - [observe] 章内自我复读 17 句（如「他知道有些话说不出口，就像此刻挂在墙上的那一张公…」）
- 第 5 章：
  - [observe] 章内自我复读 7 句（如「她不知道这意味着什么，但她知道，在接下来的日子里…」）
- 第 6 章：
  - 单条套路句式超限：「周远点了点头」×3、「”周远轻」×3、「林夏点点」×3
  - narration_para_pct 10.9 低于目标 15.0
  - [observe] 章内自我复读 16 句（如「他知道周远其实很想说出来，但他总是把话咽回去，像…」）
  - [observe] 标题重复：「笔记本上的公式」已存在
- 第 7 章：
  - 单条套路句式超限：「林夏点点」×3
- 第 8 章：
  - narration_para_pct 5.6 低于目标 15.0
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「他知道自己」×3
  - narration_para_pct 9.7 低于目标 15.0
  - [observe] 章内自我复读 21 句（如「他打开笔记本，却发现里面有一张折得整齐的纸条，上…」）

## 整书结构指标

```
chapters: 9
total_chars: 19676
chapter_chars_mean: 2186
chapter_chars_median: 2218
chapter_chars_cv: 0.2
paragraphs_mean: 56.3
dialogue_chars_pct: 27.9
dialogue_para_pct: 69.3
interiority_para_pct: 14.5
narration_para_pct: 16.1
turn_under20_pct: 90.9
turn_over200_pct: 0.0
attr_say_pct: 41.3
attr_adv_pct: 7.6
scenes_per_chapter: 1.6
dialogue_run_mean: 3.7
turn_len_median: 9
```
