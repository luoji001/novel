# 账本 生成报告

slug：`shuangwen-20261023-40`
档位：爽文　闸门模式：observe
章数：10　总字数：19305
LLM 调用：97 次，累计 427.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻账本 | 1712 | normal | 96.6 | 0 |  | 1 |
| 2 | 翻账本 | 1785 | normal | 93.1 | 0 |  | 2 |
| 3 | 翻账本 | 1635 | normal | 92.9 | 0 |  | 4 |
| 4 | 翻账本 | 2148 | normal | 93.9 | 0 |  | 3 |
| 5 | 翻账本 | 1679 | normal | 94.7 | 0 |  | 2 |
| 6 | 翻账本 | 2004 | normal | 92.8 | 0 |  | 2 |
| 7 | 翻账本 | 1720 | normal | 93.4 | 0 |  | 2 |
| 8 | 拍文件 | 1872 | normal | 37.1 | 0 |  | 3 |
| 9 | 翻账本 | 1869 | normal | 92.4 | 0 |  | 2 |
| 10 | 翻账本 | 2871 | long | 93.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王德发的」×5
- 第 2 章：
  - 单条套路句式超限：「王德发的」×3
  - [observe] 标题重复：「翻账本」已存在
- 第 3 章：
  - 单条套路句式超限：「王德发的」×4、「李小满的」×3
  - narration_para_pct 3.3 低于目标 5.0
  - dialogue_run_mean 14.5 高于目标 14.0
  - [observe] 标题重复：「翻账本」已存在
- 第 4 章：
  - 单条套路句式超限：「王德发的」×5
  - narration_para_pct 4.9 低于目标 5.0
  - [observe] 标题重复：「翻账本」已存在
- 第 5 章：
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「翻账本」已存在
- 第 6 章：
  - 单条套路句式超限：「王德发的」×4
  - [observe] 标题重复：「翻账本」已存在
- 第 7 章：
  - 单条套路句式超限：「王德发的」×7
  - [observe] 标题重复：「翻账本」已存在
- 第 8 章：
  - 单条套路句式超限：「王德发的」×5、「李小满的」×4
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 章内自我复读 2 句（如「这是来自县领导的通知…」）
- 第 9 章：
  - 单条套路句式超限：「李小满点了点头」×3、「他知道自己」×3
  - [observe] 标题重复：「翻账本」已存在
- 第 10 章：
  - [observe] 标题重复：「翻账本」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18321
chapter_chars_mean: 1832
chapter_chars_median: 1740
chapter_chars_cv: 0.19
paragraphs_mean: 43.2
dialogue_chars_pct: 49.8
dialogue_para_pct: 84.3
interiority_para_pct: 5.0
narration_para_pct: 10.7
turn_under20_pct: 72.1
turn_over200_pct: 0.0
attr_say_pct: 37.3
attr_adv_pct: 6.6
scenes_per_chapter: 2.1
dialogue_run_mean: 7.5
turn_len_median: 14
```
