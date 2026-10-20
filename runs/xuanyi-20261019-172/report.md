# 小红的登录记录 生成报告

slug：`xuanyi-20261019-172`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15195
LLM 调用：68 次，累计 230.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 小红的登录时间 | 2158 | short | 97.0 | 0 |  | 0 |
| 2 | 账单边缘的标记 | 4030 | normal | 89.0 | 0 |  | 2 |
| 3 | 照片背面的文字 | 3516 | normal | 90.9 | 0 |  | 2 |
| 4 | U盘插入口的温度 | 3632 | normal | 88.3 | 0 |  | 4 |
| 5 | 路由器连接未知节点 | 1854 | short | 93.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「陈志远的」×12、「为什么会」×4、「林海点了点头」×3
  - [observe] 章内自我复读 18 句（如「陈老板，”他转过身，直视着对方的眼睛，“你说说，…」）
- 第 3 章：
  - 单条套路句式超限：「陈志远的」×7、「“这是什么」×3
  - narration_para_pct 9.8 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×5、「他知道这」×4
  - narration_para_pct 13.0 低于目标 20.0
  - attr_adv_pct 19.2 高于目标 10.0
  - [observe] 章内自我复读 19 句（如「林海缓缓说道，语气中透着一种不容忽视的冷静，“就…」）
- 第 5 章：
  - narration_para_pct 6.9 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14386
chapter_chars_mean: 2877
chapter_chars_median: 3317
chapter_chars_cv: 0.32
paragraphs_mean: 64
dialogue_chars_pct: 41.3
dialogue_para_pct: 76.7
interiority_para_pct: 7.0
narration_para_pct: 16.2
turn_under20_pct: 67.9
turn_over200_pct: 0.0
attr_say_pct: 28.3
attr_adv_pct: 8.5
scenes_per_chapter: 3
dialogue_run_mean: 4.8
turn_len_median: 14
```
