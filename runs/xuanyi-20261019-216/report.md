# 灯灭时 生成报告

slug：`xuanyi-20261019-216`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13972
LLM 调用：68 次，累计 224.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙自行转动 | 1747 | short | 48.7 | 0 |  | 3 |
| 2 | 登记簿的缺失页角 | 3845 | normal | 91.3 | 0 |  | 2 |
| 3 | 铜色按钮的尘埃痕迹 | 3322 | normal | 91.3 | 0 |  | 2 |
| 4 | 怀表凹槽的金属屑 | 3399 | normal | 91.2 | 0 |  | 1 |
| 5 | 铁门未启的余温 | 1654 | short | 93.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 3.1 低于目标 20.0
  - interiority_para_pct 50.0 高于目标 20.0
  - dialogue_run_mean 1 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×3、「微微一笑」×3
  - narration_para_pct 7.3 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「沈文远站在」×3
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「林素云的」×3
- 第 5 章：
  - 单条套路句式超限：「林素云的」×4
  - narration_para_pct 9.4 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13359
chapter_chars_mean: 2672
chapter_chars_median: 3159
chapter_chars_cv: 0.36
paragraphs_mean: 53
dialogue_chars_pct: 32.8
dialogue_para_pct: 67.7
interiority_para_pct: 14.9
narration_para_pct: 17.4
turn_under20_pct: 81.1
turn_over200_pct: 0.0
attr_say_pct: 17.0
attr_adv_pct: 10.1
scenes_per_chapter: 2.2
dialogue_run_mean: 3.9
turn_len_median: 12
```
