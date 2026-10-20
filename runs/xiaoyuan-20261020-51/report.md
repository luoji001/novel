# 纸条 生成报告

slug：`xiaoyuan-20261020-51`
档位：校园青春　闸门模式：observe
章数：9　总字数：20363
LLM 调用：100 次，累计 429.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 磁带藏进书包夹层 | 1492 | short | 94.2 | 0 |  | 1 |
| 2 | 公告栏边缘的纸屑 | 2424 | normal | 54.2 | 0 |  | 2 |
| 3 | 旧课表藏在储物柜 | 2444 | normal | 84.4 | 0 |  | 2 |
| 4 | 校服外套的领子 | 2537 | normal | 92.4 | 0 |  | 1 |
| 5 | 纸片贴上看台栏杆 | 2518 | normal | 1.7 | 0 |  | 2 |
| 6 | 脚印擦去落叶 | 2659 | normal | 90.1 | 0 |  | 2 |
| 7 | 旧唱片上的银杏叶 | 2124 | normal | 91.2 | 0 |  | 2 |
| 8 | 分科表边缘的灰尘 | 2517 | normal | 87.7 | 0 |  | 1 |
| 9 | 旧课表藏在储物柜 | 1639 | short | 86.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 3.0 低于目标 8.0
- 第 2 章：
  - dialogue_chars_pct 14.5 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「带着一丝」×3、「不仅仅是」×3
  - [observe] 章内自我复读 27 句（如「他只是默默地把课表收好，然后转过身，望向走廊尽头…」）
- 第 4 章：
  - 单条套路句式超限：「林夏点点」×3
- 第 5 章：
  - dialogue_chars_pct 8.2 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「她知道，有些东西不能说破，有些距离不必跨越，只要…」）
- 第 6 章：
  - dialogue_chars_pct 19.6 低于目标 20.0
  - [observe] 章内自我复读 6 句（如「周野没有立刻回答，而是走到长椅另一端，蹲下来仔细…」）
- 第 7 章：
  - interiority_para_pct 5.1 低于目标 8.0
  - narration_para_pct 10.3 低于目标 15.0
- 第 8 章：
  - [observe] 章内自我复读 15 句（如「她想起了昨天晚上在床上辗转反侧的画面，那些未能说…」）
- 第 9 章：
  - interiority_para_pct 3.3 低于目标 8.0
  - [observe] 章内自我复读 16 句（如「周野的目光移到她的手腕上，那里有道浅浅的擦伤，像…」）
  - [observe] 标题重复：「旧课表藏在储物柜」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19311
chapter_chars_mean: 2146
chapter_chars_median: 2328
chapter_chars_cv: 0.2
paragraphs_mean: 46.9
dialogue_chars_pct: 22.2
dialogue_para_pct: 62.8
interiority_para_pct: 14.8
narration_para_pct: 22.4
turn_under20_pct: 89.7
turn_over200_pct: 0.0
attr_say_pct: 33.2
attr_adv_pct: 3.2
scenes_per_chapter: 2.1
dialogue_run_mean: 3.6
turn_len_median: 9
```
