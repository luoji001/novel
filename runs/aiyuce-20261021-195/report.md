# AI透视镜 生成报告

slug：`aiyuce-20261021-195`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12316
LLM 调用：53 次，累计 208.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | AI系统部署调试 | 2502 | normal | 37.9 | 0 |  | 1 |
| 2 | 博士学历门槛设定 | 2595 | normal | 35.6 | 0 |  | 2 |
| 3 | AI模型测试报告 | 1368 | normal | 91.1 | 0 |  | 0 |
| 4 | 博士学历门槛设定 | 2159 | normal | 85.6 | 0 |  | 2 |
| 5 | 翻阅测试报告 | 2285 | normal | 88.3 | 0 |  | 2 |
| 6 | 阅读招聘JD | 1401 | short | 35.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - 单条套路句式超限：「华西医院影像科」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - 单条套路句式超限：「华西医院影像科」×5
  - [observe] 标题重复：「博士学历门槛设定」已存在
- 第 5 章：
  - dialogue_chars_pct 22.1 高于目标 18.0
  - narration_para_pct 42.9 低于目标 45.0
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12040
chapter_chars_mean: 2007
chapter_chars_median: 2173
chapter_chars_cv: 0.27
paragraphs_mean: 14.8
dialogue_chars_pct: 5.5
dialogue_para_pct: 14.9
interiority_para_pct: 7.6
narration_para_pct: 77.5
turn_under20_pct: 62.0
turn_over200_pct: 0.0
attr_say_pct: 51.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 1.9
turn_len_median: 15
```
