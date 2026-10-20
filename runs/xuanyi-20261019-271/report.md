# 锁芯 生成报告

slug：`xuanyi-20261019-271`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14097
LLM 调用：68 次，累计 227.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲怀表纹路 | 1644 | short | 98.4 | 0 |  | 1 |
| 2 | 摩挲支票边缘 | 3752 | normal | 92.4 | 0 |  | 2 |
| 3 | 摩挲锁芯纹路 | 3238 | normal | 91.0 | 0 |  | 3 |
| 4 | 摩挲锁芯纹路 | 3652 | normal | 89.9 | 0 |  | 6 |
| 5 | 摩挲钥匙边缘 | 1806 | short | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 12.9 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈慕云的」×5
  - narration_para_pct 16.9 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「周启明的」×7、「沈慕云的」×7
  - narration_para_pct 11.8 低于目标 20.0
  - [observe] 标题与《摩挲怀表纹路》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「周启明的」×9、「沈慕云的」×4、「沈慕云点了点头」×3
  - 情节与已写章节重复 0.67 ≥ 0.62（撞上「沈慕云发现保险柜锁芯有异常磨损，质疑其更换时间与死者死亡…」）
  - narration_para_pct 8.0 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「周启明的声音低了下来…」）
  - [observe] attr_adv_pct 21.1 > 20.0（结构塌缩）
  - [observe] 标题重复：「摩挲锁芯纹路」已存在
- 第 5 章：
  - narration_para_pct 14.0 低于目标 20.0
  - [observe] 标题与《摩挲支票边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13422
chapter_chars_mean: 2684
chapter_chars_median: 3088
chapter_chars_cv: 0.36
paragraphs_mean: 60
dialogue_chars_pct: 45.5
dialogue_para_pct: 80.1
interiority_para_pct: 7.3
narration_para_pct: 12.6
turn_under20_pct: 67.3
turn_over200_pct: 0.0
attr_say_pct: 17.5
attr_adv_pct: 5.4
scenes_per_chapter: 2.8
dialogue_run_mean: 5.2
turn_len_median: 13
```
