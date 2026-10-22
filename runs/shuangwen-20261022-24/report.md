# 旧房产证 生成报告

slug：`shuangwen-20261022-24`
档位：爽文　闸门模式：observe
章数：10　总字数：19767
LLM 调用：97 次，累计 367.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧房产证被质疑 | 1578 | normal | 40.0 | 0 |  | 2 |
| 2 | 旧房产证被质疑 | 1918 | normal | 91.8 | 0 |  | 2 |
| 3 | 名单上的名字被抹去 | 2169 | normal | 91.6 | 0 |  | 1 |
| 4 | 签字权被剥夺 | 2519 | normal | 35.4 | 0 |  | 4 |
| 5 | 地图被替换 | 1507 | normal | 93.7 | 0 |  | 1 |
| 6 | 旧房产证被质疑 | 2017 | normal | 36.2 | 0 |  | 4 |
| 7 | 签字的手指颤抖 | 1850 | normal | 38.2 | 0 |  | 1 |
| 8 | 旧房产证被质疑 | 1635 | normal | 94.1 | 0 |  | 1 |
| 9 | 旧房产证被质疑 | 1704 | normal | 90.1 | 0 |  | 2 |
| 10 | 旧房产证被质疑 | 2860 | long | 37.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李振国的」×3
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 2 章：
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「旧房产证被质疑」已存在
- 第 3 章：
  - 单条套路句式超限：「李振国的」×6、「张德福的」×4
- 第 4 章：
  - 单条套路句式超限：「张德福的」×5、「李振国的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 22.7 高于目标 14.0
  - [observe] attr_adv_pct 61.5 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「李振国的」×3
- 第 6 章：
  - 单条套路句式超限：「李振国的」×5、「拆迁办」×3
  - [observe] 章内自我复读 6 句（如「她低声说道，仿佛是在对自己也说着什么，“这是我职…」）
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「旧房产证被质疑」已存在
- 第 7 章：
  - [observe] 章内自我复读 4 句（如「其实呢……如果你愿意提供一些额外的信息，说不定我…」）
- 第 8 章：
  - [observe] 标题重复：「旧房产证被质疑」已存在
- 第 9 章：
  - 单条套路句式超限：「李振国站在」×3、「他知道这」×3、「李振国的」×3
  - [observe] 标题重复：「旧房产证被质疑」已存在
- 第 10 章：
  - 单条套路句式超限：「李振国的」×3
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「旧房产证被质疑」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18760
chapter_chars_mean: 1876
chapter_chars_median: 1788
chapter_chars_cv: 0.21
paragraphs_mean: 42.4
dialogue_chars_pct: 43.9
dialogue_para_pct: 78.9
interiority_para_pct: 7.8
narration_para_pct: 13.2
turn_under20_pct: 69.7
turn_over200_pct: 0.0
attr_say_pct: 29.2
attr_adv_pct: 26.1
scenes_per_chapter: 1.7
dialogue_run_mean: 6.1
turn_len_median: 14
```
