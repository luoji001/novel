# 测评表 生成报告

slug：`aiyuce-20261021-161`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12770
LLM 调用：57 次，累计 229.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 质检主管的手指划过JD页面 | 1920 | normal | 94.3 | 0 |  | 0 |
| 2 | 绩效考核表泛黄一角 | 2709 | normal | 89.8 | 0 |  | 1 |
| 3 | 手指划过时间戳 | 2315 | normal | 35.7 | 0 |  | 1 |
| 4 | 平板电脑屏幕闪烁 | 2165 | normal | 85.2 | 0 |  | 1 |
| 5 | 预算表数字未变 | 2197 | normal | 80.2 | 0 |  | 3 |
| 6 | 测试报告留桌上 | 1458 | short | 85.9 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 35.7 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 27.7 高于目标 18.0
- 第 5 章：
  - dialogue_chars_pct 42.1 高于目标 18.0
  - dialogue_run_mean 7.5 高于目标 4.0
  - narration_para_pct 21.1 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 12493
chapter_chars_mean: 2082
chapter_chars_median: 2130
chapter_chars_cv: 0.2
paragraphs_mean: 14.3
dialogue_chars_pct: 15.4
dialogue_para_pct: 43.8
interiority_para_pct: 9.9
narration_para_pct: 46.3
turn_under20_pct: 51.7
turn_over200_pct: 0.0
attr_say_pct: 10.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.9
turn_len_median: 26
```
