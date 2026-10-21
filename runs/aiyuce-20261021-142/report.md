# 折旧表 生成报告

slug：`aiyuce-20261021-142`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11399
LLM 调用：57 次，累计 213.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击桌面 | 1892 | normal | 58.1 | 0 |  | 0 |
| 2 | 敲击键盘 | 2178 | normal | 35.2 | 0 |  | 1 |
| 3 | 俯身看报价单 | 1824 | normal | 91.2 | 0 |  | 0 |
| 4 | 审视折旧表 | 2352 | normal | 35.6 | 0 |  | 1 |
| 5 | 敲击桌面 | 1724 | normal | 81.9 | 0 |  | 4 |
| 6 | 审视报价单 | 1423 | short | 90.3 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 3 句（如「如果技术总监随后表示支持人事主管的做法，并建议增…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 69.0 高于目标 18.0
  - dialogue_run_mean 17 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「敲击桌面」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11141
chapter_chars_mean: 1857
chapter_chars_median: 1816
chapter_chars_cv: 0.18
paragraphs_mean: 14.7
dialogue_chars_pct: 14.4
dialogue_para_pct: 29.5
interiority_para_pct: 13.4
narration_para_pct: 57.1
turn_under20_pct: 36.2
turn_over200_pct: 0.0
attr_say_pct: 10.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 3.8
turn_len_median: 26
```
