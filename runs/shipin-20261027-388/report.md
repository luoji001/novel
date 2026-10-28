# 凹痕 生成报告

slug：`shipin-20261027-388`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5657
LLM 调用：57 次，累计 125.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙凹槽的指纹 | 414 | short | 23.3 | 0 |  | 1 |
| 2 | 贝壳滚落的瞬间 | 1362 | normal | 92.4 | 0 |  | 1 |
| 3 | 贝壳滚落的瞬间 | 1282 | normal | 37.1 | 0 |  | 2 |
| 4 | 钥匙划过纸页痕迹 | 1132 | normal | 7.8 | 0 |  | 2 |
| 5 | 手镯上的纹路 | 1012 | normal | 92.3 | 0 |  | 1 |
| 6 | 桶壁泛光的痕迹 | 449 | normal | 37.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 379 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 34.6 低于目标 35.0
- 第 3 章：
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
  - [observe] 标题重复：「贝壳滚落的瞬间」已存在
- 第 4 章：
  - dialogue_chars_pct 4.0 低于目标 5.0
  - interiority_para_pct 14.3 高于目标 6.0
- 第 5 章：
  - dialogue_run_mean 5 高于目标 4.0
- 第 6 章：
  - [observe] 章节过短 412 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5344
chapter_chars_mean: 891
chapter_chars_median: 1017
chapter_chars_cv: 0.45
paragraphs_mean: 18.2
dialogue_chars_pct: 15.6
dialogue_para_pct: 48.7
interiority_para_pct: 4.5
narration_para_pct: 46.8
turn_under20_pct: 95.2
turn_over200_pct: 0.0
attr_say_pct: 16.0
attr_adv_pct: 10.6
scenes_per_chapter: 1.5
dialogue_run_mean: 2.1
turn_len_median: 9
```
