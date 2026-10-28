# 铁钳声 生成报告

slug：`shipin-20261027-209`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6486
LLM 调用：57 次，累计 126.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 保温杯倾斜 | 734 | short | 94.8 | 0 |  | 0 |
| 2 | 钥匙划过地面 | 1289 | normal | 37.8 | 0 |  | 2 |
| 3 | 行李箱锁眼 | 983 | normal | 93.5 | 0 |  | 0 |
| 4 | 金属线坠地 | 1225 | normal | 92.3 | 0 |  | 1 |
| 5 | 铁钳抵锁 | 904 | normal | 36.6 | 0 |  | 1 |
| 6 | 保温杯倾斜 | 1345 | normal | 89.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 章内自我复读 2 句（如「那个行李箱还在停车场…」）
- 第 4 章：
  - narration_para_pct 34.2 低于目标 35.0
- 第 5 章：
  - [observe] 章节过短 828 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - [observe] 标题重复：「保温杯倾斜」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6090
chapter_chars_mean: 1015
chapter_chars_median: 1030
chapter_chars_cv: 0.24
paragraphs_mean: 26
dialogue_chars_pct: 16.3
dialogue_para_pct: 45.2
interiority_para_pct: 1.8
narration_para_pct: 53.0
turn_under20_pct: 92.5
turn_over200_pct: 0.0
attr_say_pct: 39.1
attr_adv_pct: 2.9
scenes_per_chapter: 1.2
dialogue_run_mean: 1.9
turn_len_median: 8
```
