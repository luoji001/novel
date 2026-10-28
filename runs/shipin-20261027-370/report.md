# 应急灯 生成报告

slug：`shipin-20261027-370`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7659
LLM 调用：57 次，累计 149.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 应急灯投下影子 | 878 | short | 96.9 | 0 |  | 0 |
| 2 | 铅笔敲击试卷 | 1193 | normal | 36.7 | 0 |  | 1 |
| 3 | 保温杯接热水 | 1233 | normal | 91.1 | 0 |  | 0 |
| 4 | 铅笔断成两截 | 1387 | normal | 91.7 | 0 |  | 1 |
| 5 | 应急灯照亮黑板 | 1536 | normal | 37.0 | 0 |  | 1 |
| 6 | 应急灯投下影子 | 1426 | normal | 36.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 2 句（如「你已经浪费了太多时间…」）
- 第 4 章：
  - 单条套路句式超限：「”王小雨低」×3、「王小雨的」×3
- 第 5 章：
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「李国强站在」×3、「王小雨点」×3
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）
  - [observe] 标题重复：「应急灯投下影子」已存在

## 整书结构指标

```
chapters: 6
total_chars: 7130
chapter_chars_mean: 1188
chapter_chars_median: 1227
chapter_chars_cv: 0.19
paragraphs_mean: 36.3
dialogue_chars_pct: 19.5
dialogue_para_pct: 48.2
interiority_para_pct: 0.7
narration_para_pct: 51.1
turn_under20_pct: 97.0
turn_over200_pct: 0.0
attr_say_pct: 65.2
attr_adv_pct: 7.8
scenes_per_chapter: 2
dialogue_run_mean: 1.6
turn_len_median: 10
```
