# 铜钱 生成报告

slug：`xuanyi-20261019-18`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14090
LLM 调用：68 次，累计 239.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 绣品上的诡异针脚 | 1848 | short | 98.1 | 0 |  | 1 |
| 2 | 账簿停在三天前 | 3241 | normal | 91.6 | 0 |  | 2 |
| 3 | 摩挲铜钱寻踪 | 3325 | normal | 92.2 | 0 |  | 4 |
| 4 | 摩挲茶壶寻真相 | 3753 | normal | 91.2 | 0 |  | 3 |
| 5 | 拍案问账 | 1918 | short | 91.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陆青梧的」×10、「沈文渊的」×3、「永昌绣坊」×3
- 第 2 章：
  - 单条套路句式超限：「沈文渊的」×11、「陆青梧的」×4
  - narration_para_pct 6.7 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「陆青梧的」×6、「沈文渊的」×6
  - narration_para_pct 8.2 低于目标 20.0
  - attr_adv_pct 18.8 高于目标 10.0
  - dialogue_run_mean 10.8 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「沈文渊的」×6
  - narration_para_pct 13.6 低于目标 20.0
  - attr_adv_pct 11.5 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「沈文渊的」×4
  - narration_para_pct 9.1 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13431
chapter_chars_mean: 2686
chapter_chars_median: 3106
chapter_chars_cv: 0.32
paragraphs_mean: 58.2
dialogue_chars_pct: 42.8
dialogue_para_pct: 81.3
interiority_para_pct: 7.2
narration_para_pct: 11.5
turn_under20_pct: 71.4
turn_over200_pct: 0.0
attr_say_pct: 19.6
attr_adv_pct: 8.9
scenes_per_chapter: 2.8
dialogue_run_mean: 6.1
turn_len_median: 14
```
