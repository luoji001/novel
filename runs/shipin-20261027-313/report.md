# 雨靴风波 生成报告

slug：`shipin-20261027-313`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6213
LLM 调用：57 次，累计 131.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 桶中水映旧靴 | 666 | short | 38.4 | 0 |  | 1 |
| 2 | 纸条上的数字 | 881 | normal | 22.0 | 0 |  | 1 |
| 3 | 钥匙转动的刹那 | 1246 | normal | 91.6 | 0 |  | 3 |
| 4 | 靴子与水桶对峙 | 1260 | normal | 92.0 | 0 |  | 2 |
| 5 | 水桶撞向铁门 | 943 | normal | 94.7 | 0 |  | 1 |
| 6 | 水痕下的纸条 | 1211 | normal | 91.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「水缓缓流出，在台阶上汇成一个小坑，映出她的脸…」）
- 第 2 章：
  - [observe] 章节过短 837 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - 单条套路句式超限：「陈秀兰的」×5
  - interiority_para_pct 6.9 高于目标 6.0
  - narration_para_pct 20.7 低于目标 35.0
- 第 4 章：
  - narration_para_pct 31.1 低于目标 35.0
  - dialogue_run_mean 5.2 高于目标 4.0
- 第 5 章：
  - narration_para_pct 32.3 低于目标 35.0
- 第 6 章：
  - narration_para_pct 25.0 低于目标 35.0
  - dialogue_run_mean 4.8 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 5768
chapter_chars_mean: 961
chapter_chars_median: 1002
chapter_chars_cv: 0.24
paragraphs_mean: 29.7
dialogue_chars_pct: 29.7
dialogue_para_pct: 64.2
interiority_para_pct: 1.4
narration_para_pct: 34.4
turn_under20_pct: 95.6
turn_over200_pct: 0.0
attr_say_pct: 49.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 3.2
turn_len_median: 9
```
