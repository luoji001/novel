# 假登录 生成报告

slug：`xuanyi-20261019-92`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14601
LLM 调用：68 次，累计 234.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 屏幕上的密码 | 1556 | short | 99.8 | 0 |  | 3 |
| 2 | 硬币藏身铁盒底 | 3248 | normal | 88.6 | 0 |  | 4 |
| 3 | 屏幕上的密码 | 3979 | normal | 89.4 | 0 |  | 4 |
| 4 | 账单上的空白处 | 3935 | normal | 87.7 | 0 |  | 2 |
| 5 | 登录记录的纸条 | 1878 | short | 91.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「苏婉秋的」×4
  - narration_para_pct 9.1 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「苏婉秋的」×8、「“我不知道」×3、「”苏婉秋轻」×3
  - narration_para_pct 1.4 低于目标 20.0
  - attr_adv_pct 19.2 高于目标 10.0
  - dialogue_run_mean 13.4 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「公安局」×8、「苏婉秋的」×5
  - narration_para_pct 12.8 低于目标 20.0
  - [observe] attr_adv_pct 26.5 > 20.0（结构塌缩）
  - [observe] 标题重复：「屏幕上的密码」已存在
- 第 4 章：
  - 单条套路句式超限：「苏婉秋的」×9、「林振邦的」×8、「“我不知道」×5
  - narration_para_pct 11.7 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「苏婉秋的」×3
  - narration_para_pct 9.7 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13873
chapter_chars_mean: 2775
chapter_chars_median: 3087
chapter_chars_cv: 0.39
paragraphs_mean: 65
dialogue_chars_pct: 44.7
dialogue_para_pct: 82.2
interiority_para_pct: 8.6
narration_para_pct: 9.2
turn_under20_pct: 77.5
turn_over200_pct: 0.0
attr_say_pct: 22.4
attr_adv_pct: 15.6
scenes_per_chapter: 2
dialogue_run_mean: 7.1
turn_len_median: 13
```
