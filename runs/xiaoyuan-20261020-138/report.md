# 分科表 生成报告

slug：`xiaoyuan-20261020-138`
档位：校园青春　闸门模式：observe
章数：9　总字数：20906
LLM 调用：100 次，累计 446.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 袖口褶皱 | 1525 | short | 97.9 | 0 |  | 3 |
| 2 | 摩挲铁皮公告栏 | 2429 | normal | 85.3 | 0 |  | 3 |
| 3 | 摩挲分科表草稿 | 2630 | normal | 86.3 | 0 |  | 3 |
| 4 | 摩挲校服袖口线头 | 2813 | normal | 91.7 | 0 |  | 2 |
| 5 | 摩挲课表褶皱 | 2430 | normal | 89.4 | 0 |  | 2 |
| 6 | 摩挲磁带划痕 | 2676 | normal | 91.8 | 0 |  | 1 |
| 7 | 摩挲分科表边缘 | 2067 | normal | 88.2 | 0 |  | 3 |
| 8 | 摩挲校服袖口线头 | 2690 | normal | 91.7 | 0 |  | 1 |
| 9 | 摩挲课表褶皱 | 1637 | short | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 5.7 低于目标 8.0
  - narration_para_pct 14.3 低于目标 15.0
  - [observe] 章内自我复读 1 句（如「5月20日发放分科表…」）
- 第 2 章：
  - 单条套路句式超限：「点了点头」×4、「就在这时」×3、「带着一丝」×3
  - dialogue_chars_pct 19.9 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「陈老师的声音带着一丝疲惫，手里还拿着粉笔，在纸面…」）
- 第 3 章：
  - 单条套路句式超限：「就在这时」×3
  - narration_para_pct 8.9 低于目标 15.0
  - [observe] 章内自我复读 19 句（如「然后他像是突然想起来似的，又补充了一句，“不过，…」）
- 第 4 章：
  - 单条套路句式超限：「苏婉秋的」×6、「他知道自己」×3
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「点了点头」×4
  - narration_para_pct 14.0 低于目标 15.0
- 第 6 章：
  - 单条套路句式超限：「点了点头」×3、「陆子航点」×3
- 第 7 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 章内自我复读 6 句（如「陈老师看着他，似乎想要说什么，但最终只是拍了拍他…」）
  - [observe] 标题与《摩挲分科表草稿》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - [observe] 标题重复：「摩挲校服袖口线头」已存在
- 第 9 章：
  - [observe] attr_adv_pct 40.0 > 22.0（结构塌缩）
  - [observe] 标题重复：「摩挲课表褶皱」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19860
chapter_chars_mean: 2207
chapter_chars_median: 2320
chapter_chars_cv: 0.21
paragraphs_mean: 49.2
dialogue_chars_pct: 28.9
dialogue_para_pct: 67.7
interiority_para_pct: 16.1
narration_para_pct: 16.1
turn_under20_pct: 86.6
turn_over200_pct: 0.0
attr_say_pct: 27.6
attr_adv_pct: 9.8
scenes_per_chapter: 1.7
dialogue_run_mean: 3.3
turn_len_median: 9
```
