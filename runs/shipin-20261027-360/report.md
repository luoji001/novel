# 钥匙背面 生成报告

slug：`shipin-20261027-360`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6278
LLM 调用：57 次，累计 134.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙上的薄霜 | 838 | short | 96.7 | 0 |  | 0 |
| 2 | 钥匙背面的刻痕 | 1003 | normal | 35.9 | 0 |  | 3 |
| 3 | 钥匙滑落瞬间 | 1235 | normal | 36.1 | 0 |  | 2 |
| 4 | 钥匙板下的硬物 | 1197 | normal | 89.2 | 0 |  | 1 |
| 5 | 撕页与新页 | 868 | normal | 17.4 | 0 |  | 2 |
| 6 | 钥匙滑落瞬间 | 1131 | normal | 91.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「林小满的」×4
  - narration_para_pct 29.4 低于目标 35.0
  - [observe] 章内自我复读 5 句（如「我每天都在这里工作，没看见过这把钥匙…」）
- 第 3 章：
  - narration_para_pct 29.6 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「这是新来的客人落在这里的吧？…」）
- 第 4 章：
  - narration_para_pct 32.0 低于目标 35.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「笔尖停顿片刻，又补上一行小字…」）
  - [observe] 章节过短 742 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - narration_para_pct 25.9 低于目标 35.0
  - [observe] 标题重复：「钥匙滑落瞬间」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5852
chapter_chars_mean: 975
chapter_chars_median: 1008
chapter_chars_cv: 0.18
paragraphs_mean: 25.5
dialogue_chars_pct: 24.8
dialogue_para_pct: 62.7
interiority_para_pct: 0.0
narration_para_pct: 37.3
turn_under20_pct: 91.9
turn_over200_pct: 0.0
attr_say_pct: 42.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.6
turn_len_median: 11
```
