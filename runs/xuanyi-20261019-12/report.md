# 登录簿 生成报告

slug：`xuanyi-20261019-12`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15263
LLM 调用：68 次，累计 239.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触碰冰凉的机身 | 1661 | short | 93.4 | 0 |  | 1 |
| 2 | 触碰冰凉的机身 | 4008 | normal | 88.8 | 0 |  | 4 |
| 3 | 凝视泛黄证件 | 4330 | normal | 89.2 | 0 |  | 2 |
| 4 | 摩挲褪色车票纹路 | 3198 | normal | 89.9 | 0 |  | 3 |
| 5 | 摩挲海报边缘褶子 | 2061 | short | 93.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 19.8 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「他知道自己」×5
  - narration_para_pct 15.2 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「每一个名字背后都藏着一段往事，而现在，这些往事就…」）
  - [observe] 标题重复：「触碰冰凉的机身」已存在
- 第 3 章：
  - 单条套路句式超限：「陈志远的」×5、「“我不知道」×4、「不仅仅是」×3
  - narration_para_pct 5.8 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×12、「他知道这」×4、「说道“我」×3
  - narration_para_pct 7.5 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「2000年4月15日…」）
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×5
  - narration_para_pct 4.7 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14578
chapter_chars_mean: 2916
chapter_chars_median: 3048
chapter_chars_cv: 0.38
paragraphs_mean: 60.4
dialogue_chars_pct: 32.0
dialogue_para_pct: 76.0
interiority_para_pct: 13.0
narration_para_pct: 11.1
turn_under20_pct: 82.7
turn_over200_pct: 0.0
attr_say_pct: 35.0
attr_adv_pct: 6.1
scenes_per_chapter: 3
dialogue_run_mean: 4.3
turn_len_median: 12
```
