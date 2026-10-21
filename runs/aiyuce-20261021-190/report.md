# 能耗密码 生成报告

slug：`aiyuce-20261021-190`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12668
LLM 调用：57 次，累计 225.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计算电费单上的数字 | 2342 | normal | 37.4 | 0 |  | 1 |
| 2 | 敲击键盘 | 2001 | normal | 35.7 | 0 |  | 1 |
| 3 | 计算电费单上的数字 | 2754 | normal | 35.4 | 0 |  | 3 |
| 4 | 手指划过折旧表 | 2089 | normal | 88.5 | 0 |  | 0 |
| 5 | 手指摩挲纸边 | 2162 | normal | 34.7 | 0 |  | 2 |
| 6 | 计算电费单上的数字 | 1314 | short | 89.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「她把注意力再次放回那张电费单上，心中清楚，这项数…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「计算电费单上的数字」已存在
- 第 5 章：
  - narration_para_pct 30.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 6 章：
  - interiority_para_pct 50.0 高于目标 40.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 标题重复：「计算电费单上的数字」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12408
chapter_chars_mean: 2068
chapter_chars_median: 2083
chapter_chars_cv: 0.23
paragraphs_mean: 13.5
dialogue_chars_pct: 5.1
dialogue_para_pct: 31.6
interiority_para_pct: 25.0
narration_para_pct: 43.4
turn_under20_pct: 70.3
turn_over200_pct: 0.0
attr_say_pct: 42.2
attr_adv_pct: 5.8
scenes_per_chapter: 1.3
dialogue_run_mean: 1.4
turn_len_median: 11
```
