# 船票上的日期 生成报告

slug：`shipin-20261027-04`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6981
LLM 调用：57 次，累计 146.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 船票飘落江面 | 643 | short | 37.7 | 0 |  | 1 |
| 2 | 铜钥匙与旧船票 | 1374 | normal | 92.1 | 0 |  | 0 |
| 3 | 钥匙坠入钱箱裂痕 | 1309 | normal | 36.2 | 0 |  | 1 |
| 4 | 皮尺上的暗红划痕 | 1263 | normal | 94.2 | 0 |  | 0 |
| 5 | 船票上的裂痕 | 1149 | normal | 91.6 | 0 |  | 2 |
| 6 | 铜钥匙的裂痕 | 1237 | normal | 90.9 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 593 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）
- 第 5 章：
  - 情节与已写章节重复 0.71 ≥ 0.62（撞上「陈默带着一张泛黄的旧船票找到老周，试图登上已停航多年的渡…」）
  - narration_para_pct 30.4 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 6572
chapter_chars_mean: 1095
chapter_chars_median: 1175
chapter_chars_cv: 0.23
paragraphs_mean: 26.2
dialogue_chars_pct: 21.4
dialogue_para_pct: 56.4
interiority_para_pct: 1.4
narration_para_pct: 42.2
turn_under20_pct: 96.1
turn_over200_pct: 0.0
attr_say_pct: 29.8
attr_adv_pct: 9.5
scenes_per_chapter: 2
dialogue_run_mean: 2.4
turn_len_median: 10
```
