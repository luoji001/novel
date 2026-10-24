# 房产证 生成报告

slug：`shuangwen-20261023-96`
档位：爽文　闸门模式：observe
章数：10　总字数：18648
LLM 调用：97 次，累计 431.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红绸布被扯紧 | 1750 | normal | 98.1 | 0 |  | 1 |
| 2 | 手指摩挲纸角 | 1945 | normal | 37.1 | 0 |  | 2 |
| 3 | 手指摩挲纸边 | 1975 | normal | 36.0 | 0 |  | 3 |
| 4 | 手指摩挲纸边 | 1798 | normal | 91.6 | 0 |  | 1 |
| 5 | 踢翻空酒瓶 | 1695 | normal | 92.9 | 0 |  | 1 |
| 6 | 手指摩挲纸边 | 1610 | normal | 91.9 | 0 |  | 2 |
| 7 | 手指摩挲纸边 | 1784 | normal | 35.0 | 0 |  | 4 |
| 8 | 房产证复印件的较量 | 1760 | normal | 94.2 | 0 |  | 0 |
| 9 | 手指摩挲纸边 | 1949 | normal | 92.7 | 0 |  | 2 |
| 10 | 手指摩挲纸边 | 2372 | long | 92.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×3
- 第 2 章：
  - 单条套路句式超限：「李建国的」×4、「他知道这」×3、「说道“你」×3
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「李建国的」×4
  - [observe] 章内自我复读 2 句（如「好吧，我承认你确实有资格参与这场讨论。但是，请记…」）
  - [observe] 标题与《手指摩挲纸角》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 标题重复：「手指摩挲纸边」已存在
- 第 5 章：
  - attr_adv_pct 14.3 高于目标 12.0
- 第 6 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「手指摩挲纸边」已存在
- 第 7 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 34 高于目标 14.0
  - [observe] attr_adv_pct 62.5 > 25.0（结构塌缩）
  - [observe] 标题重复：「手指摩挲纸边」已存在
- 第 9 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「手指摩挲纸边」已存在
- 第 10 章：
  - 单条套路句式超限：「李建国的」×3、「你是谁？」×3
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「手指摩挲纸边」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17646
chapter_chars_mean: 1765
chapter_chars_median: 1688
chapter_chars_cv: 0.11
paragraphs_mean: 41.6
dialogue_chars_pct: 50.9
dialogue_para_pct: 87.7
interiority_para_pct: 4.5
narration_para_pct: 7.8
turn_under20_pct: 73.4
turn_over200_pct: 0.0
attr_say_pct: 30.9
attr_adv_pct: 18.6
scenes_per_chapter: 1.4
dialogue_run_mean: 9.7
turn_len_median: 12
```
