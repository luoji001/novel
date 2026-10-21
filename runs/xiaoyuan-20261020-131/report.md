# 磁带遗落 生成报告

slug：`xiaoyuan-20261020-131`
档位：校园青春　闸门模式：observe
章数：9　总字数：20031
LLM 调用：100 次，累计 439.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 分科表签字 | 1313 | short | 45.8 | 0 |  | 3 |
| 2 | 磁带遗落 | 2531 | normal | 90.4 | 0 |  | 3 |
| 3 | 药盒与鞋带 | 2239 | normal | 92.1 | 0 |  | 1 |
| 4 | 磁带遗落 | 2807 | normal | 93.3 | 0 |  | 2 |
| 5 | 手指划过名字 | 2296 | normal | 91.0 | 0 |  | 4 |
| 6 | 手指划过名字 | 2235 | normal | 91.9 | 0 |  | 2 |
| 7 | 手指抚过衣领 | 2738 | normal | 92.6 | 0 |  | 1 |
| 8 | 手指抚过名字 | 2387 | normal | 87.7 | 0 |  | 3 |
| 9 | 钥匙环上的工作证 | 1476 | short | 91.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「教务处」×8
  - dialogue_run_mean 1.4 低于目标 1.5
  - [observe] 章内自我复读 29 句（如「他忽然想起昨天放学时，一个学生留了下来，问了一些…」）
- 第 2 章：
  - 单条套路句式超限：「知道自己」×3
  - dialogue_chars_pct 16.1 低于目标 20.0
  - [observe] attr_adv_pct 35.7 > 22.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「程景行的」×4、「林知夏的」×3
- 第 4 章：
  - 单条套路句式超限：「程景行的」×7、「林知夏站在」×3
  - [observe] 标题重复：「磁带遗落」已存在
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「程景行的」×3
  - narration_para_pct 14.5 低于目标 15.0
  - [observe] 章内自我复读 1 句（如「苏文远的声音从身后传来…」）
- 第 6 章：
  - 单条套路句式超限：「程景行的」×3
  - [observe] 标题重复：「手指划过名字」已存在
- 第 7 章：
  - 单条套路句式超限：「程景行的」×5、「林知夏点点」×3
- 第 8 章：
  - 单条套路句式超限：「林知夏站在」×3
  - dialogue_chars_pct 16.8 低于目标 20.0
  - [observe] 标题与《手指划过名字》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「林知夏站在」×3
  - dialogue_chars_pct 18.4 低于目标 20.0

## 整书结构指标

```
chapters: 9
total_chars: 19008
chapter_chars_mean: 2112
chapter_chars_median: 2172
chapter_chars_cv: 0.24
paragraphs_mean: 49.6
dialogue_chars_pct: 24.1
dialogue_para_pct: 62.6
interiority_para_pct: 14.7
narration_para_pct: 22.7
turn_under20_pct: 90.6
turn_over200_pct: 0.0
attr_say_pct: 28.7
attr_adv_pct: 7.5
scenes_per_chapter: 2
dialogue_run_mean: 2.7
turn_len_median: 9
```
