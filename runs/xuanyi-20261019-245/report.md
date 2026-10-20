# 空匣 生成报告

slug：`xuanyi-20261019-245`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14503
LLM 调用：68 次，累计 230.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 录像带的裂痕 | 1710 | short | 93.8 | 0 |  | 1 |
| 2 | 药品消失的清晨 | 3753 | normal | 84.9 | 0 |  | 4 |
| 3 | 触摸电话机的胶痕 | 3457 | normal | 86.7 | 0 |  | 3 |
| 4 | 票据上的空白签名 | 3553 | normal | 90.3 | 0 |  | 3 |
| 5 | 钥匙缝隙中的纸片 | 2025 | short | 86.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈志远的」×8
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈志远的」×7、「林子安站在」×3、「林子安的」×3
  - dialogue_chars_pct 15.5 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「你看到的东西不是你以为的那个样子…」）
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林子安点了点头」×3、「林子安的」×3、「为什么会」×3
  - dialogue_chars_pct 18.9 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×7、「林子安的」×5
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「林子安的心跳加快了几分…」）
- 第 5 章：
  - dialogue_chars_pct 13.9 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13879
chapter_chars_mean: 2776
chapter_chars_median: 3293
chapter_chars_cv: 0.33
paragraphs_mean: 54.2
dialogue_chars_pct: 18.4
dialogue_para_pct: 51.5
interiority_para_pct: 17.4
narration_para_pct: 31.1
turn_under20_pct: 80.8
turn_over200_pct: 0.0
attr_say_pct: 23.0
attr_adv_pct: 5.3
scenes_per_chapter: 4.8
dialogue_run_mean: 2.8
turn_len_median: 12
```
