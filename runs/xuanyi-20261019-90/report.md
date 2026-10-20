# 十四分钟 生成报告

slug：`xuanyi-20261019-90`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14959
LLM 调用：68 次，累计 228.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 车窗上的指纹 | 1809 | short | 84.1 | 0 |  | 2 |
| 2 | 屏幕上的空白时刻 | 3552 | normal | 90.8 | 0 |  | 3 |
| 3 | 纸片上的十四分钟 | 4124 | normal | 80.3 | 0 |  | 2 |
| 4 | 手指摩挲纸边 | 3519 | normal | 90.4 | 0 |  | 2 |
| 5 | 摩挲手机边缘 | 1950 | short | 92.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林婉如的」×3
  - dialogue_chars_pct 10.5 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈志远的」×7、「陈志远站在」×5、「林婉如的」×3
  - narration_para_pct 10.6 低于目标 20.0
  - attr_adv_pct 10.7 高于目标 10.0
- 第 3 章：
  - dialogue_chars_pct 14.8 低于目标 20.0
  - [observe] 章内自我复读 12 句（如「他小心翼翼地把它抽出来，展开一看，上面歪歪扭扭地…」）
- 第 4 章：
  - 单条套路句式超限：「林婉如的」×5、「”林婉如轻」×4、「陈志远站在」×3
  - narration_para_pct 9.6 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×4、「林婉如的」×3
  - narration_para_pct 12.2 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14295
chapter_chars_mean: 2859
chapter_chars_median: 3339
chapter_chars_cv: 0.35
paragraphs_mean: 58.2
dialogue_chars_pct: 34.7
dialogue_para_pct: 69.8
interiority_para_pct: 11.7
narration_para_pct: 18.4
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 22.9
attr_adv_pct: 6.5
scenes_per_chapter: 5
dialogue_run_mean: 4.8
turn_len_median: 14
```
