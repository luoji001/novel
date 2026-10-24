# 玉牌 生成报告

slug：`shuangwen-20261023-84`
档位：爽文　闸门模式：observe
章数：10　总字数：21248
LLM 调用：97 次，累计 478.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 夺回账簿 | 2251 | normal | 39.7 | 0 |  | 2 |
| 2 | 签字笔落下瞬间 | 2035 | normal | 36.8 | 0 |  | 2 |
| 3 | 朱砂笔落下瞬间 | 1908 | normal | 92.0 | 0 |  | 1 |
| 4 | 墨痕覆盖资格纸 | 2217 | normal | 91.2 | 0 |  | 3 |
| 5 | 墨迹未干的证书 | 2222 | normal | 93.7 | 0 |  | 0 |
| 6 | 账簿上的红印 | 2005 | normal | 91.1 | 0 |  | 2 |
| 7 | 玉牌递入掌心 | 2033 | normal | 92.7 | 0 |  | 2 |
| 8 | 玉牌递入掌心 | 2031 | normal | 92.5 | 0 |  | 1 |
| 9 | 玉牌递入掌心 | 2089 | normal | 92.6 | 0 |  | 2 |
| 10 | 撕下一页账簿 | 2447 | long | 91.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林远站在」×3
  - [observe] attr_adv_pct 75.0 > 25.0（结构塌缩）
- 第 2 章：
  - narration_para_pct 2.4 低于目标 5.0
  - [observe] attr_adv_pct 38.5 > 25.0（结构塌缩）
- 第 3 章：
  - [observe] 标题与《签字笔落下瞬间》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「林远站在」×3
  - narration_para_pct 2.8 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「李长风的」×3
  - attr_adv_pct 15.4 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「李长风的」×6
  - attr_adv_pct 18.8 高于目标 12.0
- 第 8 章：
  - [observe] 标题重复：「玉牌递入掌心」已存在
- 第 9 章：
  - 单条套路句式超限：「李长风的」×3
  - [observe] 标题重复：「玉牌递入掌心」已存在
- 第 10 章：
  - narration_para_pct 3.3 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 19.3 高于目标 14.0

## 整书结构指标

```
chapters: 10
total_chars: 20183
chapter_chars_mean: 2018
chapter_chars_median: 1970
chapter_chars_cv: 0.07
paragraphs_mean: 45.7
dialogue_chars_pct: 51.2
dialogue_para_pct: 87.8
interiority_para_pct: 5.1
narration_para_pct: 7.1
turn_under20_pct: 66.4
turn_over200_pct: 0.0
attr_say_pct: 18.1
attr_adv_pct: 21.7
scenes_per_chapter: 2.3
dialogue_run_mean: 9.2
turn_len_median: 16
```
