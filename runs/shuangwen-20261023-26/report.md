# 旧账本 生成报告

slug：`shuangwen-20261023-26`
档位：爽文　闸门模式：observe
章数：10　总字数：18971
LLM 调用：97 次，累计 423.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账册燃尽的余灰 | 1637 | normal | 97.9 | 0 |  | 0 |
| 2 | 算盘上的珠子排列 | 1747 | normal | 95.8 | 0 |  | 0 |
| 3 | 账本上的指纹痕迹 | 1882 | normal | 37.9 | 0 |  | 1 |
| 4 | 账本上的指纹痕迹 | 1949 | normal | 92.6 | 0 |  | 2 |
| 5 | 账本摊开的裂痕 | 2322 | normal | 91.5 | 0 |  | 1 |
| 6 | 药方摊开的裂痕 | 1507 | normal | 93.2 | 0 |  | 1 |
| 7 | 三两当归的补偿 | 1884 | normal | 90.4 | 0 |  | 2 |
| 8 | 账本摊开的裂痕 | 2028 | normal | 92.2 | 0 |  | 2 |
| 9 | 账本摊开的裂痕 | 1688 | normal | 92.1 | 0 |  | 3 |
| 10 | 药材清单的重量 | 2317 | long | 37.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「点了点头」×3
  - [observe] 标题重复：「账本上的指纹痕迹」已存在
- 第 5 章：
  - 单条套路句式超限：「丹房管理委员会」×3
- 第 6 章：
  - [observe] 标题与《账本摊开的裂痕》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「说道“我」×3、「丹房堂上」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 8 章：
  - narration_para_pct 2.4 低于目标 5.0
  - [observe] 标题重复：「账本摊开的裂痕」已存在
- 第 9 章：
  - 单条套路句式超限：「丹房管理委员会」×3
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「账本摊开的裂痕」已存在
- 第 10 章：
  - 单条套路句式超限：「李三点点」×5、「他知道这」×3
  - [observe] 章内自我复读 1 句（如「李师傅，王五师傅也在等你呢…」）

## 整书结构指标

```
chapters: 10
total_chars: 17981
chapter_chars_mean: 1798
chapter_chars_median: 1790
chapter_chars_cv: 0.14
paragraphs_mean: 41.3
dialogue_chars_pct: 49.7
dialogue_para_pct: 82.8
interiority_para_pct: 6.0
narration_para_pct: 11.3
turn_under20_pct: 65.7
turn_over200_pct: 0.0
attr_say_pct: 32.6
attr_adv_pct: 7.4
scenes_per_chapter: 2.1
dialogue_run_mean: 6.2
turn_len_median: 16
```
