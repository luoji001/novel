# 暗格 生成报告

slug：`xuanyi-20261019-125`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15474
LLM 调用：68 次，累计 235.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 黑衣人消失 | 1918 | short | 99.6 | 0 |  | 2 |
| 2 | 钥匙失踪 | 3818 | normal | 81.9 | 0 |  | 4 |
| 3 | 收据背面字迹 | 3961 | normal | 87.1 | 0 |  | 3 |
| 4 | 打卡记录疑云 | 4099 | normal | 89.7 | 0 |  | 3 |
| 5 | 冷藏柜门缝光亮 | 1673 | short | 93.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈文远的」×4
  - narration_para_pct 12.2 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林子安的」×5、「带着一丝」×3
  - dialogue_chars_pct 16.4 低于目标 20.0
  - interiority_para_pct 20.6 高于目标 20.0
  - [observe] 章内自我复读 20 句（如「他站起身走到桌子前面，伸手去够那个盒子，指尖刚碰…」）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×5、「林子安的」×5、「陈文远的」×3
  - [observe] 章内自我复读 14 句（如「他知道，这次的任务不仅仅是找到缺失的药品那么简单…」）
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「陈文远的」×9、「林子安的」×6、「“我不知道」×4
  - narration_para_pct 8.5 低于目标 20.0
  - [observe] 章内自我复读 20 句（如「陈文远抬起头，眼神透着一种沉思，“但我总觉得这事…」）
- 第 5 章：
  - narration_para_pct 16.7 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14715
chapter_chars_mean: 2943
chapter_chars_median: 3670
chapter_chars_cv: 0.39
paragraphs_mean: 61.8
dialogue_chars_pct: 35.7
dialogue_para_pct: 70.1
interiority_para_pct: 9.1
narration_para_pct: 20.8
turn_under20_pct: 75.4
turn_over200_pct: 0.0
attr_say_pct: 35.4
attr_adv_pct: 11.6
scenes_per_chapter: 5.2
dialogue_run_mean: 5.0
turn_len_median: 13
```
