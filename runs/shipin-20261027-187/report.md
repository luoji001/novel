# 雨靴 生成报告

slug：`shipin-20261027-187`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6851
LLM 调用：57 次，累计 138.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 雨靴的裂痕 | 543 | short | 38.1 | 0 |  | 1 |
| 2 | 通知单边缘的沙沙声 | 1158 | normal | 92.9 | 0 |  | 0 |
| 3 | 电梯里的雨靴裂痕 | 1341 | normal | 95.0 | 0 |  | 2 |
| 4 | 铜钥匙的寒意 | 1079 | normal | 57.8 | 0 |  | 2 |
| 5 | 房产证与钥匙串 | 1488 | normal | 84.1 | 0 |  | 2 |
| 6 | 雨靴的裂痕 | 1236 | normal | 91.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 496 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 23.1 低于目标 35.0
  - [observe] 标题与《雨靴的裂痕》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - interiority_para_pct 6.7 高于目标 6.0
  - narration_para_pct 33.3 低于目标 35.0
- 第 5 章：
  - dialogue_chars_pct 2.7 低于目标 5.0
  - interiority_para_pct 9.1 高于目标 6.0
- 第 6 章：
  - narration_para_pct 31.8 低于目标 35.0
  - [observe] 标题重复：「雨靴的裂痕」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6547
chapter_chars_mean: 1091
chapter_chars_median: 1146
chapter_chars_cv: 0.3
paragraphs_mean: 17.5
dialogue_chars_pct: 16.3
dialogue_para_pct: 49.5
interiority_para_pct: 3.9
narration_para_pct: 46.6
turn_under20_pct: 92.3
turn_over200_pct: 0.0
attr_say_pct: 25.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.8
turn_len_median: 10
```
