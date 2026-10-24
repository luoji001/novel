# 令牌 生成报告

slug：`shuangwen-20261023-05`
档位：爽文　闸门模式：observe
章数：10　总字数：19477
LLM 调用：97 次，累计 440.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 令牌裂痕现真相 | 1567 | normal | 99.5 | 0 |  | 0 |
| 2 | 储物戒的重量 | 1866 | normal | 90.7 | 0 |  | 2 |
| 3 | 指尖划过令牌纹路 | 1962 | normal | 36.7 | 0 |  | 1 |
| 4 | 令牌裂痕现真相 | 2005 | normal | 36.6 | 0 |  | 2 |
| 5 | 令牌背面的秘密 | 1982 | normal | 93.4 | 0 |  | 1 |
| 6 | 指尖划过令牌纹路 | 1966 | normal | 36.8 | 0 |  | 3 |
| 7 | 指尖抚过密令残页 | 1690 | normal | 88.6 | 0 |  | 4 |
| 8 | 玉简裂痕现残页 | 1755 | normal | 92.2 | 0 |  | 0 |
| 9 | 令牌裂痕现真相 | 1797 | normal | 92.2 | 0 |  | 3 |
| 10 | 指尖抚过令牌纹路 | 2877 | long | 37.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「不仅仅是」×3
  - attr_adv_pct 13.3 高于目标 12.0
- 第 3 章：
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「这不是普通的通行令牌…」）
  - [observe] 标题重复：「令牌裂痕现真相」已存在
- 第 5 章：
  - 单条套路句式超限：「藏经阁」×3
- 第 6 章：
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 与历史章节逐字重复 3 句（如「这时，远处传来一阵脚步声…」）
  - [observe] 标题重复：「指尖划过令牌纹路」已存在
- 第 7 章：
  - 单条套路句式超限：「林子安的」×3
  - narration_para_pct 2.4 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - dialogue_run_mean 40 高于目标 14.0
- 第 9 章：
  - 命中套话收尾句
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「令牌裂痕现真相」已存在
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「藏经阁」×4、「林子安站在」×3
  - [observe] attr_adv_pct 31.6 > 25.0（结构塌缩）
  - [observe] 标题与《指尖划过令牌纹路》近似 0.88 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18399
chapter_chars_mean: 1840
chapter_chars_median: 1810
chapter_chars_cv: 0.18
paragraphs_mean: 45.7
dialogue_chars_pct: 49.2
dialogue_para_pct: 83.6
interiority_para_pct: 5.0
narration_para_pct: 11.4
turn_under20_pct: 72.5
turn_over200_pct: 0.0
attr_say_pct: 24.1
attr_adv_pct: 16.8
scenes_per_chapter: 1.5
dialogue_run_mean: 9.8
turn_len_median: 12
```
