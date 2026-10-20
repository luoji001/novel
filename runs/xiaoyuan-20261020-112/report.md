# 灯灭 生成报告

slug：`xiaoyuan-20261020-112`
档位：校园青春　闸门模式：observe
章数：9　总字数：19942
LLM 调用：100 次，累计 428.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 粉笔灰落在肩头 | 1744 | short | 80.2 | 0 |  | 2 |
| 2 | 粉笔擦蹭过黑板 | 2213 | normal | 94.9 | 0 |  | 2 |
| 3 | 磁带滑落桌面 | 2602 | normal | 91.0 | 0 |  | 2 |
| 4 | 袖口的粉笔灰痕迹 | 2528 | normal | 91.5 | 0 |  | 1 |
| 5 | 收音机的电流声 | 2197 | normal | 92.7 | 0 |  | 1 |
| 6 | 志愿表的空白页 | 2214 | normal | 90.3 | 0 |  | 1 |
| 7 | 分科表的折痕 | 2368 | normal | 91.3 | 0 |  | 1 |
| 8 | 课表的错位 | 2428 | normal | 93.1 | 0 |  | 2 |
| 9 | 分科表的折痕 | 1639 | short | 89.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.0 低于目标 20.0
  - [observe] 章内自我复读 28 句（如「苏念安则不自觉地调整了一下收音机的位置，似乎想要…」）
- 第 2 章：
  - 单条套路句式超限：「知道自己」×3、「林子墨的」×3
  - narration_para_pct 11.9 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「林子墨的」×3
  - [observe] attr_adv_pct 50.0 > 22.0（结构塌缩）
- 第 4 章：
  - narration_para_pct 5.8 低于目标 15.0
- 第 5 章：
  - [observe] attr_adv_pct 30.0 > 22.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「苏念安的」×3
- 第 7 章：
  - 单条套路句式超限：「苏念安的」×4
- 第 8 章：
  - 单条套路句式超限：「苏念安的」×4
  - [observe] 章内自我复读 2 句（如「你知道自己有多在意这份工作…」）
- 第 9 章：
  - 单条套路句式超限：「林子墨的」×4
  - [observe] 标题重复：「分科表的折痕」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19018
chapter_chars_mean: 2113
chapter_chars_median: 2121
chapter_chars_cv: 0.15
paragraphs_mean: 42.3
dialogue_chars_pct: 28.7
dialogue_para_pct: 68.2
interiority_para_pct: 14.2
narration_para_pct: 17.6
turn_under20_pct: 81.7
turn_over200_pct: 0.0
attr_say_pct: 34.7
attr_adv_pct: 10.9
scenes_per_chapter: 2.4
dialogue_run_mean: 4.0
turn_len_median: 12
```
