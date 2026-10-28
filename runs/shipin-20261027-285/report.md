# 雨靴 生成报告

slug：`shipin-20261027-285`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6570
LLM 调用：57 次，累计 145.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 拽鞋带的老人 | 703 | short | 97.1 | 0 |  | 1 |
| 2 | 铁皮桶与雨靴对峙 | 1437 | normal | 92.3 | 0 |  | 0 |
| 3 | 拽鞋带的老人 | 1036 | normal | 35.4 | 0 |  | 4 |
| 4 | 伞骨上的雨靴印 | 1300 | normal | 92.6 | 0 |  | 2 |
| 5 | 摩挲电费单的老人 | 1322 | normal | 87.7 | 0 |  | 2 |
| 6 | 摩挲雨靴的老人 | 766 | normal | 36.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 25.0 低于目标 35.0
- 第 3 章：
  - narration_para_pct 10.5 低于目标 35.0
  - dialogue_run_mean 5.7 高于目标 4.0
  - [observe] 章内自我复读 9 句（如「物业管理员抬头看了看楼梯方向，又低头看向手中的对…」）
  - [observe] 标题重复：「拽鞋带的老人」已存在
- 第 4 章：
  - 单条套路句式超限：「张德顺的」×5
  - narration_para_pct 21.7 低于目标 35.0
- 第 5 章：
  - interiority_para_pct 7.7 高于目标 6.0
  - narration_para_pct 34.6 低于目标 35.0
- 第 6 章：
  - [observe] 章节过短 715 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《摩挲电费单的老人》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6234
chapter_chars_mean: 1039
chapter_chars_median: 1110
chapter_chars_cv: 0.29
paragraphs_mean: 19.8
dialogue_chars_pct: 23.2
dialogue_para_pct: 63.3
interiority_para_pct: 2.4
narration_para_pct: 34.3
turn_under20_pct: 83.2
turn_over200_pct: 0.0
attr_say_pct: 23.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.8
turn_len_median: 12
```
