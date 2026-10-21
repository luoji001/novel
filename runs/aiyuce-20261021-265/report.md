# AI写作服务的报价单 生成报告

slug：`aiyuce-20261021-265`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11554
LLM 调用：57 次，累计 218.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 营业额报表上的数字 | 2233 | normal | 37.8 | 0 |  | 1 |
| 2 | 检查电费单数字 | 2034 | normal | 87.7 | 0 |  | 1 |
| 3 | 张贴报价单 | 2026 | normal | 35.2 | 0 |  | 3 |
| 4 | 摸纸张边缘 | 1871 | normal | 90.2 | 0 |  | 1 |
| 5 | 检查折旧表数字 | 1978 | normal | 36.2 | 0 |  | 1 |
| 6 | 查看营业额报表数字 | 1406 | short | 87.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这样一来，所有记录就变得一致起来了…」）
- 第 2 章：
  - interiority_para_pct 46.2 高于目标 40.0
- 第 3 章：
  - interiority_para_pct 60.0 高于目标 40.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 13.3 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 2 句（如「我们那边的新一代激光打印机试用了两周，效率提高了…」）
- 第 6 章：
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题与《营业额报表上的数字》近似 0.78 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11278
chapter_chars_mean: 1880
chapter_chars_median: 1957
chapter_chars_cv: 0.15
paragraphs_mean: 15
dialogue_chars_pct: 6.8
dialogue_para_pct: 27.4
interiority_para_pct: 38.8
narration_para_pct: 33.8
turn_under20_pct: 62.3
turn_over200_pct: 0.0
attr_say_pct: 55.8
attr_adv_pct: 10.6
scenes_per_chapter: 2
dialogue_run_mean: 1.4
turn_len_median: 10
```
