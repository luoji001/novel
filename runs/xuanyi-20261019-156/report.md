# 纸条上的字迹 生成报告

slug：`xuanyi-20261019-156`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15050
LLM 调用：68 次，累计 246.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙的刻痕 | 1950 | short | 92.5 | 0 |  | 5 |
| 2 | 木板上的刻痕 | 3612 | normal | 91.6 | 0 |  | 3 |
| 3 | 水面泛起涟漪 | 3851 | normal | 89.8 | 0 |  | 3 |
| 4 | 木板上的刻痕 | 3585 | normal | 89.1 | 0 |  | 4 |
| 5 | 纸条上的字迹 | 2047 | short | 79.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈怀远的」×7、「林素云的」×3
  - dialogue_chars_pct 16.1 低于目标 20.0
  - interiority_para_pct 21.1 高于目标 20.0
  - narration_para_pct 18.4 低于目标 20.0
  - [observe] attr_adv_pct 40.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「林素云的」×7、「“我不知道」×3、「”沈怀远轻」×3
  - narration_para_pct 7.4 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「那你为什么要这样做？…」）
- 第 3 章：
  - 单条套路句式超限：「林素云的」×9
  - narration_para_pct 13.5 低于目标 20.0
  - attr_adv_pct 13.3 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「林素云的」×9、「沈怀远的」×8、「”沈怀远轻」×3
  - narration_para_pct 10.4 低于目标 20.0
  - [observe] 与历史章节逐字重复 3 句（如「林素云的心跳加快了几分…」）
  - [observe] 标题重复：「木板上的刻痕」已存在
- 第 5 章：
  - 单条套路句式超限：「沈怀远的」×3
  - dialogue_chars_pct 14.2 低于目标 20.0
  - interiority_para_pct 25.6 高于目标 20.0
  - narration_para_pct 17.9 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14323
chapter_chars_mean: 2865
chapter_chars_median: 3410
chapter_chars_cv: 0.31
paragraphs_mean: 64.4
dialogue_chars_pct: 33.3
dialogue_para_pct: 72.4
interiority_para_pct: 15.1
narration_para_pct: 12.5
turn_under20_pct: 85.3
turn_over200_pct: 0.0
attr_say_pct: 19.9
attr_adv_pct: 9.2
scenes_per_chapter: 2.8
dialogue_run_mean: 4.1
turn_len_median: 9
```
