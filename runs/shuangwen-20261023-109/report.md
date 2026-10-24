# 旧档案的边缘 生成报告

slug：`shuangwen-20261023-109`
档位：爽文　闸门模式：observe
章数：10　总字数：18230
LLM 调用：97 次，累计 419.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧档案的指纹 | 1655 | normal | 98.6 | 0 |  | 2 |
| 2 | 碎纸机的吞吐 | 1691 | normal | 93.8 | 0 |  | 0 |
| 3 | 签字笔的轨迹 | 1740 | normal | 93.5 | 0 |  | 1 |
| 4 | 刻痕的回声 | 1997 | normal | 92.8 | 0 |  | 2 |
| 5 | 旧档案摊开瞬间 | 1789 | normal | 90.9 | 0 |  | 2 |
| 6 | 旧档案的摊开瞬间 | 1735 | normal | 90.2 | 0 |  | 5 |
| 7 | 刻痕的回声 | 2013 | normal | 87.7 | 0 |  | 4 |
| 8 | 旧档案的摊开瞬间 | 1633 | normal | 93.6 | 0 |  | 3 |
| 9 | 旧档案的摊开瞬间 | 1718 | normal | 92.0 | 0 |  | 4 |
| 10 | 签字笔划破名册 | 2249 | long | 93.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「讲经堂」×4
  - attr_adv_pct 12.5 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「讲经堂」×4
- 第 4 章：
  - 单条套路句式超限：「李怀远的」×6、「讲经堂」×5、「陈守仁的」×4
  - attr_adv_pct 20.0 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「陈守仁的」×8、「讲经堂」×5、「李怀远的」×4
  - attr_adv_pct 16.7 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「讲经堂」×5、「李怀远点」×3
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 20 高于目标 14.0
  - [observe] 标题与《旧档案摊开瞬间》近似 0.93 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - dialogue_chars_pct 78.1 高于目标 70.0
  - narration_para_pct 1.4 低于目标 5.0
  - dialogue_run_mean 69 高于目标 14.0
  - [observe] 标题重复：「刻痕的回声」已存在
- 第 8 章：
  - 单条套路句式超限：「讲经堂」×8、「李怀远的」×3
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「旧档案的摊开瞬间」已存在
- 第 9 章：
  - 单条套路句式超限：「讲经堂」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 18 高于目标 14.0
  - [observe] 标题重复：「旧档案的摊开瞬间」已存在
- 第 10 章：
  - 单条套路句式超限：「陈守仁的」×5
  - attr_adv_pct 12.5 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17200
chapter_chars_mean: 1720
chapter_chars_median: 1638
chapter_chars_cv: 0.11
paragraphs_mean: 43.6
dialogue_chars_pct: 50.9
dialogue_para_pct: 84.6
interiority_para_pct: 5.5
narration_para_pct: 9.9
turn_under20_pct: 76.7
turn_over200_pct: 0.0
attr_say_pct: 26.6
attr_adv_pct: 12.9
scenes_per_chapter: 1.6
dialogue_run_mean: 14.5
turn_len_median: 12
```
