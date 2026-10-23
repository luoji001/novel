# 蓝笔记本 生成报告

slug：`xiaoyuan-20261020-80`
档位：校园青春　闸门模式：observe
章数：9　总字数：20001
LLM 调用：100 次，累计 427.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 笔记的归还 | 1380 | short | 97.2 | 0 |  | 3 |
| 2 | 摩挲桌角刻痕 | 2442 | normal | 93.7 | 0 |  | 1 |
| 3 | 磁带缓缓转动 | 2376 | normal | 91.7 | 0 |  | 3 |
| 4 | 借阅笔记的约定 | 2240 | normal | 88.0 | 0 |  | 1 |
| 5 | 校服外套的归还 | 2408 | normal | 89.9 | 0 |  | 3 |
| 6 | 摩挲笔记本边缘 | 2568 | normal | 93.6 | 0 |  | 2 |
| 7 | 摩挲课表边缘 | 2449 | normal | 93.3 | 0 |  | 2 |
| 8 | 摩挲笔记本边缘 | 2345 | normal | 91.2 | 0 |  | 3 |
| 9 | 摩挲校服口袋褶皱 | 1784 | short | 94.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「苏雨桐的」×4
  - narration_para_pct 13.3 低于目标 15.0
  - [observe] 章内自我复读 1 句（如「他感到有点失落，但也隐隐觉得，这一切都是有原因的…」）
- 第 2 章：
  - narration_para_pct 10.5 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「苏雨桐的」×4
  - narration_para_pct 11.3 低于目标 15.0
  - [observe] attr_adv_pct 35.7 > 22.0（结构塌缩）
- 第 4 章：
  - [observe] 章内自我复读 18 句（如「他接过笔记本，手指轻轻拂过封面，感觉到一股熟悉而…」）
- 第 5 章：
  - interiority_para_pct 3.3 低于目标 8.0
  - narration_para_pct 11.7 低于目标 15.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「林晓阳站在」×3、「他知道这」×3
  - narration_para_pct 14.5 低于目标 15.0
- 第 7 章：
  - 单条套路句式超限：「林晓阳的」×4
  - [observe] 标题与《摩挲笔记本边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「苏雨桐的」×3
  - narration_para_pct 9.6 低于目标 15.0
  - [observe] 标题重复：「摩挲笔记本边缘」已存在
- 第 9 章：
  - 单条套路句式超限：「苏雨桐的」×5

## 整书结构指标

```
chapters: 9
total_chars: 18850
chapter_chars_mean: 2094
chapter_chars_median: 2256
chapter_chars_cv: 0.17
paragraphs_mean: 54.1
dialogue_chars_pct: 32.2
dialogue_para_pct: 73.1
interiority_para_pct: 12.5
narration_para_pct: 14.4
turn_under20_pct: 90.1
turn_over200_pct: 0.0
attr_say_pct: 32.6
attr_adv_pct: 9.6
scenes_per_chapter: 2.4
dialogue_run_mean: 4.8
turn_len_median: 9
```
