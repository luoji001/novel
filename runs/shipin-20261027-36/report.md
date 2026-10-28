# 冰台 生成报告

slug：`shipin-20261027-36`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6313
LLM 调用：57 次，累计 141.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁钳与信纸 | 470 | short | 37.9 | 0 |  | 1 |
| 2 | 信纸与冰台 | 1409 | normal | 92.1 | 0 |  | 2 |
| 3 | 铁钳与鱼鳞堆 | 1238 | normal | 35.9 | 0 |  | 1 |
| 4 | 铁钳与陶罐 | 1001 | normal | 90.6 | 0 |  | 1 |
| 5 | 铜铃惊飞麻雀 | 1036 | normal | 37.0 | 0 |  | 2 |
| 6 | 皮尺与红围巾 | 1153 | normal | 90.5 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 425 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 20.0 低于目标 35.0
  - dialogue_run_mean 5.1 高于目标 4.0
- 第 3 章：
  - [observe] 章内自我复读 3 句（如「他知道这信关系着整条街的生意，可现在却成了两个人…」）
- 第 4 章：
  - [observe] 标题与《铁钳与信纸》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 章内自我复读 1 句（如「吵什么呢？都给我让开…」）

## 整书结构指标

```
chapters: 6
total_chars: 5870
chapter_chars_mean: 978
chapter_chars_median: 1024
chapter_chars_cv: 0.31
paragraphs_mean: 29.7
dialogue_chars_pct: 21.3
dialogue_para_pct: 57.3
interiority_para_pct: 0.6
narration_para_pct: 42.1
turn_under20_pct: 95.6
turn_over200_pct: 0.0
attr_say_pct: 39.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 2.3
turn_len_median: 10
```
