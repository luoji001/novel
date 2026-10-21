# 磁带 生成报告

slug：`xiaoyuan-20261020-23`
档位：校园青春　闸门模式：observe
章数：9　总字数：19906
LLM 调用：100 次，累计 445.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 贴纸压住未解的题 | 1232 | short | 78.1 | 0 |  | 3 |
| 2 | 磁带滑落桌面 | 2614 | normal | 92.8 | 0 |  | 2 |
| 3 | 偷看书包里的纸条 | 2538 | normal | 86.7 | 0 |  | 4 |
| 4 | 校服外套留在课桌 | 2300 | normal | 93.3 | 0 |  | 0 |
| 5 | 纸条飘落在肩头 | 2334 | normal | 92.9 | 0 |  | 1 |
| 6 | 笔记本滑落桌面 | 2310 | normal | 57.5 | 0 |  | 5 |
| 7 | 抹布擦过黑板边缘 | 2683 | normal | 90.1 | 0 |  | 3 |
| 8 | 笔记本压弯封面 | 2434 | normal | 92.6 | 0 |  | 2 |
| 9 | 磁带滑落桌面 | 1452 | short | 87.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林修远和沈知夏站在」×4
  - dialogue_chars_pct 13.3 低于目标 20.0
  - interiority_para_pct 0.0 低于目标 8.0
- 第 2 章：
  - 单条套路句式超限：「沈知夏的」×8、「林修远的」×6
  - narration_para_pct 13.3 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「沈知夏的」×9、「林修远的」×3
  - dialogue_chars_pct 19.9 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 章内自我复读 18 句（如「但此刻他只想知道一件事：那个在音乐室里弹奏《致爱…」）
- 第 5 章：
  - narration_para_pct 7.3 低于目标 15.0
- 第 6 章：
  - 单条套路句式超限：「他知道自己」×3、「林修远的」×3
  - dialogue_chars_pct 14.9 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 章内自我复读 4 句（如「你最近总在找些奇怪的东西…」）
  - [observe] 标题与《磁带滑落桌面》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「带着一丝」×3
  - narration_para_pct 14.0 低于目标 15.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「沈知夏的」×6、「林修远站在」×3
  - narration_para_pct 14.3 低于目标 15.0
- 第 9 章：
  - 单条套路句式超限：「林修远的」×6、「点了点头」×4、「”沈知夏低」×3
  - [observe] 章内自我复读 14 句（如「就像今天，他们站在操场边上，并肩坐着的时候多了一…」）
  - [observe] 标题重复：「磁带滑落桌面」已存在

## 整书结构指标

```
chapters: 9
total_chars: 18924
chapter_chars_mean: 2103
chapter_chars_median: 2209
chapter_chars_cv: 0.24
paragraphs_mean: 45.3
dialogue_chars_pct: 22.8
dialogue_para_pct: 68.4
interiority_para_pct: 14.7
narration_para_pct: 17.0
turn_under20_pct: 88.8
turn_over200_pct: 0.0
attr_say_pct: 26.5
attr_adv_pct: 9.1
scenes_per_chapter: 2.3
dialogue_run_mean: 3.8
turn_len_median: 10
```
