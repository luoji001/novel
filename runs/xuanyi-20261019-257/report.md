# 面单的模糊痕迹 生成报告

slug：`xuanyi-20261019-257`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15821
LLM 调用：68 次，累计 239.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 数据流中的异常信号 | 1895 | short | 99.0 | 0 |  | 1 |
| 2 | 扫描枪的绿光 | 3422 | normal | 93.4 | 0 |  | 3 |
| 3 | 数据流中的特殊编码 | 4028 | normal | 91.1 | 0 |  | 4 |
| 4 | 警报器突然鸣响 | 4321 | normal | 87.7 | 0 |  | 3 |
| 5 | 包裹3238的异常轨迹 | 2150 | short | 91.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周晓芸的」×3
- 第 2 章：
  - 单条套路句式超限：「林嘉文的」×9、「周晓芸的」×7、「周晓芸点」×3
  - narration_para_pct 9.0 低于目标 20.0
  - attr_adv_pct 13.8 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「林嘉文点点」×3、「说道“我」×3、「周晓芸的」×3
  - narration_para_pct 8.1 低于目标 20.0
  - attr_adv_pct 15.6 高于目标 10.0
  - [observe] 章内自我复读 2 句（如「男人若有所思地说，“也许我们能更快找到答案…」）
- 第 4 章：
  - 单条套路句式超限：「周晓芸点」×5、「“我不知道」×4、「”周晓芸轻」×3
  - narration_para_pct 8.8 低于目标 20.0
  - attr_adv_pct 13.7 高于目标 10.0
- 第 5 章：
  - attr_adv_pct 18.8 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14915
chapter_chars_mean: 2983
chapter_chars_median: 3249
chapter_chars_cv: 0.35
paragraphs_mean: 81.6
dialogue_chars_pct: 49.8
dialogue_para_pct: 82.9
interiority_para_pct: 3.3
narration_para_pct: 13.9
turn_under20_pct: 78.9
turn_over200_pct: 0.0
attr_say_pct: 34.7
attr_adv_pct: 13.2
scenes_per_chapter: 4.8
dialogue_run_mean: 6.2
turn_len_median: 12
```
