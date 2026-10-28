# 蓝车 生成报告

slug：`shipin-20261027-363`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5970
LLM 调用：57 次，累计 130.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙上的刻痕 | 521 | short | 18.5 | 0 |  | 1 |
| 2 | 踩碎停车票的瞬间 | 1082 | normal | 93.8 | 0 |  | 0 |
| 3 | 倒雪水显车牌 | 1130 | normal | 92.8 | 0 |  | 1 |
| 4 | 扯门把手的瞬间 | 1297 | normal | 92.8 | 0 |  | 0 |
| 5 | 钥匙转动的瞬间 | 689 | normal | 20.9 | 0 |  | 3 |
| 6 | 钥匙触碰引擎盖 | 1245 | normal | 90.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

1. 第二章提到赵强承认红色轿车是三年前购买的二手车，但第四章提到车上有妻子遗留的停车票，暗示车辆可能有更近的归属关系，前后矛盾。

2. 第五章提到李岩用黑色钥匙打开红色轿车，发现车锁与自行车锁结构相同，并在雪地中找到与之匹配的自行车，但第六章提到李岩在雪夜找到红色轿车时，发现车底藏有车标，暗示车辆本身有特殊标识，与自行车锁结构的关联未明确交代，逻辑不连贯。

3. 第三章提到陈雪用融化的雪水擦拭挡风玻璃，揭开车辆真实归属的秘密，但未明确说明她如何得知车辆归属信息，与前文信息来源不一致。

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 472 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 24.0 低于目标 35.0
- 第 5 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 614 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - 命中套话收尾句

## 整书结构指标

```
chapters: 6
total_chars: 5575
chapter_chars_mean: 929
chapter_chars_median: 1040
chapter_chars_cv: 0.34
paragraphs_mean: 24.5
dialogue_chars_pct: 15.3
dialogue_para_pct: 44.8
interiority_para_pct: 0.0
narration_para_pct: 55.2
turn_under20_pct: 97.9
turn_over200_pct: 0.0
attr_say_pct: 62.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.0
turn_len_median: 8
```
