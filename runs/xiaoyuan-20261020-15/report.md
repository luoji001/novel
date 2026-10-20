# 课表一角 生成报告

slug：`xiaoyuan-20261020-15`
档位：校园青春　闸门模式：observe
章数：9　总字数：20754
LLM 调用：100 次，累计 454.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 指尖抚过褪色名字 | 1537 | short | 92.3 | 0 |  | 2 |
| 2 | 指尖抚过褪色名字 | 2819 | normal | 91.9 | 0 |  | 3 |
| 3 | 撕碎的课表碎片 | 2702 | normal | 88.9 | 0 |  | 2 |
| 4 | 笔记本里的解剖书 | 2605 | normal | 88.1 | 0 |  | 2 |
| 5 | 指尖拂过皱褶纸页 | 2340 | normal | 89.6 | 0 |  | 0 |
| 6 | 指尖拂过粉笔灰 | 2338 | normal | 90.8 | 0 |  | 0 |
| 7 | 笔记本掉落的瞬间 | 2586 | normal | 90.5 | 0 |  | 1 |
| 8 | 名单背后的夕阳余晖 | 2328 | normal | 93.5 | 0 |  | 3 |
| 9 | 指尖抚过皱褶纸页 | 1490 | short | 90.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 3.6 低于目标 15.0
  - [observe] 章内自我复读 17 句（如「她默默地看着公告栏上的名字，突然意识到，或许她需…」）
- 第 2 章：
  - 单条套路句式超限：「苏雨桐的」×7、「苏雨桐点点」×3、「点了点头」×3
  - narration_para_pct 8.5 低于目标 15.0
  - [observe] 标题重复：「指尖抚过褪色名字」已存在
- 第 3 章：
  - 单条套路句式超限：「程子墨的」×6
  - attr_adv_pct 18.5 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「苏雨桐站在」×3
  - [observe] 章内自我复读 18 句（如「苏雨桐继续说道，声音突然变得很小，“有时候我觉得…」）
- 第 7 章：
  - 单条套路句式超限：「苏雨桐的」×3
- 第 8 章：
  - 单条套路句式超限：「省会重点高中教务处」×17
  - narration_para_pct 7.0 低于目标 15.0
  - [observe] attr_adv_pct 100.0 > 22.0（结构塌缩）
- 第 9 章：
  - 命中套话收尾句
  - narration_para_pct 13.9 低于目标 15.0
  - [observe] 章内自我复读 14 句（如「林夏点了点头，目光不经意地扫过那张纸上密密麻麻的…」）
  - [observe] 标题与《指尖拂过皱褶纸页》近似 0.88 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 9
total_chars: 19678
chapter_chars_mean: 2186
chapter_chars_median: 2242
chapter_chars_cv: 0.21
paragraphs_mean: 51.3
dialogue_chars_pct: 32.5
dialogue_para_pct: 68.9
interiority_para_pct: 15.4
narration_para_pct: 15.7
turn_under20_pct: 80.4
turn_over200_pct: 0.0
attr_say_pct: 44.4
attr_adv_pct: 14.3
scenes_per_chapter: 3.2
dialogue_run_mean: 3.6
turn_len_median: 10
```
