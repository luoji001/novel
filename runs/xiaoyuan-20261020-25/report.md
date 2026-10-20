# 分科表 生成报告

slug：`xiaoyuan-20261020-25`
档位：校园青春　闸门模式：observe
章数：9　总字数：20400
LLM 调用：100 次，累计 431.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 笔记本上的槐花 | 1256 | short | 37.9 | 0 |  | 2 |
| 2 | 袖口的粉笔灰 | 2540 | normal | 96.6 | 0 |  | 2 |
| 3 | 名单上的空白位置 | 2293 | normal | 94.1 | 0 |  | 3 |
| 4 | 磁带的播放 | 2782 | normal | 91.2 | 0 |  | 1 |
| 5 | 笔记本的最后一页 | 2758 | normal | 86.8 | 0 |  | 4 |
| 6 | 借条的揉皱 | 2429 | normal | 93.0 | 0 |  | 2 |
| 7 | 分科表的张贴 | 2357 | normal | 94.1 | 0 |  | 2 |
| 8 | 撕掉最后一页的笔记本 | 2503 | normal | 92.6 | 0 |  | 3 |
| 9 | 磁带的播放 | 1473 | short | 85.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「苏怀远点」×3、「苏怀远的」×3、「发现自己」×3
  - [observe] 章内自我复读 18 句（如「林晓棠抬头看他一眼，又迅速移回视线，假装不经意地…」）
- 第 2 章：
  - 单条套路句式超限：「苏怀远的」×3、「林晓棠的」×3
  - narration_para_pct 13.8 低于目标 15.0
- 第 3 章：
  - interiority_para_pct 7.8 低于目标 8.0
  - narration_para_pct 9.8 低于目标 15.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「苏怀远的」×4、「林晓棠站在」×3
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「“我不知道」×4
  - narration_para_pct 11.4 低于目标 15.0
  - [observe] 章内自我复读 20 句（如「你知道吗？我最近一直在想，如果当时我没有那么固执…」）
- 第 6 章：
  - 单条套路句式超限：「苏怀远的」×4、「带着一丝」×3
  - narration_para_pct 5.6 低于目标 15.0
- 第 7 章：
  - 单条套路句式超限：「苏怀远的」×4
  - narration_para_pct 1.9 低于目标 15.0
- 第 8 章：
  - 单条套路句式超限：「林晓棠站在」×3
  - narration_para_pct 14.8 低于目标 15.0
  - attr_adv_pct 15.8 高于目标 12.0
- 第 9 章：
  - dialogue_chars_pct 14.2 低于目标 20.0
  - [observe] 标题重复：「磁带的播放」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19323
chapter_chars_mean: 2147
chapter_chars_median: 2308
chapter_chars_cv: 0.24
paragraphs_mean: 52.1
dialogue_chars_pct: 32.0
dialogue_para_pct: 73.6
interiority_para_pct: 13.7
narration_para_pct: 12.7
turn_under20_pct: 88.8
turn_over200_pct: 0.0
attr_say_pct: 34.3
attr_adv_pct: 5.9
scenes_per_chapter: 2.1
dialogue_run_mean: 3.8
turn_len_median: 9
```
