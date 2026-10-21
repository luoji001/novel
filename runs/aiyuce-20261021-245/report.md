# 质检手册 生成报告

slug：`aiyuce-20261021-245`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11768
LLM 调用：57 次，累计 213.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 查看通话量统计表 | 2260 | normal | 95.8 | 0 |  | 1 |
| 2 | 测试报告上的准确率数据 | 2284 | normal | 34.2 | 0 |  | 3 |
| 3 | 递交裁员通知 | 1799 | normal | 78.1 | 0 |  | 3 |
| 4 | 客户投诉率分析表 | 1869 | normal | 81.5 | 0 |  | 3 |
| 5 | 修改招聘JD的笔尖 | 2172 | normal | 89.9 | 0 |  | 3 |
| 6 | 测试报告上的准确率数据 | 1378 | short | 80.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 43.5 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 33.6 高于目标 18.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 65.6 高于目标 18.0
  - dialogue_run_mean 9 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 44.6 高于目标 18.0
  - dialogue_run_mean 5.7 高于目标 4.0
  - narration_para_pct 19.0 低于目标 45.0
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 18.2 高于目标 18.0
  - narration_para_pct 28.0 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 74.4 高于目标 18.0
  - dialogue_run_mean 16 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「测试报告上的准确率数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11411
chapter_chars_mean: 1902
chapter_chars_median: 1958
chapter_chars_cv: 0.18
paragraphs_mean: 20.8
dialogue_chars_pct: 39.1
dialogue_para_pct: 70.8
interiority_para_pct: 7.1
narration_para_pct: 22.1
turn_under20_pct: 40.1
turn_over200_pct: 0.0
attr_say_pct: 15.0
attr_adv_pct: 6.4
scenes_per_chapter: 2.2
dialogue_run_mean: 6.5
turn_len_median: 28
```
