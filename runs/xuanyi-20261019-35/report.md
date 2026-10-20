# 停摆的手表 生成报告

slug：`xuanyi-20261019-35`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14443
LLM 调用：68 次，累计 222.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手表仍在走动 | 1844 | short | 98.1 | 0 |  | 1 |
| 2 | 死亡证明的温度 | 3561 | normal | 90.2 | 0 |  | 4 |
| 3 | 手表为何仍在走动 | 3778 | normal | 89.6 | 0 |  | 3 |
| 4 | 死亡证明的缺口 | 3519 | normal | 89.1 | 0 |  | 4 |
| 5 | 照片背面的记号 | 1736 | short | 90.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 100.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「林婉如的」×9、「”林婉如轻」×3、「林婉如点」×3
  - narration_para_pct 12.8 低于目标 20.0
  - attr_adv_pct 15.0 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「而接下来的一切，都将围绕着这张死亡证明展开…」）
- 第 3 章：
  - 单条套路句式超限：「林婉如的」×5、「“我不知道」×4
  - [observe] 章内自我复读 2 句（如「李师傅，我想跟你说件事…」）
  - [observe] 标题与《手表仍在走动》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「林婉如的」×5、「”林婉如低」×4、「点了点头」×3
  - narration_para_pct 6.1 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「因为我看到了一些东西…」）
  - [observe] 标题与《死亡证明的温度》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 18.2 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13681
chapter_chars_mean: 2736
chapter_chars_median: 3340
chapter_chars_cv: 0.35
paragraphs_mean: 68.6
dialogue_chars_pct: 35.2
dialogue_para_pct: 74.1
interiority_para_pct: 9.4
narration_para_pct: 16.4
turn_under20_pct: 85.4
turn_over200_pct: 0.0
attr_say_pct: 15.1
attr_adv_pct: 19.1
scenes_per_chapter: 3.2
dialogue_run_mean: 4.5
turn_len_median: 11
```
