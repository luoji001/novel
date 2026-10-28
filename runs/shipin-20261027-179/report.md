# 胶片上的标签 生成报告

slug：`shipin-20261027-179`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6622
LLM 调用：57 次，累计 126.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 胶片盒滑入瞬间 | 945 | short | 96.0 | 0 |  | 1 |
| 2 | 公文包轻颤时刻 | 1122 | normal | 7.8 | 0 |  | 1 |
| 3 | 塞报纸的手势 | 1119 | normal | 94.9 | 0 |  | 1 |
| 4 | 红袖章的最后一次抚摸 | 1189 | normal | 0.0 | 0 |  | 1 |
| 5 | 电影票的折痕 | 1095 | normal | 93.2 | 0 |  | 1 |
| 6 | 关闭窗棂的刹那 | 1146 | normal | 55.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 4.3 低于目标 5.0
- 第 2 章：
  - interiority_para_pct 14.3 高于目标 6.0
- 第 3 章：
  - narration_para_pct 34.5 低于目标 35.0
- 第 4 章：
  - [observe] interiority_para_pct 18.2 > 15.0（结构塌缩）
- 第 5 章：
  - narration_para_pct 22.7 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 6243
chapter_chars_mean: 1040
chapter_chars_median: 1056
chapter_chars_cv: 0.08
paragraphs_mean: 23.5
dialogue_chars_pct: 15.7
dialogue_para_pct: 41.0
interiority_para_pct: 8.4
narration_para_pct: 50.6
turn_under20_pct: 92.3
turn_over200_pct: 0.0
attr_say_pct: 42.2
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 1.6
turn_len_median: 10
```
