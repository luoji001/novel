# 合同副本 生成报告

slug：`shuangwen-20261022-30`
档位：爽文　闸门模式：observe
章数：10　总字数：19453
LLM 调用：97 次，累计 349.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指划过数字 | 1651 | normal | 40.0 | 0 |  | 2 |
| 2 | 手指抚过合同边缘 | 2257 | normal | 36.1 | 0 |  | 3 |
| 3 | 手指抚过合同边缘 | 1851 | normal | 89.7 | 0 |  | 1 |
| 4 | 手指划过合同边缘 | 1994 | normal | 90.8 | 0 |  | 3 |
| 5 | 撕毁存折 | 2186 | normal | 37.8 | 0 |  | 3 |
| 6 | 手指划过合同边缘 | 1956 | normal | 87.4 | 0 |  | 5 |
| 7 | 手指划过合同边缘 | 1934 | normal | 89.8 | 0 |  | 3 |
| 8 | 手指抚过合同边缘 | 1636 | normal | 36.9 | 0 |  | 3 |
| 9 | 手指抚过合同边缘 | 1585 | normal | 92.9 | 0 |  | 3 |
| 10 | 手指抚过合同边缘 | 2393 | long | 92.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王德发的」×3
  - [observe] attr_adv_pct 38.5 > 25.0（结构塌缩）
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「王德发的」×6、「王德发点了点头」×3、「他知道这」×3
  - [observe] attr_adv_pct 27.8 > 25.0（结构塌缩）
- 第 3 章：
  - [observe] 标题重复：「手指抚过合同边缘」已存在
- 第 4 章：
  - narration_para_pct 3.9 低于目标 5.0
  - dialogue_run_mean 16.3 高于目标 14.0
  - [observe] 标题与《手指抚过合同边缘》近似 0.88 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「李建军的」×6、「王德发的」×3
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「我也知道，你之所以能够掌控这一切，是因为你背后还…」）
- 第 6 章：
  - 单条套路句式超限：「王德发的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 17.6 高于目标 12.0
  - dialogue_run_mean 46 高于目标 14.0
  - [observe] 标题重复：「手指划过合同边缘」已存在
- 第 7 章：
  - 单条套路句式超限：「王德发的」×5、「李建军的」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「手指划过合同边缘」已存在
- 第 8 章：
  - 单条套路句式超限：「王德发的」×3、「李建军的」×3
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「手指抚过合同边缘」已存在
- 第 9 章：
  - narration_para_pct 4.9 低于目标 5.0
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「手指抚过合同边缘」已存在
- 第 10 章：
  - 单条套路句式超限：「王德发的」×5、「李建军深吸一口气」×3
  - narration_para_pct 3.0 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「手指抚过合同边缘」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18462
chapter_chars_mean: 1846
chapter_chars_median: 1846
chapter_chars_cv: 0.15
paragraphs_mean: 41.3
dialogue_chars_pct: 53.9
dialogue_para_pct: 89.1
interiority_para_pct: 3.5
narration_para_pct: 7.4
turn_under20_pct: 69.3
turn_over200_pct: 0.0
attr_say_pct: 28.6
attr_adv_pct: 17.3
scenes_per_chapter: 2
dialogue_run_mean: 12.4
turn_len_median: 14
```
