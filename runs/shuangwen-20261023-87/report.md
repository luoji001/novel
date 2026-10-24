# 地契 生成报告

slug：`shuangwen-20261023-87`
档位：爽文　闸门模式：observe
章数：10　总字数：19237
LLM 调用：97 次，累计 444.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 族谱上的朱砂笔 | 1554 | normal | 97.0 | 0 |  | 2 |
| 2 | 地契入族谱 | 2154 | normal | 90.8 | 0 |  | 1 |
| 3 | 朱砂笔的重量 | 1783 | normal | 37.6 | 0 |  | 1 |
| 4 | 签字权的争夺 | 2108 | normal | 37.5 | 0 |  | 2 |
| 5 | 地契对石碑 | 1797 | normal | 89.2 | 0 |  | 0 |
| 6 | 地契与法币对峙 | 1380 | normal | 92.9 | 0 |  | 0 |
| 7 | 地契对石碑 | 2963 | normal | 92.2 | 0 |  | 2 |
| 8 | 掀开族谱的裂缝 | 1687 | normal | 93.0 | 0 |  | 1 |
| 9 | 签字权的争夺 | 1645 | normal | 91.4 | 0 |  | 1 |
| 10 | 石碑裂痕现真章 | 2156 | long | 93.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×4
  - attr_adv_pct 16.7 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「李文远点」×3
- 第 3 章：
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 章内自我复读 2 句（如「他知道，这不仅仅是一次简单的族谱修改，而是关乎整…」）
- 第 7 章：
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「地契对石碑」已存在
- 第 8 章：
  - 单条套路句式超限：「李振邦的」×5
- 第 9 章：
  - [observe] 标题重复：「签字权的争夺」已存在
- 第 10 章：
  - 单条套路句式超限：「李文远的」×3
  - narration_para_pct 4.8 低于目标 5.0
  - attr_adv_pct 13.3 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 18279
chapter_chars_mean: 1828
chapter_chars_median: 1716
chapter_chars_cv: 0.23
paragraphs_mean: 40.3
dialogue_chars_pct: 46.2
dialogue_para_pct: 82.6
interiority_para_pct: 7.1
narration_para_pct: 10.2
turn_under20_pct: 71.8
turn_over200_pct: 0.0
attr_say_pct: 20.7
attr_adv_pct: 11.2
scenes_per_chapter: 1.4
dialogue_run_mean: 6.4
turn_len_median: 12
```
