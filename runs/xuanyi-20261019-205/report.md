# 闪影 生成报告

slug：`xuanyi-20261019-205`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13834
LLM 调用：68 次，累计 210.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 监控录像带消失 | 1491 | short | 98.5 | 0 |  | 1 |
| 2 | 夜班登记本翻页 | 3321 | normal | 91.3 | 0 |  | 4 |
| 3 | 屏幕闪现神秘人影 | 3203 | normal | 87.6 | 0 |  | 2 |
| 4 | 药瓶位置被调换 | 3780 | normal | 91.0 | 0 |  | 2 |
| 5 | 工牌背面暗码 | 2034 | short | 92.7 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 18.2 高于目标 10.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林修远的」×4、「林修远点了点头」×3、「他知道这」×3
  - narration_para_pct 16.7 低于目标 20.0
  - [observe] attr_adv_pct 26.7 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周婉如的」×5、「为什么会」×4
  - [observe] 章内自我复读 19 句（如「电话那头沉默了几秒，然后传来周婉如的声音：“林修…」）
- 第 4 章：
  - 单条套路句式超限：「周婉如的」×5
  - narration_para_pct 16.5 低于目标 20.0
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周婉如的」×7、「林修远的」×4
  - narration_para_pct 15.1 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13071
chapter_chars_mean: 2614
chapter_chars_median: 2981
chapter_chars_cv: 0.36
paragraphs_mean: 68.4
dialogue_chars_pct: 31.4
dialogue_para_pct: 62.3
interiority_para_pct: 10.1
narration_para_pct: 27.5
turn_under20_pct: 75.1
turn_over200_pct: 0.0
attr_say_pct: 23.4
attr_adv_pct: 12.3
scenes_per_chapter: 4.8
dialogue_run_mean: 3.8
turn_len_median: 11
```
