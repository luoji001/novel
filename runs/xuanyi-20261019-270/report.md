# 纸条 生成报告

slug：`xuanyi-20261019-270`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15931
LLM 调用：68 次，累计 235.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 屏幕闪烁异常 | 2097 | short | 84.1 | 0 |  | 2 |
| 2 | 副驾纸条浮现 | 3949 | normal | 78.0 | 0 |  | 4 |
| 3 | 蓝牙耳机的回放 | 3931 | normal | 83.3 | 0 |  | 2 |
| 4 | 核对计费记录 | 3980 | normal | 87.3 | 0 |  | 3 |
| 5 | 纸条藏匿座椅缝中 | 1969 | short | 82.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 10.5 低于目标 20.0
  - narration_para_pct 73.8 高于目标 70.0
- 第 2 章：
  - 单条套路句式超限：「为什么会」×5
  - dialogue_chars_pct 15.4 低于目标 20.0
  - interiority_para_pct 24.7 高于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 3 章：
  - dialogue_chars_pct 14.6 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「到了一个」×4、「他知道这」×4、「他知道自己」×3
  - [observe] 章内自我复读 4 句（如「你说的没错，”李浩对着手机说道，“但我现在才注意…」）
- 第 5 章：
  - dialogue_chars_pct 14.6 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「你最近有没有遇到什么奇怪的事情？…」）

## 整书结构指标

```
chapters: 5
total_chars: 15218
chapter_chars_mean: 3044
chapter_chars_median: 3789
chapter_chars_cv: 0.34
paragraphs_mean: 61
dialogue_chars_pct: 17.2
dialogue_para_pct: 45.6
interiority_para_pct: 19.4
narration_para_pct: 35.0
turn_under20_pct: 72.2
turn_over200_pct: 0.0
attr_say_pct: 28.0
attr_adv_pct: 7.4
scenes_per_chapter: 5.2
dialogue_run_mean: 2.3
turn_len_median: 12
```
