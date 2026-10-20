# 显影液 生成报告

slug：`xuanyi-20261019-81`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15033
LLM 调用：68 次，累计 230.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显影液中的合影 | 1868 | short | 67.9 | 0 |  | 3 |
| 2 | 显影液中的合影 | 3867 | normal | 91.4 | 0 |  | 3 |
| 3 | 翻开账本的瞬间 | 3627 | normal | 82.8 | 0 |  | 3 |
| 4 | 火车票与旧信纸 | 3825 | normal | 91.4 | 0 |  | 3 |
| 5 | 按下圆钮的刹那 | 1841 | short | 79.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈志远的」×3
  - dialogue_chars_pct 5.2 低于目标 20.0
  - interiority_para_pct 27.3 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周婉秋的」×5、「“我不知道」×3
  - narration_para_pct 19.0 低于目标 20.0
  - [observe] 标题重复：「显影液中的合影」已存在
- 第 3 章：
  - 单条套路句式超限：「心中充满了疑惑」×3、「他知道这」×3、「沈志远的」×3
  - dialogue_chars_pct 15.7 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「他皱眉，抬手拨动桌面上的小灯开关，光线稍微昏暗了…」）
- 第 4 章：
  - 单条套路句式超限：「周婉秋的」×7、「沈志远的」×4、「“我不知道」×3
  - narration_para_pct 7.6 低于目标 20.0
  - [observe] attr_adv_pct 23.1 > 20.0（结构塌缩）
- 第 5 章：
  - dialogue_chars_pct 13.4 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「他摸索着相机侧面的小机关，猛地按下了一颗圆钮，没…」）

## 整书结构指标

```
chapters: 5
total_chars: 14377
chapter_chars_mean: 2875
chapter_chars_median: 3456
chapter_chars_cv: 0.35
paragraphs_mean: 57.6
dialogue_chars_pct: 23.2
dialogue_para_pct: 62.7
interiority_para_pct: 14.4
narration_para_pct: 22.9
turn_under20_pct: 88.6
turn_over200_pct: 0.0
attr_say_pct: 25.6
attr_adv_pct: 9.9
scenes_per_chapter: 4
dialogue_run_mean: 3.3
turn_len_median: 10
```
