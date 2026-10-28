# 药瓶上的名字 生成报告

slug：`shipin-20261027-294`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6372
LLM 调用：57 次，累计 136.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记本掉落的瞬间 | 733 | short | 94.2 | 0 |  | 1 |
| 2 | 红袖章贴胸口 | 1143 | normal | 92.7 | 0 |  | 1 |
| 3 | 胸牌上的刻字 | 1273 | normal | 92.7 | 0 |  | 1 |
| 4 | 药瓶跌落的瞬间 | 1162 | normal | 90.9 | 0 |  | 0 |
| 5 | 药瓶坠地的瞬间 | 985 | normal | 88.5 | 0 |  | 4 |
| 6 | 药瓶跌落的瞬间 | 1070 | normal | 90.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李秀兰的」×3
- 第 2 章：
  - 单条套路句式超限：「李秀兰的」×4
- 第 3 章：
  - 单条套路句式超限：「输液室」×5、「周玉兰的」×4、「李秀兰站在」×3
- 第 5 章：
  - 单条套路句式超限：「李秀兰的」×4
  - narration_para_pct 25.0 低于目标 35.0
  - dialogue_run_mean 6 高于目标 4.0
  - [observe] 标题与《药瓶跌落的瞬间》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题重复：「药瓶跌落的瞬间」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5911
chapter_chars_mean: 985
chapter_chars_median: 1024
chapter_chars_cv: 0.18
paragraphs_mean: 30.5
dialogue_chars_pct: 24.1
dialogue_para_pct: 57.5
interiority_para_pct: 0.0
narration_para_pct: 42.5
turn_under20_pct: 97.6
turn_over200_pct: 0.0
attr_say_pct: 50.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 2.7
turn_len_median: 9
```
