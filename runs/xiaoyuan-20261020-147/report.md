# 磁带 生成报告

slug：`xiaoyuan-20261020-147`
档位：校园青春　闸门模式：observe
章数：9　总字数：20266
LLM 调用：100 次，累计 426.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙上的铜环 | 1587 | short | 98.6 | 0 |  | 2 |
| 2 | 玻璃珠的微光 | 2766 | normal | 92.3 | 0 |  | 1 |
| 3 | 磁带盒的秘密 | 2539 | normal | 92.0 | 0 |  | 0 |
| 4 | 钥匙交接记录 | 2112 | normal | 91.0 | 0 |  | 2 |
| 5 | 分科表边缘的指纹 | 2265 | normal | 90.8 | 0 |  | 2 |
| 6 | 钥匙归还时刻 | 2266 | normal | 91.3 | 0 |  | 0 |
| 7 | 钥匙归还时刻 | 2161 | normal | 89.1 | 0 |  | 4 |
| 8 | 作业本上的公式 | 2646 | normal | 90.7 | 0 |  | 2 |
| 9 | 钥匙与广播声 | 1915 | short | 88.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林晓棠的」×4
  - narration_para_pct 9.4 低于目标 15.0
- 第 2 章：
  - 单条套路句式超限：「周子墨的」×4、「林晓棠的」×3
- 第 4 章：
  - 单条套路句式超限：「周子墨点」×3、「他知道这」×3
  - interiority_para_pct 6.7 低于目标 8.0
- 第 5 章：
  - 单条套路句式超限：「周子墨的」×3
  - attr_adv_pct 12.5 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「林晓棠的」×4
  - narration_para_pct 14.0 低于目标 15.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「钥匙归还时刻」已存在
- 第 8 章：
  - 单条套路句式超限：「周子墨点」×4
  - [observe] 章内自我复读 10 句（如「他知道，虽然他们之间有很多未说出口的话，但他愿意…」）
- 第 9 章：
  - [observe] 章内自我复读 18 句（如「林晓棠望着窗外飘落的树叶，忽然想起上周在物理课上…」）

## 整书结构指标

```
chapters: 9
total_chars: 19175
chapter_chars_mean: 2131
chapter_chars_median: 2151
chapter_chars_cv: 0.17
paragraphs_mean: 51
dialogue_chars_pct: 26.8
dialogue_para_pct: 67.7
interiority_para_pct: 12.4
narration_para_pct: 19.9
turn_under20_pct: 88.7
turn_over200_pct: 0.0
attr_say_pct: 22.8
attr_adv_pct: 4.6
scenes_per_chapter: 1.8
dialogue_run_mean: 3.1
turn_len_median: 10
```
