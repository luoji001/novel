# 磁带的重量 生成报告

slug：`xiaoyuan-20261020-109`
档位：校园青春　闸门模式：observe
章数：9　总字数：20367
LLM 调用：100 次，累计 442.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 储物柜里的校服 | 1610 | short | 88.2 | 0 |  | 2 |
| 2 | 摸褶皱的手指 | 2440 | normal | 94.1 | 0 |  | 1 |
| 3 | 磁带盒上的刻字 | 2565 | normal | 15.8 | 0 |  | 1 |
| 4 | 课表上的模糊字迹 | 2586 | normal | 88.0 | 0 |  | 2 |
| 5 | 补袖口的毛线边 | 2595 | normal | 92.4 | 0 |  | 2 |
| 6 | 磁带缓缓转动 | 2714 | normal | 93.0 | 0 |  | 2 |
| 7 | 分科表的裂缝 | 2094 | normal | 92.3 | 0 |  | 2 |
| 8 | 接住一片雪花 | 2329 | normal | 93.0 | 0 |  | 2 |
| 9 | 窗边的画册 | 1425 | short | 87.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 15.1 低于目标 20.0
  - interiority_para_pct 6.1 低于目标 8.0
- 第 2 章：
  - 单条套路句式超限：「周子航的」×4、「带着一丝」×3
- 第 3 章：
  - dialogue_chars_pct 9.9 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「林晓棠的」×5
  - [observe] 章内自我复读 16 句（如「他的目光移回到那份课表上，手指轻轻摩挲着那些模糊…」）
- 第 5 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 章内自我复读 2 句（如「他站起身，手里还握着那张纸，眼睛直视着她的眼睛，…」）
- 第 6 章：
  - narration_para_pct 11.5 低于目标 15.0
  - [observe] attr_adv_pct 22.2 > 22.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「林晓棠的」×3
  - narration_para_pct 14.3 低于目标 15.0
- 第 8 章：
  - narration_para_pct 9.7 低于目标 15.0
  - [observe] 章内自我复读 2 句（如「你还记得我们第一次见面吗？…」）
- 第 9 章：
  - dialogue_chars_pct 19.5 低于目标 20.0
  - narration_para_pct 13.3 低于目标 15.0
  - [observe] 章内自我复读 14 句（如「她记得去年这时候，还有暖气，那时候她总会在画室待…」）

## 整书结构指标

```
chapters: 9
total_chars: 19362
chapter_chars_mean: 2151
chapter_chars_median: 2310
chapter_chars_cv: 0.21
paragraphs_mean: 48.1
dialogue_chars_pct: 23.3
dialogue_para_pct: 65.9
interiority_para_pct: 14.7
narration_para_pct: 19.3
turn_under20_pct: 93.0
turn_over200_pct: 0.0
attr_say_pct: 33.4
attr_adv_pct: 9.3
scenes_per_chapter: 1.8
dialogue_run_mean: 3.7
turn_len_median: 9
```
