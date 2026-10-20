# 重扫 生成报告

slug：`xuanyi-20261019-137`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13154
LLM 调用：68 次，累计 213.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫描枪的红光 | 1704 | short | 100.0 | 0 |  | 2 |
| 2 | 重复扫码的包裹 | 3698 | normal | 90.0 | 0 |  | 2 |
| 3 | 重复扫描的包裹 | 2932 | normal | 89.4 | 0 |  | 3 |
| 4 | 文件夹边缘的指纹 | 3219 | normal | 88.4 | 0 |  | 3 |
| 5 | 扫描枪的红光 | 1596 | short | 90.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 18.9 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「周晓芸的」×3
  - narration_para_pct 15.8 低于目标 20.0
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题与《重复扫码的包裹》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「周晓芸的」×5、「“我不知道」×3、「不仅仅是」×3
  - narration_para_pct 8.9 低于目标 20.0
  - [observe] 章内自我复读 6 句（如「如果你需要帮助的话，我可以帮你联系一些人…」）
- 第 5 章：
  - [observe] 标题重复：「扫描枪的红光」已存在

## 整书结构指标

```
chapters: 5
total_chars: 12571
chapter_chars_mean: 2514
chapter_chars_median: 2807
chapter_chars_cv: 0.36
paragraphs_mean: 50.4
dialogue_chars_pct: 36.5
dialogue_para_pct: 73.9
interiority_para_pct: 10.0
narration_para_pct: 16.1
turn_under20_pct: 68.8
turn_over200_pct: 0.0
attr_say_pct: 29.2
attr_adv_pct: 5.0
scenes_per_chapter: 2.2
dialogue_run_mean: 4.5
turn_len_median: 13
```
