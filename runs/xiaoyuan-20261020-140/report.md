# 笔记 生成报告

slug：`xiaoyuan-20261020-140`
档位：校园青春　闸门模式：observe
章数：9　总字数：20232
LLM 调用：100 次，累计 433.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕碎的课表 | 1493 | short | 97.0 | 0 |  | 0 |
| 2 | 磁带与提琴 | 2824 | normal | 95.2 | 0 |  | 3 |
| 3 | 撕碎的课表 | 2034 | normal | 87.5 | 0 |  | 3 |
| 4 | 课表残片的告别 | 2602 | normal | 90.7 | 0 |  | 2 |
| 5 | 笔记本的角落 | 2265 | normal | 89.8 | 0 |  | 3 |
| 6 | 拾起纸屑的瞬间 | 2528 | normal | 86.4 | 0 |  | 1 |
| 7 | 磁带与落叶 | 2558 | normal | 89.3 | 0 |  | 2 |
| 8 | 拾起纸屑的瞬间 | 2196 | normal | 89.8 | 0 |  | 4 |
| 9 | 折叠的排名单 | 1723 | short | 88.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「苏雨桐的」×3、「林晓阳的」×3
  - narration_para_pct 14.1 低于目标 15.0
  - attr_adv_pct 15.8 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「点了点头」×4、「苏雨桐的」×4
  - dialogue_chars_pct 17.9 低于目标 20.0
  - [observe] 标题重复：「撕碎的课表」已存在
- 第 4 章：
  - 单条套路句式超限：「苏雨桐的」×4、「“我不知道」×3、「苏雨桐点」×3
  - narration_para_pct 13.6 低于目标 15.0
- 第 5 章：
  - 单条套路句式超限：「”苏雨桐低」×4、「苏雨桐的」×3
  - interiority_para_pct 5.2 低于目标 8.0
  - narration_para_pct 8.6 低于目标 15.0
- 第 6 章：
  - [observe] 章内自我复读 16 句（如「陈老师轻轻笑了，“那你应该知道，分科表已经公布了…」）
- 第 7 章：
  - [observe] 章内自我复读 20 句（如「苏雨桐点头，“你知道吗，有时候换个角度思考问题，…」）
  - [observe] 标题与《磁带与提琴》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「“我不知道」×3、「为什么会」×3
  - narration_para_pct 12.7 低于目标 15.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「拾起纸屑的瞬间」已存在
- 第 9 章：
  - 单条套路句式超限：「林晓阳的」×4
  - [observe] 章内自我复读 16 句（如「她不知道自己为什么要这样做，但此刻的阳光透过窗户…」）

## 整书结构指标

```
chapters: 9
total_chars: 19152
chapter_chars_mean: 2128
chapter_chars_median: 2095
chapter_chars_cv: 0.2
paragraphs_mean: 49.2
dialogue_chars_pct: 30.9
dialogue_para_pct: 71.2
interiority_para_pct: 13.3
narration_para_pct: 15.5
turn_under20_pct: 87.3
turn_over200_pct: 0.0
attr_say_pct: 45.2
attr_adv_pct: 3.6
scenes_per_chapter: 2.7
dialogue_run_mean: 4.0
turn_len_median: 10
```
