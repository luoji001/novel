# 储物柜打开 生成报告

slug：`xiaoyuan-20261020-152`
档位：校园青春　闸门模式：observe
章数：9　总字数：20756
LLM 调用：100 次，累计 424.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手表滴答 | 1318 | short | 87.4 | 0 |  | 1 |
| 2 | 手电筒照亮旧本子 | 2677 | normal | 92.3 | 0 |  | 2 |
| 3 | 储物柜门缝隙透光 | 2511 | normal | 91.2 | 0 |  | 1 |
| 4 | 储物柜钥匙交接 | 2455 | normal | 89.2 | 0 |  | 1 |
| 5 | 储物柜空位痕迹 | 2635 | normal | 83.7 | 0 |  | 1 |
| 6 | 分科表复印件传递 | 2583 | normal | 90.2 | 0 |  | 3 |
| 7 | 笔记本划过指尖 | 2742 | normal | 83.3 | 0 |  | 3 |
| 8 | 笔记本划过指尖 | 2314 | normal | 90.0 | 0 |  | 2 |
| 9 | 校服外套归位 | 1512 | short | 83.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 17 句（如「她不知道这样做会不会被发现，但她知道，这一刻的默…」）
- 第 2 章：
  - 单条套路句式超限：「带着一丝」×3、「他知道这」×3、「林夏点点」×3
  - [observe] 章内自我复读 8 句（如「他看到上面密密麻麻地写着各种公式和计算步骤，每一…」）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
- 第 4 章：
  - 单条套路句式超限：「他知道这」×6、「他知道自己」×3
- 第 5 章：
  - [observe] 章内自我复读 36 句（如「她把磁带放进书包，转身走向储物柜，留下周朗一个人…」）
- 第 6 章：
  - 单条套路句式超限：「他知道这」×4、「点了点头」×3、「林夏站在」×3
  - interiority_para_pct 7.4 低于目标 8.0
  - narration_para_pct 10.3 低于目标 15.0
- 第 7 章：
  - 单条套路句式超限：「林夏点点」×4
  - narration_para_pct 8.2 低于目标 15.0
  - [observe] 章内自我复读 33 句（如「周朗摇摇头，目光扫过她放在旁边的一摞作业本，神情…」）
- 第 8 章：
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「笔记本划过指尖」已存在
- 第 9 章：
  - dialogue_chars_pct 15.5 低于目标 20.0
  - interiority_para_pct 7.1 低于目标 8.0

## 整书结构指标

```
chapters: 9
total_chars: 19700
chapter_chars_mean: 2189
chapter_chars_median: 2395
chapter_chars_cv: 0.23
paragraphs_mean: 50
dialogue_chars_pct: 26.0
dialogue_para_pct: 67.6
interiority_para_pct: 12.3
narration_para_pct: 20.0
turn_under20_pct: 88.5
turn_over200_pct: 0.0
attr_say_pct: 33.8
attr_adv_pct: 1.4
scenes_per_chapter: 1.6
dialogue_run_mean: 3.3
turn_len_median: 10
```
