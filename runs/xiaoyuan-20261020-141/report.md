# 分科表 生成报告

slug：`xiaoyuan-20261020-141`
档位：校园青春　闸门模式：observe
章数：9　总字数：20702
LLM 调用：100 次，累计 447.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 分科表的褶皱 | 1413 | short | 93.2 | 0 |  | 1 |
| 2 | 触碰旧课本的指尖 | 2751 | normal | 89.8 | 0 |  | 1 |
| 3 | 触碰旧课本的指尖 | 2250 | normal | 86.4 | 0 |  | 3 |
| 4 | 触摸撕碎的纸片 | 2606 | normal | 91.8 | 0 |  | 2 |
| 5 | 藏在铁盒里的磁带 | 2774 | normal | 92.3 | 0 |  | 3 |
| 6 | 触碰笔记本的指尖 | 2640 | normal | 94.3 | 0 |  | 4 |
| 7 | 摩挲铁盒边缘的手指 | 2333 | normal | 91.2 | 0 |  | 2 |
| 8 | 翻阅旧课本的指尖 | 2214 | normal | 90.4 | 0 |  | 3 |
| 9 | 摩挲分科表边缘的手指 | 1712 | short | 89.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_run_mean 1.4 低于目标 1.5
- 第 2 章：
  - attr_adv_pct 13.3 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「苏念站在」×3
  - [observe] 章内自我复读 19 句（如「苏念的目光落在那些整齐排列的文件盒上，突然注意到…」）
  - [observe] 标题重复：「触碰旧课本的指尖」已存在
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 15.4 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「江远舟点」×3、「江远舟的」×3
  - narration_para_pct 14.8 低于目标 15.0
  - attr_adv_pct 12.5 高于目标 12.0
- 第 6 章：
  - narration_para_pct 12.2 低于目标 15.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 章内自我复读 2 句（如「真的吗？那你为什么不说出来呢？…」）
  - [observe] 标题与《触碰旧课本的指尖》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - narration_para_pct 7.1 低于目标 15.0
  - attr_adv_pct 12.5 高于目标 12.0
- 第 8 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 6 句（如「管理员阿姨微微一笑：“这是去年毕业的一个学生留下…」）
  - [observe] 标题与《触碰旧课本的指尖》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - [observe] 标题与《摩挲铁盒边缘的手指》近似 0.74 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 9
total_chars: 19679
chapter_chars_mean: 2187
chapter_chars_median: 2204
chapter_chars_cv: 0.21
paragraphs_mean: 47.2
dialogue_chars_pct: 27.3
dialogue_para_pct: 69.4
interiority_para_pct: 13.7
narration_para_pct: 16.9
turn_under20_pct: 88.7
turn_over200_pct: 0.0
attr_say_pct: 39.8
attr_adv_pct: 9.5
scenes_per_chapter: 2.1
dialogue_run_mean: 3.6
turn_len_median: 10
```
