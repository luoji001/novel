# 账本残页 生成报告

slug：`shuangwen-20261023-113`
档位：爽文　闸门模式：observe
章数：10　总字数：19608
LLM 调用：97 次，累计 454.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本残页的印鉴 | 1758 | normal | 40.0 | 0 |  | 2 |
| 2 | 签字与收据的对峙 | 1933 | normal | 36.2 | 0 |  | 2 |
| 3 | 账本残页的对峙 | 2010 | normal | 36.2 | 0 |  | 4 |
| 4 | 墨水瓶的对峙 | 1850 | normal | 93.2 | 0 |  | 1 |
| 5 | 账本残页的对峙 | 1864 | normal | 92.2 | 0 |  | 4 |
| 6 | 墨水瓶的对峙 | 1857 | normal | 92.2 | 0 |  | 2 |
| 7 | 墨水瓶的对峙 | 1970 | normal | 87.5 | 0 |  | 5 |
| 8 | 墨水瓶的对峙 | 1709 | normal | 91.0 | 0 |  | 3 |
| 9 | 账本残页的对峙 | 1780 | normal | 36.0 | 0 |  | 3 |
| 10 | 墨水瓶的对峙 | 2867 | long | 91.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李长风的」×7
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「李长风的」×7
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「李长风的」×7
  - dialogue_run_mean 16.5 高于目标 14.0
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题与《账本残页的印鉴》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「李长风的」×4、「赵怀安的」×4
- 第 5 章：
  - 单条套路句式超限：「李长风的」×5
  - narration_para_pct 3.1 低于目标 5.0
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 标题重复：「账本残页的对峙」已存在
- 第 6 章：
  - 单条套路句式超限：「李长风的」×5、「赵怀安的」×3
  - [observe] 标题重复：「墨水瓶的对峙」已存在
- 第 7 章：
  - 单条套路句式超限：「李长风的」×5
  - narration_para_pct 2.4 低于目标 5.0
  - attr_adv_pct 15.4 高于目标 12.0
  - dialogue_run_mean 40 高于目标 14.0
  - [observe] 标题重复：「墨水瓶的对峙」已存在
- 第 8 章：
  - 单条套路句式超限：「李长风的」×6
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「墨水瓶的对峙」已存在
- 第 9 章：
  - 单条套路句式超限：「李长风的」×4、「赵怀安的」×3
  - [observe] 章内自我复读 9 句（如「赵怀安笑了笑：“很简单，我只是希望你能放下那些不…」）
  - [observe] 标题重复：「账本残页的对峙」已存在
- 第 10 章：
  - 单条套路句式超限：「李长风的」×4
  - narration_para_pct 3.1 低于目标 5.0
  - [observe] 标题重复：「墨水瓶的对峙」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18679
chapter_chars_mean: 1868
chapter_chars_median: 1777
chapter_chars_cv: 0.17
paragraphs_mean: 38.3
dialogue_chars_pct: 47.0
dialogue_para_pct: 88.1
interiority_para_pct: 4.8
narration_para_pct: 7.2
turn_under20_pct: 67.0
turn_over200_pct: 0.0
attr_say_pct: 24.5
attr_adv_pct: 16.4
scenes_per_chapter: 1.7
dialogue_run_mean: 11.4
turn_len_median: 14
```
