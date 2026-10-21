# 证书 生成报告

slug：`aiyuce-20261021-154`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12693
LLM 调用：57 次，累计 222.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对财务报表 | 2438 | normal | 96.8 | 0 |  | 0 |
| 2 | 修改报价单 | 2149 | normal | 35.8 | 0 |  | 1 |
| 3 | 核对考勤记录 | 1940 | normal | 89.7 | 0 |  | 1 |
| 4 | 核对证书模板 | 2660 | normal | 90.3 | 0 |  | 0 |
| 5 | 核对质量评估 | 2040 | normal | 36.0 | 0 |  | 1 |
| 6 | 核对证书持有率 | 1460 | short | 90.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 31.2 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的数据显示出来呢…」）
- 第 6 章：
  - [observe] 标题与《核对证书模板》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12415
chapter_chars_mean: 2069
chapter_chars_median: 2048
chapter_chars_cv: 0.2
paragraphs_mean: 15.7
dialogue_chars_pct: 6.3
dialogue_para_pct: 27.6
interiority_para_pct: 19.6
narration_para_pct: 52.8
turn_under20_pct: 47.2
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.4
turn_len_median: 18
```
