# 标尺 生成报告

slug：`aiyuce-20261021-58`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12215
LLM 调用：57 次，累计 217.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击键盘的报价单 | 2251 | normal | 37.8 | 0 |  | 1 |
| 2 | 指尖轻触证书边缘 | 2473 | normal | 35.5 | 0 |  | 1 |
| 3 | 核对薪资明细表 | 2249 | normal | 34.4 | 0 |  | 1 |
| 4 | 核对质量评估报告 | 2159 | normal | 36.2 | 0 |  | 3 |
| 5 | 手指轻触财务报表 | 2013 | normal | 89.0 | 0 |  | 1 |
| 6 | 核对报价单边缘 | 1064 | short | 87.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 3 句（如「如果有证据表明市场上有其他公司已经开始提高单价，…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 19.0 高于目标 18.0
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 29.4 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 28.0 高于目标 18.0
  - narration_para_pct 12.5 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11927
chapter_chars_mean: 1988
chapter_chars_median: 2156
chapter_chars_cv: 0.25
paragraphs_mean: 15.2
dialogue_chars_pct: 9.3
dialogue_para_pct: 28.8
interiority_para_pct: 18.3
narration_para_pct: 52.9
turn_under20_pct: 61.9
turn_over200_pct: 0.0
attr_say_pct: 33.5
attr_adv_pct: 20.1
scenes_per_chapter: 1.2
dialogue_run_mean: 1.9
turn_len_median: 22
```
