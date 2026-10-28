# 铜钥 生成报告

slug：`shipin-20261027-402`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5966
LLM 调用：57 次，累计 127.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙落入掌心 | 532 | short | 21.9 | 0 |  | 1 |
| 2 | 钥匙坠落的瞬间 | 1161 | normal | 36.2 | 0 |  | 2 |
| 3 | 钥匙与便签纸的对峙 | 944 | normal | 36.9 | 0 |  | 2 |
| 4 | 登记簿的第37页 | 1044 | normal | 55.8 | 0 |  | 2 |
| 5 | 钥匙与便签纸的对峙 | 1183 | normal | 92.1 | 0 |  | 2 |
| 6 | 钥匙碾过登记簿边缘 | 1096 | normal | 92.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 474 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「陈建国的」×3
  - [observe] 章内自我复读 1 句（如「这是您早上让我收的？…」）
- 第 3 章：
  - narration_para_pct 28.1 低于目标 35.0
  - [observe] 章节过短 863 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - narration_para_pct 13.0 低于目标 35.0
  - dialogue_run_mean 5 高于目标 4.0
- 第 5 章：
  - narration_para_pct 22.2 低于目标 35.0
  - [observe] 标题重复：「钥匙与便签纸的对峙」已存在
- 第 6 章：
  - 单条套路句式超限：「陈建国的」×3
  - narration_para_pct 34.8 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 5551
chapter_chars_mean: 925
chapter_chars_median: 1002
chapter_chars_cv: 0.26
paragraphs_mean: 25.2
dialogue_chars_pct: 25.0
dialogue_para_pct: 66.0
interiority_para_pct: 1.1
narration_para_pct: 32.9
turn_under20_pct: 94.3
turn_over200_pct: 0.0
attr_say_pct: 58.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 3.0
turn_len_median: 10
```
