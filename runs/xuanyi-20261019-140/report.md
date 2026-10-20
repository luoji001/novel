# 卡影 生成报告

slug：`xuanyi-20261019-140`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14877
LLM 调用：68 次，累计 224.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 刷卡记录疑云 | 1678 | short | 97.9 | 0 |  | 2 |
| 2 | 刷卡记录疑云 | 3442 | normal | 93.5 | 0 |  | 3 |
| 3 | 卡片划痕之谜 | 3775 | normal | 91.0 | 0 |  | 2 |
| 4 | 注销卡深夜现身 | 3639 | normal | 80.9 | 0 |  | 6 |
| 5 | 指纹比对失败 | 2338 | short | 91.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周晓琳的」×3、「陈思远的」×3
  - narration_para_pct 17.9 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈思远的」×8、「周晓琳的」×3
  - narration_para_pct 3.9 低于目标 20.0
  - [observe] 标题重复：「刷卡记录疑云」已存在
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×3、「他知道这」×3
  - narration_para_pct 16.5 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「”周晓琳轻」×5、「周晓琳点」×3、「陈思远的」×3
  - dialogue_chars_pct 65.0 高于目标 58.0
  - narration_para_pct 3.6 低于目标 20.0
  - dialogue_run_mean 19.8 高于目标 10.0
  - [observe] 章内自我复读 18 句（如「陈思远盯着她的脸看了几秒，然后转过身走到窗边，“…」）
  - [observe] attr_adv_pct 20.5 > 20.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「”周晓琳轻」×3、「陈思远的」×3
  - narration_para_pct 9.6 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14149
chapter_chars_mean: 2830
chapter_chars_median: 3276
chapter_chars_cv: 0.31
paragraphs_mean: 64.8
dialogue_chars_pct: 50.2
dialogue_para_pct: 85.5
interiority_para_pct: 5.0
narration_para_pct: 9.5
turn_under20_pct: 71.6
turn_over200_pct: 0.0
attr_say_pct: 32.8
attr_adv_pct: 9.4
scenes_per_chapter: 3.4
dialogue_run_mean: 9.4
turn_len_median: 13
```
