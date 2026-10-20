# 校服外套的重量 生成报告

slug：`xiaoyuan-20261020-29`
档位：校园青春　闸门模式：observe
章数：9　总字数：21077
LLM 调用：100 次，累计 440.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 素描本最后一页 | 1325 | short | 100.0 | 0 |  | 2 |
| 2 | 磁带上的划痕 | 3031 | normal | 94.0 | 0 |  | 2 |
| 3 | 课桌下的速写稿 | 2370 | normal | 89.4 | 0 |  | 3 |
| 4 | 纸团里的秘密 | 2515 | normal | 87.3 | 0 |  | 3 |
| 5 | 手指抚过公告栏 | 2727 | normal | 91.8 | 0 |  | 1 |
| 6 | 磁带掉在地面 | 2697 | normal | 89.7 | 0 |  | 2 |
| 7 | 素描本最后一页 | 2290 | normal | 92.5 | 0 |  | 2 |
| 8 | 校服外套的褶皱 | 2506 | normal | 57.5 | 0 |  | 2 |
| 9 | 手指抚过公告栏 | 1607 | short | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周子墨的」×4
  - narration_para_pct 7.7 低于目标 15.0
- 第 2 章：
  - 单条套路句式超限：「周子墨的」×8
  - narration_para_pct 14.8 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×3、「带着一丝」×3
  - narration_para_pct 11.7 低于目标 15.0
  - [observe] 章内自我复读 16 句（如「就像窗外的梧桐树，在寒冷中紧紧包裹着自己，不肯伸…」）
- 第 4 章：
  - 单条套路句式超限：「周子墨的」×4、「“我不知道」×3、「点了点头」×3
  - narration_para_pct 14.5 低于目标 15.0
  - [observe] 章内自我复读 17 句（如「林晚晴望着那些小小的雪花，想起昨天晚上，她在宿舍…」）
- 第 5 章：
  - 单条套路句式超限：「林晚晴站在」×3
- 第 6 章：
  - 单条套路句式超限：「周子墨的」×6
  - attr_adv_pct 20.0 高于目标 12.0
- 第 7 章：
  - narration_para_pct 13.7 低于目标 15.0
  - [observe] 标题重复：「素描本最后一页」已存在
- 第 8 章：
  - dialogue_chars_pct 14.9 低于目标 20.0
  - [observe] 章内自我复读 12 句（如「那一刻，她忽然想起去年冬天，他抱着音响在走廊上播…」）
- 第 9 章：
  - narration_para_pct 13.3 低于目标 15.0
  - [observe] 标题重复：「手指抚过公告栏」已存在

## 整书结构指标

```
chapters: 9
total_chars: 20080
chapter_chars_mean: 2231
chapter_chars_median: 2377
chapter_chars_cv: 0.24
paragraphs_mean: 47.6
dialogue_chars_pct: 26.0
dialogue_para_pct: 66.2
interiority_para_pct: 19.1
narration_para_pct: 14.7
turn_under20_pct: 88.2
turn_over200_pct: 0.0
attr_say_pct: 49.2
attr_adv_pct: 5.4
scenes_per_chapter: 1.8
dialogue_run_mean: 3.5
turn_len_median: 9
```
