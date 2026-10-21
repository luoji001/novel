# 折旧表 生成报告

slug：`aiyuce-20261021-250`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12286
LLM 调用：57 次，累计 219.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 目光停留在JD文件上 | 2041 | normal | 37.6 | 0 |  | 4 |
| 2 | 目光停留在工资条上 | 2557 | normal | 34.8 | 0 |  | 2 |
| 3 | 抽查持证人员比例 | 2228 | normal | 58.1 | 0 |  | 0 |
| 4 | 目光停留在折旧表上 | 1964 | normal | 35.7 | 0 |  | 2 |
| 5 | 目光停留在合同上 | 2148 | normal | 36.0 | 0 |  | 3 |
| 6 | 目光停留在JD文件上 | 1342 | short | 35.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×4
  - interiority_para_pct 47.1 高于目标 40.0
  - narration_para_pct 17.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「必须持有国家职业资格证书…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「人事部主管拿起那张标注员的工资条，目光停留在“每…」）
  - [observe] 标题与《目光停留在JD文件上》近似 0.63 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《目光停留在工资条上》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「标注单价为每小时80元…」）
  - [observe] 标题与《目光停留在工资条上》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 44.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「然而，这条推论会被什么推翻呢…」）
  - [observe] 标题重复：「目光停留在JD文件上」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11994
chapter_chars_mean: 1999
chapter_chars_median: 2040
chapter_chars_cv: 0.2
paragraphs_mean: 15.3
dialogue_chars_pct: 3.7
dialogue_para_pct: 26.4
interiority_para_pct: 25.7
narration_para_pct: 47.9
turn_under20_pct: 95.3
turn_over200_pct: 0.0
attr_say_pct: 48.7
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.3
turn_len_median: 11
```
