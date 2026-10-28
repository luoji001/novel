# 硬币的痕迹 生成报告

slug：`shipin-20261027-306`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5547
LLM 调用：57 次，累计 126.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币滑落掌纹 | 408 | short | 37.8 | 0 |  | 1 |
| 2 | 玻璃板上的刻痕 | 914 | normal | 37.8 | 0 |  | 2 |
| 3 | 粉笔划过玻璃 | 1317 | normal | 90.9 | 0 |  | 1 |
| 4 | 硬币落入掌心 | 939 | normal | 91.6 | 0 |  | 1 |
| 5 | 纸条上的字迹 | 884 | normal | 36.2 | 0 |  | 1 |
| 6 | 擦玻璃的手势 | 1079 | normal | 91.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 358 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 2 句（如「突然，她的手指停顿了一下，目光落在玻璃板一角的一…」）
  - [observe] 章节过短 863 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - 单条套路句式超限：「李建国的」×3
- 第 4 章：
  - [observe] 标题与《硬币滑落掌纹》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章节过短 830 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - 单条套路句式超限：「李建国的」×3

## 整书结构指标

```
chapters: 6
total_chars: 5182
chapter_chars_mean: 864
chapter_chars_median: 874
chapter_chars_cv: 0.34
paragraphs_mean: 22.8
dialogue_chars_pct: 14.7
dialogue_para_pct: 42.5
interiority_para_pct: 1.5
narration_para_pct: 56.0
turn_under20_pct: 91.6
turn_over200_pct: 0.0
attr_say_pct: 74.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.8
turn_len_median: 8
```
