# 校服外套 生成报告

slug：`xiaoyuan-20261020-99`
档位：校园青春　闸门模式：observe
章数：9　总字数：21666
LLM 调用：100 次，累计 451.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 粉笔灰的塑料袋 | 1521 | short | 89.0 | 0 |  | 1 |
| 2 | 摩挲校服边缘的手指 | 2719 | normal | 91.4 | 0 |  | 4 |
| 3 | 藏在桌底的纸条 | 2739 | normal | 92.7 | 0 |  | 2 |
| 4 | 摩挲课桌边缘的手指 | 2570 | normal | 91.9 | 0 |  | 3 |
| 5 | 藏在书包里的纸条 | 2559 | normal | 86.5 | 0 |  | 2 |
| 6 | 摩挲笔记本边缘的手指 | 2891 | normal | 91.3 | 0 |  | 4 |
| 7 | 摩挲课表边缘的手指 | 2574 | normal | 92.3 | 0 |  | 4 |
| 8 | 摩挲笔记本边缘的手指 | 2425 | normal | 90.5 | 0 |  | 1 |
| 9 | 摩挲课表边缘的手指 | 1659 | short | 89.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 17 句（如「他知道，这可能意味着他将不再和苏晴坐在一起，而这…」）
- 第 2 章：
  - 单条套路句式超限：「”苏晴轻」×4
  - narration_para_pct 13.7 低于目标 15.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 章内自我复读 9 句（如「如果我不再需要你帮忙保管这件衣服，你会不会也把我…」）
- 第 3 章：
  - narration_para_pct 12.3 低于目标 15.0
  - attr_adv_pct 14.8 高于目标 12.0
- 第 4 章：
  - 命中套话收尾句
  - narration_para_pct 13.5 低于目标 15.0
  - [observe] 标题与《摩挲校服边缘的手指》近似 0.78 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章内自我复读 17 句（如「林远赶紧转身去收拾工具，苏晴趁机瞥见了他的手——…」）
  - [observe] 标题与《藏在桌底的纸条》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「林远站在」×3
  - narration_para_pct 11.6 低于目标 15.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题与《摩挲校服边缘的手指》近似 0.74 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「林远点点」×3
  - narration_para_pct 14.3 低于目标 15.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题与《摩挲课桌边缘的手指》近似 0.89 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - [observe] 标题重复：「摩挲笔记本边缘的手指」已存在
- 第 9 章：
  - narration_para_pct 13.5 低于目标 15.0
  - [observe] 标题重复：「摩挲课表边缘的手指」已存在

## 整书结构指标

```
chapters: 9
total_chars: 20533
chapter_chars_mean: 2281
chapter_chars_median: 2431
chapter_chars_cv: 0.2
paragraphs_mean: 54.1
dialogue_chars_pct: 28.7
dialogue_para_pct: 71.0
interiority_para_pct: 13.0
narration_para_pct: 16.0
turn_under20_pct: 89.4
turn_over200_pct: 0.0
attr_say_pct: 39.2
attr_adv_pct: 8.5
scenes_per_chapter: 2.3
dialogue_run_mean: 3.5
turn_len_median: 9
```
