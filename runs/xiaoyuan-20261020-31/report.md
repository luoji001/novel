# 旧磁带 生成报告

slug：`xiaoyuan-20261020-31`
档位：校园青春　闸门模式：observe
章数：9　总字数：20566
LLM 调用：100 次，累计 436.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙与磁带的重逢 | 1546 | short | 98.3 | 0 |  | 1 |
| 2 | 蓝色笔记本的发现 | 2489 | normal | 91.2 | 0 |  | 0 |
| 3 | 旧磁带的播放 | 2510 | normal | 87.8 | 0 |  | 1 |
| 4 | 校服外套的归还 | 2952 | normal | 92.0 | 0 |  | 1 |
| 5 | 钥匙与磁带的重逢 | 2225 | normal | 91.9 | 0 |  | 4 |
| 6 | 折叠地图的触碰 | 2504 | normal | 91.1 | 0 |  | 1 |
| 7 | 课表的更新 | 2569 | normal | 93.2 | 0 |  | 1 |
| 8 | 缝补校服的指尖 | 2281 | normal | 93.2 | 0 |  | 1 |
| 9 | 分科表上的缝线痕迹 | 1481 | short | 45.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 6.0 低于目标 8.0
- 第 3 章：
  - dialogue_chars_pct 17.7 低于目标 20.0
- 第 4 章：
  - narration_para_pct 14.9 低于目标 15.0
- 第 5 章：
  - interiority_para_pct 6.6 低于目标 8.0
  - narration_para_pct 13.1 低于目标 15.0
  - [observe] 章内自我复读 3 句（如「因为它让我想起我们初见的那个午后…」）
  - [observe] 标题重复：「钥匙与磁带的重逢」已存在
- 第 6 章：
  - 单条套路句式超限：「林夏站在」×3、「林夏点点」×3
- 第 7 章：
  - 单条套路句式超限：「知道自己」×4、「林夏站在」×4
- 第 8 章：
  - narration_para_pct 9.5 低于目标 15.0
- 第 9 章：
  - 单条套路句式超限：「林夏点点」×4、「带着一丝」×3、「教务处」×3
  - narration_para_pct 3.4 低于目标 15.0
  - [observe] 章内自我复读 13 句（如「她忽然想起上周整理储物柜的时候，在一个角落发现了…」）

## 整书结构指标

```
chapters: 9
total_chars: 19497
chapter_chars_mean: 2166
chapter_chars_median: 2367
chapter_chars_cv: 0.22
paragraphs_mean: 50
dialogue_chars_pct: 25.5
dialogue_para_pct: 66.5
interiority_para_pct: 15.1
narration_para_pct: 18.4
turn_under20_pct: 86.6
turn_over200_pct: 0.0
attr_say_pct: 33.0
attr_adv_pct: 0.6
scenes_per_chapter: 2.8
dialogue_run_mean: 3.6
turn_len_median: 10
```
