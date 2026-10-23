# 账本 生成报告

slug：`shuangwen-20261022-128`
档位：爽文　闸门模式：observe
章数：10　总字数：19108
LLM 调用：97 次，累计 434.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本掀翻旧时光 | 1844 | normal | 40.0 | 0 |  | 2 |
| 2 | 账本揭开真相 | 2034 | normal | 92.1 | 0 |  | 2 |
| 3 | 撕碎登记簿 | 1667 | normal | 93.7 | 0 |  | 2 |
| 4 | 红墨水瓶的威胁 | 2087 | normal | 93.6 | 0 |  | 1 |
| 5 | 账本上的签名 | 1765 | normal | 90.5 | 0 |  | 2 |
| 6 | 撕纸角的对峙 | 1933 | normal | 93.8 | 0 |  | 2 |
| 7 | 撕纸角的对峙 | 1576 | normal | 94.8 | 0 |  | 4 |
| 8 | 账本翻页的对峙 | 1941 | normal | 93.5 | 0 |  | 0 |
| 9 | 账本上的签名 | 1840 | normal | 36.8 | 0 |  | 3 |
| 10 | 撕纸角的对峙 | 2411 | long | 93.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周建国的」×7
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周建国的」×8
  - attr_adv_pct 20.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「周建国的」×4
  - narration_para_pct 3.8 低于目标 5.0
- 第 4 章：
  - 单条套路句式超限：「周建国的」×10、「林小曼的」×5
- 第 5 章：
  - 单条套路句式超限：「周建国的」×7
  - attr_adv_pct 23.1 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「周建国的」×5
  - narration_para_pct 4.5 低于目标 5.0
- 第 7 章：
  - 单条套路句式超限：「周建国的」×5、「林小曼的」×3
  - narration_para_pct 2.9 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「撕纸角的对峙」已存在
- 第 9 章：
  - 单条套路句式超限：「周建国的」×3
  - [observe] 章内自我复读 1 句（如「那样的话，至少我能看到自己究竟欠了多少债…」）
  - [observe] 标题重复：「账本上的签名」已存在
- 第 10 章：
  - 单条套路句式超限：「周建国的」×9
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「撕纸角的对峙」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18164
chapter_chars_mean: 1816
chapter_chars_median: 1793
chapter_chars_cv: 0.13
paragraphs_mean: 39.6
dialogue_chars_pct: 48.2
dialogue_para_pct: 86.3
interiority_para_pct: 6.0
narration_para_pct: 7.7
turn_under20_pct: 69.7
turn_over200_pct: 0.0
attr_say_pct: 26.9
attr_adv_pct: 15.1
scenes_per_chapter: 1.3
dialogue_run_mean: 7.5
turn_len_median: 14
```
