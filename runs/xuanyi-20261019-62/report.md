# 当票 生成报告

slug：`xuanyi-20261019-62`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14123
LLM 调用：68 次，累计 228.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 当票与怀表的对峙 | 1470 | short | 96.6 | 0 |  | 2 |
| 2 | 铜钥匙的重量 | 3940 | normal | 90.0 | 0 |  | 3 |
| 3 | 怀表与当票对峙 | 3775 | normal | 92.0 | 0 |  | 2 |
| 4 | 铜钥匙的低语 | 3138 | normal | 91.3 | 0 |  | 3 |
| 5 | 当票与怀表的对峙 | 1795 | short | 91.6 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈知远的」×3
  - narration_para_pct 12.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周慕云的」×4、「“我不知道」×3、「”周慕云轻」×3
  - narration_para_pct 17.0 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「他开门一看，竟是个衣衫褴褛的男子抱着一个雕花木匣…」）
- 第 3 章：
  - 单条套路句式超限：「周慕云的」×4
  - narration_para_pct 12.0 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周慕云的」×9、「他知道这」×5、「沈知远的」×4
  - narration_para_pct 10.9 低于目标 20.0
  - [observe] 标题与《铜钥匙的重量》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「沈知远的」×7
  - 情节与已写章节重复 0.63 ≥ 0.62（撞上「周慕云发现怀表时间与账本不符，调查沈知远当铺异常账目，揭…」）
  - narration_para_pct 16.1 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 标题重复：「当票与怀表的对峙」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13474
chapter_chars_mean: 2695
chapter_chars_median: 2996
chapter_chars_cv: 0.4
paragraphs_mean: 56.6
dialogue_chars_pct: 34.3
dialogue_para_pct: 75.6
interiority_para_pct: 10.7
narration_para_pct: 13.7
turn_under20_pct: 77.2
turn_over200_pct: 0.0
attr_say_pct: 25.6
attr_adv_pct: 6.8
scenes_per_chapter: 2.2
dialogue_run_mean: 4.0
turn_len_median: 12
```
