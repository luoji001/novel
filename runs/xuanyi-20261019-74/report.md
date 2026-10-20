# 空单 生成报告

slug：`xuanyi-20261019-74`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14545
LLM 调用：68 次，累计 234.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的五米差 | 1913 | short | 99.1 | 0 |  | 0 |
| 2 | 蓝布的缺口 | 3766 | normal | 91.4 | 0 |  | 2 |
| 3 | 蓝布的缺口 | 3520 | normal | 90.5 | 0 |  | 4 |
| 4 | 铜印章的裂痕 | 3466 | normal | 90.1 | 0 |  | 3 |
| 5 | 纸上的空白栏位 | 1875 | short | 92.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「陈国栋的」×4、「陈国栋点」×3、「周素云的」×3
  - attr_adv_pct 12.1 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「周素云的」×4、「陈国栋的」×3
  - narration_para_pct 14.5 低于目标 20.0
  - attr_adv_pct 15.8 高于目标 10.0
  - [observe] 标题重复：「蓝布的缺口」已存在
- 第 4 章：
  - 单条套路句式超限：「周素云的」×7、「陈国栋的」×3
  - narration_para_pct 11.1 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 5 章：
  - narration_para_pct 2.5 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13834
chapter_chars_mean: 2767
chapter_chars_median: 3308
chapter_chars_cv: 0.32
paragraphs_mean: 63.6
dialogue_chars_pct: 39.9
dialogue_para_pct: 78.6
interiority_para_pct: 6.0
narration_para_pct: 15.4
turn_under20_pct: 77.3
turn_over200_pct: 0.0
attr_say_pct: 29.8
attr_adv_pct: 10.8
scenes_per_chapter: 3.8
dialogue_run_mean: 5.7
turn_len_median: 12
```
