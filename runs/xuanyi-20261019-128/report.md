# 水表 生成报告

slug：`xuanyi-20261019-128`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15070
LLM 调用：68 次，累计 238.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表停滞不动 | 1957 | short | 49.6 | 0 |  | 3 |
| 2 | 擦拭桌角油渍 | 3801 | normal | 51.7 | 0 |  | 3 |
| 3 | 电表数字反常 | 3542 | normal | 87.3 | 0 |  | 4 |
| 4 | 螺丝刀与齿轮秘密 | 4010 | normal | 88.6 | 0 |  | 3 |
| 5 | 手机充电器疑云 | 1755 | short | 88.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 5.9 低于目标 20.0
  - interiority_para_pct 46.4 高于目标 20.0
  - dialogue_run_mean 1 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「王建国的」×5、「他知道自己」×3
  - interiority_para_pct 25.8 高于目标 20.0
  - narration_para_pct 15.2 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「王建国的」×6、「说道“你」×4、「他知道这」×3
  - narration_para_pct 11.3 低于目标 20.0
  - attr_adv_pct 10.5 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「每个月15号，电费单都会送到这里…」）
- 第 4 章：
  - 单条套路句式超限：「王建国的」×7、「点了点头」×3
  - narration_para_pct 9.0 低于目标 20.0
  - attr_adv_pct 12.1 高于目标 10.0
- 第 5 章：
  - 命中套话收尾句
  - narration_para_pct 12.5 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14457
chapter_chars_mean: 2891
chapter_chars_median: 3422
chapter_chars_cv: 0.35
paragraphs_mean: 53.6
dialogue_chars_pct: 31.5
dialogue_para_pct: 67.4
interiority_para_pct: 19.0
narration_para_pct: 13.6
turn_under20_pct: 68.9
turn_over200_pct: 0.0
attr_say_pct: 18.6
attr_adv_pct: 5.7
scenes_per_chapter: 4.4
dialogue_run_mean: 4.3
turn_len_median: 14
```
