# 课表上的空白 生成报告

slug：`xiaoyuan-20261020-153`
档位：校园青春　闸门模式：observe
章数：9　总字数：21659
LLM 调用：100 次，累计 459.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 递订单的塑料袋 | 1376 | short | 96.9 | 0 |  | 1 |
| 2 | 触碰的落叶 | 2950 | normal | 93.7 | 0 |  | 2 |
| 3 | 触碰的落叶 | 2703 | normal | 90.9 | 0 |  | 3 |
| 4 | 磁带放入机器 | 2837 | normal | 89.7 | 0 |  | 4 |
| 5 | 课表上的空白 | 2300 | normal | 89.6 | 0 |  | 1 |
| 6 | 触碰的就诊卡 | 2618 | normal | 89.5 | 0 |  | 1 |
| 7 | 触碰的就诊卡 | 2646 | normal | 87.8 | 0 |  | 3 |
| 8 | 成绩单上的褶痕 | 2643 | normal | 90.3 | 0 |  | 3 |
| 9 | 触碰的课表一角 | 1577 | short | 84.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 33.3 > 22.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周子墨的」×6、「林晓棠站在」×3、「林晓棠点点」×3
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周子墨的」×6、「林晓棠站在」×3
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题重复：「触碰的落叶」已存在
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周子墨的」×5、「“我不知道」×3、「林晓棠点点」×3
  - narration_para_pct 14.1 低于目标 15.0
  - [observe] 章内自我复读 15 句（如「林晓棠看着他微驼的肩膀，想起昨夜整理成绩单的时候…」）
- 第 5 章：
  - dialogue_chars_pct 18.7 低于目标 20.0
- 第 6 章：
  - dialogue_chars_pct 18.1 低于目标 20.0
- 第 7 章：
  - 单条套路句式超限：「周子墨的」×9
  - dialogue_chars_pct 18.0 低于目标 20.0
  - [observe] 标题重复：「触碰的就诊卡」已存在
- 第 8 章：
  - 单条套路句式超限：「周子墨的」×5
  - narration_para_pct 13.6 低于目标 15.0
  - [observe] 章内自我复读 16 句（如「周子墨笑了笑，“那时候你觉得我太吵了，现在想起来…」）
- 第 9 章：
  - 单条套路句式超限：「带着一丝」×3
  - dialogue_chars_pct 14.0 低于目标 20.0
  - [observe] 章内自我复读 3 句（如「她闭上了眼睛，仿佛还能听到那句熟悉的话语，在耳边…」）

## 整书结构指标

```
chapters: 9
total_chars: 20598
chapter_chars_mean: 2289
chapter_chars_median: 2510
chapter_chars_cv: 0.23
paragraphs_mean: 49.9
dialogue_chars_pct: 21.4
dialogue_para_pct: 63.1
interiority_para_pct: 17.4
narration_para_pct: 19.5
turn_under20_pct: 89.6
turn_over200_pct: 0.0
attr_say_pct: 30.8
attr_adv_pct: 10.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.7
turn_len_median: 8
```
