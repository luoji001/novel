# 折旧表 生成报告

slug：`aiyuce-20261021-46`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13138
LLM 调用：57 次，累计 223.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 修改招聘JD | 2542 | normal | 38.4 | 0 |  | 1 |
| 2 | 调整报价单参数 | 2480 | normal | 88.3 | 0 |  | 0 |
| 3 | 折旧表上的残值数字 | 2245 | normal | 89.2 | 0 |  | 0 |
| 4 | 电费单上的数字计算 | 1943 | normal | 35.2 | 0 |  | 1 |
| 5 | 核对招聘JD数据 | 2401 | normal | 90.5 | 0 |  | 0 |
| 6 | 核对招聘JD数据 | 1521 | short | 34.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被实际的用电数据变化所推翻，例如若在未…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对招聘JD数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12861
chapter_chars_mean: 2144
chapter_chars_median: 2280
chapter_chars_cv: 0.18
paragraphs_mean: 14.7
dialogue_chars_pct: 2.8
dialogue_para_pct: 18.5
interiority_para_pct: 23.6
narration_para_pct: 57.9
turn_under20_pct: 86.5
turn_over200_pct: 0.0
attr_say_pct: 37.4
attr_adv_pct: 37.4
scenes_per_chapter: 1.2
dialogue_run_mean: 1.2
turn_len_median: 10
```
