# 代码审查表 生成报告

slug：`aiyuce-20261021-67`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11978
LLM 调用：57 次，累计 210.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 试用期进度表核查 | 2303 | normal | 95.5 | 0 |  | 1 |
| 2 | 测试报告核对 | 2330 | normal | 36.6 | 0 |  | 1 |
| 3 | JD文件修改调整 | 1932 | normal | 90.9 | 0 |  | 1 |
| 4 | 流程表边缘标记 | 1945 | normal | 91.0 | 0 |  | 1 |
| 5 | 代码审查流程表调整 | 2014 | normal | 35.9 | 0 |  | 1 |
| 6 | 代码测试报告审阅 | 1448 | short | 92.5 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 35.7 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 37.5 低于目标 45.0
- 第 4 章：
  - narration_para_pct 43.8 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11698
chapter_chars_mean: 1950
chapter_chars_median: 1934
chapter_chars_cv: 0.16
paragraphs_mean: 15
dialogue_chars_pct: 8.4
dialogue_para_pct: 34.3
interiority_para_pct: 19.3
narration_para_pct: 46.5
turn_under20_pct: 64.9
turn_over200_pct: 0.0
attr_say_pct: 12.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.4
turn_len_median: 14
```
