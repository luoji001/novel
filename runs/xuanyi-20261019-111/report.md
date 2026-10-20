# 铜钥 生成报告

slug：`xuanyi-20261019-111`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13963
LLM 调用：68 次，累计 242.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 新锁的暗红光泽 | 1771 | short | 100.0 | 0 |  | 1 |
| 2 | 摩挲账本的指尖 | 3569 | normal | 92.7 | 0 |  | 3 |
| 3 | 摩挲铜钥匙的指尖 | 3430 | normal | 89.1 | 0 |  | 5 |
| 4 | 摩挲支票的指尖 | 3416 | normal | 92.0 | 0 |  | 3 |
| 5 | 摩挲铜钥匙的指纹 | 1772 | short | 92.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 5.7 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈慕云的」×6、「周怀瑾的」×5
  - narration_para_pct 12.2 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×4、「沈慕云的」×4
  - narration_para_pct 5.9 低于目标 20.0
  - [observe] 章内自我复读 7 句（如「而且，这个钥匙的形状和以前不一样，它更宽一些，上…」）
  - [observe] attr_adv_pct 26.1 > 20.0（结构塌缩）
  - [observe] 标题与《摩挲账本的指尖》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「周怀瑾的」×7、「沈慕云的」×4
  - narration_para_pct 14.3 低于目标 20.0
  - [observe] 标题与《摩挲账本的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「周怀瑾的」×5
  - narration_para_pct 14.7 低于目标 20.0
  - [observe] 标题与《摩挲铜钥匙的指尖》近似 0.88 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13276
chapter_chars_mean: 2655
chapter_chars_median: 3244
chapter_chars_cv: 0.33
paragraphs_mean: 58.2
dialogue_chars_pct: 44.6
dialogue_para_pct: 83.0
interiority_para_pct: 6.3
narration_para_pct: 10.7
turn_under20_pct: 73.9
turn_over200_pct: 0.0
attr_say_pct: 20.7
attr_adv_pct: 9.2
scenes_per_chapter: 2.6
dialogue_run_mean: 7.1
turn_len_median: 14
```
