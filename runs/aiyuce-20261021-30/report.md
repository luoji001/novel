# 涨价令 生成报告

slug：`aiyuce-20261021-30`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12361
LLM 调用：57 次，累计 217.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的异常增幅 | 1743 | normal | 36.8 | 0 |  | 1 |
| 2 | 核对折旧表数据 | 2383 | normal | 36.2 | 0 |  | 1 |
| 3 | 报价单上的价格变动 | 2147 | normal | 36.4 | 0 |  | 2 |
| 4 | 核对招聘JD变化 | 2121 | normal | 55.1 | 0 |  | 1 |
| 5 | 核对许可证修改通知 | 2211 | normal | 35.9 | 0 |  | 1 |
| 6 | 核对许可证修改通知 | 1750 | short | 88.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 3 句（如「比如说当实际操作过程中遇到了意想不到的技术难题使…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - 单条套路句式超限：「杭州开源模型项目组」×3
  - [observe] 章内自我复读 2 句（如「如果未来某个季度内多家主流用户的订单量突然下降超…」）
- 第 4 章：
  - narration_para_pct 44.4 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 标题重复：「核对许可证修改通知」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12078
chapter_chars_mean: 2013
chapter_chars_median: 2086
chapter_chars_cv: 0.13
paragraphs_mean: 14.8
dialogue_chars_pct: 5.7
dialogue_para_pct: 22.5
interiority_para_pct: 21.2
narration_para_pct: 56.3
turn_under20_pct: 59.4
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.4
turn_len_median: 15
```
