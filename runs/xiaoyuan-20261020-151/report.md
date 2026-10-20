# 耳机线 生成报告

slug：`xiaoyuan-20261020-151`
档位：校园青春　闸门模式：observe
章数：9　总字数：21313
LLM 调用：100 次，累计 440.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 磁带滑落 | 1366 | short | 67.8 | 0 |  | 4 |
| 2 | 耳机线断裂 | 2696 | normal | 90.2 | 0 |  | 3 |
| 3 | 钥匙交出 | 2841 | normal | 83.3 | 0 |  | 4 |
| 4 | 耳机线缠绕 | 2832 | normal | 90.7 | 0 |  | 4 |
| 5 | 校服衣角轻颤 | 2491 | normal | 87.4 | 0 |  | 2 |
| 6 | 公告栏空白处 | 2513 | normal | 93.5 | 0 |  | 0 |
| 7 | 梧桐树下捡起准考证 | 2382 | normal | 93.5 | 0 |  | 0 |
| 8 | 纸条压在课本下 | 2650 | normal | 90.8 | 0 |  | 3 |
| 9 | 纸张飘入垃圾桶 | 1533 | short | 83.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 13.3 低于目标 20.0
  - interiority_para_pct 4.0 低于目标 8.0
  - dialogue_run_mean 1.2 低于目标 1.5
  - [observe] 章内自我复读 14 句（如「她只是轻轻地把磁带放回书包，然后抬头看向走廊尽头…」）
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「教务处」×4
  - [observe] 章内自我复读 14 句（如「下次播的时候，能不能不放那些什么‘愿你们在未来的…」）
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「教务处」×5、「带着一丝」×3
  - dialogue_chars_pct 17.3 低于目标 20.0
  - [observe] 章内自我复读 18 句（如「她展开来看，发现那是分班考的成绩单复印件，旁边有…」）
- 第 4 章：
  - 单条套路句式超限：「”周砚低」×3
  - [observe] 章内自我复读 11 句（如「于是，在那一瞬间，他们的目光交汇在一起，仿佛有什…」）
  - [observe] attr_adv_pct 22.6 > 22.0（结构塌缩）
  - [observe] 标题与《耳机线断裂》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「林夏站在」×3
  - dialogue_chars_pct 17.5 低于目标 20.0
- 第 8 章：
  - 单条套路句式超限：「知道自己」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 章内自我复读 2 句（如「听说这次难度比上次更高呢…」）
- 第 9 章：
  - dialogue_chars_pct 11.3 低于目标 20.0

## 整书结构指标

```
chapters: 9
total_chars: 20243
chapter_chars_mean: 2249
chapter_chars_median: 2385
chapter_chars_cv: 0.23
paragraphs_mean: 52
dialogue_chars_pct: 21.9
dialogue_para_pct: 62.2
interiority_para_pct: 14.0
narration_para_pct: 23.8
turn_under20_pct: 92.4
turn_over200_pct: 0.0
attr_say_pct: 29.3
attr_adv_pct: 4.5
scenes_per_chapter: 2.2
dialogue_run_mean: 2.7
turn_len_median: 9
```
