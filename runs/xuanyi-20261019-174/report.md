# 铜印 生成报告

slug：`xuanyi-20261019-174`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14892
LLM 调用：68 次，累计 237.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁秤称量 | 1637 | short | 100.0 | 0 |  | 1 |
| 2 | 旧发票的疑云 | 4281 | normal | 90.2 | 0 |  | 4 |
| 3 | 称量蓝布 | 3632 | normal | 86.4 | 0 |  | 4 |
| 4 | 摩挲铜印 | 3502 | normal | 90.4 | 0 |  | 2 |
| 5 | 称量蓝布 | 1835 | short | 85.7 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 11.1 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×5、「”周玉兰低」×5、「周玉兰的」×4
  - narration_para_pct 9.3 低于目标 20.0
  - attr_adv_pct 14.0 高于目标 10.0
  - [observe] 章内自我复读 3 句（如「他知道，这场调查才刚刚开始，而他自己也被卷入其中…」）
- 第 3 章：
  - 单条套路句式超限：「为什么会」×5
  - narration_para_pct 16.0 低于目标 20.0
  - attr_adv_pct 10.7 高于目标 10.0
  - [observe] 章内自我复读 16 句（如「他不知道为什么会出现这种情况，但他能感觉到事情并…」）
- 第 4 章：
  - 单条套路句式超限：「陈文远的」×8、「”周玉兰轻」×4
  - narration_para_pct 10.3 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「周玉兰的」×4、「他知道这」×3、「陈文远的」×3
  - narration_para_pct 12.9 低于目标 20.0
  - [observe] 章内自我复读 20 句（如「他记得看到张建国留下的信件，里面提到要为某些人准…」）
  - [observe] 标题重复：「称量蓝布」已存在

## 整书结构指标

```
chapters: 5
total_chars: 14189
chapter_chars_mean: 2838
chapter_chars_median: 3354
chapter_chars_cv: 0.39
paragraphs_mean: 63.6
dialogue_chars_pct: 40.0
dialogue_para_pct: 82.1
interiority_para_pct: 6.1
narration_para_pct: 11.8
turn_under20_pct: 78.6
turn_over200_pct: 0.0
attr_say_pct: 24.2
attr_adv_pct: 8.6
scenes_per_chapter: 3.6
dialogue_run_mean: 6.7
turn_len_median: 10
```
