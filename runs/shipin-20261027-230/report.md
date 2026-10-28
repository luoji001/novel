# 灯绳 生成报告

slug：`shipin-20261027-230`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7609
LLM 调用：57 次，累计 145.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 应急灯的摇晃 | 731 | short | 97.4 | 0 |  | 0 |
| 2 | 铅笔划破试卷的痕迹 | 1173 | normal | 93.5 | 0 |  | 0 |
| 3 | 钥匙插进锁孔 | 1316 | normal | 95.7 | 0 |  | 0 |
| 4 | 红绳勒腕 | 1205 | normal | 93.8 | 0 |  | 0 |
| 5 | 应急灯的摇晃 | 1903 | normal | 23.1 | 0 |  | 4 |
| 6 | 试卷边缘的颤抖 | 1275 | normal | 36.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 5 章：
  - 单条套路句式超限：「王小满的」×7、「王小满点」×3
  - narration_para_pct 24.3 低于目标 35.0
  - [observe] attr_adv_pct 28.6 > 18.0（结构塌缩）
  - [observe] 标题重复：「应急灯的摇晃」已存在
- 第 6 章：
  - 单条套路句式超限：「王小满的」×3、「李国强的」×3
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 7156
chapter_chars_mean: 1193
chapter_chars_median: 1178
chapter_chars_cv: 0.3
paragraphs_mean: 29.2
dialogue_chars_pct: 20.9
dialogue_para_pct: 60.1
interiority_para_pct: 1.4
narration_para_pct: 38.6
turn_under20_pct: 97.5
turn_over200_pct: 0.0
attr_say_pct: 30.5
attr_adv_pct: 15.2
scenes_per_chapter: 2.2
dialogue_run_mean: 2.4
turn_len_median: 10
```
