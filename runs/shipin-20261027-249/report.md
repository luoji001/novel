# 胶片上的标签 生成报告

slug：`shipin-20261027-249`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6052
LLM 调用：57 次，累计 130.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 胶片上的银光 | 792 | short | 96.3 | 0 |  | 1 |
| 2 | 公文包与胶片相撞 | 1199 | normal | 93.1 | 0 |  | 1 |
| 3 | 票根入匣 | 1243 | normal | 43.3 | 0 |  | 1 |
| 4 | 胶片入匣 | 650 | normal | 15.6 | 0 |  | 2 |
| 5 | 公文包落地的刹那 | 1155 | normal | 88.9 | 0 |  | 0 |
| 6 | 胶片入匣 | 1007 | normal | 52.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 6.2 高于目标 6.0
- 第 2 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 3 章：
  - interiority_para_pct 11.1 高于目标 6.0
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「这是《流浪地球》的第一版拷贝…」）
  - [observe] 章节过短 578 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - [observe] 标题重复：「胶片入匣」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5663
chapter_chars_mean: 944
chapter_chars_median: 1010
chapter_chars_cv: 0.25
paragraphs_mean: 24.8
dialogue_chars_pct: 14.7
dialogue_para_pct: 42.1
interiority_para_pct: 3.1
narration_para_pct: 54.7
turn_under20_pct: 97.6
turn_over200_pct: 0.0
attr_say_pct: 43.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.6
turn_len_median: 10
```
