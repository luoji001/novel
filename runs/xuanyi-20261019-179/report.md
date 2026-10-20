# 旧信封 生成报告

slug：`xuanyi-20261019-179`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13961
LLM 调用：68 次，累计 238.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铅笔轻叩桌面 | 1757 | short | 91.7 | 0 |  | 1 |
| 2 | 指纹与铜印 | 3274 | normal | 87.4 | 0 |  | 4 |
| 3 | 钥匙藏入旧箱中 | 3210 | normal | 91.7 | 0 |  | 4 |
| 4 | 铅笔轻叩桌面 | 3901 | normal | 86.0 | 0 |  | 3 |
| 5 | 铜印边缘的磨损痕迹 | 1814 | short | 91.3 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 17.9 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈海山的」×6、「林素云的」×3
  - dialogue_chars_pct 59.2 高于目标 58.0
  - narration_para_pct 2.7 低于目标 20.0
  - dialogue_run_mean 18 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「林素云的」×6、「陈海山的」×4
  - narration_para_pct 13.9 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 章内自我复读 2 句（如「林素云的手指停顿了一下，然后缓缓地展开了那封信…」）
- 第 4 章：
  - 单条套路句式超限：「陈海山的」×7、「陈海山点」×5
  - [observe] 章内自我复读 23 句（如「陈海山点点头，“确实，有些人的地址变了，但不是所…」）
  - [observe] 标题重复：「铅笔轻叩桌面」已存在
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林素云的」×5、「陈海山的」×3
  - 情节与已写章节重复 0.64 ≥ 0.62（撞上「林素云发现一笔三年前的汇款记录仍用旧地址，引发她对王振国…」）
  - narration_para_pct 8.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13291
chapter_chars_mean: 2658
chapter_chars_median: 3051
chapter_chars_cv: 0.34
paragraphs_mean: 59.2
dialogue_chars_pct: 35.7
dialogue_para_pct: 74.4
interiority_para_pct: 8.7
narration_para_pct: 16.9
turn_under20_pct: 80.2
turn_over200_pct: 0.0
attr_say_pct: 17.3
attr_adv_pct: 6.2
scenes_per_chapter: 4.2
dialogue_run_mean: 7.1
turn_len_median: 12
```
