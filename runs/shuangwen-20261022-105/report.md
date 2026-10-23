# 破本 生成报告

slug：`shuangwen-20261022-105`
档位：爽文　闸门模式：observe
章数：10　总字数：19183
LLM 调用：97 次，累计 426.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的重量 | 1769 | normal | 97.5 | 0 |  | 2 |
| 2 | 文件上的签名笔迹 | 2085 | normal | 90.7 | 0 |  | 1 |
| 3 | 签字笔的重量 | 1748 | normal | 91.2 | 0 |  | 2 |
| 4 | 纸张的脆响 | 1779 | normal | 92.8 | 0 |  | 2 |
| 5 | 工龄证明的重量 | 1994 | normal | 89.7 | 0 |  | 2 |
| 6 | 记录本的翻页声 | 2153 | normal | 34.6 | 0 |  | 4 |
| 7 | 教学记录本的翻页声 | 1829 | normal | 89.5 | 0 |  | 3 |
| 8 | 纸张的脆响 | 1634 | normal | 91.4 | 0 |  | 2 |
| 9 | 一叠泛黄的合同复印件 | 2057 | normal | 93.3 | 0 |  | 1 |
| 10 | 翻阅教学记录本 | 2125 | long | 93.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈志远的」×3
  - attr_adv_pct 18.2 高于目标 12.0
- 第 2 章：
  - attr_adv_pct 25.0 高于目标 12.0
- 第 3 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 4 章：
  - narration_para_pct 4.0 低于目标 5.0
  - attr_adv_pct 15.4 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「林婉秋的」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 6 章：
  - narration_para_pct 1.9 低于目标 5.0
  - dialogue_run_mean 26.5 高于目标 14.0
  - [observe] 章内自我复读 2 句（如「谢谢你给了我这个机会…」）
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「林婉秋的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - [observe] 标题与《记录本的翻页声》近似 0.88 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「陈志远的」×4、「微微一笑」×3
  - [observe] 标题重复：「纸张的脆响」已存在
- 第 9 章：
  - 单条套路句式超限：「陈志远的」×6
- 第 10 章：
  - 单条套路句式超限：「说道“我」×3
  - dialogue_run_mean 14.3 高于目标 14.0
  - [observe] 标题与《教学记录本的翻页声》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18317
chapter_chars_mean: 1832
chapter_chars_median: 1824
chapter_chars_cv: 0.09
paragraphs_mean: 35.3
dialogue_chars_pct: 49.9
dialogue_para_pct: 85.2
interiority_para_pct: 5.1
narration_para_pct: 9.8
turn_under20_pct: 60.2
turn_over200_pct: 0.0
attr_say_pct: 29.3
attr_adv_pct: 14.2
scenes_per_chapter: 1.5
dialogue_run_mean: 9.0
turn_len_median: 17
```
