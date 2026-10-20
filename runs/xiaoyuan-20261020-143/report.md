# 磁带 生成报告

slug：`xiaoyuan-20261020-143`
档位：校园青春　闸门模式：observe
章数：9　总字数：18871
LLM 调用：100 次，累计 413.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 磁带滑入课桌夹层 | 1696 | short | 91.0 | 0 |  | 2 |
| 2 | 纸条摩挲阳光下 | 2523 | normal | 93.5 | 0 |  | 1 |
| 3 | 纸条摩挲阳光下 | 2542 | normal | 90.2 | 0 |  | 4 |
| 4 | 分科表贴出 | 2002 | normal | 92.0 | 0 |  | 2 |
| 5 | 纸条摩挲阳光下 | 2235 | normal | 91.8 | 0 |  | 2 |
| 6 | 校服外套上的名字 | 2404 | normal | 91.5 | 0 |  | 3 |
| 7 | 纸条摩挲阳光下 | 2234 | normal | 87.5 | 0 |  | 2 |
| 8 | 课桌边缘的划痕 | 1704 | normal | 30.4 | 0 |  | 2 |
| 9 | 纸条摩挲阳光下 | 1522 | short | 90.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周砚秋的」×3
  - [observe] 章内自我复读 15 句（如「他伸手去够椅子上的作业本，手指擦过桌沿的刻痕，那…」）
- 第 2 章：
  - narration_para_pct 14.3 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「周砚秋的」×11、「林子墨的」×8
  - narration_para_pct 13.2 低于目标 15.0
  - [observe] 章内自我复读 1 句（如「你把磁带放进我的课桌，还留了一张纸条…」）
  - [observe] 标题重复：「纸条摩挲阳光下」已存在
- 第 4 章：
  - 单条套路句式超限：「市一中教务处」×5
  - interiority_para_pct 7.3 低于目标 8.0
- 第 5 章：
  - 单条套路句式超限：「林子墨的」×3
  - [observe] 标题重复：「纸条摩挲阳光下」已存在
- 第 6 章：
  - 单条套路句式超限：「周砚秋的」×6、「林子墨的」×6、「林子墨点了点头」×3
  - narration_para_pct 7.8 低于目标 15.0
  - [observe] attr_adv_pct 40.0 > 22.0（结构塌缩）
- 第 7 章：
  - dialogue_chars_pct 17.3 低于目标 20.0
  - [observe] 标题重复：「纸条摩挲阳光下」已存在
- 第 8 章：
  - 单条套路句式超限：「林子墨点点」×4、「他知道这」×4
  - [observe] 章内自我复读 21 句（如「那张熟悉的表格上，原本写着“高三（3）班”的字样…」）
- 第 9 章：
  - 单条套路句式超限：「林子墨的」×3
  - narration_para_pct 14.7 低于目标 15.0
  - [observe] 标题重复：「纸条摩挲阳光下」已存在

## 整书结构指标

```
chapters: 9
total_chars: 17881
chapter_chars_mean: 1987
chapter_chars_median: 2118
chapter_chars_cv: 0.19
paragraphs_mean: 47
dialogue_chars_pct: 25.8
dialogue_para_pct: 68.0
interiority_para_pct: 13.9
narration_para_pct: 18.0
turn_under20_pct: 88.5
turn_over200_pct: 0.0
attr_say_pct: 27.9
attr_adv_pct: 7.7
scenes_per_chapter: 2.3
dialogue_run_mean: 3.2
turn_len_median: 9
```
