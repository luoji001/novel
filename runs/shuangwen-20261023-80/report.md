# 旧约 生成报告

slug：`shuangwen-20261023-80`
档位：爽文　闸门模式：observe
章数：10　总字数：19435
LLM 调用：97 次，累计 452.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧合同的重量 | 1441 | normal | 98.8 | 0 |  | 0 |
| 2 | 登记簿上的名字 | 2337 | normal | 94.1 | 0 |  | 0 |
| 3 | 合同上的指纹 | 2095 | normal | 88.8 | 0 |  | 1 |
| 4 | 签字权的较量 | 1690 | normal | 93.6 | 0 |  | 1 |
| 5 | 翻开旧合同 | 2107 | normal | 90.9 | 0 |  | 2 |
| 6 | 翻阅登记簿 | 1955 | normal | 92.0 | 0 |  | 1 |
| 7 | 翻开登记簿 | 1869 | normal | 93.7 | 0 |  | 3 |
| 8 | 撕纸机的回响 | 1793 | normal | 37.2 | 0 |  | 2 |
| 9 | 撕旧合同 | 1721 | normal | 91.7 | 0 |  | 1 |
| 10 | 撕旧合同 | 2417 | long | 90.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - attr_adv_pct 12.5 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「李主任点了点头」×3
- 第 5 章：
  - 单条套路句式超限：「张老二的」×3
  - attr_adv_pct 14.3 高于目标 12.0
- 第 6 章：
  - narration_para_pct 4.5 低于目标 5.0
- 第 7 章：
  - 单条套路句式超限：「李主任的」×3
  - attr_adv_pct 17.6 高于目标 12.0
  - [observe] 标题与《翻阅登记簿》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「张老二的」×3
  - [observe] 章内自我复读 1 句（如「那些东西早就不知道扔哪儿去了…」）
- 第 9 章：
  - [observe] 标题与《翻开旧合同》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - attr_adv_pct 13.6 高于目标 12.0
  - [observe] 标题重复：「撕旧合同」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18393
chapter_chars_mean: 1839
chapter_chars_median: 1815
chapter_chars_cv: 0.16
paragraphs_mean: 45
dialogue_chars_pct: 47.8
dialogue_para_pct: 83.4
interiority_para_pct: 6.5
narration_para_pct: 10.1
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 29.4
attr_adv_pct: 9.4
scenes_per_chapter: 1.4
dialogue_run_mean: 6.6
turn_len_median: 13
```
