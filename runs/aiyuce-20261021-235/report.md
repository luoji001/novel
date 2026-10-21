# 代码修正 生成报告

slug：`aiyuce-20261021-235`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12204
LLM 调用：57 次，累计 216.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | AI筛选系统运行测试 | 2173 | normal | 37.6 | 0 |  | 2 |
| 2 | 实习生考核成绩表的填写 | 2038 | normal | 36.8 | 0 |  | 2 |
| 3 | 服务器日志异常排查 | 2197 | normal | 81.6 | 0 |  | 3 |
| 4 | 报销单的审核过程 | 2462 | normal | 90.2 | 0 |  | 0 |
| 5 | 文档草稿的修改讨论 | 1978 | normal | 36.1 | 0 |  | 1 |
| 6 | 文档草稿的修改讨论 | 1350 | short | 90.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 2 句（如「然而这条推论会被什么推翻呢…」）
- 第 2 章：
  - 单条套路句式超限：「广州某科技园区技术部办公室」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的证据所推翻呢…」）
- 第 3 章：
  - dialogue_chars_pct 40.3 高于目标 18.0
  - dialogue_run_mean 9 高于目标 4.0
  - narration_para_pct 13.6 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 标题重复：「文档草稿的修改讨论」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11918
chapter_chars_mean: 1986
chapter_chars_median: 2059
chapter_chars_cv: 0.18
paragraphs_mean: 14.7
dialogue_chars_pct: 10.9
dialogue_para_pct: 32.1
interiority_para_pct: 5.8
narration_para_pct: 62.1
turn_under20_pct: 50.8
turn_over200_pct: 0.0
attr_say_pct: 8.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 2.8
turn_len_median: 22
```
