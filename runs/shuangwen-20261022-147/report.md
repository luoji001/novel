# 磅单 生成报告

slug：`shuangwen-20261022-147`
档位：爽文　闸门模式：observe
章数：10　总字数：21064
LLM 调用：97 次，累计 466.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一份被篡改的磅单 | 1873 | normal | 96.8 | 0 |  | 1 |
| 2 | 递交磅单 | 1793 | normal | 94.3 | 0 |  | 2 |
| 3 | 签字的磅单 | 1946 | normal | 92.8 | 0 |  | 1 |
| 4 | 盯住磅单的指尖 | 2730 | normal | 92.5 | 0 |  | 1 |
| 5 | 盯住磅单的指尖 | 1912 | normal | 94.2 | 0 |  | 3 |
| 6 | 摩挲磅单边缘 | 2078 | normal | 91.8 | 0 |  | 3 |
| 7 | 攥紧磅单的手指 | 2059 | normal | 90.5 | 0 |  | 1 |
| 8 | 签名的指尖 | 1772 | normal | 93.7 | 0 |  | 3 |
| 9 | 摩挲磅单边缘 | 2128 | normal | 92.1 | 0 |  | 3 |
| 10 | 攥紧磅单的手指 | 2763 | long | 93.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王主任的」×3、「他知道这」×3
- 第 2 章：
  - 单条套路句式超限：「王主任的」×6
  - attr_adv_pct 14.3 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「王主任的」×5
- 第 4 章：
  - 单条套路句式超限：「王主任的」×3、「李大伟的」×3
- 第 5 章：
  - 单条套路句式超限：「王主任的」×8
  - narration_para_pct 2.9 低于目标 5.0
  - [observe] 标题重复：「盯住磅单的指尖」已存在
- 第 6 章：
  - 单条套路句式超限：「李大伟的」×4
  - attr_adv_pct 20.0 高于目标 12.0
  - dialogue_run_mean 19 高于目标 14.0
- 第 7 章：
  - attr_adv_pct 13.3 高于目标 12.0
- 第 8 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李大伟的」×5
  - attr_adv_pct 20.0 高于目标 12.0
- 第 9 章：
  - narration_para_pct 4.2 低于目标 5.0
  - dialogue_run_mean 15.3 高于目标 14.0
  - [observe] 标题重复：「摩挲磅单边缘」已存在
- 第 10 章：
  - 单条套路句式超限：「王主任的」×3、「李大伟的」×3
  - attr_adv_pct 13.5 高于目标 12.0
  - [observe] 标题重复：「攥紧磅单的手指」已存在

## 整书结构指标

```
chapters: 10
total_chars: 20016
chapter_chars_mean: 2002
chapter_chars_median: 1908
chapter_chars_cv: 0.16
paragraphs_mean: 44.8
dialogue_chars_pct: 51.6
dialogue_para_pct: 86.2
interiority_para_pct: 5.0
narration_para_pct: 8.9
turn_under20_pct: 69.6
turn_over200_pct: 0.0
attr_say_pct: 30.0
attr_adv_pct: 11.2
scenes_per_chapter: 1.8
dialogue_run_mean: 9.8
turn_len_median: 14
```
