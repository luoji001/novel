# 旧清单 生成报告

slug：`shuangwen-20261022-02`
档位：爽文　闸门模式：observe
章数：10　总字数：19938
LLM 调用：97 次，累计 368.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 审批签字 | 1586 | normal | 98.8 | 0 |  | 1 |
| 2 | 一张报表 | 2152 | normal | 89.1 | 0 |  | 2 |
| 3 | 签字笔风波 | 1796 | normal | 93.3 | 0 |  | 1 |
| 4 | 一张旧清单 | 1948 | normal | 91.2 | 0 |  | 1 |
| 5 | 一张旧清单 | 2230 | normal | 91.2 | 0 |  | 2 |
| 6 | 对峙时刻 | 2045 | normal | 36.8 | 0 |  | 2 |
| 7 | 旧清单对峙 | 1962 | normal | 90.1 | 0 |  | 3 |
| 8 | 清单对峙 | 1852 | normal | 91.5 | 0 |  | 1 |
| 9 | 签字笔风波 | 1828 | normal | 90.0 | 0 |  | 2 |
| 10 | 翻出旧清单 | 2529 | long | 91.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李志远的」×3
- 第 2 章：
  - attr_adv_pct 17.4 高于目标 12.0
  - dialogue_run_mean 18.5 高于目标 14.0
- 第 3 章：
  - narration_para_pct 2.6 低于目标 5.0
- 第 4 章：
  - 单条套路句式超限：「李志远的」×3
- 第 5 章：
  - narration_para_pct 4.7 低于目标 5.0
  - [observe] 标题重复：「一张旧清单」已存在
- 第 6 章：
  - narration_para_pct 2.3 低于目标 5.0
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「李志远的」×3
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 标题与《一张旧清单》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - [observe] 标题与《旧清单对峙》近似 0.89 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「签字笔风波」已存在
- 第 10 章：
  - narration_para_pct 4.8 低于目标 5.0
  - [observe] 标题与《旧清单对峙》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 19020
chapter_chars_mean: 1902
chapter_chars_median: 1859
chapter_chars_cv: 0.14
paragraphs_mean: 37.5
dialogue_chars_pct: 55.6
dialogue_para_pct: 88.4
interiority_para_pct: 4.9
narration_para_pct: 6.7
turn_under20_pct: 61.8
turn_over200_pct: 0.0
attr_say_pct: 25.5
attr_adv_pct: 11.7
scenes_per_chapter: 1.9
dialogue_run_mean: 9.3
turn_len_median: 16
```
