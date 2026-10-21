# 磁带 生成报告

slug：`xiaoyuan-20261020-24`
档位：校园青春　闸门模式：observe
章数：9　总字数：20124
LLM 调用：100 次，累计 432.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 课表上的名字 | 1421 | short | 78.5 | 0 |  | 4 |
| 2 | 磁带的温度 | 2732 | normal | 30.0 | 0 |  | 2 |
| 3 | 遥控器的按钮 | 2361 | normal | 88.9 | 0 |  | 3 |
| 4 | 公告栏的红线 | 2081 | normal | 93.8 | 0 |  | 2 |
| 5 | 磁带的温度 | 2706 | normal | 84.0 | 0 |  | 5 |
| 6 | 分科表的褶皱 | 2141 | normal | 91.7 | 0 |  | 2 |
| 7 | 粉笔灰落在纸条上 | 2460 | normal | 91.4 | 0 |  | 2 |
| 8 | 纸条上的字迹 | 2615 | normal | 85.4 | 0 |  | 2 |
| 9 | 纸条上的字迹 | 1598 | short | 92.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「”周子航轻」×3
  - dialogue_chars_pct 14.7 低于目标 20.0
  - narration_para_pct 8.7 低于目标 15.0
  - [observe] 章内自我复读 15 句（如「林小满低头看着自己的课表，上面写着“周子航”三个…」）
- 第 2 章：
  - 单条套路句式超限：「周子航的」×3
  - dialogue_chars_pct 11.6 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「林小满站在」×3
  - narration_para_pct 13.5 低于目标 15.0
  - [observe] 章内自我复读 13 句（如「周子航点点头，手指依然停留在遥控器上，声音低得几…」）
- 第 4 章：
  - 单条套路句式超限：「林小满的」×3
  - [observe] attr_adv_pct 28.6 > 22.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「周子航点」×4、「点了点头」×3
  - dialogue_chars_pct 19.1 低于目标 20.0
  - attr_adv_pct 13.6 高于目标 12.0
  - [observe] 章内自我复读 34 句（如「她坐下，拿出磁带，放在耳边轻轻一听，熟悉的旋律流…」）
  - [observe] 标题重复：「磁带的温度」已存在
- 第 6 章：
  - 单条套路句式超限：「林小满的」×3
  - narration_para_pct 14.0 低于目标 15.0
- 第 7 章：
  - 单条套路句式超限：「林小满的」×5、「周子航的」×4
  - narration_para_pct 13.5 低于目标 15.0
- 第 8 章：
  - 单条套路句式超限：「周子航的」×3
  - dialogue_chars_pct 15.2 低于目标 20.0
- 第 9 章：
  - 单条套路句式超限：「周子航的」×3
  - [observe] attr_adv_pct 33.3 > 22.0（结构塌缩）
  - [observe] 标题重复：「纸条上的字迹」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19179
chapter_chars_mean: 2131
chapter_chars_median: 2243
chapter_chars_cv: 0.21
paragraphs_mean: 45
dialogue_chars_pct: 21.4
dialogue_para_pct: 65.7
interiority_para_pct: 15.3
narration_para_pct: 19.0
turn_under20_pct: 91.2
turn_over200_pct: 0.0
attr_say_pct: 28.9
attr_adv_pct: 10.5
scenes_per_chapter: 2.6
dialogue_run_mean: 3.5
turn_len_median: 9
```
