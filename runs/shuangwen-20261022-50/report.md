# 担保合同 生成报告

slug：`shuangwen-20261022-50`
档位：爽文　闸门模式：observe
章数：10　总字数：19583
LLM 调用：97 次，累计 431.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字权的较量 | 2077 | normal | 98.6 | 0 |  | 2 |
| 2 | 担保合同的日期 | 2111 | normal | 90.4 | 0 |  | 1 |
| 3 | 合同上的指纹 | 1777 | normal | 91.1 | 0 |  | 1 |
| 4 | 签字权的较量 | 1710 | normal | 90.4 | 0 |  | 2 |
| 5 | 手指划过数字 | 1736 | normal | 93.2 | 0 |  | 1 |
| 6 | 签字盖章 | 1616 | normal | 91.2 | 0 |  | 2 |
| 7 | 签字盖章 | 2034 | normal | 89.7 | 0 |  | 4 |
| 8 | 手指划过日期 | 1802 | normal | 92.8 | 0 |  | 2 |
| 9 | 手指划过日期 | 1978 | normal | 91.9 | 0 |  | 2 |
| 10 | 手指划过签名栏 | 2732 | long | 90.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×4、「王小红的」×3
  - attr_adv_pct 15.4 高于目标 12.0
- 第 2 章：
  - narration_para_pct 4.5 低于目标 5.0
- 第 3 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「李建国的」×4
  - [observe] 标题重复：「签字权的较量」已存在
- 第 5 章：
  - 单条套路句式超限：「王小红的」×3
- 第 6 章：
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 15 高于目标 14.0
- 第 7 章：
  - dialogue_chars_pct 70.1 高于目标 70.0
  - narration_para_pct 2.1 低于目标 5.0
  - dialogue_run_mean 23 高于目标 14.0
  - [observe] 标题重复：「签字盖章」已存在
- 第 8 章：
  - 单条套路句式超限：「李建国点」×3
  - [observe] 标题与《手指划过数字》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「手指划过日期」已存在
- 第 10 章：
  - 单条套路句式超限：「微微一笑」×3、「他知道这」×3
  - [observe] 标题与《手指划过数字》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18577
chapter_chars_mean: 1858
chapter_chars_median: 1794
chapter_chars_cv: 0.16
paragraphs_mean: 42.9
dialogue_chars_pct: 50.6
dialogue_para_pct: 85.2
interiority_para_pct: 6.6
narration_para_pct: 8.1
turn_under20_pct: 69.2
turn_over200_pct: 0.0
attr_say_pct: 20.1
attr_adv_pct: 9.5
scenes_per_chapter: 2.6
dialogue_run_mean: 9.5
turn_len_median: 14
```
