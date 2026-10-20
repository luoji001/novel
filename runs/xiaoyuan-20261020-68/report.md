# 磁带播放 生成报告

slug：`xiaoyuan-20261020-68`
档位：校园青春　闸门模式：observe
章数：9　总字数：21149
LLM 调用：100 次，累计 457.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲纸边 | 1607 | short | 100.0 | 0 |  | 1 |
| 2 | 摩挲纸边 | 2452 | normal | 83.6 | 0 |  | 3 |
| 3 | 摩挲纸边 | 2430 | normal | 90.2 | 0 |  | 4 |
| 4 | 磁带播放 | 2433 | normal | 91.7 | 0 |  | 3 |
| 5 | 摩挲纸边 | 2685 | normal | 80.1 | 0 |  | 4 |
| 6 | 摩挲笔记本封面 | 2835 | normal | 90.2 | 0 |  | 1 |
| 7 | 摩挲笔记本封面 | 2223 | normal | 91.7 | 0 |  | 1 |
| 8 | 摩挲课本边缘 | 2560 | normal | 90.6 | 0 |  | 3 |
| 9 | 摩挲笔记本封面 | 1915 | short | 91.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「教务处」×8、「顾明远的」×3
- 第 2 章：
  - 单条套路句式超限：「顾明远的」×9、「林晚晴的」×3
  - [observe] 章内自我复读 40 句（如「林晚晴的目光不由自主地飘向那个位置，那里写着她的…」）
  - [observe] 标题重复：「摩挲纸边」已存在
- 第 3 章：
  - 单条套路句式超限：「顾明远的」×5、「林晚晴的」×3
  - [observe] 章内自我复读 15 句（如「顾明远盯着那些数字，忽然发现其中有个熟悉的符号—…」）
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
  - [observe] 标题重复：「摩挲纸边」已存在
- 第 4 章：
  - 单条套路句式超限：「林晚晴的」×3
  - narration_para_pct 11.4 低于目标 15.0
  - attr_adv_pct 14.3 高于目标 12.0
- 第 5 章：
  - dialogue_chars_pct 15.3 低于目标 20.0
  - [observe] 章内自我复读 13 句（如「窗外的风轻轻吹进来，卷起了几片落叶，飘落在地上，…」）
  - [observe] attr_adv_pct 22.2 > 22.0（结构塌缩）
  - [observe] 标题重复：「摩挲纸边」已存在
- 第 6 章：
  - 单条套路句式超限：「林晚晴的」×5、「心中充满了」×3、「顾明远点」×3
- 第 7 章：
  - [observe] 标题重复：「摩挲笔记本封面」已存在
- 第 8 章：
  - 单条套路句式超限：「顾明远的」×5、「林晚晴点点」×3、「林晚晴的」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题与《摩挲纸边》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - narration_para_pct 12.0 低于目标 15.0
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 标题重复：「摩挲笔记本封面」已存在

## 整书结构指标

```
chapters: 9
total_chars: 20007
chapter_chars_mean: 2223
chapter_chars_median: 2314
chapter_chars_cv: 0.16
paragraphs_mean: 53.6
dialogue_chars_pct: 25.8
dialogue_para_pct: 68.2
interiority_para_pct: 12.6
narration_para_pct: 19.2
turn_under20_pct: 92.2
turn_over200_pct: 0.0
attr_say_pct: 40.1
attr_adv_pct: 11.5
scenes_per_chapter: 2.2
dialogue_run_mean: 3.3
turn_len_median: 9
```
