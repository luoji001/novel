# 私章 生成报告

slug：`shuangwen-20261022-63`
档位：爽文　闸门模式：observe
章数：10　总字数：18859
LLM 调用：97 次，累计 417.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 印章的歪斜 | 1717 | normal | 98.6 | 0 |  | 1 |
| 2 | 清单副本的暗藏 | 1765 | normal | 93.5 | 0 |  | 1 |
| 3 | 撕碎的财务报表 | 1703 | normal | 95.5 | 0 |  | 3 |
| 4 | 签字笔的圈记 | 1839 | normal | 91.9 | 0 |  | 3 |
| 5 | 撕碎的财务报表 | 1632 | normal | 92.0 | 0 |  | 1 |
| 6 | 清单副本的暗藏 | 1819 | normal | 37.6 | 0 |  | 2 |
| 7 | 伪造证书的较量 | 1696 | normal | 94.2 | 0 |  | 2 |
| 8 | 签字笔的圈记 | 2227 | normal | 92.9 | 0 |  | 3 |
| 9 | 清单副本的暗藏 | 2095 | normal | 92.5 | 0 |  | 2 |
| 10 | 指缝间的数字圈记 | 2356 | long | 37.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3
- 第 2 章：
  - narration_para_pct 2.7 低于目标 5.0
- 第 3 章：
  - 单条套路句式超限：「李国强的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
- 第 4 章：
  - 命中套话收尾句
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 5 章：
  - [observe] 标题重复：「撕碎的财务报表」已存在
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「他知道，这场较量才刚刚开始…」）
  - [observe] 标题重复：「清单副本的暗藏」已存在
- 第 7 章：
  - 单条套路句式超限：「李国强的」×4
  - attr_adv_pct 16.7 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「不仅仅是」×3、「他知道这」×3
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「签字笔的圈记」已存在
- 第 9 章：
  - 单条套路句式超限：「李国强的」×4
  - [observe] 标题重复：「清单副本的暗藏」已存在
- 第 10 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] attr_adv_pct 27.8 > 25.0（结构塌缩）

## 整书结构指标

```
chapters: 10
total_chars: 17862
chapter_chars_mean: 1786
chapter_chars_median: 1698
chapter_chars_cv: 0.14
paragraphs_mean: 41.3
dialogue_chars_pct: 47.4
dialogue_para_pct: 83.2
interiority_para_pct: 7.2
narration_para_pct: 9.6
turn_under20_pct: 72.9
turn_over200_pct: 0.0
attr_say_pct: 26.0
attr_adv_pct: 12.9
scenes_per_chapter: 1.9
dialogue_run_mean: 6.4
turn_len_median: 13
```
