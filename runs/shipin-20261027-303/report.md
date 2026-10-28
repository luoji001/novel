# 钥匙 生成报告

slug：`shipin-20261027-303`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5890
LLM 调用：57 次，累计 131.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙串在锁孔发烫 | 334 | short | 21.7 | 0 |  | 3 |
| 2 | 撬开蓝色塑料箱 | 1046 | normal | 51.3 | 0 |  | 2 |
| 3 | 蓝色塑料箱震动 | 1041 | normal | 48.9 | 0 |  | 2 |
| 4 | 钥匙串与碎玻璃 | 988 | normal | 89.6 | 0 |  | 1 |
| 5 | 钥匙串在锁孔发烫 | 1075 | normal | 92.2 | 0 |  | 1 |
| 6 | 钥匙串在锁孔发烫 | 1400 | normal | 22.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

1. 第一章与第五章、第六章均出现“钥匙串在锁孔发烫”的标题，但内容和情节不一致，存在重复标题导致的混淆。  
2. 第六章提到陈志远在监控室打开蓝色收纳箱，但第三章明确指出陈志远在储物间打开蓝色收纳箱，地点不一致。  
3. 第六章提到陈志远与小林争夺录像带，但第五章提到小林藏起磁带，未提及录像带，前后不一致。  
4. 第三章提到监控画面出现异常，但未说明异常原因，与后续情节无直接关联，未交代清楚。  
5. 第六章提到陈志远在监控室打开蓝色收纳箱，但第一章提到小林用钥匙打开监控室大门，未说明监控室是否与储物间相连，逻辑不清晰。

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 294 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
- 第 3 章：
  - dialogue_chars_pct 4.0 低于目标 5.0
  - [observe] 标题与《撬开蓝色塑料箱》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_run_mean 5 高于目标 4.0
- 第 5 章：
  - [observe] 标题重复：「钥匙串在锁孔发烫」已存在
- 第 6 章：
  - 单条套路句式超限：「陈志远的」×3
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
  - [observe] 标题重复：「钥匙串在锁孔发烫」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5505
chapter_chars_mean: 918
chapter_chars_median: 978
chapter_chars_cv: 0.37
paragraphs_mean: 22.5
dialogue_chars_pct: 6.0
dialogue_para_pct: 21.8
interiority_para_pct: 0.0
narration_para_pct: 78.2
turn_under20_pct: 100.0
turn_over200_pct: 0.0
attr_say_pct: 64.5
attr_adv_pct: 10.6
scenes_per_chapter: 2.8
dialogue_run_mean: 2.5
turn_len_median: 8
```
