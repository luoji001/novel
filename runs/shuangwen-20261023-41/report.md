# 账本 生成报告

slug：`shuangwen-20261023-41`
档位：爽文　闸门模式：observe
章数：10　总字数：19380
LLM 调用：97 次，累计 431.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲章程的裂痕 | 1920 | normal | 99.9 | 0 |  | 2 |
| 2 | 签名笔的较量 | 2337 | normal | 91.9 | 0 |  | 1 |
| 3 | 签字笔的较量 | 1994 | normal | 93.5 | 0 |  | 3 |
| 4 | 划线的账本 | 1918 | normal | 92.1 | 0 |  | 2 |
| 5 | 拍案而起的签字笔 | 1786 | normal | 87.9 | 0 |  | 4 |
| 6 | 签名笔的较量 | 1797 | normal | 92.9 | 0 |  | 2 |
| 7 | 翻页的账本 | 1819 | normal | 91.2 | 0 |  | 3 |
| 8 | 翻阅账本的较量 | 1501 | normal | 93.0 | 0 |  | 0 |
| 9 | 签名笔的裂痕 | 1995 | normal | 37.3 | 0 |  | 3 |
| 10 | 账本的红印 | 2303 | long | 93.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×5、「周小满的」×3
  - attr_adv_pct 18.2 高于目标 12.0
- 第 2 章：
  - attr_adv_pct 25.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李建国的」×4、「周小满的」×4
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题与《签名笔的较量》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - narration_para_pct 2.7 低于目标 5.0
  - dialogue_run_mean 17 高于目标 14.0
- 第 5 章：
  - 单条套路句式超限：「李建国的」×4
  - narration_para_pct 2.7 低于目标 5.0
  - attr_adv_pct 23.1 高于目标 12.0
  - dialogue_run_mean 36 高于目标 14.0
- 第 6 章：
  - 单条套路句式超限：「周小满的」×3
  - [observe] 标题重复：「签名笔的较量」已存在
- 第 7 章：
  - 单条套路句式超限：「周小满的」×3
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题与《划线的账本》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「李建国的」×3
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题与《签名笔的较量》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18401
chapter_chars_mean: 1840
chapter_chars_median: 1821
chapter_chars_cv: 0.13
paragraphs_mean: 40.4
dialogue_chars_pct: 51.8
dialogue_para_pct: 85.6
interiority_para_pct: 3.7
narration_para_pct: 10.8
turn_under20_pct: 69.1
turn_over200_pct: 0.0
attr_say_pct: 32.4
attr_adv_pct: 16.5
scenes_per_chapter: 1.4
dialogue_run_mean: 10.7
turn_len_median: 14
```
