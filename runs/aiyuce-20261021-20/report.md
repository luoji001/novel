# 校对工时 生成报告

slug：`aiyuce-20261021-20`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11660
LLM 调用：57 次，累计 217.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 打开电费单核查 | 2202 | normal | 93.4 | 0 |  | 0 |
| 2 | 核对招聘JD | 2026 | normal | 35.8 | 0 |  | 4 |
| 3 | 核对推理报价单 | 1897 | normal | 35.2 | 0 |  | 1 |
| 4 | 核对订单执行情况 | 2100 | normal | 89.3 | 0 |  | 0 |
| 5 | 核对折旧表数据 | 2051 | normal | 35.4 | 0 |  | 2 |
| 6 | 泼翻咖啡渍合同 | 1378 | short | 33.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 命中套话收尾句
  - interiority_para_pct 53.8 高于目标 40.0
  - narration_para_pct 23.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 3 句（如「如果AI校对工具的实际表现未能达到预期水平，或者…」）
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 章内自我复读 2 句（如「如果公司将折旧年限调整为3年，那么年折旧额就会变…」）
- 第 6 章：
  - dialogue_chars_pct 33.9 高于目标 18.0
  - narration_para_pct 9.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被实际操作过程中出现的技术漏洞或者市场…」）

## 整书结构指标

```
chapters: 6
total_chars: 11398
chapter_chars_mean: 1900
chapter_chars_median: 1994
chapter_chars_cv: 0.15
paragraphs_mean: 13.5
dialogue_chars_pct: 5.4
dialogue_para_pct: 21.2
interiority_para_pct: 25.2
narration_para_pct: 53.6
turn_under20_pct: 82.5
turn_over200_pct: 0.0
attr_say_pct: 20.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.6
turn_len_median: 13
```
