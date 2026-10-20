# 刷卡密码 生成报告

slug：`xuanyi-20261019-240`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15767
LLM 调用：68 次，累计 238.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 刷卡机闪烁的绿光 | 1525 | short | 97.5 | 0 |  | 0 |
| 2 | 指纹识别器的异常提示 | 3879 | normal | 91.0 | 0 |  | 4 |
| 3 | 打印新表时的指尖颤抖 | 3890 | normal | 89.9 | 0 |  | 1 |
| 4 | 刷卡机闪烁的绿光 | 4480 | normal | 91.5 | 0 |  | 3 |
| 5 | 刷卡机闪烁的绿光 | 1988 | short | 90.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「沈嘉文的」×9、「周若雪的」×5
  - narration_para_pct 14.9 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「可系统显示他在周三还进了大楼…」）
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周若雪的」×3、「他知道这」×3
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×6、「他知道这」×5、「沈嘉文的」×3
  - narration_para_pct 15.0 低于目标 20.0
  - [observe] 标题重复：「刷卡机闪烁的绿光」已存在
- 第 5 章：
  - 单条套路句式超限：「周若雪的」×5、「沈嘉文的」×5
  - narration_para_pct 4.4 低于目标 20.0
  - [observe] 标题重复：「刷卡机闪烁的绿光」已存在

## 整书结构指标

```
chapters: 5
total_chars: 15028
chapter_chars_mean: 3006
chapter_chars_median: 3713
chapter_chars_cv: 0.42
paragraphs_mean: 65
dialogue_chars_pct: 35.5
dialogue_para_pct: 73.0
interiority_para_pct: 10.3
narration_para_pct: 16.7
turn_under20_pct: 74.1
turn_over200_pct: 0.0
attr_say_pct: 24.9
attr_adv_pct: 12.4
scenes_per_chapter: 4.2
dialogue_run_mean: 5.0
turn_len_median: 14
```
