# 纸条 生成报告

slug：`xuanyi-20261019-252`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14395
LLM 调用：68 次，累计 226.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 屏幕上的登录记录 | 1817 | short | 98.6 | 0 |  | 2 |
| 2 | 纸条边缘的指纹痕迹 | 3740 | normal | 91.3 | 0 |  | 4 |
| 3 | 纸张边缘的裂痕 | 3261 | normal | 92.1 | 0 |  | 3 |
| 4 | 抚摸火车票边缘 | 3702 | normal | 89.0 | 0 |  | 3 |
| 5 | 敲击键盘的指尖 | 1870 | short | 88.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 17.9 低于目标 20.0
  - attr_adv_pct 15.4 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「林志远的」×6、「“我不知道」×4、「他知道这」×4
  - narration_para_pct 11.1 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 章内自我复读 2 句（如「你知道这意味着什么吗？…」）
- 第 3 章：
  - 单条套路句式超限：「苏婉清的」×6、「林志远的」×4、「苏婉清点」×3
  - narration_para_pct 11.8 低于目标 20.0
  - [observe] 标题与《纸条边缘的指纹痕迹》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「苏婉清点」×5、「”苏婉清轻」×4、「苏婉清的」×4
  - narration_para_pct 8.3 低于目标 20.0
  - [observe] 章内自我复读 4 句（如「但我相信，他一定遇到了什么麻烦…」）
- 第 5 章：
  - dialogue_chars_pct 19.8 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「他拿出来一看，是苏婉清发来的消息：“陈远航的身份…」）

## 整书结构指标

```
chapters: 5
total_chars: 13686
chapter_chars_mean: 2737
chapter_chars_median: 3110
chapter_chars_cv: 0.34
paragraphs_mean: 62.2
dialogue_chars_pct: 38.4
dialogue_para_pct: 76.0
interiority_para_pct: 9.7
narration_para_pct: 14.3
turn_under20_pct: 78.4
turn_over200_pct: 0.0
attr_say_pct: 33.4
attr_adv_pct: 6.6
scenes_per_chapter: 3.2
dialogue_run_mean: 5.0
turn_len_median: 12
```
