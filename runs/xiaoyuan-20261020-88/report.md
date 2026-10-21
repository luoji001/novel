# 分科表 生成报告

slug：`xiaoyuan-20261020-88`
档位：校园青春　闸门模式：observe
章数：9　总字数：19980
LLM 调用：100 次，累计 429.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 分科表上的名字 | 1548 | short | 51.5 | 0 |  | 2 |
| 2 | 磁带里的秘密 | 2453 | normal | 95.2 | 0 |  | 1 |
| 3 | 缴费单上的指纹 | 2328 | normal | 90.2 | 0 |  | 3 |
| 4 | 病危通知书的纸角 | 2390 | normal | 89.5 | 0 |  | 3 |
| 5 | 书包里的蓝色信封 | 2599 | normal | 90.1 | 0 |  | 2 |
| 6 | 摩挲褶皱的指尖 | 2193 | normal | 87.3 | 0 |  | 4 |
| 7 | 折叠的通知单 | 2177 | normal | 88.9 | 0 |  | 2 |
| 8 | 翻阅旧练习册 | 2501 | normal | 90.1 | 0 |  | 1 |
| 9 | 摩挲缴费单的指尖 | 1782 | short | 93.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.6 低于目标 20.0
  - [observe] 章内自我复读 21 句（如「她翻开抽屉，拿出一本黑色笔记本，在最后一页写下一…」）
- 第 2 章：
  - 单条套路句式超限：「林晓棠站在」×3
- 第 3 章：
  - 单条套路句式超限：「周子墨的」×4
  - dialogue_chars_pct 19.7 低于目标 20.0
  - narration_para_pct 14.3 低于目标 15.0
- 第 4 章：
  - 单条套路句式超限：「周子墨的」×9
  - dialogue_chars_pct 19.6 低于目标 20.0
  - [observe] 章内自我复读 9 句（如「他慢慢地把病危通知书放回抽屉，就像放进了一个看不…」）
- 第 5 章：
  - 单条套路句式超限：「周子墨的」×6
  - narration_para_pct 13.0 低于目标 15.0
- 第 6 章：
  - 单条套路句式超限：「林晓棠的」×3
  - interiority_para_pct 7.5 低于目标 8.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 章内自我复读 17 句（如「林晓棠的目光再次落回自己的桌子上，那里依旧静静地…」）
- 第 7 章：
  - 单条套路句式超限：「林晓棠的」×3
  - dialogue_chars_pct 17.9 低于目标 20.0
- 第 8 章：
  - 单条套路句式超限：「周子墨点」×3
- 第 9 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周子墨的」×5、「林晓棠的」×5
  - interiority_para_pct 7.9 低于目标 8.0
  - [observe] 标题与《缴费单上的指纹》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 9
total_chars: 18995
chapter_chars_mean: 2111
chapter_chars_median: 2229
chapter_chars_cv: 0.16
paragraphs_mean: 44.7
dialogue_chars_pct: 21.9
dialogue_para_pct: 64.9
interiority_para_pct: 15.1
narration_para_pct: 20.0
turn_under20_pct: 90.8
turn_over200_pct: 0.0
attr_say_pct: 41.6
attr_adv_pct: 4.1
scenes_per_chapter: 2.9
dialogue_run_mean: 2.8
turn_len_median: 10
```
