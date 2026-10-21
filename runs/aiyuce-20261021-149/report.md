# 数据茧房 生成报告

slug：`aiyuce-20261021-149`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12313
LLM 调用：53 次，累计 216.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅2023年招聘JD | 2310 | normal | 38.4 | 0 |  | 1 |
| 2 | 拨打客服坐席电话 | 2845 | normal | 35.2 | 0 |  | 2 |
| 3 | AI质检工具的测试报告 | 1460 | normal | 57.9 | 0 |  | 0 |
| 4 | 核对考勤表数据 | 2265 | normal | 35.1 | 0 |  | 1 |
| 5 | 翻阅财务报表数据 | 2220 | normal | 88.3 | 0 |  | 2 |
| 6 | 翻阅财务报表数据 | 1207 | short | 81.3 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 4 句（如「这一刻让他更加坚定了自己的看法——虽然目前只能依…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 19.6 高于目标 18.0
  - narration_para_pct 44.4 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 69.7 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 7.1 低于目标 45.0
  - [observe] 标题重复：「翻阅财务报表数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12046
chapter_chars_mean: 2008
chapter_chars_median: 2198
chapter_chars_cv: 0.3
paragraphs_mean: 13.3
dialogue_chars_pct: 12.4
dialogue_para_pct: 31.0
interiority_para_pct: 18.9
narration_para_pct: 50.1
turn_under20_pct: 60.9
turn_over200_pct: 0.0
attr_say_pct: 3.1
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 2.6
turn_len_median: 15
```
