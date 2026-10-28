# 铜钥 生成报告

slug：`shipin-20261027-270`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6225
LLM 调用：57 次，累计 135.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙的温度 | 494 | short | 37.8 | 0 |  | 1 |
| 2 | 钥匙与锈迹的对话 | 1191 | normal | 92.2 | 0 |  | 0 |
| 3 | 扫码与锈迹对话 | 1061 | normal | 92.2 | 0 |  | 3 |
| 4 | 钥匙转动的瞬间 | 1091 | normal | 88.4 | 0 |  | 0 |
| 5 | 铜币落铁架 | 1170 | normal | 94.8 | 0 |  | 0 |
| 6 | 船票上的日期 | 1212 | normal | 94.3 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 446 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 20.8 低于目标 35.0
  - dialogue_run_mean 4.8 高于目标 4.0
  - [observe] 标题与《钥匙与锈迹的对话》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5768
chapter_chars_mean: 961
chapter_chars_median: 1052
chapter_chars_cv: 0.27
paragraphs_mean: 30
dialogue_chars_pct: 23.4
dialogue_para_pct: 58.1
interiority_para_pct: 0.5
narration_para_pct: 41.3
turn_under20_pct: 97.9
turn_over200_pct: 0.0
attr_say_pct: 49.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.1
turn_len_median: 8
```
