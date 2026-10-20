# 铜钥匙 生成报告

slug：`xuanyi-20261019-139`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14006
LLM 调用：68 次，累计 229.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲铜钥匙 | 1448 | short | 99.2 | 0 |  | 1 |
| 2 | 摩挲褪色身份证 | 3827 | normal | 91.6 | 0 |  | 4 |
| 3 | 摩挲褪色身份证 | 3508 | normal | 89.4 | 0 |  | 3 |
| 4 | 摩挲泛黄登记簿 | 3200 | normal | 85.5 | 0 |  | 4 |
| 5 | 摩挲铜钥匙 | 2018 | short | 85.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 18.8 低于目标 20.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林永年的」×5、「“我不知道」×4、「陈阿婆的」×3
  - narration_para_pct 11.8 低于目标 20.0
  - [observe] attr_adv_pct 28.9 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3、「林永年的」×3
  - narration_para_pct 15.1 低于目标 20.0
  - [observe] 标题重复：「摩挲褪色身份证」已存在
- 第 4 章：
  - dialogue_chars_pct 19.5 低于目标 20.0
  - interiority_para_pct 20.4 高于目标 20.0
  - [observe] 章内自我复读 2 句（如「你好，请问这里是你工作的地方吗？…」）
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 5 章：
  - interiority_para_pct 22.5 高于目标 20.0
  - [observe] 章内自我复读 15 句（如「林永年拿起一张仔细端详，发现上面不仅有姓名，还有…」）
  - [observe] 标题重复：「摩挲铜钥匙」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13338
chapter_chars_mean: 2668
chapter_chars_median: 3087
chapter_chars_cv: 0.36
paragraphs_mean: 59.2
dialogue_chars_pct: 32.6
dialogue_para_pct: 71.4
interiority_para_pct: 12.1
narration_para_pct: 16.5
turn_under20_pct: 83.1
turn_over200_pct: 0.0
attr_say_pct: 20.2
attr_adv_pct: 13.0
scenes_per_chapter: 2.6
dialogue_run_mean: 3.9
turn_len_median: 11
```
