# 铜钱 生成报告

slug：`xuanyi-20261019-67`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13260
LLM 调用：68 次，累计 232.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 端砚上的旧报纸 | 1601 | short | 97.4 | 0 |  | 1 |
| 2 | 摩挲纸边的手指 | 3749 | normal | 91.6 | 0 |  | 4 |
| 3 | 端砚上的旧报纸 | 3305 | normal | 91.8 | 0 |  | 2 |
| 4 | 摩挲铜钱的指尖 | 2938 | normal | 92.0 | 0 |  | 2 |
| 5 | 摩挲铜钱的指尖 | 1662 | short | 91.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 10.7 低于目标 20.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「北平警察局」×6、「陆文渊的」×4、「”陆文渊低」×3
  - narration_para_pct 9.6 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「陆文渊站在黄花梨木桌旁，目光落在那张盖着北平警察…」）
- 第 3 章：
  - narration_para_pct 5.7 低于目标 20.0
  - [observe] 标题重复：「端砚上的旧报纸」已存在
- 第 4 章：
  - 单条套路句式超限：「北平警察局」×7、「“我不知道」×3、「陆文渊点」×3
  - narration_para_pct 5.1 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「陆文渊的」×4
  - narration_para_pct 18.8 低于目标 20.0
  - [observe] 标题重复：「摩挲铜钱的指尖」已存在

## 整书结构指标

```
chapters: 5
total_chars: 12636
chapter_chars_mean: 2527
chapter_chars_median: 2805
chapter_chars_cv: 0.37
paragraphs_mean: 54.4
dialogue_chars_pct: 46.6
dialogue_para_pct: 84.2
interiority_para_pct: 6.8
narration_para_pct: 8.9
turn_under20_pct: 76.4
turn_over200_pct: 0.0
attr_say_pct: 21.0
attr_adv_pct: 3.3
scenes_per_chapter: 1.8
dialogue_run_mean: 6.3
turn_len_median: 12
```
