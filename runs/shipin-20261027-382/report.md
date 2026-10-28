# 船票 生成报告

slug：`shipin-20261027-382`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6640
LLM 调用：57 次，累计 143.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币上的永安二字 | 718 | short | 39.4 | 0 |  | 1 |
| 2 | 手指抚过船票边缘 | 1089 | normal | 92.4 | 0 |  | 0 |
| 3 | 陶碗碎裂的瞬间 | 1142 | normal | 34.9 | 0 |  | 3 |
| 4 | 船票上的永安二字 | 1137 | normal | 87.6 | 0 |  | 3 |
| 5 | 铜壶壶嘴对准陶碗 | 854 | normal | 36.5 | 0 |  | 1 |
| 6 | 手指抚过船票边缘 | 1694 | normal | 88.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 100.0 > 18.0（结构塌缩）
- 第 3 章：
  - narration_para_pct 12.5 低于目标 35.0
  - dialogue_run_mean 7 高于目标 4.0
  - [observe] 章内自我复读 4 句（如「可这是骗人的吧？我查了，那个航线早在十五年前就停…」）
- 第 4 章：
  - narration_para_pct 21.7 低于目标 35.0
  - dialogue_run_mean 6 高于目标 4.0
  - [observe] 标题与《硬币上的永安二字》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章节过短 790 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - narration_para_pct 17.1 低于目标 35.0
  - dialogue_run_mean 7 高于目标 4.0
  - [observe] 标题重复：「手指抚过船票边缘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6244
chapter_chars_mean: 1041
chapter_chars_median: 1050
chapter_chars_cv: 0.31
paragraphs_mean: 24.5
dialogue_chars_pct: 30.0
dialogue_para_pct: 70.0
interiority_para_pct: 0.7
narration_para_pct: 29.3
turn_under20_pct: 86.8
turn_over200_pct: 0.0
attr_say_pct: 24.4
attr_adv_pct: 20.2
scenes_per_chapter: 1
dialogue_run_mean: 4.2
turn_len_median: 12
```
