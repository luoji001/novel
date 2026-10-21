# 听评本的消减 生成报告

slug：`aiyuce-20261021-213`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12799
LLM 调用：57 次，累计 219.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单的褶皱痕迹 | 2178 | normal | 94.8 | 0 |  | 2 |
| 2 | 钢笔在纸上游走 | 2803 | normal | 91.2 | 0 |  | 0 |
| 3 | 服务器折旧表的褶皱 | 2163 | normal | 37.2 | 0 |  | 1 |
| 4 | 报价单在桌面上滑动 | 2159 | normal | 34.0 | 0 |  | 4 |
| 5 | 翻阅听课记录本 | 2030 | normal | 36.6 | 0 |  | 1 |
| 6 | 报价单在桌面上滑动 | 1460 | short | 33.9 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 46.7 高于目标 40.0
  - narration_para_pct 13.3 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 62.2 高于目标 18.0
  - dialogue_run_mean 5.8 高于目标 4.0
  - narration_para_pct 7.7 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「产品经理没有立刻回答，而是转而说道：“其实，我们…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 27.8 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「就在这个时候，教研组组长突然想起了之前那张电费单…」）
  - [observe] 标题重复：「报价单在桌面上滑动」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12477
chapter_chars_mean: 2080
chapter_chars_median: 2094
chapter_chars_cv: 0.2
paragraphs_mean: 18.2
dialogue_chars_pct: 17.9
dialogue_para_pct: 42.0
interiority_para_pct: 24.1
narration_para_pct: 33.9
turn_under20_pct: 47.3
turn_over200_pct: 0.0
attr_say_pct: 20.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 2.9
turn_len_median: 20
```
