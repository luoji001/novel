# 铜钥 生成报告

slug：`shipin-20261027-38`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6085
LLM 调用：57 次，累计 130.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙下的纸条 | 335 | short | 38.0 | 0 |  | 1 |
| 2 | 钥匙的裂痕 | 930 | normal | 56.5 | 0 |  | 0 |
| 3 | 擦拭登记簿的指纹 | 1137 | normal | 36.7 | 0 |  | 2 |
| 4 | 钥匙上的划痕 | 1275 | normal | 91.4 | 0 |  | 2 |
| 5 | 钥匙与茶杯相撞 | 1070 | normal | 92.0 | 0 |  | 0 |
| 6 | 钥匙入抽屉的瞬间 | 1332 | normal | 91.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 295 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 34.8 低于目标 35.0
  - [observe] 章内自我复读 5 句（如「透过玻璃橱窗能看到大海，浪涛声混着远处渔船的汽笛…」）
- 第 4 章：
  - 单条套路句式超限：「陈国强的」×6、「林晓阳的」×5
  - [observe] 标题与《钥匙的裂痕》近似 0.73 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 27.3 低于目标 35.0
  - attr_adv_pct 14.3 高于目标 10.0

## 整书结构指标

```
chapters: 6
total_chars: 5675
chapter_chars_mean: 946
chapter_chars_median: 1020
chapter_chars_cv: 0.37
paragraphs_mean: 26.2
dialogue_chars_pct: 19.5
dialogue_para_pct: 50.3
interiority_para_pct: 0.7
narration_para_pct: 49.0
turn_under20_pct: 91.8
turn_over200_pct: 0.0
attr_say_pct: 58.8
attr_adv_pct: 4.3
scenes_per_chapter: 1.5
dialogue_run_mean: 1.9
turn_len_median: 8
```
