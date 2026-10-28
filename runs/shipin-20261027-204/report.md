# 冰台上的信 生成报告

slug：`shipin-20261027-204`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6481
LLM 调用：57 次，累计 161.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 塑料秤敲击冰台 | 795 | short | 94.8 | 0 |  | 0 |
| 2 | 鱼鳞铺就的迷宫 | 839 | normal | 35.9 | 0 |  | 1 |
| 3 | 塑料秤敲击冰台 | 1517 | normal | 90.5 | 0 |  | 2 |
| 4 | 铁皮箱与冰台对峙 | 1219 | normal | 88.1 | 0 |  | 0 |
| 5 | 摩挲信封的指尖 | 1333 | normal | 88.7 | 0 |  | 2 |
| 6 | 拾起鱼鳞看字迹 | 772 | normal | 36.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章节过短 782 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - 单条套路句式超限：「王阿婆的」×9
  - [observe] 标题重复：「塑料秤敲击冰台」已存在
- 第 5 章：
  - narration_para_pct 32.1 低于目标 35.0
  - dialogue_run_mean 4.8 高于目标 4.0
- 第 6 章：
  - [observe] 章节过短 693 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 6067
chapter_chars_mean: 1011
chapter_chars_median: 967
chapter_chars_cv: 0.31
paragraphs_mean: 26.3
dialogue_chars_pct: 20.3
dialogue_para_pct: 56.3
interiority_para_pct: 0.4
narration_para_pct: 43.3
turn_under20_pct: 94.0
turn_over200_pct: 0.0
attr_say_pct: 27.0
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 2.6
turn_len_median: 10
```
