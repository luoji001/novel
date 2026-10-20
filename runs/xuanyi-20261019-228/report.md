# 水表反向旋转 生成报告

slug：`xuanyi-20261019-228`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15183
LLM 调用：68 次，累计 245.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表背面凹痕 | 1842 | short | 81.1 | 0 |  | 2 |
| 2 | 账本里的陌生日期 | 3921 | normal | 89.7 | 0 |  | 4 |
| 3 | 收音机调频异常 | 3549 | normal | 25.7 | 0 |  | 1 |
| 4 | 触摸木桌凹痕 | 3893 | normal | 80.6 | 0 |  | 5 |
| 5 | 电闸开关的温度 | 1973 | short | 91.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 13.6 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「他喃喃道，目光落在水表上那串新鲜的数字，“按理说…」）
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈志远站在」×4、「“我不知道」×3、「环顾四周」×3
  - narration_para_pct 15.7 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「房间里的灯光忽明忽暗，墙面上挂了一个生锈的铁皮水…」）
- 第 3 章：
  - dialogue_chars_pct 9.6 低于目标 20.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「环顾四周」×5、「陈志远的」×4、「他知道这」×3
  - dialogue_chars_pct 15.3 低于目标 20.0
  - interiority_para_pct 20.9 高于目标 20.0
  - [observe] 章内自我复读 14 句（如「他站起来，脚步轻快地走向门口，回头看了眼桌面的那…」）
- 第 5 章：
  - 单条套路句式超限：「林婉如的」×3
  - narration_para_pct 13.6 低于目标 20.0
  - attr_adv_pct 13.3 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14556
chapter_chars_mean: 2911
chapter_chars_median: 3428
chapter_chars_cv: 0.34
paragraphs_mean: 54.8
dialogue_chars_pct: 21.2
dialogue_para_pct: 54.7
interiority_para_pct: 15.5
narration_para_pct: 29.8
turn_under20_pct: 87.9
turn_over200_pct: 0.0
attr_say_pct: 17.8
attr_adv_pct: 6.3
scenes_per_chapter: 4.4
dialogue_run_mean: 3.7
turn_len_median: 11
```
