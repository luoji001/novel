# 账本 生成报告

slug：`shuangwen-20261022-53`
档位：爽文　闸门模式：observe
章数：10　总字数：18585
LLM 调用：97 次，累计 433.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜铃响起时门被撞开 | 1586 | normal | 98.4 | 0 |  | 3 |
| 2 | 药秤停了一瞬 | 1874 | normal | 92.4 | 0 |  | 1 |
| 3 | 盖章的瞬间 | 1940 | normal | 92.6 | 0 |  | 2 |
| 4 | 账簿摊开时的低语 | 1791 | normal | 91.4 | 0 |  | 3 |
| 5 | 账本摊开时的低语 | 2043 | normal | 90.3 | 0 |  | 3 |
| 6 | 账本摊开时的低语 | 1693 | normal | 90.0 | 0 |  | 2 |
| 7 | 账本摊开时的低语 | 1834 | normal | 90.1 | 0 |  | 2 |
| 8 | 账本摊开时的低语 | 1653 | normal | 93.1 | 0 |  | 3 |
| 9 | 账本摊开时的低语 | 1688 | normal | 92.1 | 0 |  | 1 |
| 10 | 清单边缘的红印 | 2473 | long | 92.2 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李守仁的」×3
  - attr_adv_pct 18.2 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「李怀远点」×3
- 第 3 章：
  - 单条套路句式超限：「李守仁的」×4
  - attr_adv_pct 14.3 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「李怀远的」×4
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 16 高于目标 14.0
- 第 5 章：
  - narration_para_pct 3.3 低于目标 5.0
  - dialogue_run_mean 14.5 高于目标 14.0
  - [observe] 标题与《账簿摊开时的低语》近似 0.88 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「李怀远的」×4
  - [observe] 标题重复：「账本摊开时的低语」已存在
- 第 7 章：
  - 单条套路句式超限：「说道“你」×4
  - [observe] 标题重复：「账本摊开时的低语」已存在
- 第 8 章：
  - narration_para_pct 2.9 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「账本摊开时的低语」已存在
- 第 9 章：
  - [observe] 标题重复：「账本摊开时的低语」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17586
chapter_chars_mean: 1759
chapter_chars_median: 1712
chapter_chars_cv: 0.14
paragraphs_mean: 41.7
dialogue_chars_pct: 48.4
dialogue_para_pct: 85.2
interiority_para_pct: 3.4
narration_para_pct: 11.4
turn_under20_pct: 65.6
turn_over200_pct: 0.0
attr_say_pct: 17.5
attr_adv_pct: 6.0
scenes_per_chapter: 1.6
dialogue_run_mean: 7.8
turn_len_median: 14
```
