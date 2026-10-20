# 重扫 生成报告

slug：`xuanyi-20261019-57`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13860
LLM 调用：68 次，累计 218.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫描枪的异常 | 1657 | short | 92.4 | 0 |  | 3 |
| 2 | 面单的双面痕迹 | 3645 | normal | 93.8 | 0 |  | 2 |
| 3 | 分拣记录表的褶痕 | 3471 | normal | 92.0 | 0 |  | 3 |
| 4 | 包裹的失踪 | 3238 | normal | 91.4 | 0 |  | 3 |
| 5 | 面单的双重扫描 | 1844 | short | 91.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 60.7 高于目标 58.0
  - narration_para_pct 2.4 低于目标 20.0
  - dialogue_run_mean 19.5 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×3、「点了点头」×3、「周晓芸的」×3
  - narration_para_pct 10.7 低于目标 20.0
- 第 3 章：
  - narration_para_pct 14.8 低于目标 20.0
  - attr_adv_pct 12.0 高于目标 10.0
  - [observe] 章内自我复读 9 句（如「不会这么简单，”陈志远摇了摇头，“如果只是一个简…」）
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3、「陈志远的」×3
  - narration_para_pct 13.8 低于目标 20.0
  - attr_adv_pct 15.8 高于目标 10.0
- 第 5 章：
  - narration_para_pct 12.1 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13207
chapter_chars_mean: 2641
chapter_chars_median: 3109
chapter_chars_cv: 0.34
paragraphs_mean: 55.6
dialogue_chars_pct: 46.8
dialogue_para_pct: 81.3
interiority_para_pct: 7.1
narration_para_pct: 11.7
turn_under20_pct: 65.5
turn_over200_pct: 0.0
attr_say_pct: 23.9
attr_adv_pct: 9.0
scenes_per_chapter: 2.2
dialogue_run_mean: 8.5
turn_len_median: 15
```
