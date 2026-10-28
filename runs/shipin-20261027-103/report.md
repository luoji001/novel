# 雨靴的脚踝 生成报告

slug：`shipin-20261027-103`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6428
LLM 调用：57 次，累计 131.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 雨靴与电费单 | 518 | short | 38.0 | 0 |  | 2 |
| 2 | 雨靴与维修发票 | 1344 | normal | 91.8 | 0 |  | 1 |
| 3 | 拧螺丝的雨靴 | 1171 | normal | 36.1 | 0 |  | 1 |
| 4 | 比划电梯口的手势 | 1122 | normal | 87.7 | 0 |  | 2 |
| 5 | 雨靴上的破洞 | 960 | normal | 91.1 | 0 |  | 1 |
| 6 | 拧螺丝的雨靴 | 1307 | normal | 84.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 3 句（如「这双靴子是他买的。现在只有我能穿上它…」）
  - [observe] 章节过短 472 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「陈秀兰的」×3
- 第 3 章：
  - [observe] 章内自我复读 2 句（如「电梯门微微晃动，几颗螺丝从缝隙中露出来…」）
- 第 4 章：
  - narration_para_pct 13.6 低于目标 35.0
  - dialogue_run_mean 6 高于目标 4.0
- 第 5 章：
  - 单条套路句式超限：「陈秀兰的」×3
- 第 6 章：
  - narration_para_pct 13.3 低于目标 35.0
  - dialogue_run_mean 8.7 高于目标 4.0
  - [observe] 标题重复：「拧螺丝的雨靴」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6007
chapter_chars_mean: 1001
chapter_chars_median: 1080
chapter_chars_cv: 0.29
paragraphs_mean: 27.3
dialogue_chars_pct: 32.0
dialogue_para_pct: 67.1
interiority_para_pct: 1.3
narration_para_pct: 31.5
turn_under20_pct: 89.1
turn_over200_pct: 0.0
attr_say_pct: 25.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 3.9
turn_len_median: 11
```
