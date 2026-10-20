# 蓝布未拆 生成报告

slug：`xuanyi-20261019-94`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13837
LLM 调用：68 次，累计 229.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 蓝布摩擦 | 1808 | short | 98.8 | 0 |  | 2 |
| 2 | 账本潮湿痕迹 | 3430 | normal | 91.8 | 0 |  | 3 |
| 3 | 蓝布摩擦 | 3419 | normal | 90.7 | 0 |  | 4 |
| 4 | 纸条褪色 | 3220 | normal | 90.1 | 0 |  | 4 |
| 5 | 布料异常光泽 | 1955 | short | 60.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈德昌的」×4、「周玉兰的」×3
  - narration_para_pct 8.3 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「供销社」×25、「周玉兰的」×4、「“我不知道」×3
  - narration_para_pct 6.9 低于目标 20.0
  - attr_adv_pct 13.0 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「陈德昌的」×7、「周玉兰的」×5、「为什么会」×5
  - narration_para_pct 12.5 低于目标 20.0
  - [observe] attr_adv_pct 30.0 > 20.0（结构塌缩）
  - [observe] 标题重复：「蓝布摩擦」已存在
- 第 4 章：
  - 单条套路句式超限：「供销社」×9、「“我不知道」×3、「”周玉兰轻」×3
  - narration_para_pct 9.6 低于目标 20.0
  - attr_adv_pct 10.5 高于目标 10.0
  - dialogue_run_mean 10.8 高于目标 10.0
- 第 5 章：
  - dialogue_chars_pct 9.5 低于目标 20.0
  - interiority_para_pct 33.3 高于目标 20.0
  - dialogue_run_mean 1.3 低于目标 1.5

## 整书结构指标

```
chapters: 5
total_chars: 13186
chapter_chars_mean: 2637
chapter_chars_median: 3062
chapter_chars_cv: 0.29
paragraphs_mean: 58.2
dialogue_chars_pct: 42.5
dialogue_para_pct: 77.6
interiority_para_pct: 9.0
narration_para_pct: 13.3
turn_under20_pct: 76.3
turn_over200_pct: 0.0
attr_say_pct: 27.4
attr_adv_pct: 13.1
scenes_per_chapter: 3.4
dialogue_run_mean: 6.9
turn_len_median: 12
```
