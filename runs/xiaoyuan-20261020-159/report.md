# 旧磁带 生成报告

slug：`xiaoyuan-20261020-159`
档位：校园青春　闸门模式：observe
章数：9　总字数：21237
LLM 调用：100 次，累计 459.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 风吹动的纸张 | 1563 | short | 84.2 | 0 |  | 2 |
| 2 | 旧磁带的重量 | 2505 | normal | 91.3 | 0 |  | 2 |
| 3 | 旧磁带的重量 | 2853 | normal | 87.8 | 0 |  | 5 |
| 4 | 字条飘落的瞬间 | 2531 | normal | 90.2 | 0 |  | 1 |
| 5 | 旧磁带的重量 | 2690 | normal | 88.0 | 0 |  | 4 |
| 6 | 旧磁带的重量 | 2200 | normal | 92.0 | 0 |  | 4 |
| 7 | 字条边缘的褶皱 | 2515 | normal | 85.1 | 0 |  | 4 |
| 8 | 轻声哼唱的尾音 | 2559 | normal | 92.0 | 0 |  | 3 |
| 9 | 字条飘落的瞬间 | 1812 | short | 90.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 15.1 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「他转身走向教室后排，留下苏晚晴独自站在公告栏前，…」）
- 第 2 章：
  - 单条套路句式超限：「苏晚晴的」×9、「林子墨的」×3
  - narration_para_pct 11.7 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「苏晚晴点」×4、「心中充满了」×3、「林子墨站在」×3
  - narration_para_pct 8.5 低于目标 15.0
  - attr_adv_pct 17.9 高于目标 12.0
  - [observe] 章内自我复读 15 句（如「林子墨笑了笑，“不过，我真的很喜欢跟你在一起的感…」）
  - [observe] 标题重复：「旧磁带的重量」已存在
- 第 4 章：
  - narration_para_pct 12.5 低于目标 15.0
- 第 5 章：
  - 单条套路句式超限：「苏晚晴的」×6、「“我不知道」×3、「苏晚晴点」×3
  - [observe] 章内自我复读 13 句（如「她知道，林子墨一直在默默关注着她，虽然从未直接表…」）
  - [observe] attr_adv_pct 22.2 > 22.0（结构塌缩）
  - [observe] 标题重复：「旧磁带的重量」已存在
- 第 6 章：
  - 单条套路句式超限：「苏晚晴的」×4
  - interiority_para_pct 6.1 低于目标 8.0
  - narration_para_pct 14.3 低于目标 15.0
  - [observe] 标题重复：「旧磁带的重量」已存在
- 第 7 章：
  - 单条套路句式超限：「苏晚晴的」×6、「林子墨点了点头」×3
  - interiority_para_pct 1.8 低于目标 8.0
  - narration_para_pct 12.5 低于目标 15.0
  - attr_adv_pct 13.3 高于目标 12.0
- 第 8 章：
  - interiority_para_pct 6.6 低于目标 8.0
  - narration_para_pct 6.6 低于目标 15.0
  - [observe] attr_adv_pct 28.6 > 22.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「苏晚晴的」×5
  - interiority_para_pct 4.9 低于目标 8.0
  - [observe] 标题重复：「字条飘落的瞬间」已存在

## 整书结构指标

```
chapters: 9
total_chars: 20088
chapter_chars_mean: 2232
chapter_chars_median: 2374
chapter_chars_cv: 0.18
paragraphs_mean: 55.3
dialogue_chars_pct: 33.3
dialogue_para_pct: 74.3
interiority_para_pct: 9.9
narration_para_pct: 15.8
turn_under20_pct: 85.1
turn_over200_pct: 0.0
attr_say_pct: 34.0
attr_adv_pct: 11.4
scenes_per_chapter: 2.4
dialogue_run_mean: 5.1
turn_len_median: 11
```
