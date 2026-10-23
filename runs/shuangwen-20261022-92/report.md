# 令牌 生成报告

slug：`shuangwen-20261022-92`
档位：爽文　闸门模式：observe
章数：10　总字数：19723
LLM 调用：97 次，累计 444.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 香炉暗纹映怀表光 | 1959 | normal | 97.8 | 0 |  | 2 |
| 2 | 雕花木桌的凹陷 | 1931 | normal | 37.5 | 0 |  | 2 |
| 3 | 令牌撕裂的光 | 2049 | normal | 92.0 | 0 |  | 1 |
| 4 | 触摸页码的指尖 | 2200 | normal | 91.9 | 0 |  | 1 |
| 5 | 签名笔尖触纸纹 | 1850 | normal | 93.3 | 0 |  | 0 |
| 6 | 铜制怀表的刻痕 | 1902 | normal | 92.0 | 0 |  | 3 |
| 7 | 令牌与怀表相触 | 1841 | normal | 92.3 | 0 |  | 1 |
| 8 | 签名笔尖触纸纹 | 1891 | normal | 92.6 | 0 |  | 2 |
| 9 | 铜制怀表映令牌光 | 1657 | normal | 91.3 | 0 |  | 0 |
| 10 | 怀表刻痕映令牌光 | 2433 | long | 93.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陆长风的」×5
  - attr_adv_pct 25.0 高于目标 12.0
- 第 2 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「林远的心跳加快了几分…」）
- 第 3 章：
  - 单条套路句式超限：「陆长风的」×5
- 第 4 章：
  - 单条套路句式超限：「陆长风的」×7
- 第 6 章：
  - 单条套路句式超限：「陆长风的」×6
  - narration_para_pct 3.0 低于目标 5.0
  - dialogue_run_mean 15 高于目标 14.0
- 第 7 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「陆长风的」×6
  - [observe] 标题重复：「签名笔尖触纸纹」已存在
- 第 10 章：
  - 单条套路句式超限：「陆长风的」×13
  - [observe] 标题与《铜制怀表映令牌光》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18797
chapter_chars_mean: 1880
chapter_chars_median: 1832
chapter_chars_cv: 0.11
paragraphs_mean: 38.2
dialogue_chars_pct: 41.4
dialogue_para_pct: 81.0
interiority_para_pct: 8.6
narration_para_pct: 10.4
turn_under20_pct: 71.5
turn_over200_pct: 0.0
attr_say_pct: 20.9
attr_adv_pct: 9.7
scenes_per_chapter: 1.6
dialogue_run_mean: 6.3
turn_len_median: 14
```
