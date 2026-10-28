# 鱼鳞 生成报告

slug：`shipin-20261027-344`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5843
LLM 调用：57 次，累计 139.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 信纸飘落 | 486 | short | 39.4 | 0 |  | 1 |
| 2 | 铁锈暗格 | 1253 | normal | 93.5 | 0 |  | 1 |
| 3 | 鱼鳞飞溅 | 1139 | normal | 36.5 | 0 |  | 3 |
| 4 | 刀锋贴喉 | 1052 | normal | 91.5 | 0 |  | 0 |
| 5 | 刀锋贴喉 | 963 | normal | 90.6 | 0 |  | 1 |
| 6 | 刀锋贴喉 | 944 | normal | 93.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

1. 第五章与第六章标题重复为《刀锋贴喉》，存在标题重复问题。  
2. 第二章提到“因秤杆暗格引发冲突”，但第三章和第四章均未提及“秤杆暗格”这一关键物件，前后不一致。  
3. 第六章提到“信中鱼鳞与她手腕红绳相连”，但前文从未提及王婶有“手腕红绳”，属于新增信息未提前铺垫。  
4. 第五章提到“两人在风中达成某种默契”，但前文未有任何铺垫或暗示两人关系有转变，人物立场无理由翻转。

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 444 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 34.5 低于目标 35.0
- 第 3 章：
  - narration_para_pct 17.1 低于目标 35.0
  - dialogue_run_mean 5.8 高于目标 4.0
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 5 章：
  - [observe] 标题重复：「刀锋贴喉」已存在
- 第 6 章：
  - [observe] 标题重复：「刀锋贴喉」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5469
chapter_chars_mean: 912
chapter_chars_median: 952
chapter_chars_cv: 0.28
paragraphs_mean: 24.7
dialogue_chars_pct: 24.1
dialogue_para_pct: 60.1
interiority_para_pct: 1.5
narration_para_pct: 38.4
turn_under20_pct: 98.0
turn_over200_pct: 0.0
attr_say_pct: 39.4
attr_adv_pct: 4.8
scenes_per_chapter: 1
dialogue_run_mean: 2.6
turn_len_median: 8
```
