# 行李箱 生成报告

slug：`xuanyi-20261019-183`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13446
LLM 调用：68 次，累计 224.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 行李箱的踪迹 | 1816 | short | 98.5 | 0 |  | 2 |
| 2 | 火车票的追问 | 3191 | normal | 91.9 | 0 |  | 4 |
| 3 | 钥匙上的锈迹 | 3418 | normal | 91.6 | 0 |  | 3 |
| 4 | 登记簿的低语 | 3025 | normal | 91.3 | 0 |  | 3 |
| 5 | 钥匙与箱子的对峙 | 1991 | short | 91.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - attr_adv_pct 20.0 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「周小曼的」×5、「林振邦站在」×4、「他知道这」×3
  - narration_para_pct 17.4 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「林振邦盯着她的眼睛，试图从中看出些什么…」）
  - [observe] attr_adv_pct 23.8 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×6、「周小曼的」×4
  - narration_para_pct 16.2 低于目标 20.0
  - attr_adv_pct 10.5 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「林振邦的」×5、「“我不知道」×3、「他知道这」×3
  - narration_para_pct 16.7 低于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0
- 第 5 章：
  - narration_para_pct 8.5 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「所以你就把它藏起来了？…」）

## 整书结构指标

```
chapters: 5
total_chars: 12665
chapter_chars_mean: 2533
chapter_chars_median: 2879
chapter_chars_cv: 0.27
paragraphs_mean: 70.4
dialogue_chars_pct: 36.8
dialogue_para_pct: 75.5
interiority_para_pct: 7.2
narration_para_pct: 17.3
turn_under20_pct: 83.5
turn_over200_pct: 0.0
attr_say_pct: 23.7
attr_adv_pct: 15.2
scenes_per_chapter: 5.6
dialogue_run_mean: 5.3
turn_len_median: 10
```
