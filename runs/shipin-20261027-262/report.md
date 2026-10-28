# 铁盒 生成报告

slug：`shipin-20261027-262`
档位：视频分镜　闸门模式：observe
章数：6　总字数：4106
LLM 调用：57 次，累计 110.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙落回原位 | 739 | short | 39.6 | 0 |  | 3 |
| 2 | 保险柜裂痕 | 494 | normal | 19.4 | 0 |  | 3 |
| 3 | 钥匙与房卡的对峙 | 991 | normal | 87.5 | 0 |  | 2 |
| 4 | 粉笔划过桌面 | 465 | normal | 13.5 | 0 |  | 3 |
| 5 | 钥匙坠入雨痕 | 507 | normal | 36.3 | 0 |  | 1 |
| 6 | 钥匙坠入锁孔 | 904 | normal | 36.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 27.8 低于目标 35.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - [observe] 章内自我复读 2 句（如「这种老式钥匙，应该还有主人…」）
- 第 2 章：
  - dialogue_chars_pct 0.9 低于目标 5.0
  - narration_para_pct 95.0 高于目标 90.0
  - [observe] 章节过短 441 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - narration_para_pct 15.4 低于目标 35.0
  - dialogue_run_mean 5.5 高于目标 4.0
- 第 4 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 409 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - [observe] 章节过短 453 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - [observe] 章节过短 834 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《钥匙坠入雨痕》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 3749
chapter_chars_mean: 625
chapter_chars_median: 571
chapter_chars_cv: 0.36
paragraphs_mean: 22.2
dialogue_chars_pct: 24.6
dialogue_para_pct: 49.4
interiority_para_pct: 0.0
narration_para_pct: 50.6
turn_under20_pct: 97.8
turn_over200_pct: 0.0
attr_say_pct: 81.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.8
turn_len_median: 8
```
