# 表里藏信 生成报告

slug：`xuanyi-20261019-115`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14638
LLM 调用：68 次，累计 233.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手表指针不停转动 | 1734 | short | 98.4 | 0 |  | 2 |
| 2 | 手表指针不停转动 | 3544 | normal | 93.3 | 0 |  | 2 |
| 3 | 手表指针不停转动 | 3640 | normal | 91.0 | 0 |  | 2 |
| 4 | 香烟纸筒藏密信 | 3762 | normal | 88.0 | 0 |  | 3 |
| 5 | 手表指针不停转动 | 1953 | short | 91.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - narration_para_pct 5.7 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×3、「他知道这」×3、「周振邦的」×3
  - [observe] 标题重复：「手表指针不停转动」已存在
- 第 3 章：
  - 单条套路句式超限：「就在这时」×3、「沈文澜的」×3、「他知道这」×3
  - [observe] 标题重复：「手表指针不停转动」已存在
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×4、「周振邦的」×3、「变得更加」×3
  - [observe] 章内自我复读 18 句（如「哥，我刚刚听说了一个可怕的消息，”他妹妹的声音听…」）
- 第 5 章：
  - narration_para_pct 8.3 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 标题重复：「手表指针不停转动」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13929
chapter_chars_mean: 2786
chapter_chars_median: 3380
chapter_chars_cv: 0.34
paragraphs_mean: 62.4
dialogue_chars_pct: 34.2
dialogue_para_pct: 69.3
interiority_para_pct: 11.5
narration_para_pct: 19.3
turn_under20_pct: 76.3
turn_over200_pct: 0.0
attr_say_pct: 20.8
attr_adv_pct: 7.1
scenes_per_chapter: 3
dialogue_run_mean: 4.3
turn_len_median: 10
```
