# AI作文批改报告 生成报告

slug：`aiyuce-20261021-33`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11672
LLM 调用：57 次，累计 214.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 听课记录核查 | 1813 | normal | 36.9 | 0 |  | 1 |
| 2 | 误评率波动监测 | 2254 | normal | 35.9 | 0 |  | 3 |
| 3 | 听课记录核查 | 2133 | normal | 91.0 | 0 |  | 1 |
| 4 | 核对AI批改报告 | 1983 | normal | 34.6 | 0 |  | 2 |
| 5 | 核对年度预算报表 | 2187 | normal | 36.6 | 0 |  | 2 |
| 6 | 工作量统计表 | 1296 | short | 34.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「如果下周某个班级的听课记录未能及时提交或者存在严…」）
- 第 2 章：
  - dialogue_chars_pct 23.7 高于目标 18.0
  - narration_para_pct 31.6 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「他站在窗边望着操场上奔跑的孩子们，心中盘算着未来…」）
- 第 3 章：
  - [observe] 标题重复：「听课记录核查」已存在
- 第 4 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 38.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11384
chapter_chars_mean: 1897
chapter_chars_median: 2015
chapter_chars_cv: 0.18
paragraphs_mean: 15.3
dialogue_chars_pct: 11.7
dialogue_para_pct: 39.4
interiority_para_pct: 13.8
narration_para_pct: 46.8
turn_under20_pct: 48.3
turn_over200_pct: 0.0
attr_say_pct: 16.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.2
turn_len_median: 20
```
