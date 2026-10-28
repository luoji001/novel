# 红布条 生成报告

slug：`shipin-20261027-53`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6811
LLM 调用：57 次，累计 138.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 放映胶片的划痕 | 693 | short | 36.2 | 0 |  | 2 |
| 2 | 钢笔戳票根 | 1048 | normal | 92.9 | 0 |  | 0 |
| 3 | 擦拭灯泡的午后 | 1163 | normal | 94.5 | 0 |  | 0 |
| 4 | 擦拭镜头的午后 | 1295 | normal | 90.6 | 0 |  | 1 |
| 5 | 摩挲铜徽章的黄昏 | 1273 | normal | 90.5 | 0 |  | 0 |
| 6 | 转动生锈的钥匙 | 1333 | normal | 90.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 96.3 高于目标 90.0
- 第 4 章：
  - [observe] 标题与《擦拭灯泡的午后》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「老张站在」×3

## 整书结构指标

```
chapters: 6
total_chars: 6399
chapter_chars_mean: 1066
chapter_chars_median: 1152
chapter_chars_cv: 0.23
paragraphs_mean: 26.2
dialogue_chars_pct: 21.0
dialogue_para_pct: 46.2
interiority_para_pct: 0.4
narration_para_pct: 53.4
turn_under20_pct: 82.7
turn_over200_pct: 0.0
attr_say_pct: 69.8
attr_adv_pct: 0.0
scenes_per_chapter: 2.8
dialogue_run_mean: 1.6
turn_len_median: 11
```
