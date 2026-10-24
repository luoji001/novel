# 旧籍残页 生成报告

slug：`shuangwen-20261023-129`
档位：爽文　闸门模式：observe
章数：10　总字数：19211
LLM 调用：97 次，累计 448.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕碎旧籍 | 2034 | normal | 39.5 | 0 |  | 2 |
| 2 | 撕碎旧籍 | 2088 | normal | 92.1 | 0 |  | 1 |
| 3 | 撕碎旧籍 | 1752 | normal | 94.4 | 0 |  | 2 |
| 4 | 展家谱 | 1696 | normal | 88.9 | 0 |  | 2 |
| 5 | 展旧籍 | 2277 | normal | 37.0 | 0 |  | 2 |
| 6 | 签署新名录 | 1670 | normal | 94.2 | 0 |  | 1 |
| 7 | 递职级 | 1746 | normal | 91.6 | 0 |  | 1 |
| 8 | 展旧籍 | 2055 | normal | 90.4 | 0 |  | 1 |
| 9 | 展古地图 | 1568 | normal | 94.8 | 0 |  | 0 |
| 10 | 展旧籍 | 2315 | long | 94.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「林子安深吸一口气，努力让自己冷静下来…」）
- 第 2 章：
  - [observe] 标题重复：「撕碎旧籍」已存在
- 第 3 章：
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「撕碎旧籍」已存在
- 第 4 章：
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 34 高于目标 14.0
- 第 5 章：
  - 单条套路句式超限：「李怀远的」×4、「林子安的」×4
  - [observe] attr_adv_pct 35.0 > 25.0（结构塌缩）
- 第 6 章：
  - attr_adv_pct 18.8 高于目标 12.0
- 第 7 章：
  - 命中套话收尾句
- 第 8 章：
  - [observe] 标题重复：「展旧籍」已存在
- 第 10 章：
  - 单条套路句式超限：「李怀远的」×6、「他知道这」×3
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「展旧籍」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18226
chapter_chars_mean: 1823
chapter_chars_median: 1802
chapter_chars_cv: 0.14
paragraphs_mean: 43
dialogue_chars_pct: 51.0
dialogue_para_pct: 84.6
interiority_para_pct: 3.4
narration_para_pct: 12.0
turn_under20_pct: 72.5
turn_over200_pct: 0.0
attr_say_pct: 20.2
attr_adv_pct: 15.0
scenes_per_chapter: 1.1
dialogue_run_mean: 9.4
turn_len_median: 14
```
