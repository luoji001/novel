# 副本 生成报告

slug：`shuangwen-20261022-66`
档位：爽文　闸门模式：observe
章数：10　总字数：18893
LLM 调用：97 次，累计 424.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 结算单边缘 | 1694 | normal | 100.0 | 0 |  | 1 |
| 2 | 签字笔消失 | 1747 | normal | 93.5 | 0 |  | 1 |
| 3 | 签字笔划痕 | 1807 | normal | 92.0 | 0 |  | 1 |
| 4 | 工牌边缘 | 1743 | normal | 90.9 | 0 |  | 0 |
| 5 | 翻找手机记录 | 1996 | normal | 36.5 | 0 |  | 1 |
| 6 | 一份副本较量 | 1887 | normal | 92.8 | 0 |  | 2 |
| 7 | 一份副本较量 | 1789 | normal | 35.8 | 0 |  | 4 |
| 8 | 签字笔划痕 | 1990 | normal | 92.7 | 0 |  | 2 |
| 9 | 签字笔划痕 | 1754 | normal | 92.4 | 0 |  | 1 |
| 10 | 签字笔指向名字 | 2476 | long | 91.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「办公室」×4
- 第 3 章：
  - [observe] 标题与《签字笔消失》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「办公室」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 7 章：
  - dialogue_run_mean 18.5 高于目标 14.0
  - [observe] 章内自我复读 1 句（如「我们是不是该开始计算一下这笔尾款了？…」）
  - [observe] attr_adv_pct 27.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「一份副本较量」已存在
- 第 8 章：
  - attr_adv_pct 17.6 高于目标 12.0
  - [observe] 标题重复：「签字笔划痕」已存在
- 第 9 章：
  - [observe] 标题重复：「签字笔划痕」已存在
- 第 10 章：
  - narration_para_pct 4.0 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17911
chapter_chars_mean: 1791
chapter_chars_median: 1696
chapter_chars_cv: 0.13
paragraphs_mean: 41.9
dialogue_chars_pct: 48.1
dialogue_para_pct: 82.2
interiority_para_pct: 6.3
narration_para_pct: 11.5
turn_under20_pct: 69.2
turn_over200_pct: 0.0
attr_say_pct: 36.9
attr_adv_pct: 14.7
scenes_per_chapter: 2
dialogue_run_mean: 7.1
turn_len_median: 14
```
