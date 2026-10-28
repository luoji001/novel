# 扫码风波 生成报告

slug：`shipin-20261027-185`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6280
LLM 调用：57 次，累计 133.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙碰响手机屏 | 853 | short | 99.5 | 0 |  | 0 |
| 2 | 警示牌摇晃 | 938 | normal | 37.1 | 0 |  | 1 |
| 3 | 手机壳翻转时刻度 | 1192 | normal | 93.3 | 0 |  | 1 |
| 4 | 硬币碰撞清脆声 | 1032 | normal | 96.3 | 0 |  | 1 |
| 5 | 钥匙触碰饭盒边缘 | 1150 | normal | 91.5 | 0 |  | 1 |
| 6 | 硬币入袋瞬间 | 1109 | normal | 36.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章节过短 843 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - 单条套路句式超限：「陈阿婆的」×4
- 第 4 章：
  - narration_para_pct 32.4 低于目标 35.0
- 第 5 章：
  - narration_para_pct 28.0 低于目标 35.0
- 第 6 章：
  - narration_para_pct 28.6 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「我儿子寄来的钱，总得存进银行…」）

## 整书结构指标

```
chapters: 6
total_chars: 5775
chapter_chars_mean: 962
chapter_chars_median: 991
chapter_chars_cv: 0.15
paragraphs_mean: 34.2
dialogue_chars_pct: 27.8
dialogue_para_pct: 58.2
interiority_para_pct: 0.0
narration_para_pct: 41.8
turn_under20_pct: 95.4
turn_over200_pct: 0.0
attr_say_pct: 54.9
attr_adv_pct: 0.0
scenes_per_chapter: 2.3
dialogue_run_mean: 2.0
turn_len_median: 8
```
