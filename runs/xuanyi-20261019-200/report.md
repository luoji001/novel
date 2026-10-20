# 打卡记录 生成报告

slug：`xuanyi-20261019-200`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13545
LLM 调用：68 次，累计 217.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 刷卡记录打印件 | 1874 | short | 98.5 | 0 |  | 1 |
| 2 | 屏幕闪烁异常 | 3198 | normal | 93.5 | 0 |  | 4 |
| 3 | 摩挲桌面边缘 | 3253 | normal | 55.0 | 0 |  | 3 |
| 4 | 摩挲钥匙凹凸纹路 | 3409 | normal | 87.9 | 0 |  | 4 |
| 5 | 摩挲泛黄照片边角 | 1806 | short | 89.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周启明的」×3、「林子安的」×3
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×3、「周启明点」×3
  - narration_para_pct 5.3 低于目标 20.0
  - attr_adv_pct 19.0 高于目标 10.0
  - dialogue_run_mean 10.4 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×5、「林子安的」×5
  - dialogue_chars_pct 13.7 低于目标 20.0
  - interiority_para_pct 21.6 高于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周启明的」×3
  - dialogue_chars_pct 19.4 低于目标 20.0
  - attr_adv_pct 17.6 高于目标 10.0
  - [observe] 章内自我复读 15 句（如「林子安想了想，决定暂时保留这个悬念，于是礼貌地说…」）

## 整书结构指标

```
chapters: 5
total_chars: 12989
chapter_chars_mean: 2598
chapter_chars_median: 3069
chapter_chars_cv: 0.3
paragraphs_mean: 47.4
dialogue_chars_pct: 30.7
dialogue_para_pct: 65.1
interiority_para_pct: 12.1
narration_para_pct: 22.8
turn_under20_pct: 70.9
turn_over200_pct: 0.0
attr_say_pct: 16.9
attr_adv_pct: 9.0
scenes_per_chapter: 4.2
dialogue_run_mean: 4.5
turn_len_median: 14
```
