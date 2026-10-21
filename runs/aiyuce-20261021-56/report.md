# 校对尺 生成报告

slug：`aiyuce-20261021-56`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11965
LLM 调用：57 次，累计 220.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的数字 | 1696 | normal | 38.0 | 0 |  | 1 |
| 2 | 校对软件运行界面 | 2666 | normal | 35.8 | 0 |  | 1 |
| 3 | 核对报价单数据 | 2126 | normal | 90.1 | 0 |  | 1 |
| 4 | 核对电脑折旧表 | 1887 | normal | 35.7 | 0 |  | 1 |
| 5 | 核对报价单数据 | 2232 | normal | 88.7 | 0 |  | 1 |
| 6 | 核对报价单数据 | 1352 | short | 80.2 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「如果有证据表明某个时间段内的电力消耗并未如预测那…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的证据推翻呢…」）
- 第 3 章：
  - dialogue_chars_pct 18.4 高于目标 18.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 标题重复：「核对报价单数据」已存在
- 第 6 章：
  - dialogue_chars_pct 43.3 高于目标 18.0
  - dialogue_run_mean 11 高于目标 4.0
  - narration_para_pct 8.3 低于目标 45.0
  - [observe] 标题重复：「核对报价单数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11670
chapter_chars_mean: 1945
chapter_chars_median: 1954
chapter_chars_cv: 0.23
paragraphs_mean: 16.5
dialogue_chars_pct: 12.7
dialogue_para_pct: 33.4
interiority_para_pct: 13.3
narration_para_pct: 53.3
turn_under20_pct: 40.1
turn_over200_pct: 0.0
attr_say_pct: 14.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 3.0
turn_len_median: 24
```
