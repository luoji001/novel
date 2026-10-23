# 账本残页 生成报告

slug：`shuangwen-20261022-86`
档位：爽文　闸门模式：observe
章数：10　总字数：20343
LLM 调用：97 次，累计 452.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 拍纸留痕 | 2087 | normal | 39.8 | 0 |  | 3 |
| 2 | 拍纸留痕 | 1740 | normal | 93.9 | 0 |  | 3 |
| 3 | 签字笔对决 | 1998 | normal | 94.1 | 0 |  | 1 |
| 4 | 拍纸留痕 | 1876 | normal | 37.1 | 0 |  | 3 |
| 5 | 拍纸留痕 | 2151 | normal | 93.9 | 0 |  | 3 |
| 6 | 对峙雪夜 | 2111 | normal | 90.9 | 0 |  | 3 |
| 7 | 拍桌留痕 | 1800 | normal | 91.4 | 0 |  | 2 |
| 8 | 撕纸留痕 | 1973 | normal | 87.5 | 0 |  | 5 |
| 9 | 撕纸留痕 | 2075 | normal | 92.6 | 0 |  | 3 |
| 10 | 纸条留痕 | 2522 | long | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈建国的」×4
  - [observe] 章内自我复读 2 句（如「林小满坚定地说，“除非你愿意面对真相…」）
  - [observe] attr_adv_pct 31.2 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「陈建国的」×6、「林小满的」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「拍纸留痕」已存在
- 第 3 章：
  - 单条套路句式超限：「林小满的」×3
- 第 4 章：
  - 单条套路句式超限：「陈建国的」×6
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「拍纸留痕」已存在
- 第 5 章：
  - 单条套路句式超限：「陈建国的」×6
  - narration_para_pct 3.7 低于目标 5.0
  - [observe] 标题重复：「拍纸留痕」已存在
- 第 6 章：
  - 单条套路句式超限：「陈建国的」×3、「办公室」×3
  - narration_para_pct 3.3 低于目标 5.0
  - dialogue_run_mean 19 高于目标 14.0
- 第 7 章：
  - 单条套路句式超限：「陈建国的」×3
  - [observe] 标题与《拍纸留痕》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「陈建国的」×5
  - narration_para_pct 2.6 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - dialogue_run_mean 37 高于目标 14.0
  - [observe] 标题与《拍纸留痕》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「陈建国的」×4、「林小满的」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「撕纸留痕」已存在
- 第 10 章：
  - 单条套路句式超限：「陈建国的」×7
  - [observe] 标题与《撕纸留痕》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 19234
chapter_chars_mean: 1923
chapter_chars_median: 1926
chapter_chars_cv: 0.1
paragraphs_mean: 48.9
dialogue_chars_pct: 47.7
dialogue_para_pct: 85.8
interiority_para_pct: 4.8
narration_para_pct: 9.4
turn_under20_pct: 81.5
turn_over200_pct: 0.0
attr_say_pct: 34.0
attr_adv_pct: 12.4
scenes_per_chapter: 2
dialogue_run_mean: 10.7
turn_len_median: 12
```
