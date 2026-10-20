# xuanyi-20261019-01 生成报告

档位：悬疑推理　闸门模式：observe
章数：5　总字数：15984
LLM 调用：67 次，累计 245.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 照片上的学生证 | 1770 | short | 95.1 | 0 |  | 2 |
| 2 | 文件夹上的指纹 | 3885 | normal | 87.6 | 0 |  | 3 |
| 3 | 学生证的磨损处 | 4256 | normal | 83.1 | 0 |  | 4 |
| 4 | 照片背面的指纹 | 3857 | normal | 85.4 | 0 |  | 4 |
| 5 | 照片边缘的指纹 | 2211 | short | 89.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈素英的」×3
  - narration_para_pct 9.5 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈素英的」×6
  - narration_para_pct 4.7 低于目标 20.0
  - attr_adv_pct 11.8 高于目标 10.0
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林永年站在」×4、「陈素英的」×4、「林永年点了点头」×3
  - narration_para_pct 18.2 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「就在最近几个月的记录里，有一笔特别注明是‘李明远…」）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「“我不知道」×5、「他知道自己」×4、「陈素英点」×4
  - narration_para_pct 13.6 低于目标 20.0
  - [observe] 章内自我复读 21 句（如「你看，这张照片里的孩子，穿的是1987年的校服，…」）
- 第 5 章：
  - 单条套路句式超限：「陈素英的」×3
  - narration_para_pct 5.8 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 标题与《照片背面的指纹》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 15126
chapter_chars_mean: 3025
chapter_chars_median: 3622
chapter_chars_cv: 0.35
paragraphs_mean: 77.8
dialogue_chars_pct: 46.6
dialogue_para_pct: 83.4
interiority_para_pct: 5.5
narration_para_pct: 11.1
turn_under20_pct: 76.1
turn_over200_pct: 0.0
attr_say_pct: 33.2
attr_adv_pct: 7.8
scenes_per_chapter: 2.8
dialogue_run_mean: 7.4
turn_len_median: 12
```
