# 雨靴 生成报告

slug：`shipin-20261027-131`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6242
LLM 调用：57 次，累计 137.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 面粉的较量 | 732 | short | 38.8 | 0 |  | 1 |
| 2 | 钥匙撬门 | 1057 | normal | 36.8 | 0 |  | 3 |
| 3 | 雨靴与电费单 | 1263 | normal | 93.3 | 0 |  | 1 |
| 4 | 面粉的较量 | 961 | normal | 90.9 | 0 |  | 1 |
| 5 | 钥匙揭开门缝 | 1108 | normal | 89.2 | 0 |  | 1 |
| 6 | 面粉的较量 | 1115 | normal | 92.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「李婶站在」×3
  - narration_para_pct 34.6 低于目标 35.0
  - [observe] 章内自我复读 1 句（如「你儿子死了三年，你还在这里搞这套？…」）
- 第 3 章：
  - narration_para_pct 29.6 低于目标 35.0
- 第 4 章：
  - [observe] 标题重复：「面粉的较量」已存在
- 第 5 章：
  - [observe] 标题与《钥匙撬门》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题重复：「面粉的较量」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5809
chapter_chars_mean: 968
chapter_chars_median: 1006
chapter_chars_cv: 0.18
paragraphs_mean: 29
dialogue_chars_pct: 29.5
dialogue_para_pct: 58.1
interiority_para_pct: 0.0
narration_para_pct: 41.9
turn_under20_pct: 91.8
turn_over200_pct: 0.0
attr_say_pct: 16.0
attr_adv_pct: 3.8
scenes_per_chapter: 1.3
dialogue_run_mean: 2.7
turn_len_median: 12
```
