# 水瓶 生成报告

slug：`xiaoyuan-20261020-19`
档位：校园青春　闸门模式：observe
章数：9　总字数：20406
LLM 调用：100 次，累计 447.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触摸课本的湿气 | 1492 | short | 87.9 | 0 |  | 1 |
| 2 | 分科表的边缘卷曲 | 2942 | normal | 89.1 | 0 |  | 3 |
| 3 | 笔记本的夹层秘密 | 2772 | normal | 84.2 | 0 |  | 2 |
| 4 | 磁带的录音 | 2582 | normal | 55.8 | 0 |  | 1 |
| 5 | 笔记本的夹层秘密 | 2324 | normal | 40.8 | 0 |  | 4 |
| 6 | 课表边缘的折痕 | 2068 | normal | 86.8 | 0 |  | 3 |
| 7 | 笔记本的铅笔印 | 2366 | normal | 92.1 | 0 |  | 1 |
| 8 | 银杏叶的夹层秘密 | 2305 | normal | 91.0 | 0 |  | 3 |
| 9 | 口袋里的小纸条 | 1546 | short | 78.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 14.1 低于目标 20.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「教务处」×6
  - [observe] 章内自我复读 18 句（如「她看到上面列满了各个班级的名单，其中就包括她所在…」）
- 第 3 章：
  - dialogue_chars_pct 16.6 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「新的座位表已经贴出来了…」）
- 第 4 章：
  - dialogue_chars_pct 14.7 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「他知道这」×4
  - dialogue_chars_pct 12.9 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「不是因为它代表着他即将要做的一件大事，而是因为它…」）
  - [observe] 标题重复：「笔记本的夹层秘密」已存在
- 第 6 章：
  - 单条套路句式超限：「林夏点点」×3
  - dialogue_chars_pct 18.8 低于目标 20.0
  - [observe] 章内自我复读 21 句（如「周野抱着一摞作业本走了进来，他的头发还带着晨露，…」）
- 第 7 章：
  - narration_para_pct 10.5 低于目标 15.0
- 第 8 章：
  - narration_para_pct 11.6 低于目标 15.0
  - [observe] 章内自我复读 17 句（如「林夏手指触碰到封面的瞬间，忽然想起上周放晴的傍晚…」）
  - [observe] 标题与《笔记本的夹层秘密》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - dialogue_chars_pct 12.6 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「陈老师的语气平静如常，仿佛早已习惯了这样的安排，…」）

## 整书结构指标

```
chapters: 9
total_chars: 19538
chapter_chars_mean: 2171
chapter_chars_median: 2216
chapter_chars_cv: 0.22
paragraphs_mean: 40.1
dialogue_chars_pct: 18.5
dialogue_para_pct: 56.5
interiority_para_pct: 17.8
narration_para_pct: 25.7
turn_under20_pct: 87.2
turn_over200_pct: 0.0
attr_say_pct: 28.8
attr_adv_pct: 3.5
scenes_per_chapter: 2.7
dialogue_run_mean: 2.6
turn_len_median: 10
```
