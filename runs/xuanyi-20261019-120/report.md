# 门禁卡重现 生成报告

slug：`xuanyi-20261019-120`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14579
LLM 调用：68 次，累计 235.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 屏幕上的诡异数字 | 1878 | short | 98.1 | 0 |  | 1 |
| 2 | 屏幕上的诡异数字 | 3900 | normal | 90.8 | 0 |  | 3 |
| 3 | 刷卡轨迹浮现谜影 | 3513 | normal | 90.4 | 0 |  | 2 |
| 4 | 捏住空白报销单 | 3277 | normal | 91.3 | 0 |  | 2 |
| 5 | 点击空白报销单 | 2006 | short | 87.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3
- 第 2 章：
  - 单条套路句式超限：「沈婉如的」×6、「他知道自己」×3、「“我不知道」×3
  - narration_para_pct 13.8 低于目标 20.0
  - [observe] 标题重复：「屏幕上的诡异数字」已存在
- 第 3 章：
  - 单条套路句式超限：「周启明的」×11
  - narration_para_pct 17.2 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「沈婉如的」×7、「周启明的」×4、「为什么会」×4
  - narration_para_pct 11.9 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「带着一丝」×3
  - [observe] 章内自我复读 16 句（如「沈婉如将手中的纸张递过去，上面赫然是一页空白的报…」）
  - [observe] 标题与《捏住空白报销单》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13918
chapter_chars_mean: 2784
chapter_chars_median: 3128
chapter_chars_cv: 0.31
paragraphs_mean: 57.8
dialogue_chars_pct: 36.5
dialogue_para_pct: 71.7
interiority_para_pct: 10.4
narration_para_pct: 18.0
turn_under20_pct: 70.5
turn_over200_pct: 0.0
attr_say_pct: 16.8
attr_adv_pct: 4.6
scenes_per_chapter: 2.8
dialogue_run_mean: 4.7
turn_len_median: 11
```
