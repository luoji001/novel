# 承诺书 生成报告

slug：`shuangwen-20261022-89`
档位：爽文　闸门模式：observe
章数：10　总字数：18338
LLM 调用：97 次，累计 412.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 报价单上的签名 | 1765 | normal | 97.4 | 0 |  | 0 |
| 2 | 合同上的指纹 | 1789 | normal | 93.6 | 0 |  | 1 |
| 3 | 敲门声 | 2004 | normal | 37.3 | 0 |  | 3 |
| 4 | 撕碎的报价单 | 1672 | normal | 93.1 | 0 |  | 0 |
| 5 | 撕碎的报价单 | 1856 | normal | 36.9 | 0 |  | 2 |
| 6 | 撕碎的报价单 | 1799 | normal | 93.2 | 0 |  | 3 |
| 7 | 承诺书背面的字 | 1844 | normal | 94.6 | 0 |  | 1 |
| 8 | 撕碎的报价单 | 1790 | normal | 92.5 | 0 |  | 2 |
| 9 | 撕碎的名册 | 1487 | normal | 37.0 | 0 |  | 1 |
| 10 | 文件上的指纹 | 2322 | long | 93.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 3.3 低于目标 5.0
- 第 3 章：
  - narration_para_pct 4.5 低于目标 5.0
  - attr_adv_pct 12.1 高于目标 12.0
  - [observe] 章内自我复读 3 句（如「不过，我希望你能记住，你所做的一切都是建立在我的…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「既然你觉得我不合适，那不如让其他人试试？…」）
  - [observe] 标题重复：「撕碎的报价单」已存在
- 第 6 章：
  - 单条套路句式超限：「周婉如的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - [observe] 标题重复：「撕碎的报价单」已存在
- 第 7 章：
  - attr_adv_pct 23.5 高于目标 12.0
- 第 8 章：
  - attr_adv_pct 20.7 高于目标 12.0
  - [observe] 标题重复：「撕碎的报价单」已存在
- 第 9 章：
  - [observe] 章内自我复读 1 句（如「有些人抢来的不只是生意，还有信任…」）
- 第 10 章：
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题与《合同上的指纹》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 17452
chapter_chars_mean: 1745
chapter_chars_median: 1721
chapter_chars_cv: 0.12
paragraphs_mean: 36.9
dialogue_chars_pct: 51.1
dialogue_para_pct: 84.5
interiority_para_pct: 6.7
narration_para_pct: 8.8
turn_under20_pct: 70.4
turn_over200_pct: 0.0
attr_say_pct: 31.1
attr_adv_pct: 12.9
scenes_per_chapter: 2.6
dialogue_run_mean: 8.2
turn_len_median: 13
```
