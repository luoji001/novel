# 破证 生成报告

slug：`shuangwen-20261022-85`
档位：爽文　闸门模式：observe
章数：10　总字数：18225
LLM 调用：97 次，累计 403.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 指纹盖在表格上 | 1750 | normal | 99.1 | 0 |  | 1 |
| 2 | 签字权的争夺 | 1665 | normal | 92.6 | 0 |  | 1 |
| 3 | 证件的折痕 | 1735 | normal | 87.7 | 0 |  | 3 |
| 4 | 评语表上的指纹印 | 1958 | normal | 92.7 | 0 |  | 0 |
| 5 | 工资条的争议 | 1953 | normal | 37.1 | 0 |  | 1 |
| 6 | 撕碎的代课协议 | 1856 | normal | 91.5 | 0 |  | 1 |
| 7 | 工资条的争议 | 1575 | normal | 93.7 | 0 |  | 3 |
| 8 | 握手与纸页的摩擦 | 1769 | normal | 87.3 | 0 |  | 3 |
| 9 | 撕碎的代课协议 | 1807 | normal | 93.3 | 0 |  | 2 |
| 10 | 教学成果记录本的展示 | 2147 | long | 36.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周正国的」×3
- 第 2 章：
  - attr_adv_pct 12.5 高于目标 12.0
- 第 3 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 36 高于目标 14.0
- 第 5 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 6 章：
  - narration_para_pct 0.0 低于目标 5.0
- 第 7 章：
  - 单条套路句式超限：「周正国的」×7、「林婉秋的」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「工资条的争议」已存在
- 第 8 章：
  - 单条套路句式超限：「林婉秋的」×4
  - narration_para_pct 3.3 低于目标 5.0
  - dialogue_run_mean 29 高于目标 14.0
- 第 9 章：
  - 单条套路句式超限：「周正国的」×4、「林婉秋的」×3
  - [observe] 标题重复：「撕碎的代课协议」已存在
- 第 10 章：
  - [observe] 章内自我复读 1 句（如「他知道，这个女人真的不一样…」）

## 整书结构指标

```
chapters: 10
total_chars: 17377
chapter_chars_mean: 1738
chapter_chars_median: 1706
chapter_chars_cv: 0.09
paragraphs_mean: 34.4
dialogue_chars_pct: 52.2
dialogue_para_pct: 87.0
interiority_para_pct: 5.2
narration_para_pct: 7.8
turn_under20_pct: 56.7
turn_over200_pct: 0.0
attr_say_pct: 19.3
attr_adv_pct: 10.8
scenes_per_chapter: 1.9
dialogue_run_mean: 12.3
turn_len_median: 16
```
