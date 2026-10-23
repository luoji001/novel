# 登记表 生成报告

slug：`shuangwen-20261022-136`
档位：爽文　闸门模式：observe
章数：10　总字数：18295
LLM 调用：97 次，累计 431.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指触碰木桌边缘 | 1748 | normal | 96.6 | 0 |  | 1 |
| 2 | 手指摩挲纸边 | 1767 | normal | 89.9 | 0 |  | 0 |
| 3 | 手指摩挲登记表 | 1471 | normal | 92.1 | 0 |  | 2 |
| 4 | 手指递交纸条 | 1964 | normal | 89.6 | 0 |  | 1 |
| 5 | 登记表上的签名 | 2046 | normal | 90.4 | 0 |  | 1 |
| 6 | 手指摩挲登记表 | 1380 | normal | 93.6 | 0 |  | 2 |
| 7 | 手指按住登记表一角 | 1851 | normal | 90.2 | 0 |  | 3 |
| 8 | 递纸条的手指 | 1890 | normal | 90.4 | 0 |  | 1 |
| 9 | 递纸条的手指 | 2141 | normal | 91.7 | 0 |  | 2 |
| 10 | 递纸条的手指 | 2027 | long | 90.2 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王守义的」×3
- 第 3 章：
  - narration_para_pct 3.4 低于目标 5.0
  - [observe] 标题与《手指摩挲纸边》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「李怀安的」×4
- 第 5 章：
  - 单条套路句式超限：「李怀安站在」×3
- 第 6 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「手指摩挲登记表」已存在
- 第 7 章：
  - 单条套路句式超限：「王守义的」×4
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题与《手指摩挲登记表》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - attr_adv_pct 21.4 高于目标 12.0
- 第 9 章：
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「递纸条的手指」已存在
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×4、「李怀安的」×3
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「递纸条的手指」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17311
chapter_chars_mean: 1731
chapter_chars_median: 1781
chapter_chars_cv: 0.13
paragraphs_mean: 41.3
dialogue_chars_pct: 41.2
dialogue_para_pct: 79.2
interiority_para_pct: 8.4
narration_para_pct: 12.4
turn_under20_pct: 72.4
turn_over200_pct: 0.0
attr_say_pct: 22.4
attr_adv_pct: 13.1
scenes_per_chapter: 1.5
dialogue_run_mean: 5.0
turn_len_median: 13
```
