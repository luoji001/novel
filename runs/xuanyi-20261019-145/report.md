# 存药 生成报告

slug：`xuanyi-20261019-145`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14290
LLM 调用：68 次，累计 228.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 存储卡读取异常 | 1704 | short | 81.9 | 0 |  | 1 |
| 2 | 登记本上的签名 | 3425 | normal | 92.6 | 0 |  | 3 |
| 3 | 降压药消失的夜晚 | 3751 | normal | 89.8 | 0 |  | 6 |
| 4 | 药品标签的裂痕 | 3371 | normal | 91.1 | 0 |  | 3 |
| 5 | 存储卡插入门缝 | 2034 | short | 85.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 8.7 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林修远的」×6、「”沈婉清轻」×3、「沈婉清的」×3
  - narration_para_pct 12.7 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「林修远点点」×3
  - dialogue_chars_pct 59.3 高于目标 58.0
  - narration_para_pct 16.2 低于目标 20.0
  - attr_adv_pct 16.0 高于目标 10.0
  - dialogue_run_mean 11.6 高于目标 10.0
  - [observe] 章内自我复读 5 句（如「天泽药业代表提议道，“这样才能确保万无一失…」）
- 第 4 章：
  - 单条套路句式超限：「林修远点点」×4、「林修远的」×3
  - narration_para_pct 14.1 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「林修远的」×4
  - dialogue_chars_pct 15.2 低于目标 20.0
  - [observe] attr_adv_pct 60.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13570
chapter_chars_mean: 2714
chapter_chars_median: 3214
chapter_chars_cv: 0.31
paragraphs_mean: 64
dialogue_chars_pct: 36.7
dialogue_para_pct: 71.9
interiority_para_pct: 9.9
narration_para_pct: 18.2
turn_under20_pct: 82.5
turn_over200_pct: 0.0
attr_say_pct: 16.3
attr_adv_pct: 23.7
scenes_per_chapter: 3.8
dialogue_run_mean: 5.4
turn_len_median: 12
```
