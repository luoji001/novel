# 借阅券 生成报告

slug：`shuangwen-20261022-119`
档位：爽文　闸门模式：observe
章数：10　总字数：19814
LLM 调用：97 次，累计 436.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手令与借阅券对决 | 1668 | normal | 99.3 | 0 |  | 1 |
| 2 | 签字权之争 | 2283 | normal | 93.0 | 0 |  | 2 |
| 3 | 签字权之争 | 2048 | normal | 90.2 | 0 |  | 2 |
| 4 | 印章覆旧印 | 2055 | normal | 92.1 | 0 |  | 1 |
| 5 | 借阅券对峙登记簿 | 2003 | normal | 91.1 | 0 |  | 1 |
| 6 | 借阅券覆登记簿 | 2057 | normal | 90.5 | 0 |  | 3 |
| 7 | 借阅券覆登记簿 | 2000 | normal | 88.3 | 0 |  | 5 |
| 8 | 指尖抚过折痕 | 1520 | normal | 93.6 | 0 |  | 2 |
| 9 | 登记簿上的签字权 | 1879 | normal | 91.5 | 0 |  | 0 |
| 10 | 指尖抚过折痕 | 2291 | long | 92.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈长风的」×3
- 第 2 章：
  - 单条套路句式超限：「沈长风的」×3
  - attr_adv_pct 18.8 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「沈长风的」×7
  - [observe] 标题重复：「签字权之争」已存在
- 第 4 章：
  - 单条套路句式超限：「沈长风的」×11
- 第 5 章：
  - 单条套路句式超限：「沈长风的」×3
- 第 6 章：
  - narration_para_pct 1.8 低于目标 5.0
  - attr_adv_pct 19.0 高于目标 12.0
  - [observe] 标题与《借阅券对峙登记簿》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈长风的」×5、「他知道这」×3、「李怀远的」×3
  - dialogue_chars_pct 28.4 低于目标 30.0
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「借阅券覆登记簿」已存在
- 第 8 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「李怀远的」×4、「沈长风的」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「指尖抚过折痕」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18833
chapter_chars_mean: 1883
chapter_chars_median: 1920
chapter_chars_cv: 0.12
paragraphs_mean: 41.3
dialogue_chars_pct: 43.5
dialogue_para_pct: 84.7
interiority_para_pct: 6.6
narration_para_pct: 8.7
turn_under20_pct: 69.8
turn_over200_pct: 0.0
attr_say_pct: 27.6
attr_adv_pct: 11.2
scenes_per_chapter: 2.1
dialogue_run_mean: 7.5
turn_len_median: 14
```
