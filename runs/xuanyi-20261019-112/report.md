# 登录簿 生成报告

slug：`xuanyi-20261019-112`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15043
LLM 调用：68 次，累计 225.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 打印稿边缘的指纹 | 1794 | short | 98.9 | 0 |  | 3 |
| 2 | 屏幕边缘的冷光 | 3509 | normal | 91.3 | 0 |  | 2 |
| 3 | 深夜的上网记录 | 4564 | normal | 90.0 | 0 |  | 3 |
| 4 | 暂停键上的光斑 | 3455 | normal | 90.6 | 0 |  | 3 |
| 5 | 纸张背面的水渍 | 1716 | short | 93.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈文远的」×4、「周雪梅的」×3
  - narration_para_pct 14.7 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周雪梅的」×6、「沈文远的」×6、「“我不知道」×3
  - narration_para_pct 15.5 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×4、「”周雪梅轻」×3
  - narration_para_pct 7.4 低于目标 20.0
  - [observe] 章内自我复读 5 句（如「他注意到其中有一份记录特别引起了他的注意——那就…」）
- 第 4 章：
  - 单条套路句式超限：「周雪梅的」×10、「沈文远的」×7、「沈文远点了点头」×3
  - narration_para_pct 11.5 低于目标 20.0
  - [observe] attr_adv_pct 30.8 > 20.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「周雪梅的」×7

## 整书结构指标

```
chapters: 5
total_chars: 14304
chapter_chars_mean: 2861
chapter_chars_median: 3266
chapter_chars_cv: 0.41
paragraphs_mean: 65.8
dialogue_chars_pct: 43.9
dialogue_para_pct: 78.6
interiority_para_pct: 8.8
narration_para_pct: 12.6
turn_under20_pct: 72.4
turn_over200_pct: 0.0
attr_say_pct: 19.2
attr_adv_pct: 11.0
scenes_per_chapter: 3.2
dialogue_run_mean: 4.9
turn_len_median: 13
```
