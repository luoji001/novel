# 通风管 生成报告

slug：`shipin-20261027-107`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5897
LLM 调用：57 次，累计 121.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙与黑影 | 499 | short | 17.6 | 0 |  | 2 |
| 2 | 螺丝刀裂痕 | 976 | normal | 88.7 | 0 |  | 1 |
| 3 | 钥匙与黑影 | 1320 | normal | 91.7 | 0 |  | 2 |
| 4 | 锁芯与暗道 | 1153 | normal | 92.1 | 0 |  | 0 |
| 5 | 螺丝刀与黑影 | 1009 | normal | 91.3 | 0 |  | 0 |
| 6 | 钥匙沾机油 | 934 | normal | 85.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

1. 第一章和第三章均出现《钥匙与黑影》标题，内容重复，存在标题重复问题。  
2. 第二章提到周子墨用螺丝刀撬锁，但第六章提到钥匙沾机油，暗示钥匙可能与机油有关，但未明确说明钥匙是否与螺丝刀有关联。  
3. 第三章提到便利店经理和小林发现黑车规律出现，但第一章只提到小林观察到一辆黑车，未提及经理参与，前后人物参与程度不一致。  
4. 第五章提到小林察觉有人在监视录像，但未提及任何人物对此作出反应或调查，情节未延续。  
5. 第六章提到小林回忆与周子墨的争执，但前文未提及两人有争执情节，人物关系突兀。

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 2.4 低于目标 5.0
  - [observe] 章节过短 452 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - dialogue_chars_pct 2.3 低于目标 5.0
- 第 3 章：
  - narration_para_pct 26.9 低于目标 35.0
  - [observe] 标题重复：「钥匙与黑影」已存在
- 第 6 章：
  - interiority_para_pct 8.7 高于目标 6.0

## 整书结构指标

```
chapters: 6
total_chars: 5429
chapter_chars_mean: 905
chapter_chars_median: 937
chapter_chars_cv: 0.29
paragraphs_mean: 27.2
dialogue_chars_pct: 17.0
dialogue_para_pct: 38.0
interiority_para_pct: 1.9
narration_para_pct: 60.1
turn_under20_pct: 93.2
turn_over200_pct: 0.0
attr_say_pct: 38.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.6
turn_len_median: 10
```
