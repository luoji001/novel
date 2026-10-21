# AI合同 生成报告

slug：`aiyuce-20261021-97`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12512
LLM 调用：57 次，累计 218.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单核对 | 2185 | normal | 95.0 | 0 |  | 0 |
| 2 | 招聘JD修改三次 | 2385 | normal | 90.7 | 0 |  | 1 |
| 3 | 查看推理报价单 | 1884 | normal | 35.4 | 0 |  | 1 |
| 4 | 查看折旧表 | 2398 | normal | 36.4 | 0 |  | 2 |
| 5 | 打印机吐出签名页 | 2648 | normal | 89.5 | 0 |  | 0 |
| 6 | 对比电费单与报价单 | 1006 | short | 88.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 41.2 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 3 句（如「如果AI生成的文案在实际使用过程中出现了错误，导…」）
- 第 4 章：
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 6 章：
  - interiority_para_pct 42.9 高于目标 40.0

## 整书结构指标

```
chapters: 6
total_chars: 12244
chapter_chars_mean: 2041
chapter_chars_median: 2240
chapter_chars_cv: 0.28
paragraphs_mean: 14.3
dialogue_chars_pct: 3.9
dialogue_para_pct: 24.5
interiority_para_pct: 25.2
narration_para_pct: 50.2
turn_under20_pct: 78.1
turn_over200_pct: 0.0
attr_say_pct: 43.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.4
turn_len_median: 10
```
