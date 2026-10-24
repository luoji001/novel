# 交割页 生成报告

slug：`shuangwen-20261023-14`
档位：爽文　闸门模式：observe
章数：10　总字数：19392
LLM 调用：97 次，累计 411.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 支票与笑容的交锋 | 1796 | normal | 39.8 | 0 |  | 2 |
| 2 | 采购记录本的较量 | 2158 | normal | 93.9 | 0 |  | 2 |
| 3 | 敲击桌面的回响 | 1743 | normal | 94.1 | 0 |  | 3 |
| 4 | 翻开财务审批账册 | 2195 | normal | 93.2 | 0 |  | 0 |
| 5 | 撕页的动作 | 1586 | normal | 94.6 | 0 |  | 1 |
| 6 | 指尖轻叩桌面 | 1708 | normal | 93.2 | 0 |  | 1 |
| 7 | 手指摩挲记录本 | 1967 | normal | 94.0 | 0 |  | 2 |
| 8 | 手指摩挲银行卡 | 1924 | normal | 90.9 | 0 |  | 2 |
| 9 | 手指摩挲记录本 | 2077 | normal | 86.1 | 0 |  | 4 |
| 10 | 翻阅采购记录本 | 2228 | long | 88.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈志远的」×3
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 2 章：
  - narration_para_pct 2.2 低于目标 5.0
  - dialogue_run_mean 14.7 高于目标 14.0
- 第 3 章：
  - 单条套路句式超限：「陈志远的」×3
  - narration_para_pct 3.0 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
- 第 5 章：
  - 命中套话收尾句
- 第 6 章：
  - 单条套路句式超限：「林晓薇的」×3
- 第 7 章：
  - 单条套路句式超限：「林晓薇的」×4
  - narration_para_pct 2.8 低于目标 5.0
- 第 8 章：
  - 单条套路句式超限：「陈志远的」×6、「带着一丝」×3
  - attr_adv_pct 14.3 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「陈志远的」×5、「林晓薇的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 43 高于目标 14.0
  - [observe] 标题重复：「手指摩挲记录本」已存在
- 第 10 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 38 高于目标 14.0
  - [observe] 标题与《采购记录本的较量》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18458
chapter_chars_mean: 1846
chapter_chars_median: 1862
chapter_chars_cv: 0.12
paragraphs_mean: 38
dialogue_chars_pct: 56.4
dialogue_para_pct: 92.1
interiority_para_pct: 4.0
narration_para_pct: 4.0
turn_under20_pct: 64.7
turn_over200_pct: 0.0
attr_say_pct: 22.1
attr_adv_pct: 8.8
scenes_per_chapter: 2
dialogue_run_mean: 15.6
turn_len_median: 15
```
