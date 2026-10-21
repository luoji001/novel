# 分科表 生成报告

slug：`xiaoyuan-20261020-94`
档位：校园青春　闸门模式：observe
章数：9　总字数：20218
LLM 调用：100 次，累计 438.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记簿上的空位 | 1578 | short | 90.0 | 0 |  | 2 |
| 2 | 课表上的红圈 | 2322 | normal | 93.2 | 0 |  | 2 |
| 3 | 磁带与数学题 | 2339 | normal | 92.3 | 0 |  | 1 |
| 4 | 磁带与未拆封的承诺 | 2671 | normal | 89.6 | 0 |  | 2 |
| 5 | 名字后的圆圈 | 2163 | normal | 91.0 | 0 |  | 3 |
| 6 | 名字后的圆圈 | 2387 | normal | 89.8 | 0 |  | 3 |
| 7 | 笔记本上的铅笔痕 | 2366 | normal | 91.4 | 0 |  | 2 |
| 8 | 作业本上的折痕 | 2723 | normal | 92.6 | 0 |  | 2 |
| 9 | 粉笔削成的尖角 | 1660 | short | 87.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「发现自己」×3
  - [observe] 章内自我复读 12 句（如「她终于意识到，也许不只是她的身高数据出现了问题，…」）
- 第 2 章：
  - 单条套路句式超限：「林晓棠的」×4、「林晓棠点了点头」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 3 章：
  - narration_para_pct 14.0 低于目标 15.0
- 第 4 章：
  - 单条套路句式超限：「林晓棠站在」×4
  - [observe] 章内自我复读 19 句（如「空气中弥漫着一种淡淡的忧伤，像是一种无法言说的心…」）
- 第 5 章：
  - 单条套路句式超限：「林晓棠点点」×3
  - narration_para_pct 12.5 低于目标 15.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「林晓棠的」×3
  - [observe] 章内自我复读 5 句（如「陈老师继续批改作业，而林晓棠的目光始终停留在那张…」）
  - [observe] 标题重复：「名字后的圆圈」已存在
- 第 7 章：
  - 单条套路句式超限：「林晓棠的」×5
  - [observe] attr_adv_pct 33.3 > 22.0（结构塌缩）
- 第 8 章：
  - 单条套路句式超限：「林晓棠的」×6
  - interiority_para_pct 7.2 低于目标 8.0
- 第 9 章：
  - dialogue_chars_pct 19.0 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「她记得上周五下午，当她在办公室门口拦住陈老师的时…」）

## 整书结构指标

```
chapters: 9
total_chars: 19271
chapter_chars_mean: 2141
chapter_chars_median: 2239
chapter_chars_cv: 0.17
paragraphs_mean: 44.7
dialogue_chars_pct: 25.2
dialogue_para_pct: 67.3
interiority_para_pct: 15.4
narration_para_pct: 17.3
turn_under20_pct: 86.2
turn_over200_pct: 0.0
attr_say_pct: 32.4
attr_adv_pct: 9.9
scenes_per_chapter: 2.2
dialogue_run_mean: 3.1
turn_len_median: 10
```
