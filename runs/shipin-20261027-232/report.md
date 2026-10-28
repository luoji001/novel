# 鱼鳞 生成报告

slug：`shipin-20261027-232`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6418
LLM 调用：57 次，累计 134.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 鱼腹贴冰面 | 806 | short | 95.4 | 0 |  | 0 |
| 2 | 鱼鳞入袋 | 1097 | normal | 91.3 | 0 |  | 0 |
| 3 | 鱼鳞入袋 | 1266 | normal | 90.1 | 0 |  | 1 |
| 4 | 信封飘落冰面 | 1142 | normal | 91.3 | 0 |  | 0 |
| 5 | 鱼鳞入秤 | 928 | normal | 90.1 | 0 |  | 1 |
| 6 | 鱼鳞入水 | 1173 | normal | 57.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - [observe] 标题重复：「鱼鳞入袋」已存在
- 第 5 章：
  - [observe] 标题与《鱼鳞入袋》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题与《鱼鳞入袋》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6008
chapter_chars_mean: 1001
chapter_chars_median: 1050
chapter_chars_cv: 0.16
paragraphs_mean: 27.3
dialogue_chars_pct: 22.8
dialogue_para_pct: 52.4
interiority_para_pct: 0.6
narration_para_pct: 47.0
turn_under20_pct: 97.3
turn_over200_pct: 0.0
attr_say_pct: 57.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.6
turn_len_median: 10
```
