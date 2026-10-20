# 撕碎的面单 生成报告

slug：`xuanyi-20261019-37`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14729
LLM 调用：68 次，累计 232.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 咔嗒声的回响 | 1909 | short | 97.8 | 0 |  | 3 |
| 2 | 撕碎的面单 | 3542 | normal | 91.7 | 0 |  | 3 |
| 3 | 撕碎的面单 | 3627 | normal | 90.4 | 0 |  | 3 |
| 4 | 扫描枪的校准 | 3594 | normal | 89.9 | 0 |  | 3 |
| 5 | 暗红色的血迹 | 2052 | short | 89.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林雨桐的」×4
  - narration_para_pct 13.2 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「周正阳的」×7、「林雨桐的」×4、「林雨桐站在」×3
  - narration_para_pct 15.7 低于目标 20.0
  - [observe] attr_adv_pct 40.0 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「林雨桐站在」×4、「周正阳的」×4
  - narration_para_pct 15.5 低于目标 20.0
  - [observe] 标题重复：「撕碎的面单」已存在
- 第 4 章：
  - 单条套路句式超限：「周正阳的」×4、「林雨桐的」×4
  - narration_para_pct 14.5 低于目标 20.0
  - attr_adv_pct 10.5 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「林雨桐的」×4
  - narration_para_pct 18.4 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14044
chapter_chars_mean: 2809
chapter_chars_median: 3389
chapter_chars_cv: 0.3
paragraphs_mean: 61.2
dialogue_chars_pct: 35.1
dialogue_para_pct: 75.5
interiority_para_pct: 9.0
narration_para_pct: 15.4
turn_under20_pct: 77.1
turn_over200_pct: 0.0
attr_say_pct: 17.9
attr_adv_pct: 16.4
scenes_per_chapter: 4.8
dialogue_run_mean: 5.0
turn_len_median: 12
```
