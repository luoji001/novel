# 签单 生成报告

slug：`shuangwen-20261022-29`
档位：爽文　闸门模式：observe
章数：10　总字数：18639
LLM 调用：97 次，累计 344.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红线划过的报价单 | 1703 | normal | 99.3 | 0 |  | 0 |
| 2 | 名片上的指纹痕迹 | 2058 | normal | 92.4 | 0 |  | 2 |
| 3 | 手指摩挲纸页边缘 | 1466 | normal | 90.9 | 0 |  | 2 |
| 4 | 合同摊开的瞬间 | 1633 | normal | 94.9 | 0 |  | 2 |
| 5 | 手指摩挲纸币边缘 | 1712 | normal | 92.4 | 0 |  | 1 |
| 6 | 手指摩挲名单边缘 | 1805 | normal | 36.1 | 0 |  | 2 |
| 7 | 手指摩挲合同边缘 | 2267 | normal | 37.1 | 0 |  | 2 |
| 8 | 摩挲名单边缘 | 1967 | normal | 87.4 | 0 |  | 4 |
| 9 | 名单上的红圈印记 | 1732 | normal | 93.3 | 0 |  | 1 |
| 10 | 手指摩挲名单边缘 | 2286 | long | 92.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 25.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李文远的」×3
  - attr_adv_pct 12.5 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「带着一丝」×3
  - attr_adv_pct 25.0 高于目标 12.0
- 第 5 章：
  - [observe] 标题与《手指摩挲纸页边缘》近似 0.88 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题与《手指摩挲纸页边缘》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题与《手指摩挲纸页边缘》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 21.4 高于目标 12.0
  - dialogue_run_mean 40 高于目标 14.0
  - [observe] 标题与《手指摩挲名单边缘》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - attr_adv_pct 12.5 高于目标 12.0
- 第 10 章：
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题重复：「手指摩挲名单边缘」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17655
chapter_chars_mean: 1766
chapter_chars_median: 1682
chapter_chars_cv: 0.15
paragraphs_mean: 39.6
dialogue_chars_pct: 49.2
dialogue_para_pct: 83.1
interiority_para_pct: 5.3
narration_para_pct: 11.6
turn_under20_pct: 66.7
turn_over200_pct: 0.0
attr_say_pct: 19.4
attr_adv_pct: 19.5
scenes_per_chapter: 2.1
dialogue_run_mean: 9.9
turn_len_median: 14
```
