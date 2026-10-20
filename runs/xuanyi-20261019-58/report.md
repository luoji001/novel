# 金线 生成报告

slug：`xuanyi-20261019-58`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15213
LLM 调用：68 次，累计 248.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 金线的消失 | 1778 | short | 99.4 | 0 |  | 2 |
| 2 | 账本的裂痕 | 3622 | normal | 91.9 | 0 |  | 3 |
| 3 | 摩挲银元的纹路 | 3829 | normal | 89.5 | 0 |  | 3 |
| 4 | 金线的异样纹路 | 3776 | normal | 89.4 | 0 |  | 4 |
| 5 | 绣绷上的金线纹路 | 2203 | short | 83.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈怀瑾的」×9
  - narration_para_pct 6.1 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈怀瑾的」×12
  - narration_para_pct 14.1 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「沈怀瑾的」×7、「周砚秋的」×4、「“我不知道」×3
  - narration_para_pct 13.3 低于目标 20.0
  - attr_adv_pct 16.0 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「沈怀瑾的」×9、「周砚秋的」×5、「周砚秋点」×3
  - narration_para_pct 8.4 低于目标 20.0
  - attr_adv_pct 15.4 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「你是不是知道些什么？…」）
- 第 5 章：
  - 单条套路句式超限：「周砚秋的」×5
  - [observe] 章内自我复读 35 句（如「但他很快又注意到了别的地方——那件衣服的袖口上，…」）

## 整书结构指标

```
chapters: 5
total_chars: 14483
chapter_chars_mean: 2897
chapter_chars_median: 3453
chapter_chars_cv: 0.32
paragraphs_mean: 63.6
dialogue_chars_pct: 37.6
dialogue_para_pct: 75.9
interiority_para_pct: 10.7
narration_para_pct: 13.4
turn_under20_pct: 79.1
turn_over200_pct: 0.0
attr_say_pct: 20.8
attr_adv_pct: 13.0
scenes_per_chapter: 4.2
dialogue_run_mean: 4.8
turn_len_median: 12
```
