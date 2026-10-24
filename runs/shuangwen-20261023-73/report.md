# 账簿背面 生成报告

slug：`shuangwen-20261023-73`
档位：爽文　闸门模式：observe
章数：10　总字数：19723
LLM 调用：97 次，累计 444.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 折痕下的账簿 | 2157 | normal | 98.2 | 0 |  | 1 |
| 2 | 账簿背面的暗格 | 2236 | normal | 34.8 | 0 |  | 5 |
| 3 | 钥匙与账簿的对决 | 2062 | normal | 93.2 | 0 |  | 1 |
| 4 | 签字权的较量 | 1837 | normal | 92.8 | 0 |  | 3 |
| 5 | 钢笔与账簿的对峙 | 1957 | normal | 37.0 | 0 |  | 4 |
| 6 | 纸条上的旧职级 | 1736 | normal | 93.8 | 0 |  | 1 |
| 7 | 账簿背面的暗格 | 1827 | normal | 91.8 | 0 |  | 2 |
| 8 | 折痕下的账簿 | 1980 | normal | 95.0 | 0 |  | 2 |
| 9 | 铜钥匙的真相 | 1958 | normal | 37.0 | 0 |  | 2 |
| 10 | 账簿里的新名单 | 1963 | long | 93.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李怀安的」×5
- 第 2 章：
  - 单条套路句式超限：「李怀安的」×9、「变得更加」×3
  - narration_para_pct 2.2 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 21 高于目标 14.0
  - [observe] 章内自我复读 20 句（如「李怀安的表情变得更加凝重，他似乎意识到事情并不像…」）
- 第 3 章：
  - 单条套路句式超限：「李怀安的」×7
- 第 4 章：
  - narration_para_pct 2.6 低于目标 5.0
  - attr_adv_pct 23.8 高于目标 12.0
  - dialogue_run_mean 18.5 高于目标 14.0
- 第 5 章：
  - 单条套路句式超限：「李怀安的」×7
  - [observe] 章内自我复读 1 句（如「你以为这样就能扳倒我？…」）
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
  - [observe] 标题与《钥匙与账簿的对决》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「李怀安的」×4
- 第 7 章：
  - 单条套路句式超限：「李怀安的」×7
  - [observe] 标题重复：「账簿背面的暗格」已存在
- 第 8 章：
  - 单条套路句式超限：「李怀安的」×4
  - [observe] 标题重复：「折痕下的账簿」已存在
- 第 9 章：
  - 单条套路句式超限：「李怀安的」×10
  - [observe] attr_adv_pct 42.9 > 25.0（结构塌缩）
- 第 10 章：
  - 单条套路句式超限：「李怀安的」×3

## 整书结构指标

```
chapters: 10
total_chars: 18737
chapter_chars_mean: 1874
chapter_chars_median: 1868
chapter_chars_cv: 0.08
paragraphs_mean: 41.4
dialogue_chars_pct: 47.9
dialogue_para_pct: 83.3
interiority_para_pct: 6.9
narration_para_pct: 9.8
turn_under20_pct: 70.4
turn_over200_pct: 0.0
attr_say_pct: 24.1
attr_adv_pct: 19.5
scenes_per_chapter: 1.4
dialogue_run_mean: 7.9
turn_len_median: 14
```
