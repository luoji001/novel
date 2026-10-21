# 电表 生成报告

slug：`aiyuce-20261021-209`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11005
LLM 调用：57 次，累计 216.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单与服务器能耗 | 1840 | normal | 37.6 | 0 |  | 1 |
| 2 | 修改招聘JD | 2051 | normal | 37.4 | 0 |  | 4 |
| 3 | 翻阅测试报告 | 1958 | normal | 33.3 | 0 |  | 4 |
| 4 | 检查绩效考核表 | 1985 | normal | 36.8 | 0 |  | 2 |
| 5 | 翻阅折旧表 | 1863 | normal | 35.6 | 0 |  | 2 |
| 6 | 误判率1.7%数据圈 | 1302 | short | 34.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - 单条套路句式超限：「他知道这」×4
  - dialogue_chars_pct 18.4 高于目标 18.0
  - narration_para_pct 23.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「监听录音并标注问题类型…」）
- 第 3 章：
  - dialogue_chars_pct 45.9 高于目标 18.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - narration_para_pct 31.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - 单条套路句式超限：「南京鼓楼区某外包客服公司办公室」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 20.7 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 10736
chapter_chars_mean: 1789
chapter_chars_median: 1864
chapter_chars_cv: 0.15
paragraphs_mean: 14.3
dialogue_chars_pct: 18.1
dialogue_para_pct: 44.7
interiority_para_pct: 9.4
narration_para_pct: 45.9
turn_under20_pct: 48.7
turn_over200_pct: 0.0
attr_say_pct: 34.9
attr_adv_pct: 5.2
scenes_per_chapter: 1.5
dialogue_run_mean: 2.4
turn_len_median: 22
```
