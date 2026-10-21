# 代码审查报告 生成报告

slug：`aiyuce-20261021-115`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12156
LLM 调用：57 次，累计 209.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 张伟查看招聘JD | 2236 | normal | 38.7 | 0 |  | 2 |
| 2 | 张伟查看薪资条 | 2134 | normal | 35.2 | 0 |  | 2 |
| 3 | 代码审查报告修正 | 2063 | normal | 36.2 | 0 |  | 2 |
| 4 | 服务器折旧表更新 | 2178 | normal | 90.4 | 0 |  | 0 |
| 5 | 代码审查报告修正 | 2092 | normal | 34.8 | 0 |  | 5 |
| 6 | 代码审查报告修正 | 1447 | short | 86.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 1 句（如「如果张伟最终能够成功通过试用期并获得转正机会，那…」）
- 第 2 章：
  - narration_para_pct 5.6 低于目标 45.0
  - [observe] 章内自我复读 5 句（如「正如这张纸上所写的那样，“月工资：15,000元…」）
- 第 3 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - 单条套路句式超限：「点了点头」×3
  - dialogue_chars_pct 23.6 高于目标 18.0
  - narration_para_pct 34.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「代码审查报告修正」已存在
- 第 6 章：
  - dialogue_chars_pct 30.6 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 标题重复：「代码审查报告修正」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11839
chapter_chars_mean: 1973
chapter_chars_median: 2054
chapter_chars_cv: 0.14
paragraphs_mean: 18
dialogue_chars_pct: 12.9
dialogue_para_pct: 37.2
interiority_para_pct: 25.3
narration_para_pct: 37.4
turn_under20_pct: 66.9
turn_over200_pct: 0.0
attr_say_pct: 19.7
attr_adv_pct: 15.6
scenes_per_chapter: 2.5
dialogue_run_mean: 1.6
turn_len_median: 16
```
