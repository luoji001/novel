# 公文包 生成报告

slug：`shipin-20261027-321`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7141
LLM 调用：57 次，累计 147.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 公文包的拉链带 | 772 | short | 39.0 | 0 |  | 1 |
| 2 | 公文包的拉链带 | 1264 | normal | 90.6 | 0 |  | 2 |
| 3 | 公文包的拉链带 | 1576 | normal | 36.2 | 0 |  | 4 |
| 4 | 公文包的拉链带 | 1189 | normal | 59.9 | 0 |  | 1 |
| 5 | 钥匙串的重量 | 1210 | normal | 91.5 | 0 |  | 0 |
| 6 | 红围巾的重量 | 1124 | normal | 92.1 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 2 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 标题重复：「公文包的拉链带」已存在
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×3
  - narration_para_pct 23.8 低于目标 35.0
  - [observe] 章内自我复读 4 句（如「我不知道，但我觉得我们应该小心一点…」）
  - [observe] 标题重复：「公文包的拉链带」已存在
- 第 4 章：
  - [observe] 标题重复：「公文包的拉链带」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6644
chapter_chars_mean: 1107
chapter_chars_median: 1130
chapter_chars_cv: 0.21
paragraphs_mean: 33.2
dialogue_chars_pct: 23.5
dialogue_para_pct: 56.0
interiority_para_pct: 0.3
narration_para_pct: 43.6
turn_under20_pct: 99.1
turn_over200_pct: 0.0
attr_say_pct: 50.8
attr_adv_pct: 3.2
scenes_per_chapter: 1.3
dialogue_run_mean: 2.1
turn_len_median: 10
```
