# 签字笔的痕迹 生成报告

slug：`xuanyi-20261019-209`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14172
LLM 调用：68 次，累计 229.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 算盘珠子不动了 | 1753 | short | 95.8 | 0 |  | 1 |
| 2 | 药瓶上的陌生签名 | 3879 | normal | 89.6 | 0 |  | 4 |
| 3 | 翻看病历本的指尖 | 3078 | normal | 88.2 | 0 |  | 2 |
| 4 | 签字笔的指纹纹路 | 3414 | normal | 88.2 | 0 |  | 3 |
| 5 | 药瓶上的陌生签名 | 2043 | short | 92.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 10.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×5、「陈志远点了点头」×3、「为什么会」×3
  - dialogue_chars_pct 59.2 高于目标 58.0
  - narration_para_pct 7.7 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「你是不是发现了什么？…」）
- 第 3 章：
  - 单条套路句式超限：「陈志远的」×3
  - [observe] 章内自我复读 2 句（如「正当他沉浸在思绪之中时，一个念头突然闪过脑海：“…」）
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×6、「”林素梅轻」×3
  - narration_para_pct 5.7 低于目标 20.0
  - dialogue_run_mean 14.2 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×4
  - narration_para_pct 14.3 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 标题重复：「药瓶上的陌生签名」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13454
chapter_chars_mean: 2691
chapter_chars_median: 2948
chapter_chars_cv: 0.32
paragraphs_mean: 63.4
dialogue_chars_pct: 44.8
dialogue_para_pct: 79.9
interiority_para_pct: 8.4
narration_para_pct: 11.8
turn_under20_pct: 76.3
turn_over200_pct: 0.0
attr_say_pct: 32.4
attr_adv_pct: 3.3
scenes_per_chapter: 2.8
dialogue_run_mean: 7.9
turn_len_median: 12
```
