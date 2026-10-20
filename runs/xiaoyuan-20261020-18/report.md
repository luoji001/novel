# 分科表 生成报告

slug：`xiaoyuan-20261020-18`
档位：校园青春　闸门模式：observe
章数：9　总字数：20967
LLM 调用：100 次，累计 470.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 磁带在口袋发烫 | 1295 | short | 39.7 | 0 |  | 2 |
| 2 | 课表上的红笔圈 | 3175 | normal | 93.0 | 0 |  | 1 |
| 3 | 手指划过分科表 | 2554 | normal | 84.4 | 0 |  | 2 |
| 4 | 磁带在口袋发烫 | 2422 | normal | 86.5 | 0 |  | 4 |
| 5 | 纪律考核表上的勾 | 2819 | normal | 88.2 | 0 |  | 2 |
| 6 | 笔记本上的名字 | 2401 | normal | 91.2 | 0 |  | 0 |
| 7 | 粉笔写下的祝贺语 | 2342 | normal | 88.7 | 0 |  | 1 |
| 8 | 笔记本里的纸条 | 2479 | normal | 89.4 | 0 |  | 1 |
| 9 | 磁带在口袋发烫 | 1471 | short | 91.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「就在这时」×3
  - [observe] 章内自我复读 21 句（如「就在这时候，广播里突然传来通知：“请各班同学注意…」）
- 第 2 章：
  - 单条套路句式超限：「带着一丝」×3
- 第 3 章：
  - 单条套路句式超限：「他知道这」×4、「他知道自己」×3、「知道自己」×3
  - dialogue_chars_pct 16.7 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
  - interiority_para_pct 5.6 低于目标 8.0
  - [observe] 章内自我复读 14 句（如「林小满感觉心跳加速，但他知道这并不是爱情的感觉，…」）
  - [observe] 标题重复：「磁带在口袋发烫」已存在
- 第 5 章：
  - dialogue_chars_pct 16.6 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「点了点头」×3
- 第 8 章：
  - narration_para_pct 9.6 低于目标 15.0
- 第 9 章：
  - [observe] 标题重复：「磁带在口袋发烫」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19975
chapter_chars_mean: 2219
chapter_chars_median: 2299
chapter_chars_cv: 0.26
paragraphs_mean: 47
dialogue_chars_pct: 24.6
dialogue_para_pct: 65.4
interiority_para_pct: 14.4
narration_para_pct: 20.2
turn_under20_pct: 88.6
turn_over200_pct: 0.0
attr_say_pct: 16.7
attr_adv_pct: 5.2
scenes_per_chapter: 2.2
dialogue_run_mean: 3.5
turn_len_median: 9
```
