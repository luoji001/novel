# 广播磁带 生成报告

slug：`xiaoyuan-20261020-33`
档位：校园青春　闸门模式：observe
章数：9　总字数：22307
LLM 调用：100 次，累计 461.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 分科表折痕 | 1342 | short | 44.0 | 0 |  | 2 |
| 2 | 旧磁带机上的红痕 | 3094 | normal | 95.2 | 0 |  | 3 |
| 3 | 校服外套留在课桌 | 2781 | normal | 87.1 | 0 |  | 2 |
| 4 | 耳机线缠绕指尖 | 2441 | normal | 92.7 | 0 |  | 1 |
| 5 | 作业本上的小人儿 | 2905 | normal | 84.1 | 0 |  | 2 |
| 6 | 手表滴答声 | 2644 | normal | 92.4 | 0 |  | 2 |
| 7 | 笔记本上的裂纹 | 2469 | normal | 92.3 | 0 |  | 0 |
| 8 | 耳机线缠绕指尖 | 2759 | normal | 87.9 | 0 |  | 4 |
| 9 | 纸条飘落 | 1863 | short | 91.1 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 12.4 低于目标 20.0
  - [observe] 章内自我复读 23 句（如「周野的声音混杂着广播站播放的钢琴曲，他在讲台旁边…」）
- 第 2 章：
  - 单条套路句式超限：「林夏站在」×3
  - interiority_para_pct 7.5 低于目标 8.0
  - [observe] 章内自我复读 2 句（如「因为你总是最后一个离开广播站…」）
- 第 3 章：
  - dialogue_chars_pct 19.4 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「他笑了笑，“有时候是你忘了带钥匙，有时候是钥匙没…」）
- 第 4 章：
  - narration_para_pct 14.7 低于目标 15.0
- 第 5 章：
  - 单条套路句式超限：「林夏点点」×4、「说道“我」×3
  - [observe] 章内自我复读 41 句（如「教室里只剩下钟声依旧静静地回荡着，而在他们心底，…」）
- 第 6 章：
  - 单条套路句式超限：「教务处」×5、「林夏点点」×4
  - narration_para_pct 10.9 低于目标 15.0
- 第 8 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林夏站在」×5
  - [observe] 章内自我复读 18 句（如「林夏站在原地，看着他专注的表情，忽然觉得，有些事…」）
  - [observe] 标题重复：「耳机线缠绕指尖」已存在

## 整书结构指标

```
chapters: 9
total_chars: 21147
chapter_chars_mean: 2350
chapter_chars_median: 2521
chapter_chars_cv: 0.22
paragraphs_mean: 56.7
dialogue_chars_pct: 28.0
dialogue_para_pct: 68.0
interiority_para_pct: 12.9
narration_para_pct: 19.1
turn_under20_pct: 89.9
turn_over200_pct: 0.0
attr_say_pct: 35.9
attr_adv_pct: 3.6
scenes_per_chapter: 2.7
dialogue_run_mean: 3.2
turn_len_median: 9
```
