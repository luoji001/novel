# 旧工龄证明 生成报告

slug：`shuangwen-20261022-25`
档位：爽文　闸门模式：observe
章数：10　总字数：20619
LLM 调用：97 次，累计 380.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 复印件在阳光下颤抖 | 1658 | normal | 95.9 | 0 |  | 2 |
| 2 | 复印件在阳光下颤抖 | 1759 | normal | 94.0 | 0 |  | 2 |
| 3 | 文件在桌上摊开 | 2010 | normal | 93.2 | 0 |  | 1 |
| 4 | 签名笔落在名册上 | 2087 | normal | 93.7 | 0 |  | 1 |
| 5 | 复印件在阳光下颤抖 | 2052 | normal | 92.8 | 0 |  | 3 |
| 6 | 复印件在桌上摊开 | 2253 | normal | 92.5 | 0 |  | 1 |
| 7 | 签名笔划破文件 | 2117 | normal | 92.1 | 0 |  | 3 |
| 8 | 文件在桌上摊开 | 2061 | normal | 37.1 | 0 |  | 3 |
| 9 | 签名笔划破文件 | 2033 | normal | 93.2 | 0 |  | 1 |
| 10 | 复印件在桌上摊开 | 2579 | long | 90.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林秋实的」×3
- 第 2 章：
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「复印件在阳光下颤抖」已存在
- 第 3 章：
  - attr_adv_pct 18.8 高于目标 12.0
- 第 4 章：
  - narration_para_pct 2.2 低于目标 5.0
- 第 5 章：
  - 单条套路句式超限：「陈启明的」×5、「他知道这」×3
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「复印件在阳光下颤抖」已存在
- 第 6 章：
  - [observe] 标题与《文件在桌上摊开》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「陈启明的」×4
  - narration_para_pct 3.0 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「林秋实的」×3
  - [observe] attr_adv_pct 35.7 > 25.0（结构塌缩）
  - [observe] 标题重复：「文件在桌上摊开」已存在
- 第 9 章：
  - [observe] 标题重复：「签名笔划破文件」已存在
- 第 10 章：
  - 单条套路句式超限：「林秋实的」×7
  - [observe] 标题重复：「复印件在桌上摊开」已存在

## 整书结构指标

```
chapters: 10
total_chars: 19650
chapter_chars_mean: 1965
chapter_chars_median: 1958
chapter_chars_cv: 0.12
paragraphs_mean: 39.9
dialogue_chars_pct: 46.3
dialogue_para_pct: 83.1
interiority_para_pct: 7.0
narration_para_pct: 9.9
turn_under20_pct: 69.6
turn_over200_pct: 0.0
attr_say_pct: 24.5
attr_adv_pct: 15.3
scenes_per_chapter: 1.6
dialogue_run_mean: 5.9
turn_len_median: 14
```
