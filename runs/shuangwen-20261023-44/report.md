# 墨迹 生成报告

slug：`shuangwen-20261023-44`
档位：爽文　闸门模式：observe
章数：10　总字数：18265
LLM 调用：97 次，累计 422.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账簿与木匣的对峙 | 1320 | normal | 99.1 | 0 |  | 0 |
| 2 | 账本上的三两银 | 2169 | normal | 93.2 | 0 |  | 2 |
| 3 | 指尖触碰账页 | 1818 | normal | 93.3 | 0 |  | 2 |
| 4 | 铜锁的裂痕 | 2013 | normal | 90.7 | 0 |  | 0 |
| 5 | 账本摊开的瞬间 | 1819 | normal | 91.0 | 0 |  | 0 |
| 6 | 账页上的缺口 | 1888 | normal | 91.1 | 0 |  | 2 |
| 7 | 旧账本摊开的刹那 | 1842 | normal | 36.6 | 0 |  | 4 |
| 8 | 红印压不住旧账本 | 1853 | normal | 91.7 | 0 |  | 2 |
| 9 | 指尖摩挲旧账本 | 1582 | normal | 94.5 | 0 |  | 1 |
| 10 | 指尖摩挲旧账本 | 1951 | long | 92.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 14.3 高于目标 12.0
- 第 3 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 15.4 高于目标 12.0
- 第 6 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 18.5 高于目标 14.0
- 第 7 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「他知道，这场较量才刚刚开始…」）
  - [observe] 标题与《账本摊开的瞬间》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「天机阁」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 9 章：
  - narration_para_pct 2.9 低于目标 5.0
- 第 10 章：
  - [observe] 标题重复：「指尖摩挲旧账本」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17272
chapter_chars_mean: 1727
chapter_chars_median: 1752
chapter_chars_cv: 0.13
paragraphs_mean: 41.7
dialogue_chars_pct: 52.1
dialogue_para_pct: 85.8
interiority_para_pct: 5.2
narration_para_pct: 9.1
turn_under20_pct: 73.5
turn_over200_pct: 0.0
attr_say_pct: 22.6
attr_adv_pct: 8.3
scenes_per_chapter: 1.9
dialogue_run_mean: 8.6
turn_len_median: 13
```
