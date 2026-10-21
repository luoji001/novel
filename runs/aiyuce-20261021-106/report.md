# 证书 生成报告

slug：`aiyuce-20261021-106`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13759
LLM 调用：57 次，累计 225.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对持证员工名单 | 2247 | normal | 38.1 | 0 |  | 1 |
| 2 | 核对持证员工名单 | 2969 | normal | 35.0 | 0 |  | 4 |
| 3 | 敲打桌面的手指 | 2381 | normal | 35.2 | 0 |  | 1 |
| 4 | 手指划过新增条目 | 2788 | normal | 86.7 | 0 |  | 0 |
| 5 | 手指划过单价涨幅 | 1876 | normal | 87.2 | 0 |  | 2 |
| 6 | 手指划过技术投入 | 1492 | short | 35.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 20.4 高于目标 18.0
  - narration_para_pct 26.9 低于目标 45.0
  - [observe] 章内自我复读 4 句（如「人事主管接过那份资料，仔细浏览了几页之后抬起头来…」）
  - [observe] 标题重复：「核对持证员工名单」已存在
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 22.2 高于目标 18.0
  - narration_para_pct 36.8 低于目标 45.0
- 第 6 章：
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 13466
chapter_chars_mean: 2244
chapter_chars_median: 2270
chapter_chars_cv: 0.24
paragraphs_mean: 16
dialogue_chars_pct: 8.8
dialogue_para_pct: 28.4
interiority_para_pct: 20.5
narration_para_pct: 51.1
turn_under20_pct: 72.4
turn_over200_pct: 0.0
attr_say_pct: 5.0
attr_adv_pct: 2.3
scenes_per_chapter: 1.3
dialogue_run_mean: 1.7
turn_len_median: 10
```
