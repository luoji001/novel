# 签单 生成报告

slug：`shuangwen-20261023-42`
档位：爽文　闸门模式：observe
章数：10　总字数：18470
LLM 调用：97 次，累计 409.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签下名字的瞬间 | 1622 | normal | 39.1 | 0 |  | 1 |
| 2 | 手表的反光 | 2061 | normal | 36.8 | 0 |  | 4 |
| 3 | 确认书的褶痕 | 1932 | normal | 94.4 | 0 |  | 1 |
| 4 | 执照在手 | 1869 | normal | 92.9 | 0 |  | 2 |
| 5 | 纸上折痕 | 1760 | normal | 92.3 | 0 |  | 1 |
| 6 | 纸上的折痕 | 1815 | normal | 93.1 | 0 |  | 1 |
| 7 | 父亲的名片 | 1811 | normal | 92.2 | 0 |  | 1 |
| 8 | 合同落地 | 1735 | normal | 93.3 | 0 |  | 1 |
| 9 | 揉皱的合同 | 1874 | normal | 92.1 | 0 |  | 1 |
| 10 | 揉皱的合同 | 1981 | long | 88.7 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「李文远的」×4、「他知道这」×3
  - narration_para_pct 3.6 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「他深吸一口气，努力让自己冷静下来…」）
- 第 3 章：
  - attr_adv_pct 18.2 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「李文远的」×3
  - attr_adv_pct 14.3 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3、「李文远的」×3
- 第 6 章：
  - [observe] 标题与《纸上折痕》近似 0.89 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「他知道这」×3
- 第 8 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 9 章：
  - attr_adv_pct 18.8 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「李文远的」×3
  - narration_para_pct 2.2 低于目标 5.0
  - dialogue_run_mean 44 高于目标 14.0
  - [observe] 标题重复：「揉皱的合同」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17608
chapter_chars_mean: 1761
chapter_chars_median: 1758
chapter_chars_cv: 0.07
paragraphs_mean: 36.1
dialogue_chars_pct: 42.7
dialogue_para_pct: 79.2
interiority_para_pct: 10.2
narration_para_pct: 10.6
turn_under20_pct: 68.1
turn_over200_pct: 0.0
attr_say_pct: 27.6
attr_adv_pct: 14.8
scenes_per_chapter: 1.8
dialogue_run_mean: 8.3
turn_len_median: 14
```
