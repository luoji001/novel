# 汇款单 生成报告

slug：`xuanyi-20261019-259`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15206
LLM 调用：68 次，累计 239.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲汇款单一角 | 1685 | short | 98.1 | 0 |  | 1 |
| 2 | 摩挲印章刻痕 | 3867 | normal | 90.8 | 0 |  | 3 |
| 3 | 摩挲信纸边缘 | 3939 | normal | 84.4 | 0 |  | 4 |
| 4 | 摩挲钥匙纹路 | 3787 | normal | 82.7 | 0 |  | 5 |
| 5 | 摩挲照片背面落款 | 1923 | short | 89.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「那人问道，“林师傅，我是来看望王大海的…」）
- 第 2 章：
  - 单条套路句式超限：「陈秀兰的」×13、「林振国的」×6、「”陈秀兰轻」×3
  - narration_para_pct 6.4 低于目标 20.0
  - attr_adv_pct 13.5 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「到了一个」×3、「林振国的」×3
  - dialogue_chars_pct 16.7 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 章内自我复读 19 句（如「信的内容大致是在谈论某次搬家事宜，提到了一个旧地…」）
- 第 4 章：
  - 单条套路句式超限：「他知道这」×4、「陈秀兰的」×3、「林振国的」×3
  - dialogue_chars_pct 19.3 低于目标 20.0
  - interiority_para_pct 23.4 高于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 章内自我复读 17 句（如「他拿出那把生锈的钥匙，仔细端详了一会儿，然后将其…」）
- 第 5 章：
  - narration_para_pct 12.8 低于目标 20.0
  - [observe] 章内自我复读 5 句（如「他打开信封，里面是一张泛黄的照片，照片上是一个男…」）

## 整书结构指标

```
chapters: 5
total_chars: 14463
chapter_chars_mean: 2893
chapter_chars_median: 3619
chapter_chars_cv: 0.37
paragraphs_mean: 66.6
dialogue_chars_pct: 30.2
dialogue_para_pct: 63.6
interiority_para_pct: 15.1
narration_para_pct: 21.3
turn_under20_pct: 85.6
turn_over200_pct: 0.0
attr_say_pct: 41.1
attr_adv_pct: 11.3
scenes_per_chapter: 2.4
dialogue_run_mean: 4.1
turn_len_median: 10
```
