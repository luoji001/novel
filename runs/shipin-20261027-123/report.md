# 红绳 生成报告

slug：`shipin-20261027-123`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6177
LLM 调用：57 次，累计 131.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 胶片缓缓展开 | 596 | short | 15.4 | 0 |  | 3 |
| 2 | 钥匙坠入雪中 | 1351 | normal | 57.2 | 0 |  | 0 |
| 3 | 钥匙坠入雪中 | 1204 | normal | 37.2 | 0 |  | 2 |
| 4 | 红绳解开的瞬间 | 805 | normal | 21.2 | 0 |  | 2 |
| 5 | 银戒摩挲刻痕 | 911 | normal | 37.1 | 0 |  | 2 |
| 6 | 胶片缓缓展开 | 1304 | normal | 89.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 528 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
  - [observe] 标题重复：「钥匙坠入雪中」已存在
- 第 4 章：
  - narration_para_pct 93.9 高于目标 90.0
  - [observe] 章节过短 601 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - [observe] 章内自我复读 3 句（如「他突然转身，手中的公文包砸向控制台，溅起几粒灰尘…」）
  - [observe] 章节过短 835 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - interiority_para_pct 8.3 高于目标 6.0
  - [observe] 标题重复：「胶片缓缓展开」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5603
chapter_chars_mean: 934
chapter_chars_median: 984
chapter_chars_cv: 0.35
paragraphs_mean: 34.3
dialogue_chars_pct: 20.1
dialogue_para_pct: 42.2
interiority_para_pct: 1.8
narration_para_pct: 56.0
turn_under20_pct: 88.1
turn_over200_pct: 0.0
attr_say_pct: 70.1
attr_adv_pct: 8.9
scenes_per_chapter: 2.2
dialogue_run_mean: 1.4
turn_len_median: 11
```
