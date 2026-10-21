# 褶皱 生成报告

slug：`xiaoyuan-20261020-75`
档位：校园青春　闸门模式：observe
章数：9　总字数：21262
LLM 调用：100 次，累计 442.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 课表边缘的褶皱 | 1452 | short | 80.2 | 0 |  | 3 |
| 2 | 磁带上的名字 | 2781 | normal | 87.0 | 0 |  | 4 |
| 3 | 整理校服的褶皱 | 2748 | normal | 89.6 | 0 |  | 4 |
| 4 | 撕碎的纸片 | 2462 | normal | 31.7 | 0 |  | 3 |
| 5 | 撕碎的纸片 | 2470 | normal | 91.6 | 0 |  | 2 |
| 6 | 摩挲纸张的指尖 | 2601 | normal | 91.3 | 0 |  | 2 |
| 7 | 摩挲衣角的指尖 | 2789 | normal | 89.8 | 0 |  | 4 |
| 8 | 摩挲纸张的指尖 | 2320 | normal | 89.7 | 0 |  | 4 |
| 9 | 摩挲公告栏的指尖 | 1630 | short | 91.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林雨桐的」×3
  - dialogue_chars_pct 14.2 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「陈老师愣了一下，随即笑了笑，“分科表已经贴出来了…」）
- 第 2 章：
  - 单条套路句式超限：「周子航的」×5、「林雨桐的」×5、「他知道这」×3
  - narration_para_pct 5.6 低于目标 15.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 章内自我复读 22 句（如「周子航看着她的背影，心中升起了一种莫名的感觉，仿…」）
- 第 3 章：
  - 单条套路句式超限：「林雨桐点点」×3
  - narration_para_pct 13.8 低于目标 15.0
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 章内自我复读 17 句（如「然后她轻轻地转过了身，继续看着那块还没有撤下去的…」）
- 第 4 章：
  - 单条套路句式超限：「林雨桐的」×3
  - dialogue_chars_pct 11.8 低于目标 20.0
  - [observe] 章内自我复读 11 句（如「她知道，不管怎样，那一天的记忆都会像钉子一样扎进…」）
- 第 5 章：
  - narration_para_pct 14.0 低于目标 15.0
  - [observe] 标题重复：「撕碎的纸片」已存在
- 第 6 章：
  - 单条套路句式超限：「”周子航低」×3、「林雨桐的」×3
  - narration_para_pct 13.0 低于目标 15.0
- 第 7 章：
  - 单条套路句式超限：「林雨桐的」×6、「林雨桐站在」×4、「教务处」×4
  - narration_para_pct 9.7 低于目标 15.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题与《摩挲纸张的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「林雨桐的」×3
  - narration_para_pct 13.0 低于目标 15.0
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题重复：「摩挲纸张的指尖」已存在
- 第 9 章：
  - 单条套路句式超限：「林雨桐的」×4
  - narration_para_pct 9.7 低于目标 15.0
  - [observe] 标题与《摩挲纸张的指尖》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 9
total_chars: 20274
chapter_chars_mean: 2253
chapter_chars_median: 2371
chapter_chars_cv: 0.21
paragraphs_mean: 47.1
dialogue_chars_pct: 22.7
dialogue_para_pct: 65.5
interiority_para_pct: 21.4
narration_para_pct: 13.1
turn_under20_pct: 87.5
turn_over200_pct: 0.0
attr_say_pct: 23.8
attr_adv_pct: 8.1
scenes_per_chapter: 2.9
dialogue_run_mean: 3.3
turn_len_median: 9
```
