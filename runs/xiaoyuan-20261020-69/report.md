# 画室钥匙 生成报告

slug：`xiaoyuan-20261020-69`
档位：校园青春　闸门模式：observe
章数：9　总字数：21426
LLM 调用：100 次，累计 447.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕碎的课表边缘 | 1497 | short | 97.9 | 0 |  | 0 |
| 2 | 磁带边缘摩挲 | 2660 | normal | 91.9 | 0 |  | 3 |
| 3 | 钥匙链摩挲 | 3010 | normal | 89.7 | 0 |  | 4 |
| 4 | 校服外套 | 2774 | normal | 92.3 | 0 |  | 2 |
| 5 | 翻阅旧画册 | 2560 | normal | 89.5 | 0 |  | 2 |
| 6 | 雪落值日表 | 2257 | normal | 82.8 | 0 |  | 1 |
| 7 | 撕碎的课表边缘 | 2365 | normal | 92.3 | 0 |  | 2 |
| 8 | 翻阅旧年鉴 | 2570 | normal | 93.8 | 0 |  | 3 |
| 9 | 钥匙链摩挲 | 1724 | short | 94.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「中带着一丝」×3、「周子墨的」×3、「林夏站在」×3
  - narration_para_pct 10.2 低于目标 15.0
  - [observe] 章内自我复读 16 句（如「那是她在早上抄写的美院招生简章，里面有一句话让她…」）
- 第 3 章：
  - 单条套路句式超限：「知道自己」×3
  - narration_para_pct 13.1 低于目标 15.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 章内自我复读 19 句（如「陈老师沉默了一会儿，然后说：“如果你愿意，我可以…」）
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×3
  - narration_para_pct 10.7 低于目标 15.0
- 第 5 章：
  - 单条套路句式超限：「知道自己」×5、「林夏站在」×3
  - [observe] 章内自我复读 21 句（如「她知道，自己还有很长一段时间要面对这个选择，而此…」）
- 第 6 章：
  - [observe] 章内自我复读 37 句（如「她想起了上周放学时看到的情景——他在广播站附近徘…」）
- 第 7 章：
  - 单条套路句式超限：「“我不知道」×3
  - [observe] 标题重复：「撕碎的课表边缘」已存在
- 第 8 章：
  - 单条套路句式超限：「市重点中学」×26、「林夏点点」×3
  - narration_para_pct 12.3 低于目标 15.0
  - [observe] 标题与《翻阅旧画册》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - narration_para_pct 11.8 低于目标 15.0
  - [observe] 标题重复：「钥匙链摩挲」已存在

## 整书结构指标

```
chapters: 9
total_chars: 20370
chapter_chars_mean: 2263
chapter_chars_median: 2427
chapter_chars_cv: 0.21
paragraphs_mean: 51.4
dialogue_chars_pct: 27.5
dialogue_para_pct: 67.7
interiority_para_pct: 15.1
narration_para_pct: 17.2
turn_under20_pct: 88.6
turn_over200_pct: 0.0
attr_say_pct: 35.5
attr_adv_pct: 5.1
scenes_per_chapter: 2.8
dialogue_run_mean: 3.4
turn_len_median: 10
```
