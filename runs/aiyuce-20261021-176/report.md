# 校对钟 生成报告

slug：`aiyuce-20261021-176`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11881
LLM 调用：57 次，累计 216.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲打键盘的校对主管 | 1944 | normal | 38.8 | 0 |  | 2 |
| 2 | 凝视客户反馈表 | 2480 | normal | 89.8 | 0 |  | 1 |
| 3 | 凝视财务报表的数据 | 2269 | normal | 36.0 | 0 |  | 1 |
| 4 | 凝视测试报告数据 | 1764 | normal | 36.8 | 0 |  | 1 |
| 5 | 凝视测试报告数据 | 2126 | normal | 35.5 | 0 |  | 4 |
| 6 | 凝视客户反馈表 | 1292 | short | 33.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 28.6 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - 命中套话收尾句
  - narration_para_pct 41.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「凝视测试报告数据」已存在
- 第 6 章：
  - dialogue_chars_pct 45.3 高于目标 18.0
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的事实所推翻呢…」）
  - [observe] 标题重复：「凝视客户反馈表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11609
chapter_chars_mean: 1935
chapter_chars_median: 1988
chapter_chars_cv: 0.22
paragraphs_mean: 14.2
dialogue_chars_pct: 13.1
dialogue_para_pct: 48.5
interiority_para_pct: 12.2
narration_para_pct: 39.4
turn_under20_pct: 65.6
turn_over200_pct: 0.0
attr_say_pct: 11.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.0
turn_len_median: 16
```
