# 铜锁 生成报告

slug：`xuanyi-20261019-251`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13880
LLM 调用：68 次，累计 230.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撬棍触锁未开 | 1334 | short | 37.9 | 0 |  | 2 |
| 2 | 登记簿的隐藏标记 | 3949 | normal | 95.2 | 0 |  | 3 |
| 3 | 钥匙的秘密 | 3166 | normal | 90.4 | 0 |  | 2 |
| 4 | 文件夹的异常触感 | 3576 | normal | 91.8 | 0 |  | 1 |
| 5 | 钥匙与墨迹交织 | 1850 | short | 91.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_run_mean 1.3 低于目标 1.5
  - [observe] 章内自我复读 21 句（如「就在他准备检查另一道锁的时候，余光瞥见角落里的登…」）
- 第 2 章：
  - 单条套路句式超限：「沈慕云的」×4、「”周怀瑾轻」×3、「周怀瑾的」×3
  - narration_para_pct 6.0 低于目标 20.0
  - attr_adv_pct 12.2 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「为什么会」×3
  - narration_para_pct 4.2 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「沈慕云的」×5、「沈慕云站在」×4、「“我不知道」×3
- 第 5 章：
  - 单条套路句式超限：「周怀瑾的」×3、「沈慕云的」×3
  - narration_para_pct 6.5 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13217
chapter_chars_mean: 2643
chapter_chars_median: 3009
chapter_chars_cv: 0.41
paragraphs_mean: 56.2
dialogue_chars_pct: 40.9
dialogue_para_pct: 77.8
interiority_para_pct: 7.4
narration_para_pct: 14.8
turn_under20_pct: 76.9
turn_over200_pct: 0.0
attr_say_pct: 18.5
attr_adv_pct: 9.9
scenes_per_chapter: 2.8
dialogue_run_mean: 5.5
turn_len_median: 12
```
