# 显卡交易 生成报告

slug：`aiyuce-20261021-74`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12198
LLM 调用：57 次，累计 223.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单的疑问 | 1923 | normal | 37.9 | 0 |  | 1 |
| 2 | 电费单的疑问 | 2572 | normal | 36.1 | 0 |  | 2 |
| 3 | 推理报价单的疑云 | 2205 | normal | 35.6 | 0 |  | 1 |
| 4 | 折旧表的折旧率 | 1791 | normal | 35.7 | 0 |  | 4 |
| 5 | 七月的招聘JD | 2001 | normal | 88.6 | 0 |  | 2 |
| 6 | 电费单的疑问 | 1700 | short | 90.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 3 句（如「假如在未来的一段时间内，市场交易量没有延续当前的…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「电费单的疑问」已存在
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 4 章：
  - dialogue_chars_pct 18.4 高于目标 18.0
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 29.4 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「然后继续盯着那张折旧表看了好一会儿才开口问，“你…」）
- 第 5 章：
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
- 第 6 章：
  - [observe] 标题重复：「电费单的疑问」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11932
chapter_chars_mean: 1989
chapter_chars_median: 1920
chapter_chars_cv: 0.16
paragraphs_mean: 14.3
dialogue_chars_pct: 5.9
dialogue_para_pct: 29.1
interiority_para_pct: 28.9
narration_para_pct: 42.0
turn_under20_pct: 83.9
turn_over200_pct: 0.0
attr_say_pct: 11.8
attr_adv_pct: 0.0
scenes_per_chapter: 2.3
dialogue_run_mean: 2.2
turn_len_median: 12
```
