# 清单 生成报告

slug：`shuangwen-20261023-95`
档位：爽文　闸门模式：observe
章数：10　总字数：18197
LLM 调用：97 次，累计 417.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 清单副本的隐藏页 | 1703 | normal | 96.0 | 0 |  | 1 |
| 2 | 盖章的验收单 | 2029 | normal | 90.8 | 0 |  | 2 |
| 3 | 清单上的指纹痕迹 | 1896 | normal | 93.3 | 0 |  | 3 |
| 4 | 手指抚过合同表面 | 1576 | normal | 92.6 | 0 |  | 1 |
| 5 | 手指划过合同边缘 | 1921 | normal | 37.5 | 0 |  | 3 |
| 6 | 手指划过合同边缘 | 1687 | normal | 92.4 | 0 |  | 2 |
| 7 | 手指摩挲清单边缘 | 1522 | normal | 36.2 | 0 |  | 4 |
| 8 | 手指摩挲证书边缘 | 1707 | normal | 35.3 | 0 |  | 4 |
| 9 | 手指划过合同边缘 | 2055 | normal | 91.5 | 0 |  | 1 |
| 10 | 手指划过清单边缘 | 2091 | long | 86.1 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 22.2 高于目标 12.0
- 第 2 章：
  - narration_para_pct 2.5 低于目标 5.0
  - dialogue_run_mean 19.5 高于目标 14.0
- 第 3 章：
  - 命中套话收尾句
  - narration_para_pct 2.2 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「李国强的」×5
- 第 5 章：
  - 单条套路句式超限：「李国强的」×3
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题与《手指抚过合同表面》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「手指划过合同边缘」已存在
- 第 7 章：
  - 单条套路句式超限：「李国强的」×7
  - narration_para_pct 2.9 低于目标 5.0
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「只是你一直没有拿出来…」）
- 第 8 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 41 高于目标 14.0
  - [observe] 章内自我复读 1 句（如「小王，帮我查一下张磊的资质情况…」）
  - [observe] 标题与《手指摩挲清单边缘》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - [observe] 标题重复：「手指划过合同边缘」已存在
- 第 10 章：
  - 单条套路句式超限：「李国强的」×4
  - narration_para_pct 1.9 低于目标 5.0
  - dialogue_run_mean 25.5 高于目标 14.0
  - [observe] 标题与《手指划过合同边缘》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 17247
chapter_chars_mean: 1725
chapter_chars_median: 1698
chapter_chars_cv: 0.12
paragraphs_mean: 39.1
dialogue_chars_pct: 53.4
dialogue_para_pct: 88.4
interiority_para_pct: 4.3
narration_para_pct: 7.3
turn_under20_pct: 64.7
turn_over200_pct: 0.0
attr_say_pct: 26.9
attr_adv_pct: 13.3
scenes_per_chapter: 2.5
dialogue_run_mean: 14.2
turn_len_median: 16
```
