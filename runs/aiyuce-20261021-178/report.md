# 刻度 生成报告

slug：`aiyuce-20261021-178`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11856
LLM 调用：57 次，累计 206.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指摩挲记录单 | 2102 | normal | 38.3 | 0 |  | 2 |
| 2 | 核对工资条数字 | 2309 | normal | 36.8 | 0 |  | 2 |
| 3 | 手指划过数据点 | 2395 | normal | 89.3 | 0 |  | 2 |
| 4 | 手指划过数据点 | 1821 | normal | 33.9 | 0 |  | 4 |
| 5 | 手指划过数据点 | 1894 | normal | 86.6 | 0 |  | 4 |
| 6 | 手指划过数据点 | 1329 | short | 35.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 41.2 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「如果有证据表明公司在未来几个月内会不得不削减预算…」）
- 第 2 章：
  - narration_para_pct 41.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 22.4 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 41.8 高于目标 18.0
  - narration_para_pct 22.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「手指划过数据点」已存在
- 第 5 章：
  - dialogue_chars_pct 44.8 高于目标 18.0
  - dialogue_run_mean 4.2 高于目标 4.0
  - narration_para_pct 15.4 低于目标 45.0
  - [observe] 标题重复：「手指划过数据点」已存在
- 第 6 章：
  - dialogue_chars_pct 52.8 高于目标 18.0
  - narration_para_pct 15.4 低于目标 45.0
  - [observe] 章内自我复读 4 句（如「李晓阳突然开口，“如果证书获取成本真的大幅上升，…」）
  - [observe] 标题重复：「手指划过数据点」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11528
chapter_chars_mean: 1921
chapter_chars_median: 1940
chapter_chars_cv: 0.2
paragraphs_mean: 19.3
dialogue_chars_pct: 30.6
dialogue_para_pct: 58.9
interiority_para_pct: 11.3
narration_para_pct: 29.8
turn_under20_pct: 46.5
turn_over200_pct: 0.0
attr_say_pct: 17.3
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 2.6
turn_len_median: 20
```
