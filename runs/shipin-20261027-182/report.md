# 药瓶 生成报告

slug：`shipin-20261027-182`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7278
LLM 调用：57 次，累计 145.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药瓶上的水渍 | 710 | short | 97.1 | 0 |  | 0 |
| 2 | 登记本的折痕 | 1309 | normal | 90.4 | 0 |  | 1 |
| 3 | 擦拭药瓶的双手 | 1217 | normal | 37.2 | 0 |  | 1 |
| 4 | 攥紧药瓶的手 | 1460 | normal | 87.0 | 0 |  | 4 |
| 5 | 耳钉入袋 | 1200 | normal | 92.0 | 0 |  | 0 |
| 6 | 攥紧药瓶的手 | 1376 | normal | 90.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 11.1 高于目标 10.0
- 第 3 章：
  - [observe] 章内自我复读 2 句（如「不能随便扔，得等家属来签字…」）
- 第 4 章：
  - 单条套路句式超限：「张晓梅的」×4、「周雪梅点」×3
  - narration_para_pct 21.4 低于目标 35.0
  - dialogue_run_mean 6.6 高于目标 4.0
  - [observe] 标题与《擦拭药瓶的双手》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「张晓梅的」×3
  - [observe] 标题重复：「攥紧药瓶的手」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6802
chapter_chars_mean: 1134
chapter_chars_median: 1190
chapter_chars_cv: 0.22
paragraphs_mean: 32.2
dialogue_chars_pct: 26.4
dialogue_para_pct: 61.1
interiority_para_pct: 0.4
narration_para_pct: 38.6
turn_under20_pct: 95.4
turn_over200_pct: 0.0
attr_say_pct: 53.0
attr_adv_pct: 2.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.8
turn_len_median: 10
```
