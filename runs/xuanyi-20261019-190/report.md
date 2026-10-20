# 空白时光 生成报告

slug：`xuanyi-20261019-190`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15083
LLM 调用：68 次，累计 224.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触摸屏幕的颤抖手指 | 1769 | short | 98.5 | 0 |  | 1 |
| 2 | 触摸屏幕的颤抖手指 | 3947 | normal | 89.8 | 0 |  | 3 |
| 3 | 触碰车票的指尖 | 3961 | normal | 58.3 | 0 |  | 5 |
| 4 | 触摸车票的指尖 | 3631 | normal | 88.8 | 0 |  | 1 |
| 5 | 触摸刹车痕迹的手指 | 1770 | short | 92.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 20.0 高于目标 10.0
- 第 2 章：
  - attr_adv_pct 11.8 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「他深吸一口气，努力让自己冷静下来…」）
  - [observe] 标题重复：「触摸屏幕的颤抖手指」已存在
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「为什么会」×6、「他知道这」×4、「深吸一口气」×3
  - interiority_para_pct 25.0 高于目标 20.0
  - attr_adv_pct 15.0 高于目标 10.0
  - [observe] 章内自我复读 3 句（如「我不知道你在说什么，但我希望你能告诉我，为什么我…」）
- 第 4 章：
  - [observe] 标题与《触碰车票的指尖》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 8.1 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
  - [observe] 标题与《触摸车票的指尖》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 14355
chapter_chars_mean: 2871
chapter_chars_median: 3430
chapter_chars_cv: 0.38
paragraphs_mean: 64.2
dialogue_chars_pct: 25.3
dialogue_para_pct: 58.2
interiority_para_pct: 16.2
narration_para_pct: 25.6
turn_under20_pct: 82.7
turn_over200_pct: 0.0
attr_say_pct: 26.5
attr_adv_pct: 13.3
scenes_per_chapter: 3.4
dialogue_run_mean: 3.4
turn_len_median: 11
```
