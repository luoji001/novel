# AI初筛 生成报告

slug：`aiyuce-20261021-207`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13210
LLM 调用：57 次，累计 229.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对预算表数据 | 2480 | normal | 94.8 | 0 |  | 1 |
| 2 | 敲击桌面计算数字 | 2237 | normal | 91.3 | 0 |  | 1 |
| 3 | 敲击桌面计算数字 | 1791 | normal | 34.3 | 0 |  | 4 |
| 4 | 修改招聘JD | 2993 | normal | 35.3 | 0 |  | 1 |
| 5 | 核对预算表数据 | 2381 | normal | 35.6 | 0 |  | 2 |
| 6 | 核对预算表数据 | 1322 | short | 85.2 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 46.2 高于目标 40.0
- 第 2 章：
  - narration_para_pct 43.8 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 33.3 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「这时，李明的目光落在那份详细列出的服务内容上，似…」）
  - [observe] 标题重复：「敲击桌面计算数字」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对预算表数据」已存在
- 第 6 章：
  - 命中套话收尾句
  - dialogue_chars_pct 34.8 高于目标 18.0
  - narration_para_pct 15.4 低于目标 45.0
  - [observe] 标题重复：「核对预算表数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12913
chapter_chars_mean: 2152
chapter_chars_median: 2260
chapter_chars_cv: 0.27
paragraphs_mean: 16.7
dialogue_chars_pct: 12.0
dialogue_para_pct: 34.3
interiority_para_pct: 20.0
narration_para_pct: 45.7
turn_under20_pct: 51.7
turn_over200_pct: 0.0
attr_say_pct: 15.5
attr_adv_pct: 2.4
scenes_per_chapter: 1.5
dialogue_run_mean: 2.2
turn_len_median: 19
```
