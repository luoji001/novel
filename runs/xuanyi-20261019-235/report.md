# 走表 生成报告

slug：`xuanyi-20261019-235`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13328
LLM 调用：68 次，累计 210.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手表仍在走动 | 1680 | short | 99.1 | 0 |  | 1 |
| 2 | 撕下的纸页痕迹 | 3098 | normal | 90.6 | 0 |  | 2 |
| 3 | 存折上的红印章 | 3423 | normal | 89.2 | 0 |  | 1 |
| 4 | 存折上的红印章 | 3383 | normal | 89.4 | 0 |  | 3 |
| 5 | 铁盒边缘的锈迹 | 1739 | short | 70.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 18.8 低于目标 20.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×4
- 第 3 章：
  - 单条套路句式超限：「点了点头」×3、「带着一丝」×3、「他知道这」×3
- 第 4 章：
  - 单条套路句式超限：「沈婉如的」×6、「为什么会」×4、「带着一丝」×3
  - narration_para_pct 14.3 低于目标 20.0
  - [observe] 标题重复：「存折上的红印章」已存在
- 第 5 章：
  - dialogue_chars_pct 10.9 低于目标 20.0
  - interiority_para_pct 28.6 高于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 12715
chapter_chars_mean: 2543
chapter_chars_median: 2949
chapter_chars_cv: 0.33
paragraphs_mean: 53.6
dialogue_chars_pct: 28.0
dialogue_para_pct: 61.7
interiority_para_pct: 14.9
narration_para_pct: 23.4
turn_under20_pct: 85.3
turn_over200_pct: 0.0
attr_say_pct: 24.1
attr_adv_pct: 2.4
scenes_per_chapter: 4.2
dialogue_run_mean: 3.3
turn_len_median: 12
```
