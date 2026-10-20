# 铜钥匙 生成报告

slug：`xuanyi-20261019-191`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14070
LLM 调用：68 次，累计 236.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摸着签名的指尖 | 1639 | short | 86.4 | 0 |  | 2 |
| 2 | 摸着签名的指尖 | 3329 | normal | 93.4 | 0 |  | 3 |
| 3 | 翻阅泛黄的账本 | 3432 | normal | 90.3 | 0 |  | 2 |
| 4 | 抚摸怀表凹陷处 | 3716 | normal | 92.0 | 0 |  | 3 |
| 5 | 掀开保险柜的瞬间 | 1949 | short | 92.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 13.3 低于目标 20.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周怀瑾的」×6、「他知道这」×3、「沈慕云的」×3
  - narration_para_pct 12.5 低于目标 20.0
  - [observe] 标题重复：「摸着签名的指尖」已存在
- 第 3 章：
  - 单条套路句式超限：「沈慕云的」×4、「周怀瑾的」×3
  - narration_para_pct 14.8 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「沈慕云的」×5、「周怀瑾的」×4、「微微一笑」×3
  - narration_para_pct 18.2 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「沈慕云的」×6、「周怀瑾的」×4
  - narration_para_pct 13.0 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13441
chapter_chars_mean: 2688
chapter_chars_median: 3174
chapter_chars_cv: 0.34
paragraphs_mean: 55.2
dialogue_chars_pct: 30.5
dialogue_para_pct: 73.4
interiority_para_pct: 9.1
narration_para_pct: 17.5
turn_under20_pct: 75.4
turn_over200_pct: 0.0
attr_say_pct: 21.6
attr_adv_pct: 14.2
scenes_per_chapter: 3.4
dialogue_run_mean: 4.1
turn_len_median: 12
```
