# 铜尺 生成报告

slug：`xuanyi-20261019-42`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13295
LLM 调用：68 次，累计 223.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜铃响了三次 | 1766 | short | 98.2 | 0 |  | 2 |
| 2 | 报纸上的日期 | 3582 | normal | 91.9 | 0 |  | 4 |
| 3 | 铜尺比对玉佩纹路 | 3288 | normal | 91.6 | 0 |  | 2 |
| 4 | 铜牌划痕映铜锁 | 3279 | normal | 91.1 | 0 |  | 3 |
| 5 | 铜锁与旧账册 | 1375 | short | 59.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 12.5 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「沈文远的」×5
  - 情节与已写章节重复 0.63 ≥ 0.62（撞上「沈文远发现一张当票日期与当物不符，引发他对一件神秘物品和…」）
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「欲购者请至霞飞路123号当铺详谈…」）
- 第 3 章：
  - 单条套路句式超限：「沈文远的」×7、「不仅仅是」×3
  - narration_para_pct 13.1 低于目标 20.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈文远的」×7
  - narration_para_pct 11.9 低于目标 20.0
- 第 5 章：
  - dialogue_chars_pct 15.3 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「沈文远伸手抽出最上面那本，翻开封面，看到“民国二…」）

## 整书结构指标

```
chapters: 5
total_chars: 12693
chapter_chars_mean: 2539
chapter_chars_median: 3096
chapter_chars_cv: 0.38
paragraphs_mean: 52.4
dialogue_chars_pct: 32.5
dialogue_para_pct: 72.0
interiority_para_pct: 10.0
narration_para_pct: 18.0
turn_under20_pct: 78.3
turn_over200_pct: 0.0
attr_say_pct: 22.0
attr_adv_pct: 9.1
scenes_per_chapter: 2.4
dialogue_run_mean: 3.6
turn_len_median: 12
```
