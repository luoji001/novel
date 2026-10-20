# 错位登录 生成报告

slug：`xuanyi-20261019-32`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15973
LLM 调用：68 次，累计 236.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 指纹与老式键盘 | 1740 | short | 99.0 | 0 |  | 2 |
| 2 | 登记表上的异常时间 | 4399 | normal | 87.8 | 0 |  | 4 |
| 3 | 纸条上的陌生IP | 3618 | normal | 91.2 | 0 |  | 3 |
| 4 | 指缝间的数字密码 | 4181 | normal | 87.4 | 0 |  | 4 |
| 5 | 手指拂过老式屏幕 | 2030 | short | 88.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈雪梅的」×4
  - narration_para_pct 13.3 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈雪梅的」×13、「林志远的」×5、「他知道这」×4
  - narration_para_pct 16.7 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 章内自我复读 19 句（如「他指向那个写着某个具体时间段的地方，“这个时间比…」）
- 第 3 章：
  - 单条套路句式超限：「林志远的」×9、「”陈雪梅轻」×3、「”陈雪梅低」×3
  - narration_para_pct 10.9 低于目标 20.0
  - attr_adv_pct 10.5 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「林志远的」×8、「陈雪梅的」×7
  - narration_para_pct 6.2 低于目标 20.0
  - attr_adv_pct 11.8 高于目标 10.0
  - [observe] 章内自我复读 19 句（如「林志远的目光没有移开，而是直视着她的眼睛，“而且…」）
- 第 5 章：
  - 单条套路句式超限：「陈雪梅的」×7、「林志远的」×3
  - narration_para_pct 2.7 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - dialogue_run_mean 11.7 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 15298
chapter_chars_mean: 3060
chapter_chars_median: 3474
chapter_chars_cv: 0.39
paragraphs_mean: 59
dialogue_chars_pct: 45.1
dialogue_para_pct: 82.4
interiority_para_pct: 7.1
narration_para_pct: 10.5
turn_under20_pct: 65.3
turn_over200_pct: 0.0
attr_say_pct: 16.2
attr_adv_pct: 11.5
scenes_per_chapter: 2.4
dialogue_run_mean: 7.0
turn_len_median: 15
```
