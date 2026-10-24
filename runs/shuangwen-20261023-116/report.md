# 旧契书 生成报告

slug：`shuangwen-20261023-116`
档位：爽文　闸门模式：observe
章数：10　总字数：19641
LLM 调用：97 次，累计 439.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签署契书之争 | 1571 | normal | 99.0 | 0 |  | 3 |
| 2 | 契书对峙印章前 | 1918 | normal | 37.3 | 0 |  | 2 |
| 3 | 契书碎于印章下 | 2071 | normal | 93.4 | 0 |  | 2 |
| 4 | 印章压契书 | 1977 | normal | 92.0 | 0 |  | 2 |
| 5 | 契书对峙印章前 | 1917 | normal | 93.0 | 0 |  | 4 |
| 6 | 契书对峙印章前 | 1987 | normal | 93.9 | 0 |  | 2 |
| 7 | 契书落笔时 | 2010 | normal | 90.4 | 0 |  | 1 |
| 8 | 签字权的争夺 | 1822 | normal | 91.4 | 0 |  | 1 |
| 9 | 契书飘落纸纷飞 | 1978 | normal | 90.0 | 0 |  | 0 |
| 10 | 契书入废纸篓 | 2380 | long | 92.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王小梅的」×3
  - narration_para_pct 4.2 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「王小梅的」×4
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「王小梅的」×3
  - attr_adv_pct 25.0 高于目标 12.0
- 第 4 章：
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 15.5 高于目标 14.0
- 第 5 章：
  - 单条套路句式超限：「李建国的」×4、「王小梅的」×3
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「契书对峙印章前」已存在
- 第 6 章：
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「契书对峙印章前」已存在
- 第 7 章：
  - 单条套路句式超限：「李建国的」×5、「王小梅的」×3
- 第 8 章：
  - attr_adv_pct 14.3 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「李建国的」×5
  - narration_para_pct 4.5 低于目标 5.0

## 整书结构指标

```
chapters: 10
total_chars: 18785
chapter_chars_mean: 1878
chapter_chars_median: 1895
chapter_chars_cv: 0.1
paragraphs_mean: 35.1
dialogue_chars_pct: 46.0
dialogue_para_pct: 85.4
interiority_para_pct: 5.9
narration_para_pct: 8.7
turn_under20_pct: 59.1
turn_over200_pct: 0.0
attr_say_pct: 16.9
attr_adv_pct: 13.1
scenes_per_chapter: 1.6
dialogue_run_mean: 8.7
turn_len_median: 16
```
