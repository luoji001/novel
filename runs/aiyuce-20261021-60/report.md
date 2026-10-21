# 电磁模型 生成报告

slug：`aiyuce-20261021-60`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13642
LLM 调用：57 次，累计 237.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻看成绩统计表 | 2443 | normal | 94.6 | 0 |  | 0 |
| 2 | 核对图纸参数 | 2285 | normal | 89.8 | 0 |  | 1 |
| 3 | 核对折旧计算表 | 3028 | normal | 89.1 | 0 |  | 0 |
| 4 | 修改岗位说明书 | 2648 | normal | 35.5 | 0 |  | 1 |
| 5 | 核对原材料需求表 | 1964 | normal | 36.0 | 0 |  | 1 |
| 6 | 翻看成绩统计表 | 1268 | short | 87.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 33.3 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 7 句（如「如果新供应商能够在两天内顺利送达所需材料，并且订…」）
- 第 6 章：
  - interiority_para_pct 50.0 高于目标 40.0
  - [observe] 标题重复：「翻看成绩统计表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 13376
chapter_chars_mean: 2229
chapter_chars_median: 2318
chapter_chars_cv: 0.27
paragraphs_mean: 14.2
dialogue_chars_pct: 4.2
dialogue_para_pct: 22.2
interiority_para_pct: 22.6
narration_para_pct: 55.2
turn_under20_pct: 68.2
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 16.1
scenes_per_chapter: 1.3
dialogue_run_mean: 1.1
turn_len_median: 14
```
