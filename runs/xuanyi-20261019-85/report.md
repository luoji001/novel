# 黑衣人 生成报告

slug：`xuanyi-20261019-85`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15830
LLM 调用：68 次，累计 236.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 影子多了一寸 | 2281 | short | 92.3 | 0 |  | 4 |
| 2 | 日期错位 | 4139 | normal | 91.1 | 0 |  | 2 |
| 3 | 遗落的身份证 | 3750 | normal | 90.5 | 0 |  | 3 |
| 4 | 指纹在玻璃上留下痕迹 | 3778 | normal | 88.3 | 0 |  | 4 |
| 5 | 凝视收银机的陌生人 | 1877 | short | 76.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周启明的」×5、「林子墨的」×4
  - dialogue_chars_pct 16.5 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「周启明的」×10、「林子墨点了点头」×3、「林子墨站在」×3
  - [observe] 章内自我复读 11 句（如「你知道你在做什么吗？这些录像是我们公司最重要的资…」）
- 第 3 章：
  - 单条套路句式超限：「周启明的」×8、「为什么会」×4、「“我不知道」×3
  - narration_para_pct 12.2 低于目标 20.0
  - attr_adv_pct 15.6 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「周启明的」×13、「林子墨的」×7、「为什么会」×3
  - narration_para_pct 5.6 低于目标 20.0
  - attr_adv_pct 19.0 高于目标 10.0
  - dialogue_run_mean 11.4 高于目标 10.0
- 第 5 章：
  - dialogue_chars_pct 10.5 低于目标 20.0
  - dialogue_run_mean 1.3 低于目标 1.5
  - [observe] attr_adv_pct 100.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 15072
chapter_chars_mean: 3014
chapter_chars_median: 3572
chapter_chars_cv: 0.32
paragraphs_mean: 67.8
dialogue_chars_pct: 33.2
dialogue_para_pct: 67.5
interiority_para_pct: 9.3
narration_para_pct: 23.1
turn_under20_pct: 78.7
turn_over200_pct: 0.0
attr_say_pct: 17.0
attr_adv_pct: 23.4
scenes_per_chapter: 3.4
dialogue_run_mean: 4.7
turn_len_median: 12
```
