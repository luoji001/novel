# 铜钥匙 生成报告

slug：`xuanyi-20261019-79`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14077
LLM 调用：68 次，累计 233.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 擦拭铜钥匙 | 1575 | short | 99.5 | 0 |  | 1 |
| 2 | 摩挲铜钥匙 | 3693 | normal | 91.6 | 0 |  | 3 |
| 3 | 摩挲生锈的铁皮钥匙 | 3597 | normal | 86.7 | 0 |  | 4 |
| 4 | 摩挲泛黄信纸 | 3297 | normal | 92.1 | 0 |  | 2 |
| 5 | 摩挲铜钥匙 | 1910 | short | 92.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 7.9 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林德昌的」×5、「林德昌站在」×3、「陈阿婆点」×3
  - narration_para_pct 17.5 低于目标 20.0
  - [observe] 标题与《擦拭铜钥匙》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道自己」×4、「”陈阿婆低」×3、「林德昌的」×3
  - narration_para_pct 14.7 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「她停顿片刻，随后补充道，“而且，有时候你以为失去…」）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林德昌的」×6、「他知道这」×4、「林德昌点了点头」×3
- 第 5 章：
  - 单条套路句式超限：「林德昌的」×4
  - narration_para_pct 12.5 低于目标 20.0
  - [observe] attr_adv_pct 23.1 > 20.0（结构塌缩）
  - [observe] 标题重复：「摩挲铜钥匙」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13398
chapter_chars_mean: 2680
chapter_chars_median: 3147
chapter_chars_cv: 0.36
paragraphs_mean: 60.4
dialogue_chars_pct: 33.9
dialogue_para_pct: 70.7
interiority_para_pct: 12.5
narration_para_pct: 16.8
turn_under20_pct: 78.9
turn_over200_pct: 0.0
attr_say_pct: 24.8
attr_adv_pct: 5.5
scenes_per_chapter: 1.4
dialogue_run_mean: 4.0
turn_len_median: 11
```
