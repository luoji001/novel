# 标签编号 生成报告

slug：`xuanyi-20261019-194`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13915
LLM 调用：68 次，累计 232.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 布料消失 | 1429 | short | 100.0 | 0 |  | 1 |
| 2 | 布料未登 | 3559 | normal | 91.5 | 0 |  | 4 |
| 3 | 钥匙疑云 | 3251 | normal | 89.2 | 0 |  | 4 |
| 4 | 布料标签对不上 | 3582 | normal | 91.4 | 0 |  | 2 |
| 5 | 手提箱开启 | 2089 | short | 93.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 0.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周素云的」×7、「“我不知道」×3、「陈永年的」×3
  - narration_para_pct 17.4 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 章内自我复读 8 句（如「周素云的声音低了下来，“我知道你不肯说，但我相信…」）
- 第 3 章：
  - 单条套路句式超限：「周素云的」×4、「“我不知道」×3、「”周素云轻」×3
  - narration_para_pct 6.9 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - dialogue_run_mean 13.4 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×4、「周素云的」×3、「陈永年的」×3
  - narration_para_pct 8.3 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「陈永年的」×4
  - narration_para_pct 16.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13207
chapter_chars_mean: 2641
chapter_chars_median: 3096
chapter_chars_cv: 0.35
paragraphs_mean: 62.2
dialogue_chars_pct: 47.4
dialogue_para_pct: 85.8
interiority_para_pct: 3.6
narration_para_pct: 10.6
turn_under20_pct: 78.6
turn_over200_pct: 0.0
attr_say_pct: 40.8
attr_adv_pct: 10.2
scenes_per_chapter: 4
dialogue_run_mean: 7.5
turn_len_median: 13
```
