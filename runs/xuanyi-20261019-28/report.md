# 水表 生成报告

slug：`xuanyi-20261019-28`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14996
LLM 调用：68 次，累计 237.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表指针的异常转动 | 1734 | short | 99.8 | 0 |  | 3 |
| 2 | 洗衣粉的日期争议 | 3953 | normal | 89.7 | 0 |  | 3 |
| 3 | 便签纸的潮湿痕迹 | 3816 | normal | 88.6 | 0 |  | 2 |
| 4 | 水表仍在转动 | 3453 | normal | 90.1 | 0 |  | 3 |
| 5 | 水表仍在转动 | 2035 | short | 91.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周慧兰的」×3
  - narration_para_pct 9.7 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周慧兰的」×10、「“我不知道」×5、「陈志远的」×4
  - narration_para_pct 8.3 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「周慧兰的」×10、「陈志远的」×5、「“我不知道」×4
  - narration_para_pct 8.4 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周慧兰的」×11、「陈志远站在」×3、「陈志远的」×3
  - narration_para_pct 10.4 低于目标 20.0
  - attr_adv_pct 10.5 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「周慧兰的」×3
  - narration_para_pct 10.4 低于目标 20.0
  - attr_adv_pct 13.3 高于目标 10.0
  - [observe] 标题重复：「水表仍在转动」已存在

## 整书结构指标

```
chapters: 5
total_chars: 14264
chapter_chars_mean: 2853
chapter_chars_median: 3285
chapter_chars_cv: 0.35
paragraphs_mean: 64.6
dialogue_chars_pct: 43.6
dialogue_para_pct: 85.0
interiority_para_pct: 5.7
narration_para_pct: 9.3
turn_under20_pct: 80.1
turn_over200_pct: 0.0
attr_say_pct: 27.7
attr_adv_pct: 12.0
scenes_per_chapter: 2.6
dialogue_run_mean: 6.9
turn_len_median: 12
```
