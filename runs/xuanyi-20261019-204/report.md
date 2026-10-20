# 旧粮票的重量 生成报告

slug：`xuanyi-20261019-204`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15226
LLM 调用：68 次，累计 240.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙开铁皮柜 | 1810 | short | 97.9 | 0 |  | 2 |
| 2 | 锁孔旁的划痕 | 4605 | normal | 0.0 | 0 |  | 6 |
| 3 | 旧粮票的重量 | 3809 | normal | 89.1 | 0 |  | 3 |
| 4 | 工牌背面的凹陷 | 3198 | normal | 15.7 | 0 |  | 4 |
| 5 | 粮票背面的日期 | 1799 | short | 55.1 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈文远的」×4
  - attr_adv_pct 12.5 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「陈文远的」×5、「他知道这」×3
  - dialogue_run_mean 1 低于目标 1.5
  - [observe] 章内自我复读 32 句（如「一张薄薄的便签纸从中滑落出来，纸上用圆珠笔歪歪扭…」）
  - [observe] dialogue_chars_pct 2.0 < 6.0（结构塌缩）
  - [observe] interiority_para_pct 34.0 > 32.0（结构塌缩）
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「陈文远的」×5
  - narration_para_pct 16.0 低于目标 20.0
  - [observe] 章内自我复读 20 句（如「周淑芬没有多说什么，只是将目光投向远处墙上的生产…」）
- 第 4 章：
  - 单条套路句式超限：「周淑芬的」×4、「陈文远的」×3
  - dialogue_chars_pct 8.2 低于目标 20.0
  - interiority_para_pct 22.4 高于目标 20.0
  - dialogue_run_mean 1.2 低于目标 1.5
- 第 5 章：
  - 单条套路句式超限：「他知道自己」×3
  - dialogue_chars_pct 6.9 低于目标 20.0
  - interiority_para_pct 29.0 高于目标 20.0
  - dialogue_run_mean 1.2 低于目标 1.5
  - [observe] 章内自我复读 16 句（如「正面印着“凭此票可兑换粮食”的字样，背面则用铅笔…」）

## 整书结构指标

```
chapters: 5
total_chars: 14664
chapter_chars_mean: 2933
chapter_chars_median: 3085
chapter_chars_cv: 0.41
paragraphs_mean: 48.8
dialogue_chars_pct: 14.3
dialogue_para_pct: 41.8
interiority_para_pct: 22.4
narration_para_pct: 35.8
turn_under20_pct: 92.2
turn_over200_pct: 0.0
attr_say_pct: 12.2
attr_adv_pct: 11.6
scenes_per_chapter: 4.2
dialogue_run_mean: 2.2
turn_len_median: 10
```
