# 分科表 生成报告

slug：`xiaoyuan-20261020-35`
档位：校园青春　闸门模式：observe
章数：9　总字数：20198
LLM 调用：100 次，累计 436.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 粉笔灰的重量 | 1405 | short | 96.2 | 0 |  | 2 |
| 2 | 课桌上的光斑 | 2626 | normal | 91.8 | 0 |  | 1 |
| 3 | 磁带的暂停键 | 2308 | normal | 92.2 | 0 |  | 1 |
| 4 | 钥匙的温度 | 2461 | normal | 91.8 | 0 |  | 0 |
| 5 | 粉笔灰的重量 | 2439 | normal | 90.7 | 0 |  | 2 |
| 6 | 最后一首歌的按钮 | 2474 | normal | 91.1 | 0 |  | 0 |
| 7 | 校服外套的温度 | 2176 | normal | 92.2 | 0 |  | 1 |
| 8 | 拉手的瞬间 | 2677 | normal | 91.5 | 0 |  | 1 |
| 9 | 铅笔盒的裂痕 | 1623 | short | 92.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「这名单……是不是又贴了一遍？…」）
- 第 2 章：
  - narration_para_pct 11.3 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×3
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「我们永远是最好的朋友…」）
  - [observe] 标题重复：「粉笔灰的重量」已存在
- 第 7 章：
  - attr_adv_pct 18.2 高于目标 12.0
- 第 8 章：
  - narration_para_pct 12.7 低于目标 15.0
- 第 9 章：
  - 单条套路句式超限：「知道自己」×3
  - attr_adv_pct 14.3 高于目标 12.0

## 整书结构指标

```
chapters: 9
total_chars: 19155
chapter_chars_mean: 2128
chapter_chars_median: 2313
chapter_chars_cv: 0.2
paragraphs_mean: 50.4
dialogue_chars_pct: 27.9
dialogue_para_pct: 68.9
interiority_para_pct: 14.6
narration_para_pct: 16.5
turn_under20_pct: 85.6
turn_over200_pct: 0.0
attr_say_pct: 39.1
attr_adv_pct: 6.4
scenes_per_chapter: 1.7
dialogue_run_mean: 3.0
turn_len_median: 10
```
