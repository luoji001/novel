# 旧账本 生成报告

slug：`shuangwen-20261023-100`
档位：爽文　闸门模式：observe
章数：10　总字数：18248
LLM 调用：97 次，累计 412.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 碎纸机的低鸣 | 1925 | normal | 97.9 | 0 |  | 2 |
| 2 | 账本与钢笔的对峙 | 1941 | normal | 93.8 | 0 |  | 2 |
| 3 | 编制文件的压制 | 1979 | normal | 94.6 | 0 |  | 1 |
| 4 | 钥匙的争夺 | 2018 | normal | 92.2 | 0 |  | 1 |
| 5 | 碎纸机的低鸣 | 1528 | normal | 37.5 | 0 |  | 6 |
| 6 | 铁盒里的账册 | 1523 | normal | 94.4 | 0 |  | 3 |
| 7 | 账本摊开的瞬间 | 1788 | normal | 93.1 | 0 |  | 2 |
| 8 | 账本摊开的瞬间 | 1641 | normal | 93.9 | 0 |  | 2 |
| 9 | 铁盒里的账册 | 1946 | normal | 94.7 | 0 |  | 1 |
| 10 | 账本摊开的瞬间 | 1949 | long | 92.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王主任的」×8
  - attr_adv_pct 17.6 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「李国庆点」×3
  - attr_adv_pct 12.5 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「王主任的」×4
- 第 4 章：
  - 单条套路句式超限：「李国庆的」×5、「他知道这」×3
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「王主任的」×5
  - narration_para_pct 3.0 低于目标 5.0
  - dialogue_run_mean 14.5 高于目标 14.0
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「碎纸机的低鸣」已存在
- 第 6 章：
  - 单条套路句式超限：「李国庆的」×3
  - narration_para_pct 3.7 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 21.4 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「王主任的」×5、「李国庆的」×3
  - [observe] 标题重复：「账本摊开的瞬间」已存在
- 第 9 章：
  - [observe] 标题重复：「铁盒里的账册」已存在
- 第 10 章：
  - 单条套路句式超限：「王主任的」×5、「他知道这」×3
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 标题重复：「账本摊开的瞬间」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17327
chapter_chars_mean: 1733
chapter_chars_median: 1825
chapter_chars_cv: 0.1
paragraphs_mean: 38.3
dialogue_chars_pct: 48.4
dialogue_para_pct: 82.6
interiority_para_pct: 7.0
narration_para_pct: 10.3
turn_under20_pct: 69.0
turn_over200_pct: 0.0
attr_say_pct: 29.0
attr_adv_pct: 13.0
scenes_per_chapter: 1.5
dialogue_run_mean: 6.8
turn_len_median: 12
```
