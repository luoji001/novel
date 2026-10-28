# 裂痕 生成报告

slug：`shipin-20261027-156`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5776
LLM 调用：57 次，累计 119.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 剪刀落地的瞬间 | 446 | short | 37.4 | 0 |  | 1 |
| 2 | 镜子边缘的裂痕 | 1180 | normal | 35.9 | 0 |  | 2 |
| 3 | 包裹镜子的布巾 | 966 | normal | 35.9 | 0 |  | 1 |
| 4 | 电推子的嗡鸣声 | 1030 | normal | 92.7 | 0 |  | 0 |
| 5 | 擦镜子的抹布 | 985 | normal | 55.4 | 0 |  | 2 |
| 6 | 补丁上的细碎光斑 | 1163 | normal | 89.9 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 383 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 26.7 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「那是我年轻时候留下的…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「老周回头看了一眼镜中的自己，嘴角浮现出一抹笑意…」）
- 第 5 章：
  - narration_para_pct 30.4 低于目标 35.0
  - [observe] 标题与《包裹镜子的布巾》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5392
chapter_chars_mean: 899
chapter_chars_median: 949
chapter_chars_cv: 0.3
paragraphs_mean: 24
dialogue_chars_pct: 18.2
dialogue_para_pct: 47.7
interiority_para_pct: 1.3
narration_para_pct: 50.9
turn_under20_pct: 94.8
turn_over200_pct: 0.0
attr_say_pct: 78.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.9
turn_len_median: 10
```
