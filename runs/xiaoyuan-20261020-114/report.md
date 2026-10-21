# 纽扣 生成报告

slug：`xiaoyuan-20261020-114`
档位：校园青春　闸门模式：observe
章数：9　总字数：21077
LLM 调用：100 次，累计 465.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 数学科代表的纽扣 | 1421 | short | 95.8 | 0 |  | 1 |
| 2 | 红笔圈出的物理课 | 2718 | normal | 86.2 | 0 |  | 3 |
| 3 | 纸页上的折痕 | 2557 | normal | 55.0 | 0 |  | 3 |
| 4 | 第三颗纽扣的温度 | 2894 | normal | 86.2 | 0 |  | 2 |
| 5 | 磁带盒里的歌 | 2337 | normal | 89.6 | 0 |  | 1 |
| 6 | 录音机的指示灯 | 2580 | normal | 91.6 | 0 |  | 2 |
| 7 | 擦玻璃的指节 | 2575 | normal | 91.7 | 0 |  | 1 |
| 8 | 分科表的张贴日 | 2550 | normal | 92.0 | 0 |  | 0 |
| 9 | 手指划过报名表边缘 | 1436 | short | 86.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 17.5 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周子航的」×7、「知道自己」×4、「”周子航低」×3
  - [observe] 章内自我复读 33 句（如「她的手指轻轻捏住衣角，想起昨天早上看到的那张体检…」）
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「林晓棠的」×4
  - dialogue_chars_pct 14.6 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「林晓棠站在」×3、「周子航的」×3
  - dialogue_chars_pct 15.3 低于目标 20.0
- 第 5 章：
  - dialogue_chars_pct 18.5 低于目标 20.0
- 第 6 章：
  - 单条套路句式超限：「为什么会」×3
  - interiority_para_pct 7.1 低于目标 8.0
- 第 7 章：
  - attr_adv_pct 14.3 高于目标 12.0
- 第 9 章：
  - dialogue_chars_pct 16.0 低于目标 20.0
  - [observe] 与历史章节逐字重复 3 句（如「林晓棠站在公告栏前，手指轻轻划过报名表上的名字…」）

## 整书结构指标

```
chapters: 9
total_chars: 20126
chapter_chars_mean: 2236
chapter_chars_median: 2449
chapter_chars_cv: 0.23
paragraphs_mean: 44
dialogue_chars_pct: 21.2
dialogue_para_pct: 64.3
interiority_para_pct: 15.2
narration_para_pct: 20.5
turn_under20_pct: 86.4
turn_over200_pct: 0.0
attr_say_pct: 43.1
attr_adv_pct: 8.0
scenes_per_chapter: 2.6
dialogue_run_mean: 2.9
turn_len_median: 9
```
