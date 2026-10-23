# 旧凭牌 生成报告

slug：`shuangwen-20261022-117`
档位：爽文　闸门模式：observe
章数：10　总字数：19369
LLM 调用：97 次，累计 445.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧凭牌的触感 | 1869 | normal | 100.0 | 0 |  | 2 |
| 2 | 翻登记簿的少年 | 1562 | normal | 90.1 | 0 |  | 2 |
| 3 | 签名的重量 | 1903 | normal | 91.8 | 0 |  | 1 |
| 4 | 手指摩挲登记簿边缘 | 1933 | normal | 91.9 | 0 |  | 2 |
| 5 | 拍桌的回音 | 1607 | normal | 93.3 | 0 |  | 1 |
| 6 | 拍桌的回音 | 1821 | normal | 90.9 | 0 |  | 2 |
| 7 | 拍桌的回音 | 1743 | normal | 89.6 | 0 |  | 2 |
| 8 | 翻旧凭牌的少年 | 1907 | normal | 36.7 | 0 |  | 4 |
| 9 | 翻旧凭牌的少年 | 2251 | normal | 91.5 | 0 |  | 4 |
| 10 | 拍桌的回音 | 2763 | long | 90.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李怀远的」×3
  - attr_adv_pct 14.3 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「李怀远的」×5
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「登记处」×4
- 第 4 章：
  - 单条套路句式超限：「李怀远的」×9
  - attr_adv_pct 12.5 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「李怀远的」×4
- 第 6 章：
  - 单条套路句式超限：「李怀远的」×10
  - [observe] 标题重复：「拍桌的回音」已存在
- 第 7 章：
  - 单条套路句式超限：「李怀远的」×3
  - [observe] 标题重复：「拍桌的回音」已存在
- 第 8 章：
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 16.5 高于目标 14.0
  - [observe] attr_adv_pct 29.4 > 25.0（结构塌缩）
  - [observe] 标题与《旧凭牌的触感》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「李怀远的」×4
  - narration_para_pct 2.0 低于目标 5.0
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「翻旧凭牌的少年」已存在
- 第 10 章：
  - 单条套路句式超限：「李怀远的」×10
  - [observe] 标题重复：「拍桌的回音」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18378
chapter_chars_mean: 1838
chapter_chars_median: 1770
chapter_chars_cv: 0.18
paragraphs_mean: 42
dialogue_chars_pct: 47.9
dialogue_para_pct: 86.5
interiority_para_pct: 5.9
narration_para_pct: 7.6
turn_under20_pct: 75.8
turn_over200_pct: 0.0
attr_say_pct: 32.7
attr_adv_pct: 12.0
scenes_per_chapter: 1.9
dialogue_run_mean: 7.9
turn_len_median: 14
```
