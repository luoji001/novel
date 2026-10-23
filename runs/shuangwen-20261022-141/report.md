# 旧签 生成报告

slug：`shuangwen-20261022-141`
档位：爽文　闸门模式：observe
章数：10　总字数：19475
LLM 调用：97 次，累计 425.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红笔划去旧账目 | 2032 | normal | 98.9 | 0 |  | 0 |
| 2 | 红笔划去旧账目 | 1667 | normal | 91.7 | 0 |  | 2 |
| 3 | 红笔划去旧账目 | 1951 | normal | 93.6 | 0 |  | 2 |
| 4 | 红印章压住旧账单 | 1981 | normal | 92.3 | 0 |  | 0 |
| 5 | 红笔划去旧账目 | 1716 | normal | 93.2 | 0 |  | 4 |
| 6 | 红笔划去旧账目 | 1895 | normal | 93.4 | 0 |  | 5 |
| 7 | 红笔划去旧账目 | 1872 | normal | 94.5 | 0 |  | 3 |
| 8 | 钢印压住旧账单 | 2127 | normal | 37.6 | 0 |  | 3 |
| 9 | 红笔划去旧账目 | 1841 | normal | 93.1 | 0 |  | 2 |
| 10 | 签字页被撕下 | 2383 | long | 93.2 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「红笔划去旧账目」已存在
- 第 3 章：
  - attr_adv_pct 15.6 高于目标 12.0
  - [observe] 标题重复：「红笔划去旧账目」已存在
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×4
  - narration_para_pct 3.6 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「红笔划去旧账目」已存在
- 第 6 章：
  - 单条套路句式超限：「李建国的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 18.8 高于目标 12.0
  - dialogue_run_mean 16 高于目标 14.0
  - [observe] 标题重复：「红笔划去旧账目」已存在
- 第 7 章：
  - narration_para_pct 4.4 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「红笔划去旧账目」已存在
- 第 8 章：
  - 单条套路句式超限：「李建国的」×3
  - [observe] attr_adv_pct 27.8 > 25.0（结构塌缩）
  - [observe] 标题与《红印章压住旧账单》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「陈志远的」×3
  - [observe] 标题重复：「红笔划去旧账目」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18483
chapter_chars_mean: 1848
chapter_chars_median: 1819
chapter_chars_cv: 0.1
paragraphs_mean: 41.5
dialogue_chars_pct: 51.6
dialogue_para_pct: 85.7
interiority_para_pct: 6.4
narration_para_pct: 7.8
turn_under20_pct: 63.3
turn_over200_pct: 0.0
attr_say_pct: 18.6
attr_adv_pct: 13.7
scenes_per_chapter: 1.8
dialogue_run_mean: 8.4
turn_len_median: 15
```
