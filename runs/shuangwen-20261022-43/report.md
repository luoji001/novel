# 未盖章的验收单 生成报告

slug：`shuangwen-20261022-43`
档位：爽文　闸门模式：observe
章数：10　总字数：19219
LLM 调用：97 次，累计 358.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 验收单在桌上摇晃 | 1949 | normal | 97.9 | 0 |  | 1 |
| 2 | 碎纸机吞进验收单 | 1684 | normal | 93.5 | 0 |  | 1 |
| 3 | 验收单在桌上摇晃 | 1902 | normal | 87.9 | 0 |  | 5 |
| 4 | 验收单在桌上摇晃 | 1751 | normal | 92.0 | 0 |  | 2 |
| 5 | 验收单在桌上摇晃 | 2111 | normal | 93.3 | 0 |  | 3 |
| 6 | 验收单在桌上摇晃 | 1912 | normal | 90.8 | 0 |  | 3 |
| 7 | 验收单被手指按住 | 1593 | normal | 91.0 | 0 |  | 2 |
| 8 | 验收单被手指按住 | 1975 | normal | 90.5 | 0 |  | 4 |
| 9 | 验收单被手指按住 | 1744 | normal | 93.7 | 0 |  | 2 |
| 10 | 验收单被手指按住 | 2588 | long | 93.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「市卫健委」×4
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3、「张磊点点」×3
- 第 3 章：
  - 单条套路句式超限：「李建国的」×3
  - narration_para_pct 3.8 低于目标 5.0
  - attr_adv_pct 13.6 高于目标 12.0
  - dialogue_run_mean 25 高于目标 14.0
  - [observe] 标题重复：「验收单在桌上摇晃」已存在
- 第 4 章：
  - 单条套路句式超限：「李建国的」×9
  - [observe] 标题重复：「验收单在桌上摇晃」已存在
- 第 5 章：
  - narration_para_pct 4.2 低于目标 5.0
  - attr_adv_pct 19.2 高于目标 12.0
  - [observe] 标题重复：「验收单在桌上摇晃」已存在
- 第 6 章：
  - 单条套路句式超限：「李建国的」×5
  - narration_para_pct 3.2 低于目标 5.0
  - [observe] 标题重复：「验收单在桌上摇晃」已存在
- 第 7 章：
  - narration_para_pct 4.0 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「李建国的」×5
  - narration_para_pct 2.6 低于目标 5.0
  - dialogue_run_mean 18.5 高于目标 14.0
  - [observe] 标题重复：「验收单被手指按住」已存在
- 第 9 章：
  - 单条套路句式超限：「李建国的」×4
  - [observe] 标题重复：「验收单被手指按住」已存在
- 第 10 章：
  - [observe] 标题重复：「验收单被手指按住」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18303
chapter_chars_mean: 1830
chapter_chars_median: 1808
chapter_chars_cv: 0.15
paragraphs_mean: 37.3
dialogue_chars_pct: 49.5
dialogue_para_pct: 87.7
interiority_para_pct: 5.4
narration_para_pct: 7.0
turn_under20_pct: 65.9
turn_over200_pct: 0.0
attr_say_pct: 32.9
attr_adv_pct: 8.6
scenes_per_chapter: 1.8
dialogue_run_mean: 10.1
turn_len_median: 14
```
