# 旧卡 生成报告

slug：`shuangwen-20261023-112`
档位：爽文　闸门模式：observe
章数：10　总字数：19883
LLM 调用：97 次，累计 443.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 借阅卡的有效期限 | 1703 | normal | 99.8 | 0 |  | 2 |
| 2 | 盖印的借阅卡 | 1723 | normal | 37.1 | 0 |  | 1 |
| 3 | 钥匙上的数字密码 | 1542 | normal | 36.6 | 0 |  | 3 |
| 4 | 签字的借阅卡 | 2133 | normal | 37.4 | 0 |  | 2 |
| 5 | 借阅卡的泛黄痕迹 | 2140 | normal | 91.7 | 0 |  | 3 |
| 6 | 盖印的借阅卡 | 1988 | normal | 91.0 | 0 |  | 2 |
| 7 | 拍打石块夺书人 | 1978 | normal | 91.9 | 0 |  | 1 |
| 8 | 借阅卡的泛黄痕迹 | 1939 | normal | 93.0 | 0 |  | 2 |
| 9 | 借阅卡的泛黄痕迹 | 2026 | normal | 85.7 | 0 |  | 3 |
| 10 | 借阅卡的泛黄痕迹 | 2701 | long | 91.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈长风的」×4
- 第 2 章：
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
- 第 3 章：
  - 命中套话收尾句
  - dialogue_chars_pct 25.9 低于目标 30.0
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 4 章：
  - [observe] attr_adv_pct 31.2 > 25.0（结构塌缩）
  - [observe] 标题与《盖印的借阅卡》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×4、「点了点头」×3、「李怀安的」×3
  - attr_adv_pct 21.7 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「沈长风的」×3
  - [observe] 标题重复：「盖印的借阅卡」已存在
- 第 7 章：
  - attr_adv_pct 18.2 高于目标 12.0
- 第 8 章：
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「借阅卡的泛黄痕迹」已存在
- 第 9 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 26 高于目标 14.0
  - [observe] 标题重复：「借阅卡的泛黄痕迹」已存在
- 第 10 章：
  - 单条套路句式超限：「沈长风的」×5、「李怀安的」×4、「带着一丝」×3
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题重复：「借阅卡的泛黄痕迹」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18852
chapter_chars_mean: 1885
chapter_chars_median: 1890
chapter_chars_cv: 0.16
paragraphs_mean: 43.4
dialogue_chars_pct: 45.0
dialogue_para_pct: 79.1
interiority_para_pct: 7.9
narration_para_pct: 13.0
turn_under20_pct: 71.3
turn_over200_pct: 0.0
attr_say_pct: 35.8
attr_adv_pct: 17.6
scenes_per_chapter: 2.6
dialogue_run_mean: 6.8
turn_len_median: 12
```
