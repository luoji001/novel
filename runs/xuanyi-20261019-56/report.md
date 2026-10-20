# 铜纽扣 生成报告

slug：`xuanyi-20261019-56`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14422
LLM 调用：68 次，累计 241.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 烟锅底的裂痕 | 1652 | short | 100.0 | 0 |  | 3 |
| 2 | 账单的背面纹路 | 3699 | normal | 90.8 | 0 |  | 2 |
| 3 | 木牌的缺口痕迹 | 3442 | normal | 92.1 | 0 |  | 3 |
| 4 | 烛光下的纸条 | 3697 | normal | 87.8 | 0 |  | 5 |
| 5 | 铜纽扣的重现 | 1927 | short | 89.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈素云的」×4、「沈文远的」×3
  - narration_para_pct 15.8 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「沈文远的」×6、「“我不知道」×4、「陈素云的」×4
  - narration_para_pct 5.6 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「陈素云的」×7、「沈文远的」×6
  - narration_para_pct 9.2 低于目标 20.0
  - [observe] attr_adv_pct 31.6 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「陈素云的」×5、「“我不知道」×4、「沈文远点」×4
  - 情节与已写章节重复 0.73 ≥ 0.62（撞上「沈文远和陈素云在防空洞中发现李老板的遗物，揭开他死亡背后…」）
  - narration_para_pct 6.2 低于目标 20.0
  - attr_adv_pct 19.6 高于目标 10.0
  - dialogue_run_mean 12.2 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「沈文远的」×3
  - narration_para_pct 9.5 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13647
chapter_chars_mean: 2729
chapter_chars_median: 3275
chapter_chars_cv: 0.35
paragraphs_mean: 67.8
dialogue_chars_pct: 43.7
dialogue_para_pct: 83.5
interiority_para_pct: 8.1
narration_para_pct: 8.3
turn_under20_pct: 79.5
turn_over200_pct: 0.0
attr_say_pct: 24.4
attr_adv_pct: 16.1
scenes_per_chapter: 4.2
dialogue_run_mean: 7.3
turn_len_median: 12
```
