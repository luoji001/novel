# 签条 生成报告

slug：`shuangwen-20261023-137`
档位：爽文　闸门模式：observe
章数：10　总字数：19539
LLM 调用：97 次，累计 456.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字的钢笔 | 2448 | normal | 39.2 | 0 |  | 2 |
| 2 | 抽屉里的代课证明 | 2007 | normal | 92.3 | 0 |  | 1 |
| 3 | 签字的钢笔 | 1830 | normal | 37.6 | 0 |  | 2 |
| 4 | 签字的钢笔 | 1819 | normal | 92.6 | 0 |  | 2 |
| 5 | 签字的钢笔 | 1514 | normal | 88.9 | 0 |  | 4 |
| 6 | 一张旧证明的边缘 | 2017 | normal | 37.4 | 0 |  | 3 |
| 7 | 撕碎的审批表 | 1715 | normal | 93.5 | 0 |  | 2 |
| 8 | 手指触碰铁盒边缘 | 1814 | normal | 94.2 | 0 |  | 2 |
| 9 | 指尖抚过名册边缘 | 2182 | normal | 36.6 | 0 |  | 2 |
| 10 | 手指抚过名册边缘 | 2183 | long | 91.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「张主任的」×4、「李素芬的」×4
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 2 章：
  - attr_adv_pct 22.2 高于目标 12.0
- 第 3 章：
  - [observe] attr_adv_pct 44.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字的钢笔」已存在
- 第 4 章：
  - 单条套路句式超限：「张主任的」×7
  - [observe] 标题重复：「签字的钢笔」已存在
- 第 5 章：
  - narration_para_pct 2.6 低于目标 5.0
  - attr_adv_pct 17.6 高于目标 12.0
  - dialogue_run_mean 36 高于目标 14.0
  - [observe] 标题重复：「签字的钢笔」已存在
- 第 6 章：
  - 单条套路句式超限：「张主任的」×3
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 章内自我复读 2 句（如「我只是想要一个公平的机会…」）
- 第 7 章：
  - 情节与已写章节重复 0.70 ≥ 0.7（撞上「李素芬与张主任因工龄证明产生冲突，最终通过互相妥协达成暂…」）
  - attr_adv_pct 14.3 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「张主任的」×3
  - attr_adv_pct 14.3 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「李素芬的」×5、「张主任的」×3
  - [observe] 章内自我复读 1 句（如「他知道，这场较量还没有结束…」）
- 第 10 章：
  - 单条套路句式超限：「张主任的」×6
  - [observe] 标题与《指尖抚过名册边缘》近似 0.88 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18529
chapter_chars_mean: 1853
chapter_chars_median: 1824
chapter_chars_cv: 0.14
paragraphs_mean: 42.7
dialogue_chars_pct: 46.5
dialogue_para_pct: 81.1
interiority_para_pct: 6.4
narration_para_pct: 12.5
turn_under20_pct: 69.5
turn_over200_pct: 0.0
attr_say_pct: 22.3
attr_adv_pct: 17.6
scenes_per_chapter: 1.5
dialogue_run_mean: 8.6
turn_len_median: 13
```
