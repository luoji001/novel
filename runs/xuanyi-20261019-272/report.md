# 登录纸条 生成报告

slug：`xuanyi-20261019-272`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15453
LLM 调用：68 次，累计 235.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 小飞电脑登录成功 | 1709 | short | 100.0 | 0 |  | 3 |
| 2 | 账单上的异常数字 | 3843 | normal | 85.1 | 0 |  | 4 |
| 3 | 屏幕前的沉默对峙 | 3589 | normal | 90.1 | 0 |  | 5 |
| 4 | 屏幕前的异常登录 | 4329 | normal | 90.9 | 0 |  | 2 |
| 5 | 密码纸条的发现 | 1978 | short | 92.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈雪梅的」×3
  - narration_para_pct 9.8 低于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「市网络安全中心」×6
  - narration_para_pct 16.7 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 章内自我复读 23 句（如「那天夜里，他确实记得小飞电脑有动静，但也只是正常…」）
- 第 3 章：
  - 单条套路句式超限：「林志远的」×13、「陈雪梅的」×6、「”陈雪梅低」×5
  - dialogue_chars_pct 58.8 高于目标 58.0
  - narration_para_pct 6.5 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - dialogue_run_mean 11.7 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「他知道这」×5、「说道“我」×4、「林志远和陈雪梅」×3
  - narration_para_pct 19.4 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「陈雪梅点」×3、「林志远的」×3
  - narration_para_pct 14.6 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14733
chapter_chars_mean: 2947
chapter_chars_median: 3419
chapter_chars_cv: 0.38
paragraphs_mean: 63.6
dialogue_chars_pct: 38.6
dialogue_para_pct: 77.1
interiority_para_pct: 8.9
narration_para_pct: 14.1
turn_under20_pct: 74.6
turn_over200_pct: 0.0
attr_say_pct: 18.1
attr_adv_pct: 11.7
scenes_per_chapter: 4.4
dialogue_run_mean: 5.8
turn_len_median: 10
```
