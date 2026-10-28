# 硬币落地 生成报告

slug：`shipin-20261027-362`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6119
LLM 调用：57 次，累计 127.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币与车窗的对峙 | 626 | short | 38.0 | 0 |  | 2 |
| 2 | 硬币与练习本的对峙 | 1161 | normal | 91.0 | 0 |  | 2 |
| 3 | 刹车踏板的较量 | 1122 | normal | 36.7 | 0 |  | 3 |
| 4 | 计时器的启动时刻 | 1162 | normal | 36.4 | 0 |  | 1 |
| 5 | 硬币在地面滚动 | 993 | normal | 92.9 | 0 |  | 3 |
| 6 | 硬币与练习本的对峙 | 1049 | normal | 36.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 章节过短 580 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「陈志强的」×4
  - [observe] 标题与《硬币与车窗的对峙》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「陈志强的」×3
  - narration_para_pct 28.6 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「她突然用力一蹬，刹车踏板发出一阵金属摩擦的声音，…」）
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「我只想知道它为什么出现在你的车上…」）
- 第 5 章：
  - 单条套路句式超限：「林婉如的」×3
  - narration_para_pct 22.7 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
- 第 6 章：
  - 单条套路句式超限：「陈志强的」×3
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
  - [observe] 标题重复：「硬币与练习本的对峙」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5738
chapter_chars_mean: 956
chapter_chars_median: 1008
chapter_chars_cv: 0.21
paragraphs_mean: 23.2
dialogue_chars_pct: 24.7
dialogue_para_pct: 62.7
interiority_para_pct: 0.7
narration_para_pct: 36.7
turn_under20_pct: 95.1
turn_over200_pct: 0.0
attr_say_pct: 17.9
attr_adv_pct: 4.2
scenes_per_chapter: 1.8
dialogue_run_mean: 2.8
turn_len_median: 10
```
