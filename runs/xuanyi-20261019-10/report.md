# 钥匙串 生成报告

slug：`xuanyi-20261019-10`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15658
LLM 调用：68 次，累计 235.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手机蓝光映脸 | 2148 | short | 93.7 | 0 |  | 3 |
| 2 | 手机蓝光映脸 | 4035 | normal | 6.4 | 0 |  | 6 |
| 3 | 钥匙串低语 | 3862 | normal | 54.3 | 0 |  | 4 |
| 4 | 钥匙串低语 | 3638 | normal | 89.3 | 0 |  | 4 |
| 5 | 计费单失踪时刻 | 1970 | short | 90.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「城东旧货市场」×3
  - dialogue_chars_pct 18.1 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「刚才那张计费单上显示的是他完成了一个订单后立即接…」）
- 第 2 章：
  - 单条套路句式超限：「不仅仅是」×3
  - dialogue_chars_pct 6.9 低于目标 20.0
  - interiority_para_pct 26.4 高于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - dialogue_run_mean 1.3 低于目标 1.5
  - [observe] 标题重复：「手机蓝光映脸」已存在
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「个神秘的」×3
  - dialogue_chars_pct 13.6 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「您正等待一位尚未预订的乘客…」）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈志远的」×5、「点了点头」×3
  - narration_para_pct 15.3 低于目标 20.0
  - [observe] 标题重复：「钥匙串低语」已存在

## 整书结构指标

```
chapters: 5
total_chars: 15060
chapter_chars_mean: 3012
chapter_chars_median: 3481
chapter_chars_cv: 0.32
paragraphs_mean: 52.2
dialogue_chars_pct: 18.3
dialogue_para_pct: 52.5
interiority_para_pct: 19.2
narration_para_pct: 28.3
turn_under20_pct: 80.6
turn_over200_pct: 0.0
attr_say_pct: 34.6
attr_adv_pct: 6.4
scenes_per_chapter: 4.6
dialogue_run_mean: 2.6
turn_len_median: 11
```
