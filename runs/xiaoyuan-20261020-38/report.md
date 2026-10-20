# 铁皮桶 生成报告

slug：`xiaoyuan-20261020-38`
档位：校园青春　闸门模式：observe
章数：9　总字数：20278
LLM 调用：100 次，累计 424.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 贴错的分科表 | 1347 | short | 96.6 | 0 |  | 0 |
| 2 | 摩挲笔记本的指尖 | 2195 | normal | 94.1 | 0 |  | 1 |
| 3 | 食堂的铁皮桶 | 2828 | normal | 85.8 | 0 |  | 3 |
| 4 | 铁皮桶里的磁带 | 2312 | normal | 93.7 | 0 |  | 1 |
| 5 | 摩挲手表的手指 | 2348 | normal | 92.1 | 0 |  | 1 |
| 6 | 摩挲书包夹层的手指 | 2847 | normal | 86.1 | 0 |  | 4 |
| 7 | 食堂的铁皮桶 | 2240 | normal | 91.4 | 0 |  | 2 |
| 8 | 摩挲借条的指尖 | 2533 | normal | 93.2 | 0 |  | 4 |
| 9 | 摩挲饭票的指尖 | 1619 | short | 85.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 4.4 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「带着一丝」×3
  - attr_adv_pct 15.8 高于目标 12.0
  - [observe] 章内自我复读 34 句（如「当他回到教室时，看见桌上摆着一些早餐食物，那是林…」）
- 第 4 章：
  - 单条套路句式超限：「周晓阳点」×3、「他知道这」×3
- 第 5 章：
  - [observe] attr_adv_pct 29.4 > 22.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「林子安的」×9、「他知道这」×4
  - narration_para_pct 11.1 低于目标 15.0
  - [observe] 章内自我复读 34 句（如「而在林子安的眼中，这张简单的课表仿佛变成了一块巨…」）
  - [observe] 标题与《摩挲手表的手指》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - dialogue_chars_pct 19.0 低于目标 20.0
  - [observe] 标题重复：「食堂的铁皮桶」已存在
- 第 8 章：
  - 单条套路句式超限：「周晓阳的」×4
  - narration_para_pct 14.8 低于目标 15.0
  - [observe] attr_adv_pct 37.5 > 22.0（结构塌缩）
  - [observe] 标题与《摩挲笔记本的指尖》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「他知道这」×3、「林子安的」×3
  - narration_para_pct 10.5 低于目标 15.0
  - [observe] 章内自我复读 13 句（如「林子安的手指在裤兜里握紧了饭票，忽然想起来昨天下…」）
  - [observe] 标题与《摩挲借条的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 9
total_chars: 19192
chapter_chars_mean: 2132
chapter_chars_median: 2169
chapter_chars_cv: 0.22
paragraphs_mean: 52.3
dialogue_chars_pct: 27.2
dialogue_para_pct: 66.4
interiority_para_pct: 15.5
narration_para_pct: 18.0
turn_under20_pct: 86.6
turn_over200_pct: 0.0
attr_say_pct: 26.9
attr_adv_pct: 12.9
scenes_per_chapter: 3
dialogue_run_mean: 3.5
turn_len_median: 9
```
