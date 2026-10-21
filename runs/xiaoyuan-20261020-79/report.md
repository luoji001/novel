# 磁带的重量 生成报告

slug：`xiaoyuan-20261020-79`
档位：校园青春　闸门模式：observe
章数：9　总字数：20896
LLM 调用：100 次，累计 441.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 课表上的墨渍 | 1610 | short | 98.1 | 0 |  | 1 |
| 2 | 纽扣上的字母M | 2745 | normal | 92.5 | 0 |  | 3 |
| 3 | 照片上的座号 | 2365 | normal | 89.7 | 0 |  | 3 |
| 4 | 座位表的折痕 | 2288 | normal | 88.8 | 0 |  | 3 |
| 5 | 麦克风的震颤 | 2489 | normal | 92.1 | 0 |  | 1 |
| 6 | 抹布与磁带 | 2798 | normal | 92.0 | 0 |  | 2 |
| 7 | 脚印的指引 | 2414 | normal | 93.0 | 0 |  | 1 |
| 8 | 作业本上的褶皱 | 2628 | normal | 82.6 | 0 |  | 3 |
| 9 | 磁带的重量 | 1550 | short | 90.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 7.6 低于目标 8.0
- 第 2 章：
  - 单条套路句式超限：「苏晚晴的」×5、「林子墨的」×3
  - narration_para_pct 14.3 低于目标 15.0
  - attr_adv_pct 21.7 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「苏晚晴的」×4、「苏晚晴点」×3
  - interiority_para_pct 7.8 低于目标 8.0
  - [observe] 章内自我复读 17 句（如「她知道，有些事情永远都不会说出来，就像那些藏在书…」）
- 第 4 章：
  - 单条套路句式超限：「林子墨点点」×3、「苏晚晴点」×3
  - narration_para_pct 14.7 低于目标 15.0
  - [observe] 章内自我复读 22 句（如「苏晚晴没有回答，只是轻轻地叹了口气，然后抬起了眼…」）
- 第 5 章：
  - 单条套路句式超限：「苏晚晴的」×3
- 第 6 章：
  - 单条套路句式超限：「苏晚晴的」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「苏晚晴的」×5、「林子墨站在」×3、「他知道这」×3
- 第 8 章：
  - 单条套路句式超限：「苏晚晴的」×9、「林子墨点点」×4
  - dialogue_chars_pct 16.4 低于目标 20.0
  - [observe] 章内自我复读 13 句（如「后来在值日的时候，他们不得不一起打扫教室，虽然什…」）
- 第 9 章：
  - 单条套路句式超限：「苏晚晴的」×5

## 整书结构指标

```
chapters: 9
total_chars: 19748
chapter_chars_mean: 2194
chapter_chars_median: 2269
chapter_chars_cv: 0.21
paragraphs_mean: 56.3
dialogue_chars_pct: 24.6
dialogue_para_pct: 63.5
interiority_para_pct: 13.8
narration_para_pct: 22.7
turn_under20_pct: 92.1
turn_over200_pct: 0.0
attr_say_pct: 20.7
attr_adv_pct: 7.6
scenes_per_chapter: 2.3
dialogue_run_mean: 3.0
turn_len_median: 8
```
