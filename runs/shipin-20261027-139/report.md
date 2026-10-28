# 钥匙 生成报告

slug：`shipin-20261027-139`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6249
LLM 调用：57 次，累计 141.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙与父亲的遗言 | 879 | short | 95.5 | 0 |  | 0 |
| 2 | 保温杯边缘的冰碴 | 888 | normal | 38.1 | 0 |  | 2 |
| 3 | 保温杯边缘的冰碴 | 1274 | normal | 94.8 | 0 |  | 4 |
| 4 | 钥匙与父亲的遗言 | 1202 | normal | 36.4 | 0 |  | 2 |
| 5 | 军用背包里的小铁盒 | 812 | normal | 19.9 | 0 |  | 3 |
| 6 | 手电筒照亮的车门缝隙 | 1188 | normal | 91.5 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 31.2 低于目标 35.0
  - [observe] 章节过短 840 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - 单条套路句式超限：「林浩站在」×3
  - narration_para_pct 20.5 低于目标 35.0
  - dialogue_run_mean 4.1 高于目标 4.0
  - [observe] 标题重复：「保温杯边缘的冰碴」已存在
- 第 4 章：
  - [observe] 章内自我复读 3 句（如「三年前的票根，说明你们父子见面了…」）
  - [observe] 标题重复：「钥匙与父亲的遗言」已存在
- 第 5 章：
  - dialogue_chars_pct 2.5 低于目标 5.0
  - narration_para_pct 94.1 高于目标 90.0
  - [observe] 章节过短 727 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5832
chapter_chars_mean: 972
chapter_chars_median: 987
chapter_chars_cv: 0.2
paragraphs_mean: 26
dialogue_chars_pct: 18.9
dialogue_para_pct: 51.2
interiority_para_pct: 1.0
narration_para_pct: 47.7
turn_under20_pct: 95.6
turn_over200_pct: 0.0
attr_say_pct: 33.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.1
turn_len_median: 8
```
