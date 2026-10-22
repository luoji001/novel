# 登记簿 生成报告

slug：`shuangwen-20261022-19`
档位：爽文　闸门模式：observe
章数：10　总字数：17524
LLM 调用：97 次，累计 358.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记簿上的名字 | 1365 | normal | 99.4 | 0 |  | 1 |
| 2 | 盗书人手中的书 | 1755 | normal | 37.6 | 0 |  | 1 |
| 3 | 签字的重量 | 1400 | normal | 90.2 | 0 |  | 1 |
| 4 | 签字笔的重量 | 1770 | normal | 91.7 | 0 |  | 2 |
| 5 | 登记簿的折叠痕迹 | 1856 | normal | 92.0 | 0 |  | 1 |
| 6 | 登记簿的折叠痕迹 | 1742 | normal | 91.0 | 0 |  | 1 |
| 7 | 登记簿的折叠痕迹 | 1714 | normal | 88.2 | 0 |  | 4 |
| 8 | 登记簿的折叠痕迹 | 1803 | normal | 92.9 | 0 |  | 1 |
| 9 | 登记簿的折叠痕迹 | 1965 | normal | 92.3 | 0 |  | 3 |
| 10 | 登记簿的折叠痕迹 | 2144 | long | 92.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈长风的」×4
- 第 2 章：
  - [observe] attr_adv_pct 35.3 > 25.0（结构塌缩）
- 第 3 章：
  - attr_adv_pct 14.3 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「李怀远的」×3
  - [observe] 标题与《签字的重量》近似 0.91 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「沈长风的」×5
- 第 6 章：
  - [observe] 标题重复：「登记簿的折叠痕迹」已存在
- 第 7 章：
  - narration_para_pct 2.7 低于目标 5.0
  - attr_adv_pct 17.6 高于目标 12.0
  - dialogue_run_mean 35 高于目标 14.0
  - [observe] 标题重复：「登记簿的折叠痕迹」已存在
- 第 8 章：
  - [observe] 标题重复：「登记簿的折叠痕迹」已存在
- 第 9 章：
  - 命中套话收尾句
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题重复：「登记簿的折叠痕迹」已存在
- 第 10 章：
  - 单条套路句式超限：「沈长风的」×3
  - dialogue_run_mean 15.3 高于目标 14.0
  - [observe] 标题重复：「登记簿的折叠痕迹」已存在

## 整书结构指标

```
chapters: 10
total_chars: 16597
chapter_chars_mean: 1660
chapter_chars_median: 1674
chapter_chars_cv: 0.13
paragraphs_mean: 38.2
dialogue_chars_pct: 48.8
dialogue_para_pct: 82.3
interiority_para_pct: 5.3
narration_para_pct: 12.4
turn_under20_pct: 72.3
turn_over200_pct: 0.0
attr_say_pct: 23.7
attr_adv_pct: 10.2
scenes_per_chapter: 2
dialogue_run_mean: 10.1
turn_len_median: 14
```
