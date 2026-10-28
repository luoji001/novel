# 二维码 生成报告

slug：`shipin-20261027-157`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6566
LLM 调用：57 次，累计 141.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲打收银机 | 885 | short | 39.4 | 0 |  | 1 |
| 2 | 二维码边缘的裂纹 | 1193 | normal | 95.7 | 0 |  | 2 |
| 3 | 银环坠入屏幕光影 | 1209 | normal | 89.7 | 0 |  | 0 |
| 4 | 擦拭炒粉锅 | 1067 | normal | 51.6 | 0 |  | 2 |
| 5 | 红胶布缠绕手腕 | 1150 | normal | 91.7 | 0 |  | 0 |
| 6 | 竹签落地声响 | 1056 | normal | 91.1 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「我靠，这天都快黑透了…」）
- 第 2 章：
  - narration_para_pct 21.1 低于目标 35.0
  - dialogue_run_mean 5 高于目标 4.0
- 第 4 章：
  - dialogue_chars_pct 0.9 低于目标 5.0
  - interiority_para_pct 6.2 高于目标 6.0

## 整书结构指标

```
chapters: 6
total_chars: 6187
chapter_chars_mean: 1031
chapter_chars_median: 1052
chapter_chars_cv: 0.11
paragraphs_mean: 23.8
dialogue_chars_pct: 18.2
dialogue_para_pct: 46.2
interiority_para_pct: 1.0
narration_para_pct: 52.8
turn_under20_pct: 94.4
turn_over200_pct: 0.0
attr_say_pct: 31.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.1
turn_len_median: 8
```
