# 课桌 生成报告

slug：`xiaoyuan-20261020-59`
档位：校园青春　闸门模式：observe
章数：9　总字数：19888
LLM 调用：100 次，累计 434.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 课桌上的拖鞋 | 1277 | short | 39.2 | 0 |  | 3 |
| 2 | 纸条上的字迹 | 2014 | normal | 45.8 | 0 |  | 1 |
| 3 | 拼接磁带的黄昏 | 2491 | normal | 45.0 | 0 |  | 2 |
| 4 | 分科表的边缘 | 2542 | normal | 92.2 | 0 |  | 2 |
| 5 | 纸条上的字迹 | 2378 | normal | 94.3 | 0 |  | 3 |
| 6 | 纸条上的字迹 | 2736 | normal | 86.4 | 0 |  | 4 |
| 7 | 校服外套的褶皱 | 2412 | normal | 86.7 | 0 |  | 2 |
| 8 | 窗外的铁丝网 | 2399 | normal | 91.8 | 0 |  | 1 |
| 9 | 纸条上的字迹 | 1630 | short | 85.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 15.8 低于目标 20.0
  - interiority_para_pct 0.0 低于目标 8.0
  - [observe] 章内自我复读 17 句（如「他说完这句话后，立刻低下头继续研究手中的课表，像…」）
- 第 2 章：
  - dialogue_chars_pct 13.5 低于目标 20.0
- 第 3 章：
  - dialogue_chars_pct 13.4 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「那人忽然开口，语气温和，“有时候，我们并不是不愿…」）
- 第 4 章：
  - 单条套路句式超限：「苏雨桐的」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「苏雨桐的」×3
  - [observe] attr_adv_pct 22.2 > 22.0（结构塌缩）
  - [observe] 标题重复：「纸条上的字迹」已存在
- 第 6 章：
  - 单条套路句式超限：「苏雨桐的」×3
  - narration_para_pct 14.8 低于目标 15.0
  - [observe] 章内自我复读 17 句（如「林夏点点头，眼神却落在那些已经被扔掉的矿泉水瓶上…」）
  - [observe] 标题重复：「纸条上的字迹」已存在
- 第 7 章：
  - dialogue_chars_pct 17.8 低于目标 20.0
  - narration_para_pct 12.5 低于目标 15.0
- 第 8 章：
  - 单条套路句式超限：「苏雨桐的」×3
- 第 9 章：
  - dialogue_chars_pct 18.1 低于目标 20.0
  - [observe] 标题重复：「纸条上的字迹」已存在

## 整书结构指标

```
chapters: 9
total_chars: 18911
chapter_chars_mean: 2101
chapter_chars_median: 2279
chapter_chars_cv: 0.22
paragraphs_mean: 46.1
dialogue_chars_pct: 22.1
dialogue_para_pct: 62.9
interiority_para_pct: 15.8
narration_para_pct: 21.3
turn_under20_pct: 86.8
turn_over200_pct: 0.0
attr_say_pct: 33.4
attr_adv_pct: 6.1
scenes_per_chapter: 2.4
dialogue_run_mean: 2.9
turn_len_median: 9
```
