# 手写船票 生成报告

slug：`shipin-20261027-326`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5657
LLM 调用：57 次，累计 126.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙抵住门板 | 503 | short | 21.6 | 0 |  | 1 |
| 2 | 手机屏幕的光 | 1274 | normal | 88.9 | 0 |  | 3 |
| 3 | 系红绳的清晨 | 790 | normal | 19.3 | 0 |  | 4 |
| 4 | 铜钥匙叩木门 | 1208 | normal | 90.9 | 0 |  | 3 |
| 5 | 帆布包里的船票 | 934 | normal | 37.4 | 0 |  | 2 |
| 6 | 收音机动辄三分钟 | 942 | normal | 36.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 440 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 6.2 低于目标 35.0
  - attr_adv_pct 16.7 高于目标 10.0
  - dialogue_run_mean 9.7 高于目标 4.0
- 第 3 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 94.7 高于目标 90.0
  - [observe] 章内自我复读 1 句（如「灰尘扬起，在晨光中飘散…」）
  - [observe] 章节过短 738 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - interiority_para_pct 7.7 高于目标 6.0
  - narration_para_pct 23.1 低于目标 35.0
  - [observe] 标题与《铜钥匙抵住门板》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「晨光洒在江面上，波光粼粼…」）
  - [observe] 章节过短 831 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - [observe] 章节过短 846 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5193
chapter_chars_mean: 866
chapter_chars_median: 838
chapter_chars_cv: 0.32
paragraphs_mean: 30.3
dialogue_chars_pct: 24.9
dialogue_para_pct: 52.0
interiority_para_pct: 3.2
narration_para_pct: 44.8
turn_under20_pct: 95.8
turn_over200_pct: 0.0
attr_say_pct: 33.3
attr_adv_pct: 4.5
scenes_per_chapter: 2
dialogue_run_mean: 3.3
turn_len_median: 10
```
