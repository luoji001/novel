# 契书 生成报告

slug：`shuangwen-20261023-128`
档位：爽文　闸门模式：observe
章数：10　总字数：18600
LLM 调用：97 次，累计 431.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 墨痕抹去旧契书 | 1384 | normal | 100.0 | 0 |  | 0 |
| 2 | 签字簿上的名字 | 2241 | normal | 91.1 | 0 |  | 1 |
| 3 | 旧契书自行拼合 | 1700 | normal | 36.0 | 0 |  | 1 |
| 4 | 残页映照契约真相 | 2090 | normal | 93.7 | 0 |  | 0 |
| 5 | 契约自签 | 1424 | normal | 92.3 | 0 |  | 2 |
| 6 | 玉牌照亮残页真相 | 1743 | normal | 92.5 | 0 |  | 2 |
| 7 | 残页对峙契约真相 | 1727 | normal | 92.4 | 0 |  | 3 |
| 8 | 残页轻颤契约现 | 1598 | normal | 92.5 | 0 |  | 0 |
| 9 | 玉牌遮挡旧契书 | 2163 | normal | 92.8 | 0 |  | 1 |
| 10 | 玉牌揭开旧契书 | 2520 | long | 91.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「验货台」×5、「他知道这」×4
- 第 3 章：
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「验货台」×3
  - attr_adv_pct 18.2 高于目标 12.0
- 第 6 章：
  - 命中套话收尾句
  - attr_adv_pct 20.0 高于目标 12.0
- 第 7 章：
  - narration_para_pct 3.3 低于目标 5.0
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题与《残页映照契约真相》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「验货台」×5
- 第 10 章：
  - 单条套路句式超限：「验货台」×3
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题与《玉牌遮挡旧契书》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 17698
chapter_chars_mean: 1770
chapter_chars_median: 1656
chapter_chars_cv: 0.2
paragraphs_mean: 37.1
dialogue_chars_pct: 44.6
dialogue_para_pct: 80.3
interiority_para_pct: 8.0
narration_para_pct: 11.7
turn_under20_pct: 67.1
turn_over200_pct: 0.0
attr_say_pct: 29.0
attr_adv_pct: 14.3
scenes_per_chapter: 1.2
dialogue_run_mean: 5.8
turn_len_median: 14
```
