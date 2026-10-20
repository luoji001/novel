# 病历本 生成报告

slug：`xuanyi-20261019-65`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15340
LLM 调用：68 次，累计 236.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 屏幕闪烁 | 1789 | short | 99.2 | 0 |  | 0 |
| 2 | 屏幕闪烁 | 3838 | normal | 88.6 | 0 |  | 4 |
| 3 | 文件袋浮现神秘名字 | 3732 | normal | 91.7 | 0 |  | 3 |
| 4 | 考勤记录空缺处 | 3910 | normal | 90.6 | 0 |  | 3 |
| 5 | 监控存储卡消失 | 2066 | short | 92.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「周文远的」×5、「林子安站在」×3
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 章内自我复读 2 句（如「凌晨一点，周文远巡视完毕…」）
  - [observe] 标题重复：「屏幕闪烁」已存在
- 第 3 章：
  - 单条套路句式超限：「周文远的」×5
  - narration_para_pct 11.1 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「周文远的声音打断了他的思绪…」）
- 第 4 章：
  - 单条套路句式超限：「周文远的」×6、「林子安的」×5、「林子安点点」×3
  - narration_para_pct 9.9 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「林子安的」×4
  - attr_adv_pct 18.2 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14624
chapter_chars_mean: 2925
chapter_chars_median: 3553
chapter_chars_cv: 0.34
paragraphs_mean: 62.4
dialogue_chars_pct: 31.3
dialogue_para_pct: 70.0
interiority_para_pct: 9.7
narration_para_pct: 20.3
turn_under20_pct: 79.3
turn_over200_pct: 0.0
attr_say_pct: 27.6
attr_adv_pct: 10.0
scenes_per_chapter: 8.4
dialogue_run_mean: 4.0
turn_len_median: 11
```
