# 电表 生成报告

slug：`aiyuce-20261021-64`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12140
LLM 调用：53 次，累计 208.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 用电量统计图 | 2225 | normal | 92.9 | 0 |  | 0 |
| 2 | 核对电费单数据 | 2205 | normal | 90.1 | 0 |  | 0 |
| 3 | 核对服务器折旧表 | 2267 | normal | 35.3 | 0 |  | 1 |
| 4 | 手指敲击桌面 | 2713 | normal | 36.2 | 0 |  | 1 |
| 5 | 核对电费单数据 | 1262 | normal | 90.0 | 0 |  | 2 |
| 6 | 核对电费单数据 | 1462 | short | 90.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 标题重复：「核对电费单数据」已存在
- 第 6 章：
  - [observe] 标题重复：「核对电费单数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11883
chapter_chars_mean: 1980
chapter_chars_median: 2172
chapter_chars_cv: 0.27
paragraphs_mean: 13.5
dialogue_chars_pct: 3.3
dialogue_para_pct: 18.9
interiority_para_pct: 13.9
narration_para_pct: 67.2
turn_under20_pct: 80.3
turn_over200_pct: 0.0
attr_say_pct: 12.7
attr_adv_pct: 12.7
scenes_per_chapter: 1
dialogue_run_mean: 1.3
turn_len_median: 9
```
