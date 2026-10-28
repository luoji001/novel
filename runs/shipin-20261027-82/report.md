# 硬币密码 生成报告

slug：`shipin-20261027-82`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6045
LLM 调用：57 次，累计 124.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币上的微光 | 391 | short | 33.6 | 0 |  | 3 |
| 2 | 掀开帆布包的一角 | 1096 | normal | 86.8 | 0 |  | 2 |
| 3 | 摩挲金属扣 | 1046 | normal | 91.7 | 0 |  | 0 |
| 4 | 摩挲计时器边缘 | 1102 | normal | 91.6 | 0 |  | 0 |
| 5 | 摩挲帆布包边缘 | 1198 | normal | 33.9 | 0 |  | 2 |
| 6 | 摩挲方向盘边缘 | 1206 | normal | 90.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 357 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - dialogue_chars_pct 1.0 低于目标 5.0
  - narration_para_pct 97.9 高于目标 90.0
- 第 5 章：
  - dialogue_chars_pct 3.9 低于目标 5.0
  - [observe] 章内自我复读 3 句（如「远处传来一阵引擎启动的声音，苏晴抬起头，看见一辆…」）
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3

## 整书结构指标

```
chapters: 6
total_chars: 5635
chapter_chars_mean: 939
chapter_chars_median: 1020
chapter_chars_cv: 0.31
paragraphs_mean: 26.3
dialogue_chars_pct: 7.1
dialogue_para_pct: 25.8
interiority_para_pct: 0.5
narration_para_pct: 73.7
turn_under20_pct: 98.6
turn_over200_pct: 0.0
attr_say_pct: 9.9
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.6
turn_len_median: 8
```
