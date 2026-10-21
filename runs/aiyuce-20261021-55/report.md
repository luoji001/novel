# 代码镜像 生成报告

slug：`aiyuce-20261021-55`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12622
LLM 调用：57 次，累计 219.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 代码审查记录提交 | 2431 | normal | 38.1 | 0 |  | 1 |
| 2 | 代码审查报告提交 | 2298 | normal | 36.2 | 0 |  | 2 |
| 3 | 代码审查报告提交 | 2466 | normal | 87.4 | 0 |  | 2 |
| 4 | 提交代码审查报告 | 1797 | normal | 89.0 | 0 |  | 3 |
| 5 | 代码审查报告提交 | 2243 | normal | 34.0 | 0 |  | 3 |
| 6 | 翻动代码审查报告 | 1381 | short | 90.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的事实推翻呢…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《代码审查记录提交》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「智创科技有限公司的」×3
  - [observe] 标题重复：「代码审查报告提交」已存在
- 第 4 章：
  - dialogue_chars_pct 23.5 高于目标 18.0
  - narration_para_pct 36.8 低于目标 45.0
  - [observe] 标题与《代码审查报告提交》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「某科技公司技术部」×5
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「代码审查报告提交」已存在
- 第 6 章：
  - 命中套话收尾句
  - [observe] 标题与《提交代码审查报告》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12312
chapter_chars_mean: 2052
chapter_chars_median: 2214
chapter_chars_cv: 0.21
paragraphs_mean: 17.3
dialogue_chars_pct: 6.2
dialogue_para_pct: 17.7
interiority_para_pct: 8.6
narration_para_pct: 73.8
turn_under20_pct: 63.4
turn_over200_pct: 0.0
attr_say_pct: 29.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 1.5
turn_len_median: 20
```
