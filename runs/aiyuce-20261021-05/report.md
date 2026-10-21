# 质检尺 生成报告

slug：`aiyuce-20261021-05`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11334
LLM 调用：57 次，累计 209.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对质检报告数据 | 2232 | normal | 38.2 | 0 |  | 1 |
| 2 | 划动预算表指腹 | 2102 | normal | 36.8 | 0 |  | 3 |
| 3 | 摩挲测试报告边缘 | 1936 | normal | 88.3 | 0 |  | 2 |
| 4 | 划掉工作经验条款 | 1886 | normal | 34.8 | 0 |  | 4 |
| 5 | 摩挲测试报告边缘 | 2039 | normal | 32.9 | 0 |  | 5 |
| 6 | 摩挲测试报告边缘 | 1133 | short | 35.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 21.1 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被客户满意度调查结果推翻…」）
- 第 3 章：
  - dialogue_chars_pct 23.4 高于目标 18.0
  - narration_para_pct 6.7 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 65.5 高于目标 18.0
  - dialogue_run_mean 4.8 高于目标 4.0
  - narration_para_pct 16.7 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「张慧提出了自己的疑问…」）
- 第 5 章：
  - dialogue_chars_pct 67.3 高于目标 18.0
  - dialogue_run_mean 6.3 高于目标 4.0
  - narration_para_pct 9.5 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果AI质检工具在2024年初达到了95%以上的…」）
  - [observe] 标题重复：「摩挲测试报告边缘」已存在
- 第 6 章：
  - dialogue_chars_pct 19.9 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「摩挲测试报告边缘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11022
chapter_chars_mean: 1837
chapter_chars_median: 1936
chapter_chars_cv: 0.21
paragraphs_mean: 17.7
dialogue_chars_pct: 34.2
dialogue_para_pct: 62.9
interiority_para_pct: 10.5
narration_para_pct: 26.6
turn_under20_pct: 46.4
turn_over200_pct: 0.0
attr_say_pct: 16.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 3.4
turn_len_median: 30
```
