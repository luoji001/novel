# 旧账本 生成报告

slug：`shuangwen-20261022-93`
档位：爽文　闸门模式：observe
章数：10　总字数：19188
LLM 调用：97 次，累计 448.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药罐上的指纹 | 1846 | normal | 39.6 | 0 |  | 2 |
| 2 | 揭开旧账本的秘密 | 1737 | normal | 92.7 | 0 |  | 3 |
| 3 | 账本摊开的瞬间 | 1921 | normal | 94.2 | 0 |  | 1 |
| 4 | 手指抚过清单边缘 | 2055 | normal | 93.0 | 0 |  | 0 |
| 5 | 手指抚过清单边缘 | 1788 | normal | 92.1 | 0 |  | 4 |
| 6 | 玉佩上的刻纹 | 1862 | normal | 92.1 | 0 |  | 1 |
| 7 | 手指抚过空白页 | 1765 | normal | 94.0 | 0 |  | 1 |
| 8 | 手指抚过账本边缘 | 1770 | normal | 91.5 | 0 |  | 2 |
| 9 | 铜秤摔落的刹那 | 1771 | normal | 36.8 | 0 |  | 3 |
| 10 | 手指抚过清单边缘 | 2663 | long | 37.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林小满的」×4
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 2 章：
  - narration_para_pct 4.1 低于目标 5.0
  - attr_adv_pct 17.4 高于目标 12.0
  - dialogue_run_mean 15.7 高于目标 14.0
- 第 3 章：
  - 单条套路句式超限：「李守仁的」×4、「林小满的」×4
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李守仁的」×3
  - narration_para_pct 2.3 低于目标 5.0
  - [observe] 标题重复：「手指抚过清单边缘」已存在
- 第 6 章：
  - 单条套路句式超限：「林小满的」×3
- 第 7 章：
  - 单条套路句式超限：「林小满的」×3
- 第 8 章：
  - 单条套路句式超限：「李守仁的」×5
  - [observe] 标题与《手指抚过清单边缘》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「李守仁的」×6、「林小满的」×4
  - narration_para_pct 3.4 低于目标 5.0
  - [observe] 章内自我复读 1 句（如「李守仁的手指微微发抖，他终于明白，自己这些年掌握…」）
- 第 10 章：
  - 单条套路句式超限：「李守仁的」×7
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「手指抚过清单边缘」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18160
chapter_chars_mean: 1816
chapter_chars_median: 1727
chapter_chars_cv: 0.15
paragraphs_mean: 43
dialogue_chars_pct: 51.3
dialogue_para_pct: 87.8
interiority_para_pct: 5.2
narration_para_pct: 7.0
turn_under20_pct: 75.1
turn_over200_pct: 0.0
attr_say_pct: 22.1
attr_adv_pct: 13.4
scenes_per_chapter: 1.9
dialogue_run_mean: 9.0
turn_len_median: 12
```
