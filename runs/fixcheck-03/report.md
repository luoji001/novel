# 磁带藏入夹层 生成报告

slug：`fixcheck-03`
档位：校园青春　闸门模式：observe
章数：9　总字数：19185
LLM 调用：100 次，累计 689.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 分科表落下一角 | 1398 | short | 97.4 | 0 |  | 1 |
| 2 | 铅笔别肩 | 2517 | normal | 92.7 | 0 |  | 2 |
| 3 | 磁带边缘摩挲 | 2195 | normal | 91.3 | 0 |  | 1 |
| 4 | 照片滑落桌面 | 2005 | normal | 90.3 | 0 |  | 1 |
| 5 | 诊断书碎片拾起 | 2129 | normal | 91.1 | 0 |  | 0 |
| 6 | 铅笔别肩 | 2517 | normal | 90.3 | 0 |  | 2 |
| 7 | 梧桐树影斑驳 | 2648 | normal | 91.5 | 0 |  | 1 |
| 8 | 磁带消失在夹层 | 2133 | normal | 91.4 | 0 |  | 1 |
| 9 | 旧照片压在课本下 | 1634 | short | 85.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林子墨的」×3
- 第 2 章：
  - 单条套路句式超限：「周雨桐的」×8、「林子墨的」×4
  - narration_para_pct 9.6 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「周雨桐的」×6、「“我不知道」×3
- 第 4 章：
  - dialogue_chars_pct 19.4 低于目标 20.0
- 第 6 章：
  - 单条套路句式超限：「带着一丝」×3
  - [observe] 标题重复：「铅笔别肩」已存在
- 第 7 章：
  - 单条套路句式超限：「周雨桐的」×6、「林子墨站在」×4
- 第 8 章：
  - 单条套路句式超限：「周雨桐的」×4、「林子墨的」×3
- 第 9 章：
  - dialogue_chars_pct 16.8 低于目标 20.0

## 整书结构指标

```
chapters: 9
total_chars: 18265
chapter_chars_mean: 2029
chapter_chars_median: 2044
chapter_chars_cv: 0.19
paragraphs_mean: 43.6
dialogue_chars_pct: 24.0
dialogue_para_pct: 63.5
interiority_para_pct: 17.6
narration_para_pct: 18.9
turn_under20_pct: 88.0
turn_over200_pct: 0.0
attr_say_pct: 32.4
attr_adv_pct: 2.7
scenes_per_chapter: 1.4
dialogue_run_mean: 2.7
turn_len_median: 10
```
