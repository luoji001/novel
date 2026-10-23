# 确权证明 生成报告

slug：`shuangwen-20261022-124`
档位：爽文　闸门模式：observe
章数：10　总字数：19337
LLM 调用：97 次，累计 434.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔划破纸面 | 1809 | normal | 98.3 | 0 |  | 0 |
| 2 | 签字笔写下的数字 | 2203 | normal | 94.7 | 0 |  | 2 |
| 3 | 工牌反光的刹那 | 1979 | normal | 91.8 | 0 |  | 3 |
| 4 | 确权证摊在桌面 | 1744 | normal | 94.2 | 0 |  | 1 |
| 5 | 确权证明摊在桌面 | 1725 | normal | 92.1 | 0 |  | 3 |
| 6 | 确权证明摊在桌面 | 1760 | normal | 93.2 | 0 |  | 3 |
| 7 | 确权证明摊在桌面 | 1893 | normal | 92.7 | 0 |  | 3 |
| 8 | 名册摊在桌面 | 2060 | normal | 38.0 | 0 |  | 2 |
| 9 | 签字笔划破纸面 | 1865 | normal | 92.9 | 0 |  | 2 |
| 10 | 确权证明摊在桌面 | 2289 | long | 91.2 | 0 |  | 6 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「张建国的」×4
  - narration_para_pct 4.9 低于目标 5.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×4、「市规划局」×3
  - narration_para_pct 4.0 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「他知道自己」×3
- 第 5 章：
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题与《确权证摊在桌面》近似 0.93 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「他知道自己」×4、「李国强的」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「确权证明摊在桌面」已存在
- 第 7 章：
  - 单条套路句式超限：「市规划局」×4
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「确权证明摊在桌面」已存在
- 第 8 章：
  - [observe] attr_adv_pct 50.0 > 25.0（结构塌缩）
  - [observe] 标题与《确权证摊在桌面》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「市规划局」×3
  - [observe] 标题重复：「签字笔划破纸面」已存在
- 第 10 章：
  - 单条套路句式超限：「张建国的」×4
  - 情节与已写章节重复 0.73 ≥ 0.7（撞上「张建国凭借父亲留下的宅基地确权证明，挑战李国强的补偿协议…」）
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 17.6 高于目标 12.0
  - dialogue_run_mean 20.5 高于目标 14.0
  - [observe] 标题重复：「确权证明摊在桌面」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18396
chapter_chars_mean: 1840
chapter_chars_median: 1778
chapter_chars_cv: 0.11
paragraphs_mean: 38.5
dialogue_chars_pct: 49.1
dialogue_para_pct: 86.1
interiority_para_pct: 5.0
narration_para_pct: 8.9
turn_under20_pct: 64.5
turn_over200_pct: 0.0
attr_say_pct: 24.6
attr_adv_pct: 15.6
scenes_per_chapter: 1.5
dialogue_run_mean: 8.1
turn_len_median: 14
```
