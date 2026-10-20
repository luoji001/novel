# 磁带 生成报告

slug：`xiaoyuan-20261020-66`
档位：校园青春　闸门模式：observe
章数：9　总字数：19355
LLM 调用：100 次，累计 416.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 课表边缘的指纹 | 1279 | short | 98.1 | 0 |  | 0 |
| 2 | 课表边缘的指纹 | 2478 | normal | 85.7 | 0 |  | 5 |
| 3 | 未发送的短信 | 2387 | normal | 24.2 | 0 |  | 2 |
| 4 | 磁带的温度 | 2197 | normal | 0.0 | 0 |  | 2 |
| 5 | 磁带的温度 | 2253 | normal | 89.0 | 0 |  | 4 |
| 6 | 抚摸分科表边缘 | 2340 | normal | 90.8 | 0 |  | 3 |
| 7 | 纸片飘落的瞬间 | 2492 | normal | 55.8 | 0 |  | 3 |
| 8 | 抚摸课表边缘 | 2401 | normal | 89.7 | 0 |  | 4 |
| 9 | 磁带塞入书包的瞬间 | 1519 | short | 79.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「周子航的」×4、「林晚晴的」×3
  - dialogue_chars_pct 19.1 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 章内自我复读 19 句（如「陈老师抬头看了她一眼，“下周的课程安排有些调整，…」）
  - [observe] 标题重复：「课表边缘的指纹」已存在
- 第 3 章：
  - dialogue_chars_pct 10.9 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「她站起来的时候，桌面上那个未发送的短信记录突然变…」）
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「风掠过耳边，带来一点点清脆的声响，像是某种遥远的…」）
  - [observe] dialogue_chars_pct 6.7 < 8.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「林晚晴站在」×3、「周子航的」×3
  - narration_para_pct 13.6 低于目标 15.0
  - [observe] 章内自我复读 19 句（如「她低头看了看自己手中的作业本，里面还有几封没寄出…」）
  - [observe] 标题重复：「磁带的温度」已存在
- 第 6 章：
  - 单条套路句式超限：「林晚晴站在」×3
  - narration_para_pct 7.3 低于目标 15.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「林晚晴站在」×4、「带着一丝」×3
  - dialogue_chars_pct 14.7 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「她回头一看，看到的是另一个身影正朝这边走来，脸上…」）
- 第 8 章：
  - 单条套路句式超限：「林晚晴的」×4
  - [observe] 章内自我复读 14 句（如「陈老师一边说着，一边往桌上放了一杯热茶，“不过我…」）
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
  - [observe] 标题与《抚摸分科表边缘》近似 0.77 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「周子航的」×3
  - dialogue_chars_pct 13.8 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「林晚晴看着他胸前的工牌，突然想起上周他替她补习数…」）
  - [observe] attr_adv_pct 200.0 > 22.0（结构塌缩）

## 整书结构指标

```
chapters: 9
total_chars: 18515
chapter_chars_mean: 2057
chapter_chars_median: 2243
chapter_chars_cv: 0.21
paragraphs_mean: 38.9
dialogue_chars_pct: 18.6
dialogue_para_pct: 57.0
interiority_para_pct: 21.8
narration_para_pct: 21.2
turn_under20_pct: 88.3
turn_over200_pct: 0.0
attr_say_pct: 22.6
attr_adv_pct: 23.4
scenes_per_chapter: 3.4
dialogue_run_mean: 3.2
turn_len_median: 9
```
