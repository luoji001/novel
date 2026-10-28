# 镜中剪影 生成报告

slug：`shipin-20261027-86`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6060
LLM 调用：57 次，累计 127.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 推子划过弧度 | 556 | short | 38.8 | 0 |  | 3 |
| 2 | 碎镜贴肤 | 1228 | normal | 37.1 | 0 |  | 1 |
| 3 | 账本上的乌云 | 1072 | normal | 94.0 | 0 |  | 0 |
| 4 | 蓝布条的重量 | 1132 | normal | 92.9 | 0 |  | 1 |
| 5 | 推子划过弧度 | 1008 | normal | 59.3 | 0 |  | 1 |
| 6 | 镜子贴头皮 | 1058 | normal | 92.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 31.6 低于目标 35.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - [observe] 章节过短 504 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 4 句（如「小林蹲下身子，手指轻轻拂过那些锋利的边缘，像是在…」）
- 第 4 章：
  - attr_adv_pct 12.5 高于目标 10.0
- 第 5 章：
  - [observe] 标题重复：「推子划过弧度」已存在
- 第 6 章：
  - narration_para_pct 30.0 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 5651
chapter_chars_mean: 942
chapter_chars_median: 1010
chapter_chars_cv: 0.24
paragraphs_mean: 25.8
dialogue_chars_pct: 23.0
dialogue_para_pct: 51.5
interiority_para_pct: 0.4
narration_para_pct: 48.1
turn_under20_pct: 86.2
turn_over200_pct: 0.0
attr_say_pct: 47.8
attr_adv_pct: 2.3
scenes_per_chapter: 1.7
dialogue_run_mean: 2.4
turn_len_median: 10
```
