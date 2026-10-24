# 玉简 生成报告

slug：`shuangwen-20261023-08`
档位：爽文　闸门模式：observe
章数：10　总字数：19395
LLM 调用：97 次，累计 450.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜秤上的瓷盘 | 2249 | normal | 39.1 | 0 |  | 2 |
| 2 | 翻阅账本的指尖 | 2085 | normal | 93.4 | 0 |  | 3 |
| 3 | 玉简残片的共鸣 | 2154 | normal | 91.2 | 0 |  | 3 |
| 4 | 玉简轻叩木桌 | 1872 | normal | 91.5 | 0 |  | 1 |
| 5 | 玉简轻叩木桌 | 1819 | normal | 93.5 | 0 |  | 3 |
| 6 | 玉简轻叩木桌 | 1611 | normal | 91.1 | 0 |  | 3 |
| 7 | 铜秤上的碎石 | 1593 | normal | 37.2 | 0 |  | 3 |
| 8 | 玉简轻叩木桌 | 1837 | normal | 92.6 | 0 |  | 4 |
| 9 | 玉简轻叩铜秤 | 1599 | normal | 92.6 | 0 |  | 2 |
| 10 | 玉简轻叩铜秤 | 2566 | long | 90.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李怀远的」×9
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李怀远的」×3
  - attr_adv_pct 12.5 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李怀远的」×3、「验货台」×3
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 21 高于目标 14.0
- 第 4 章：
  - narration_para_pct 2.6 低于目标 5.0
- 第 5 章：
  - 单条套路句式超限：「验货台」×5、「李怀远的」×4
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「玉简轻叩木桌」已存在
- 第 6 章：
  - 单条套路句式超限：「李怀远的」×5、「验货台」×4
  - narration_para_pct 3.2 低于目标 5.0
  - [observe] 标题重复：「玉简轻叩木桌」已存在
- 第 7 章：
  - 单条套路句式超限：「李怀远的」×3
  - [observe] 章内自我复读 2 句（如「那你为什么现在才拿出来？…」）
  - [observe] 标题与《铜秤上的瓷盘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李怀远的」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「玉简轻叩木桌」已存在
- 第 9 章：
  - 单条套路句式超限：「李怀远的」×3
  - [observe] 标题与《玉简轻叩木桌》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「验货台」×5
  - dialogue_chars_pct 29.7 低于目标 30.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「玉简轻叩铜秤」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18393
chapter_chars_mean: 1839
chapter_chars_median: 1760
chapter_chars_cv: 0.17
paragraphs_mean: 42.7
dialogue_chars_pct: 44.3
dialogue_para_pct: 82.3
interiority_para_pct: 5.4
narration_para_pct: 12.3
turn_under20_pct: 77.8
turn_over200_pct: 0.0
attr_say_pct: 20.8
attr_adv_pct: 12.4
scenes_per_chapter: 1.3
dialogue_run_mean: 7.0
turn_len_median: 12
```
