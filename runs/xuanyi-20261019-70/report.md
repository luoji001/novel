# 断电 生成报告

slug：`xuanyi-20261019-70`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14950
LLM 调用：68 次，累计 221.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 黑屏十四分钟 | 1917 | short | 96.6 | 0 |  | 1 |
| 2 | 摩挲车钥匙的手指 | 3579 | normal | 89.6 | 0 |  | 4 |
| 3 | 摩挲车钥匙的手指 | 3648 | normal | 91.2 | 0 |  | 4 |
| 4 | 摩挲方向盘套的手指 | 3693 | normal | 30.7 | 0 |  | 4 |
| 5 | 触摸摄像头外壳 | 2108 | short | 88.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 11.1 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「陈志远的」×5
  - narration_para_pct 19.4 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「你确定是你的记录仪？…」）
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×3、「”周晓芸低」×3、「点了点头」×3
  - narration_para_pct 10.8 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 标题重复：「摩挲车钥匙的手指」已存在
- 第 4 章：
  - 单条套路句式超限：「天启科技」×7
  - dialogue_chars_pct 10.3 低于目标 20.0
  - interiority_para_pct 26.5 高于目标 20.0
  - [observe] 章内自我复读 1 句（如「你不是第一个发现这个问题的人…」）
- 第 5 章：
  - 单条套路句式超限：「为什么会」×3
  - narration_para_pct 8.5 低于目标 20.0
  - attr_adv_pct 13.3 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14297
chapter_chars_mean: 2859
chapter_chars_median: 3439
chapter_chars_cv: 0.31
paragraphs_mean: 57
dialogue_chars_pct: 36.4
dialogue_para_pct: 68.5
interiority_para_pct: 11.8
narration_para_pct: 19.7
turn_under20_pct: 64.8
turn_over200_pct: 0.0
attr_say_pct: 17.4
attr_adv_pct: 9.4
scenes_per_chapter: 3.6
dialogue_run_mean: 4.4
turn_len_median: 17
```
