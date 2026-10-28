# 手电筒光 生成报告

slug：`shipin-20261027-153`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6627
LLM 调用：57 次，累计 145.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手电筒照车牌 | 541 | short | 39.1 | 0 |  | 1 |
| 2 | 公文包落地 | 1164 | normal | 91.8 | 0 |  | 0 |
| 3 | 公文包落地 | 1051 | normal | 92.8 | 0 |  | 2 |
| 4 | 充电宝坠地 | 1334 | normal | 36.8 | 0 |  | 1 |
| 5 | 公文包脱手而出 | 1270 | normal | 89.0 | 0 |  | 0 |
| 6 | 公文包脱手而出 | 1261 | normal | 89.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

1. 第二章与第三章标题相同，内容重复，导致章节混乱。  
2. 第四章提到“父亲遗留的充电宝”，但前文未提及充电宝的存在。  
3. 第五章提到“父亲遗言”，但前文仅提到“父亲遗书”，表述不一致。  
4. 第六章与第五章标题相同，内容重复，导致章节混乱。

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 501 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 28.6 低于目标 35.0
  - [observe] 标题重复：「公文包落地」已存在
- 第 4 章：
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）
- 第 6 章：
  - [observe] 标题重复：「公文包脱手而出」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6110
chapter_chars_mean: 1018
chapter_chars_median: 1113
chapter_chars_cv: 0.26
paragraphs_mean: 35.7
dialogue_chars_pct: 16.3
dialogue_para_pct: 41.3
interiority_para_pct: 0.4
narration_para_pct: 58.3
turn_under20_pct: 99.2
turn_over200_pct: 0.0
attr_say_pct: 41.3
attr_adv_pct: 4.4
scenes_per_chapter: 1.2
dialogue_run_mean: 2.0
turn_len_median: 8
```
