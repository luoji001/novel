# 胶片的归宿 生成报告

slug：`shipin-20261027-207`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6308
LLM 调用：57 次，累计 130.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触摸胶片边缘 | 721 | short | 40.1 | 0 |  | 2 |
| 2 | 抚摸胶片标签 | 1142 | normal | 88.5 | 0 |  | 1 |
| 3 | 钥匙转动的瞬间 | 894 | normal | 19.4 | 0 |  | 2 |
| 4 | 触摸电影票根边缘 | 1190 | normal | 88.9 | 0 |  | 0 |
| 5 | 触摸胶片标签 | 1177 | normal | 90.5 | 0 |  | 2 |
| 6 | 触摸胶片标签 | 1178 | normal | 34.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 96.7 高于目标 90.0
- 第 2 章：
  - interiority_para_pct 8.0 高于目标 6.0
- 第 3 章：
  - dialogue_chars_pct 2.1 低于目标 5.0
  - [observe] 章节过短 845 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - narration_para_pct 31.6 低于目标 35.0
  - [observe] 标题与《抚摸胶片标签》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - interiority_para_pct 8.0 高于目标 6.0
  - [observe] 章内自我复读 1 句（如「这是父亲留下的东西，我不能让它消失…」）
  - [observe] 标题重复：「触摸胶片标签」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5922
chapter_chars_mean: 987
chapter_chars_median: 1096
chapter_chars_cv: 0.2
paragraphs_mean: 24
dialogue_chars_pct: 14.6
dialogue_para_pct: 40.5
interiority_para_pct: 4.0
narration_para_pct: 55.5
turn_under20_pct: 91.1
turn_over200_pct: 0.0
attr_say_pct: 49.5
attr_adv_pct: 0.0
scenes_per_chapter: 2.5
dialogue_run_mean: 1.9
turn_len_median: 10
```
