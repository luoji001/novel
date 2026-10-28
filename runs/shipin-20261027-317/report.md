# 红瓶 生成报告

slug：`shipin-20261027-317`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6429
LLM 调用：57 次，累计 123.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手电筒的光柱摇晃 | 619 | short | 38.6 | 0 |  | 1 |
| 2 | 蓝色金属打火机的温度 | 1142 | normal | 93.5 | 0 |  | 1 |
| 3 | 手电筒照出空位 | 1155 | normal | 91.0 | 0 |  | 1 |
| 4 | 打火机熄灭的瞬间 | 1378 | normal | 92.4 | 0 |  | 1 |
| 5 | 手电筒照出空位 | 1102 | normal | 89.3 | 0 |  | 2 |
| 6 | 写入记事本的时刻 | 1027 | normal | 54.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 545 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「陈志远的」×3
- 第 3 章：
  - 单条套路句式超限：「小林站在」×3
- 第 4 章：
  - narration_para_pct 23.3 低于目标 35.0
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×3
  - [observe] 标题重复：「手电筒照出空位」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6019
chapter_chars_mean: 1003
chapter_chars_median: 1058
chapter_chars_cv: 0.25
paragraphs_mean: 25.7
dialogue_chars_pct: 12.6
dialogue_para_pct: 48.2
interiority_para_pct: 1.5
narration_para_pct: 50.3
turn_under20_pct: 100.0
turn_over200_pct: 0.0
attr_say_pct: 33.8
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 2.3
turn_len_median: 7
```
