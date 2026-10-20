# 钥匙的真相 生成报告

slug：`xuanyi-20261019-231`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14223
LLM 调用：68 次，累计 219.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 锁舌上的锈迹 | 1756 | short | 100.0 | 0 |  | 2 |
| 2 | 钥匙的回声 | 3726 | normal | 90.0 | 0 |  | 1 |
| 3 | 钥匙的失踪时刻 | 3317 | normal | 91.1 | 0 |  | 3 |
| 4 | 登记簿的锯齿痕迹 | 3565 | normal | 89.3 | 0 |  | 4 |
| 5 | 钥匙与空口袋 | 1854 | short | 92.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈慕云的」×4
  - attr_adv_pct 11.1 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「沈慕云的」×5、「他知道这」×4、「沈慕云点了点头」×3
- 第 3 章：
  - 单条套路句式超限：「沈慕云的」×5、「他知道这」×3
  - narration_para_pct 18.8 低于目标 20.0
  - attr_adv_pct 15.4 高于目标 10.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈慕云的」×9、「他知道这」×6、「周启明的」×3
  - narration_para_pct 16.7 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「走出登记室，他抬头望向外面的街道，阳光照在他的脸…」）
- 第 5 章：
  - 单条套路句式超限：「周启明的」×10
  - narration_para_pct 5.9 低于目标 20.0
  - dialogue_run_mean 10.3 高于目标 10.0
  - [observe] attr_adv_pct 40.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13560
chapter_chars_mean: 2712
chapter_chars_median: 3164
chapter_chars_cv: 0.34
paragraphs_mean: 58.6
dialogue_chars_pct: 35.3
dialogue_para_pct: 71.1
interiority_para_pct: 11.0
narration_para_pct: 17.9
turn_under20_pct: 68.2
turn_over200_pct: 0.0
attr_say_pct: 13.6
attr_adv_pct: 11.1
scenes_per_chapter: 3.4
dialogue_run_mean: 5.3
turn_len_median: 15
```
