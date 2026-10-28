# 公文包移动 生成报告

slug：`shipin-20261027-167`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6703
LLM 调用：57 次，累计 142.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 雪铲撬门 | 723 | short | 38.7 | 0 |  | 1 |
| 2 | 雪铲横扫 | 1354 | normal | 92.8 | 0 |  | 2 |
| 3 | 保温杯砸地 | 1049 | normal | 92.7 | 0 |  | 1 |
| 4 | 公文包坠地 | 1224 | normal | 92.1 | 0 |  | 1 |
| 5 | 雪铲抵包 | 1094 | normal | 92.0 | 0 |  | 0 |
| 6 | 雪铲抵包 | 1253 | normal | 92.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「李志远的」×6
  - narration_para_pct 33.3 低于目标 35.0
- 第 3 章：
  - 单条套路句式超限：「李志远的」×3
- 第 4 章：
  - 单条套路句式超限：「王海生的」×3
- 第 6 章：
  - [observe] 标题重复：「雪铲抵包」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6295
chapter_chars_mean: 1049
chapter_chars_median: 1082
chapter_chars_cv: 0.2
paragraphs_mean: 27.3
dialogue_chars_pct: 19.2
dialogue_para_pct: 51.8
interiority_para_pct: 1.1
narration_para_pct: 47.1
turn_under20_pct: 98.0
turn_over200_pct: 0.0
attr_say_pct: 46.3
attr_adv_pct: 4.4
scenes_per_chapter: 1.3
dialogue_run_mean: 1.9
turn_len_median: 8
```
