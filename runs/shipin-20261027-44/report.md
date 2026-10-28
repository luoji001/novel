# 铜推子的重量 生成报告

slug：`shipin-20261027-44`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6522
LLM 调用：57 次，累计 132.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 推子上的凹痕 | 696 | short | 48.4 | 0 |  | 2 |
| 2 | 摔碎镜子的瞬间 | 1115 | normal | 36.8 | 0 |  | 2 |
| 3 | 铜质推子的温度 | 1209 | normal | 90.9 | 0 |  | 0 |
| 4 | 铜质推子滑落 | 1270 | normal | 57.3 | 0 |  | 1 |
| 5 | 铜质推子的震颤 | 1121 | normal | 91.4 | 0 |  | 1 |
| 6 | 摩挲推子边缘 | 1105 | normal | 89.1 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 1.5 低于目标 5.0
  - narration_para_pct 92.9 高于目标 90.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「你该不会是在找谁吧？…」）
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 4 章：
  - [observe] 标题与《铜质推子的温度》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 标题与《铜质推子的温度》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6114
chapter_chars_mean: 1019
chapter_chars_median: 1056
chapter_chars_cv: 0.19
paragraphs_mean: 25
dialogue_chars_pct: 21.2
dialogue_para_pct: 47.6
interiority_para_pct: 1.1
narration_para_pct: 51.3
turn_under20_pct: 92.7
turn_over200_pct: 0.0
attr_say_pct: 76.6
attr_adv_pct: 6.1
scenes_per_chapter: 1.3
dialogue_run_mean: 1.8
turn_len_median: 10
```
