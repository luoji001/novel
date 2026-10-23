# 残页 生成报告

slug：`shuangwen-20261022-71`
档位：爽文　闸门模式：observe
章数：10　总字数：19103
LLM 调用：97 次，累计 441.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账簿上的红字 | 2301 | normal | 98.7 | 0 |  | 1 |
| 2 | 残页的微光 | 1568 | normal | 95.4 | 0 |  | 1 |
| 3 | 竹篓里的灵石 | 1518 | normal | 38.1 | 0 |  | 1 |
| 4 | 竹篓倒扣的刹那 | 2098 | normal | 38.2 | 0 |  | 2 |
| 5 | 竹篓倒扣的刹那 | 2196 | normal | 93.2 | 0 |  | 2 |
| 6 | 签名的瞬间 | 1813 | normal | 94.0 | 0 |  | 0 |
| 7 | 残页上的符咒 | 1971 | normal | 94.2 | 0 |  | 0 |
| 8 | 空气凝滞的刹那 | 1731 | normal | 91.1 | 0 |  | 1 |
| 9 | 竹篓里的灵石 | 1700 | normal | 94.5 | 0 |  | 1 |
| 10 | 蓝光冲霄 | 2197 | long | 37.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 25.0 高于目标 12.0
- 第 2 章：
  - attr_adv_pct 18.8 高于目标 12.0
- 第 3 章：
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「我只是想请您帮我签个字而已…」）
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「陈长老的」×3
  - [observe] 标题重复：「竹篓倒扣的刹那」已存在
- 第 8 章：
  - 单条套路句式超限：「陈长老的」×5
- 第 9 章：
  - [observe] 标题重复：「竹篓里的灵石」已存在
- 第 10 章：
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）

## 整书结构指标

```
chapters: 10
total_chars: 18088
chapter_chars_mean: 1809
chapter_chars_median: 1794
chapter_chars_cv: 0.15
paragraphs_mean: 43.3
dialogue_chars_pct: 41.5
dialogue_para_pct: 77.2
interiority_para_pct: 8.2
narration_para_pct: 14.7
turn_under20_pct: 76.0
turn_over200_pct: 0.0
attr_say_pct: 16.4
attr_adv_pct: 18.3
scenes_per_chapter: 1.3
dialogue_run_mean: 4.9
turn_len_median: 12
```
