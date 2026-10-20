# 银针 生成报告

slug：`xuanyi-20261019-98`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15050
LLM 调用：68 次，累计 255.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 银针上的私印 | 1652 | short | 96.5 | 0 |  | 0 |
| 2 | 银针入绣 | 4582 | normal | 88.2 | 0 |  | 3 |
| 3 | 抚摸账页边缘 | 3680 | normal | 90.6 | 0 |  | 3 |
| 4 | 旧棉线的回响 | 3222 | normal | 89.1 | 0 |  | 3 |
| 5 | 旧棉线的回响 | 1909 | short | 85.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「沈砚秋的」×6、「陆青梧的」×4、「“我不知道」×3
  - narration_para_pct 9.4 低于目标 20.0
  - [observe] 章内自我复读 18 句（如「他清楚记得那个傍晚，当他在临河边见到那具尸体的时…」）
- 第 3 章：
  - 单条套路句式超限：「沈砚秋的」×7、「陆青梧点」×3
  - narration_para_pct 8.3 低于目标 20.0
  - attr_adv_pct 13.0 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「带着一丝」×5、「沈砚秋的」×5、「陆青梧点」×3
  - narration_para_pct 12.7 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「带着一丝」×3
  - narration_para_pct 14.7 低于目标 20.0
  - [observe] 章内自我复读 18 句（如「先生，我总觉得……绣工死得蹊跷。他临走前还说要交…」）
  - [observe] 标题重复：「旧棉线的回响」已存在

## 整书结构指标

```
chapters: 5
total_chars: 14394
chapter_chars_mean: 2879
chapter_chars_median: 3080
chapter_chars_cv: 0.41
paragraphs_mean: 57.4
dialogue_chars_pct: 42.7
dialogue_para_pct: 80.6
interiority_para_pct: 7.3
narration_para_pct: 12.1
turn_under20_pct: 66.3
turn_over200_pct: 0.0
attr_say_pct: 16.2
attr_adv_pct: 10.1
scenes_per_chapter: 3.2
dialogue_run_mean: 5.2
turn_len_median: 15
```
