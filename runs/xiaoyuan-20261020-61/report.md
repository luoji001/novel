# 橡皮的痕迹 生成报告

slug：`xiaoyuan-20261020-61`
档位：校园青春　闸门模式：observe
章数：9　总字数：21714
LLM 调用：100 次，累计 463.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触碰笔记的指尖 | 1301 | short | 83.9 | 0 |  | 3 |
| 2 | 触碰笔记的指尖 | 3011 | normal | 88.4 | 0 |  | 3 |
| 3 | 橡皮的裂痕 | 2234 | normal | 94.2 | 0 |  | 3 |
| 4 | 橡皮的裂痕 | 2596 | normal | 92.6 | 0 |  | 2 |
| 5 | 橡皮的裂痕 | 2836 | normal | 92.3 | 0 |  | 4 |
| 6 | 磁带的触碰 | 2777 | normal | 93.0 | 0 |  | 1 |
| 7 | 粉笔画的裂痕 | 2815 | normal | 86.1 | 0 |  | 3 |
| 8 | 磁带的触碰 | 2548 | normal | 90.1 | 0 |  | 4 |
| 9 | 触摸分科表的指尖 | 1587 | short | 87.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林小满的」×3
  - dialogue_chars_pct 16.5 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「陈老师抱着一摞作业走进走廊，看见两个人站着的样子…」）
- 第 2 章：
  - 单条套路句式超限：「林小满的」×11、「周远舟的」×5
  - [observe] 章内自我复读 18 句（如「她闭上眼睛，听着那些熟悉的旋律，仿佛看到了一个遥…」）
  - [observe] 标题重复：「触碰笔记的指尖」已存在
- 第 3 章：
  - 单条套路句式超限：「周远舟的」×4
  - narration_para_pct 14.6 低于目标 15.0
  - [observe] attr_adv_pct 41.7 > 22.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「”林小满低」×3、「林小满的」×3
  - [observe] 标题重复：「橡皮的裂痕」已存在
- 第 5 章：
  - 单条套路句式超限：「林小满的」×8、「周远舟的」×3
  - narration_para_pct 11.3 低于目标 15.0
  - [observe] 章内自我复读 1 句（如「你们两个都在这儿啊？…」）
  - [observe] 标题重复：「橡皮的裂痕」已存在
- 第 6 章：
  - narration_para_pct 11.5 低于目标 15.0
- 第 7 章：
  - 单条套路句式超限：「林小满点」×3
  - interiority_para_pct 7.5 低于目标 8.0
  - [observe] 章内自我复读 25 句（如「林小满点了点头，目光落在公告栏下方的一行小字上：…」）
- 第 8 章：
  - 单条套路句式超限：「林小满的」×4、「周远舟的」×3
  - dialogue_chars_pct 18.6 低于目标 20.0
  - narration_para_pct 14.9 低于目标 15.0
  - [observe] 标题重复：「磁带的触碰」已存在
- 第 9 章：
  - 单条套路句式超限：「周远舟的」×5、「周远舟站在」×3
  - [observe] 章内自我复读 15 句（如「周远舟的目光也落在上面，像是第一次仔细看清那些名…」）

## 整书结构指标

```
chapters: 9
total_chars: 20657
chapter_chars_mean: 2295
chapter_chars_median: 2479
chapter_chars_cv: 0.25
paragraphs_mean: 51.2
dialogue_chars_pct: 25.0
dialogue_para_pct: 69.2
interiority_para_pct: 13.5
narration_para_pct: 17.3
turn_under20_pct: 89.0
turn_over200_pct: 0.0
attr_say_pct: 24.6
attr_adv_pct: 7.5
scenes_per_chapter: 2.2
dialogue_run_mean: 4.1
turn_len_median: 9
```
