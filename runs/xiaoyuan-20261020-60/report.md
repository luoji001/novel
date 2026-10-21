# 蓝本 生成报告

slug：`xiaoyuan-20261020-60`
档位：校园青春　闸门模式：observe
章数：9　总字数：20816
LLM 调用：100 次，累计 438.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 笔记本的归还时刻 | 1365 | short | 98.0 | 0 |  | 1 |
| 2 | 值日表上的名字 | 2688 | normal | 92.8 | 0 |  | 3 |
| 3 | 磁带滑向她手中 | 2266 | normal | 90.4 | 0 |  | 2 |
| 4 | 信纸飘落梧桐叶上 | 2247 | normal | 92.2 | 0 |  | 2 |
| 5 | 分科表的摊开瞬间 | 2203 | normal | 92.4 | 0 |  | 2 |
| 6 | 储物柜上的光斑 | 2560 | normal | 87.5 | 0 |  | 2 |
| 7 | 纸飞机落在掌心 | 2686 | normal | 92.5 | 0 |  | 3 |
| 8 | 冻疮与围巾流苏 | 3043 | normal | 85.0 | 0 |  | 3 |
| 9 | 笔记本的归还时刻 | 1749 | short | 93.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 50.0 > 22.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「林晓阳的」×4
  - interiority_para_pct 6.3 低于目标 8.0
  - narration_para_pct 7.9 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「苏雨桐点」×3、「苏雨桐的」×3
  - narration_para_pct 14.3 低于目标 15.0
- 第 4 章：
  - 单条套路句式超限：「带着一丝」×3、「苏雨桐的」×3、「林晓阳的」×3
  - narration_para_pct 14.9 低于目标 15.0
- 第 5 章：
  - 单条套路句式超限：「苏雨桐点」×3
  - interiority_para_pct 5.8 低于目标 8.0
- 第 6 章：
  - 单条套路句式超限：「林晓阳站在」×3
  - [observe] 章内自我复读 21 句（如「苏雨桐点点头，指尖轻轻碰了碰储物柜边沿，“不过你…」）
- 第 7 章：
  - 单条套路句式超限：「苏雨桐的」×4、「林晓阳的」×4
  - narration_para_pct 11.1 低于目标 15.0
  - [observe] attr_adv_pct 40.0 > 22.0（结构塌缩）
- 第 8 章：
  - 单条套路句式超限：「苏雨桐的」×5、「林晓阳的」×4、「林晓阳点点」×3
  - interiority_para_pct 6.7 低于目标 8.0
  - [observe] 章内自我复读 26 句（如「第一次是在图书馆，苏雨桐不小心碰掉了林晓阳的书，…」）
- 第 9 章：
  - 单条套路句式超限：「“我不知道」×3、「他知道这」×3、「高三（3）班」×3
  - interiority_para_pct 7.1 低于目标 8.0
  - [observe] 标题重复：「笔记本的归还时刻」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19680
chapter_chars_mean: 2187
chapter_chars_median: 2139
chapter_chars_cv: 0.23
paragraphs_mean: 54.9
dialogue_chars_pct: 31.6
dialogue_para_pct: 71.2
interiority_para_pct: 9.6
narration_para_pct: 19.2
turn_under20_pct: 87.4
turn_over200_pct: 0.0
attr_say_pct: 36.3
attr_adv_pct: 8.9
scenes_per_chapter: 2
dialogue_run_mean: 4.0
turn_len_median: 9
```
