# 铜钥 生成报告

slug：`xuanyi-20261019-99`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14861
LLM 调用：68 次，累计 242.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的空白收据 | 1667 | short | 97.5 | 0 |  | 1 |
| 2 | 铜钥匙上的刻痕 | 3902 | normal | 90.6 | 0 |  | 3 |
| 3 | 铜钥匙开箱瞬间 | 3761 | normal | 92.3 | 0 |  | 3 |
| 4 | 泛黄汇款单飘落 | 3672 | normal | 89.6 | 0 |  | 3 |
| 5 | 存折翻动的声响 | 1854 | short | 92.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 17.2 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈阿婆的」×5、「他知道自己」×3、「林阿福的」×3
  - narration_para_pct 13.1 低于目标 20.0
  - [observe] 章内自我复读 22 句（如「陈阿婆叹了口气，从抽屉里拿出一把生锈的铜钥匙，递…」）
- 第 3 章：
  - 单条套路句式超限：「林阿福的」×9、「陈阿婆的」×5、「他知道这」×4
  - narration_para_pct 16.7 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「林阿福的」×3
  - narration_para_pct 16.9 低于目标 20.0
  - [observe] attr_adv_pct 27.3 > 20.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「林阿福的」×4、「他知道这」×3、「为什么会」×3
  - narration_para_pct 5.9 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14140
chapter_chars_mean: 2828
chapter_chars_median: 3479
chapter_chars_cv: 0.37
paragraphs_mean: 64
dialogue_chars_pct: 35.2
dialogue_para_pct: 72.4
interiority_para_pct: 13.1
narration_para_pct: 14.5
turn_under20_pct: 79.1
turn_over200_pct: 0.0
attr_say_pct: 22.2
attr_adv_pct: 15.0
scenes_per_chapter: 2.4
dialogue_run_mean: 3.7
turn_len_median: 12
```
