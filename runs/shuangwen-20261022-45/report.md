# 作废流程文件 生成报告

slug：`shuangwen-20261022-45`
档位：爽文　闸门模式：observe
章数：10　总字数：20603
LLM 调用：97 次，累计 378.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指摩挲纸页边缘 | 2262 | normal | 98.5 | 0 |  | 1 |
| 2 | 签署离职协议 | 1852 | normal | 91.8 | 0 |  | 1 |
| 3 | 拍碎红头文件 | 2048 | normal | 90.6 | 0 |  | 1 |
| 4 | 签字权 | 1621 | normal | 92.7 | 0 |  | 1 |
| 5 | 摩挲纸页边缘 | 2097 | normal | 91.4 | 0 |  | 2 |
| 6 | 摩挲纸页边缘 | 2191 | normal | 94.0 | 0 |  | 2 |
| 7 | 摩挲纸页边缘 | 2186 | normal | 94.0 | 0 |  | 2 |
| 8 | 摩挲纸页边缘 | 2261 | normal | 92.3 | 0 |  | 1 |
| 9 | 按压指纹 | 1838 | normal | 93.7 | 0 |  | 1 |
| 10 | 撕碎审批表 | 2237 | long | 93.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周文远的」×3
- 第 2 章：
  - 单条套路句式超限：「周文远的」×6
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
- 第 4 章：
  - 单条套路句式超限：「他知道这」×5、「周文远的」×3
- 第 5 章：
  - 单条套路句式超限：「李建国的」×7、「周文远的」×5
  - [observe] 标题与《手指摩挲纸页边缘》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 4.8 低于目标 5.0
  - [observe] 标题重复：「摩挲纸页边缘」已存在
- 第 7 章：
  - attr_adv_pct 15.8 高于目标 12.0
  - [observe] 标题重复：「摩挲纸页边缘」已存在
- 第 8 章：
  - [observe] 标题重复：「摩挲纸页边缘」已存在
- 第 9 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「李建国的」×3
  - narration_para_pct 4.2 低于目标 5.0

## 整书结构指标

```
chapters: 10
total_chars: 19595
chapter_chars_mean: 1960
chapter_chars_median: 2048
chapter_chars_cv: 0.11
paragraphs_mean: 43.1
dialogue_chars_pct: 43.9
dialogue_para_pct: 82.6
interiority_para_pct: 6.5
narration_para_pct: 11.0
turn_under20_pct: 74.6
turn_over200_pct: 0.0
attr_say_pct: 24.5
attr_adv_pct: 7.7
scenes_per_chapter: 2.1
dialogue_run_mean: 7.2
turn_len_median: 12
```
