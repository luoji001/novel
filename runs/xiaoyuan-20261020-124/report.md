# 钥匙 生成报告

slug：`xiaoyuan-20261020-124`
档位：校园青春　闸门模式：observe
章数：9　总字数：22261
LLM 调用：100 次，累计 458.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 等待分科表的清晨 | 1943 | short | 97.8 | 0 |  | 3 |
| 2 | 磁带散落的黄昏 | 2786 | normal | 92.1 | 0 |  | 2 |
| 3 | 分科表被划去的瞬间 | 2655 | normal | 88.8 | 0 |  | 3 |
| 4 | 手抚公告栏的微光 | 2494 | normal | 89.0 | 0 |  | 2 |
| 5 | 钥匙与未贴的分科表 | 2333 | normal | 90.3 | 0 |  | 2 |
| 6 | 飞鸟集的便签 | 2799 | normal | 91.4 | 0 |  | 1 |
| 7 | 病历单上的银杏叶 | 2643 | normal | 91.3 | 0 |  | 3 |
| 8 | 摩挲失业证明的指尖 | 2928 | normal | 0.8 | 0 |  | 3 |
| 9 | 分科表飘落的瞬间 | 1671 | short | 92.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林小满的」×7、「周子航的」×5
  - narration_para_pct 6.5 低于目标 15.0
  - attr_adv_pct 15.4 高于目标 12.0
- 第 2 章：
  - narration_para_pct 12.3 低于目标 15.0
  - attr_adv_pct 15.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「周子航的」×4、「他知道这」×4、「“我不知道」×3
  - [observe] 章内自我复读 20 句（如「林小满犹豫了一瞬，最终还是说出了口，“可是上周我…」）
  - [observe] attr_adv_pct 28.6 > 22.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「周子航点」×3、「他知道这」×3
  - dialogue_chars_pct 17.2 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「林小满站在」×4、「林小满的」×3
  - [observe] attr_adv_pct 22.2 > 22.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「周子航的」×8、「周子航点」×4、「带着一丝」×3
- 第 7 章：
  - 单条套路句式超限：「周子航点」×4、「”周子航低」×3
  - narration_para_pct 14.5 低于目标 15.0
  - [observe] 章内自我复读 20 句（如「周子航低头看着手中的病历单，手指无意识地摩挲着纸…」）
- 第 8 章：
  - 单条套路句式超限：「知道自己」×3
  - dialogue_chars_pct 8.1 低于目标 20.0
  - interiority_para_pct 38.1 高于目标 35.0
- 第 9 章：
  - 单条套路句式超限：「他知道这」×4
  - dialogue_chars_pct 18.4 低于目标 20.0
  - [observe] 标题与《分科表被划去的瞬间》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 9
total_chars: 21208
chapter_chars_mean: 2356
chapter_chars_median: 2492
chapter_chars_cv: 0.17
paragraphs_mean: 50
dialogue_chars_pct: 24.1
dialogue_para_pct: 62.2
interiority_para_pct: 18.3
narration_para_pct: 19.5
turn_under20_pct: 88.3
turn_over200_pct: 0.0
attr_say_pct: 24.6
attr_adv_pct: 10.9
scenes_per_chapter: 3
dialogue_run_mean: 3.7
turn_len_median: 9
```
