# 行李箱 生成报告

slug：`xuanyi-20261019-203`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14414
LLM 调用：68 次，累计 236.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 箱子消失 | 1747 | short | 100.0 | 0 |  | 3 |
| 2 | 记录本被涂改 | 3537 | normal | 92.6 | 0 |  | 2 |
| 3 | 工牌与请假单不符 | 4003 | normal | 91.3 | 0 |  | 3 |
| 4 | 方便面与纸条 | 3319 | normal | 90.0 | 0 |  | 3 |
| 5 | 触摸晾衣绳 | 1803 | short | 92.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林志远的」×3
  - narration_para_pct 15.2 低于目标 20.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「林志远的」×5
  - attr_adv_pct 15.8 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「南方电子厂」×14、「“我不知道」×3、「发现自己」×3
  - narration_para_pct 13.1 低于目标 20.0
  - [observe] 章内自我复读 4 句（如「除了几件衣服外，还有一些不属于她的物品，比如一本…」）
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×4、「苏婉儿的」×3
  - narration_para_pct 11.8 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 5 章：
  - narration_para_pct 11.6 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13740
chapter_chars_mean: 2748
chapter_chars_median: 3169
chapter_chars_cv: 0.36
paragraphs_mean: 60
dialogue_chars_pct: 37.9
dialogue_para_pct: 74.6
interiority_para_pct: 9.0
narration_para_pct: 16.5
turn_under20_pct: 78.1
turn_over200_pct: 0.0
attr_say_pct: 27.6
attr_adv_pct: 12.7
scenes_per_chapter: 5.8
dialogue_run_mean: 5.8
turn_len_median: 12
```
