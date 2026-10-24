# 报价单 生成报告

slug：`shuangwen-20261023-122`
档位：爽文　闸门模式：observe
章数：10　总字数：19705
LLM 调用：97 次，累计 422.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕碎的报价单 | 1861 | normal | 99.2 | 0 |  | 2 |
| 2 | 任命书上的名字 | 1880 | normal | 92.2 | 0 |  | 1 |
| 3 | 签字笔划过名单 | 1706 | normal | 93.1 | 0 |  | 1 |
| 4 | 名片上的市长夫人 | 2632 | normal | 91.2 | 0 |  | 2 |
| 5 | 签字笔划过名单 | 1628 | normal | 93.7 | 0 |  | 3 |
| 6 | 名册上的备案印章 | 1779 | normal | 34.8 | 0 |  | 4 |
| 7 | 手指摩挲纸页边缘 | 1701 | normal | 90.7 | 0 |  | 1 |
| 8 | 手指摩挲纸页边缘 | 1887 | normal | 36.6 | 0 |  | 3 |
| 9 | 手指摩挲纸页边缘 | 2139 | normal | 37.4 | 0 |  | 3 |
| 10 | 签字笔划过名单 | 2482 | long | 37.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×6、「林晓阳的」×4
  - attr_adv_pct 22.2 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「李建国的」×5
- 第 3 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「李建国的」×6
  - narration_para_pct 4.5 低于目标 5.0
- 第 5 章：
  - 单条套路句式超限：「李建国的」×3
  - narration_para_pct 3.6 低于目标 5.0
  - [observe] 标题重复：「签字笔划过名单」已存在
- 第 6 章：
  - 单条套路句式超限：「李建国的」×7、「市文化局」×3
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 35 高于目标 14.0
  - [observe] attr_adv_pct 36.8 > 25.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「李建国的」×4
- 第 8 章：
  - 单条套路句式超限：「李建国的」×6、「他知道自己」×3、「市文化局」×3
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
  - [observe] 标题重复：「手指摩挲纸页边缘」已存在
- 第 9 章：
  - 单条套路句式超限：「带着一丝」×3
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
  - [observe] 标题重复：「手指摩挲纸页边缘」已存在
- 第 10 章：
  - narration_para_pct 3.3 低于目标 5.0
  - dialogue_run_mean 14.2 高于目标 14.0
  - [observe] attr_adv_pct 29.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔划过名单」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18683
chapter_chars_mean: 1868
chapter_chars_median: 1771
chapter_chars_cv: 0.17
paragraphs_mean: 42.9
dialogue_chars_pct: 49.9
dialogue_para_pct: 86.1
interiority_para_pct: 5.4
narration_para_pct: 8.5
turn_under20_pct: 72.3
turn_over200_pct: 0.0
attr_say_pct: 31.2
attr_adv_pct: 21.2
scenes_per_chapter: 2.1
dialogue_run_mean: 9.8
turn_len_median: 14
```
