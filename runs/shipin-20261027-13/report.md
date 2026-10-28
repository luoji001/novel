# 充电宝 生成报告

slug：`shipin-20261027-13`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7247
LLM 调用：57 次，累计 136.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 行李箱争夺战 | 1045 | short | 37.3 | 0 |  | 3 |
| 2 | 监控摄像头争夺战 | 1544 | normal | 35.6 | 0 |  | 4 |
| 3 | 热水瓶碎裂 | 1032 | normal | 91.4 | 0 |  | 1 |
| 4 | 登记簿残页 | 1089 | normal | 35.5 | 0 |  | 3 |
| 5 | 充电宝摔落现场 | 1234 | normal | 92.1 | 0 |  | 1 |
| 6 | 热水瓶裂痕 | 1297 | normal | 37.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 17.9 低于目标 35.0
  - dialogue_run_mean 11.5 高于目标 4.0
  - [observe] 章内自我复读 1 句（如「你凭什么这么肯定它是你的？…」）
- 第 2 章：
  - narration_para_pct 20.0 低于目标 35.0
  - attr_adv_pct 14.3 高于目标 10.0
  - dialogue_run_mean 6 高于目标 4.0
  - [observe] 章内自我复读 1 句（如「你少装了！这箱子是我捡的…」）
- 第 3 章：
  - narration_para_pct 28.6 低于目标 35.0
- 第 4 章：
  - narration_para_pct 31.8 低于目标 35.0
  - dialogue_run_mean 5 高于目标 4.0
  - [observe] 章内自我复读 3 句（如「赵志远踉跄后退，脚下一滑，碰倒装满水的塑料桶…」）
- 第 5 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 6 章：
  - 单条套路句式超限：「李建军的」×3
  - narration_para_pct 30.0 低于目标 35.0
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）
  - [observe] 标题与《热水瓶碎裂》近似 0.80 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6834
chapter_chars_mean: 1139
chapter_chars_median: 1096
chapter_chars_cv: 0.17
paragraphs_mean: 26.8
dialogue_chars_pct: 27.7
dialogue_para_pct: 71.4
interiority_para_pct: 1.8
narration_para_pct: 26.8
turn_under20_pct: 89.7
turn_over200_pct: 0.0
attr_say_pct: 26.0
attr_adv_pct: 12.0
scenes_per_chapter: 1.5
dialogue_run_mean: 5.3
turn_len_median: 11
```
