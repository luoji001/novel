# 铜铃 生成报告

slug：`xuanyi-20261019-212`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14845
LLM 调用：68 次，累计 225.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲纸边 | 1751 | short | 97.5 | 0 |  | 2 |
| 2 | 摩挲纸边 | 3879 | normal | 87.9 | 0 |  | 4 |
| 3 | 摩挲纸边 | 3840 | normal | 89.1 | 0 |  | 5 |
| 4 | 摩挲U盘边缘 | 3725 | normal | 91.0 | 0 |  | 4 |
| 5 | 摩挲金属接口 | 1645 | short | 93.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈文远的」×4
  - narration_para_pct 15.6 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「市网监大队」×7、「陈文远的」×5、「他知道这」×4
  - attr_adv_pct 13.8 高于目标 10.0
  - [observe] 章内自我复读 18 句（如「他的目光再次落在桌面上那一排硬币上，仿佛想要从中…」）
  - [observe] 标题重复：「摩挲纸边」已存在
- 第 3 章：
  - 单条套路句式超限：「林振邦的」×4、「“我不知道」×3、「陈文远点」×3
  - narration_para_pct 6.5 低于目标 20.0
  - attr_adv_pct 11.5 高于目标 10.0
  - dialogue_run_mean 11.9 高于目标 10.0
  - [observe] 标题重复：「摩挲纸边」已存在
- 第 4 章：
  - 单条套路句式超限：「陈文远点」×5、「陈文远的」×3
  - narration_para_pct 8.6 低于目标 20.0
  - attr_adv_pct 11.4 高于目标 10.0
  - [observe] 标题与《摩挲纸边》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「陈文远的」×3、「林振邦的」×3
  - narration_para_pct 10.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14083
chapter_chars_mean: 2817
chapter_chars_median: 3525
chapter_chars_cv: 0.39
paragraphs_mean: 69.4
dialogue_chars_pct: 41.7
dialogue_para_pct: 75.8
interiority_para_pct: 6.3
narration_para_pct: 17.9
turn_under20_pct: 77.5
turn_over200_pct: 0.0
attr_say_pct: 25.6
attr_adv_pct: 9.4
scenes_per_chapter: 1.8
dialogue_run_mean: 6.4
turn_len_median: 13
```
