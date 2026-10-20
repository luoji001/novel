# 绣花绷 生成报告

slug：`xuanyi-20261019-158`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13303
LLM 调用：68 次，累计 235.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 绣花绷上的丝线痕迹 | 1928 | short | 100.0 | 0 |  | 2 |
| 2 | 绣花绷上的针脚痕迹 | 3307 | normal | 89.1 | 0 |  | 5 |
| 3 | 指尖拂过绢面 | 3373 | normal | 89.7 | 0 |  | 2 |
| 4 | 指尖拂过绣花针 | 3176 | normal | 90.1 | 0 |  | 4 |
| 5 | 指尖拂过绣花针 | 1514 | short | 72.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「顾青梧的」×3
  - attr_adv_pct 14.3 高于目标 10.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「顾青梧的」×6
  - narration_para_pct 7.1 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「他顿了顿，从抽屉取出一本陈旧账册，在摊开的页面翻…」）
  - [observe] 标题与《绣花绷上的丝线痕迹》近似 0.78 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「沈怀瑾的」×7、「他知道这」×3
  - narration_para_pct 14.3 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×3、「微微一笑」×3
  - narration_para_pct 2.9 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 标题与《指尖拂过绢面》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - dialogue_chars_pct 12.7 低于目标 20.0
  - interiority_para_pct 22.2 高于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5
  - [observe] 标题重复：「指尖拂过绣花针」已存在

## 整书结构指标

```
chapters: 5
total_chars: 12644
chapter_chars_mean: 2529
chapter_chars_median: 3021
chapter_chars_cv: 0.33
paragraphs_mean: 57.6
dialogue_chars_pct: 40.1
dialogue_para_pct: 75.3
interiority_para_pct: 10.8
narration_para_pct: 13.8
turn_under20_pct: 78.2
turn_over200_pct: 0.0
attr_say_pct: 13.7
attr_adv_pct: 6.7
scenes_per_chapter: 2.6
dialogue_run_mean: 4.6
turn_len_median: 12
```
