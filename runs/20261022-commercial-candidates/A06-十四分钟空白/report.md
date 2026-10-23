# 十四分钟空白 生成报告

slug：`xuanyi-20261019-250`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14870
LLM 调用：68 次，累计 230.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计费器的停滞时刻 | 1765 | short | 97.9 | 0 |  | 2 |
| 2 | 车载音响的沉默 | 4104 | normal | 87.5 | 0 |  | 5 |
| 3 | 数据屏的闪烁残影 | 3637 | normal | 90.9 | 0 |  | 3 |
| 4 | 车票的日期重叠 | 3458 | normal | 90.4 | 0 |  | 2 |
| 5 | 手机的通话记录 | 1901 | short | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈志远的」×5、「他知道这」×3
  - narration_para_pct 11.1 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×5、「点了点头」×3、「带着一丝」×3
  - dialogue_chars_pct 19.8 低于目标 20.0
  - interiority_para_pct 21.0 高于目标 20.0
  - narration_para_pct 18.5 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「或许，正是这段音乐带他回到了那个雨夜，那些未曾被…」）
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈志远的」×8、「点了点头」×3、「为什么会」×3
  - narration_para_pct 10.7 低于目标 20.0
- 第 4 章：
  - narration_para_pct 16.7 低于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0
- 第 5 章：
  - 命中套话收尾句
  - narration_para_pct 13.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14134
chapter_chars_mean: 2827
chapter_chars_median: 3299
chapter_chars_cv: 0.36
paragraphs_mean: 65.4
dialogue_chars_pct: 39.4
dialogue_para_pct: 73.8
interiority_para_pct: 11.5
narration_para_pct: 14.6
turn_under20_pct: 75.8
turn_over200_pct: 0.0
attr_say_pct: 38.0
attr_adv_pct: 7.9
scenes_per_chapter: 4
dialogue_run_mean: 5.5
turn_len_median: 13
```
