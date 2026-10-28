# 雨靴悬空 生成报告

slug：`shipin-20261027-61`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7156
LLM 调用：57 次，累计 142.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁钩与电梯故障 | 684 | short | 55.0 | 0 |  | 0 |
| 2 | 铁钩敲击电梯按钮 | 1257 | normal | 92.2 | 0 |  | 2 |
| 3 | 晾衣绳悬空 | 1411 | normal | 36.8 | 0 |  | 2 |
| 4 | 螺丝与雨靴的对峙 | 1385 | normal | 94.6 | 0 |  | 2 |
| 5 | 晾衣绳悬空 | 1193 | normal | 36.6 | 0 |  | 3 |
| 6 | 晾衣绳上的雨靴 | 1220 | normal | 85.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 12.5 低于目标 35.0
  - dialogue_run_mean 7 高于目标 4.0
- 第 3 章：
  - narration_para_pct 28.6 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「她伸手抓起雨靴，转身朝楼梯口走去，晾衣绳在身后晃…」）
- 第 4 章：
  - narration_para_pct 22.2 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
- 第 5 章：
  - narration_para_pct 26.5 低于目标 35.0
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
  - [observe] 标题重复：「晾衣绳悬空」已存在
- 第 6 章：
  - dialogue_chars_pct 46.7 高于目标 45.0
  - narration_para_pct 8.0 低于目标 35.0
  - dialogue_run_mean 23 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 6719
chapter_chars_mean: 1120
chapter_chars_median: 1166
chapter_chars_cv: 0.23
paragraphs_mean: 28.7
dialogue_chars_pct: 36.1
dialogue_para_pct: 78.6
interiority_para_pct: 0.0
narration_para_pct: 21.4
turn_under20_pct: 90.6
turn_over200_pct: 0.0
attr_say_pct: 43.4
attr_adv_pct: 5.5
scenes_per_chapter: 2
dialogue_run_mean: 7.1
turn_len_median: 11
```
